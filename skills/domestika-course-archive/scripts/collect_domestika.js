// Run in Zen's developer console while signed in on a Domestika course unit page.
(async () => {
  const match = location.pathname.match(/^(\/[a-z]{2}\/courses\/(\d+)-[^/]+)\/units\/[^/]+/);
  if (!match) throw new Error('Open a course unit page before running this collector.');
  const [coursePath, courseId] = [match[1], Number(match[2])];
  const unitPath = coursePath + '/units/';
  const urls = [...new Set([...document.querySelectorAll('a[href]')]
    .map(a => new URL(a.href))
    .filter(u => u.origin === location.origin && u.pathname.startsWith(unitPath)
      && /^\d+-[^/]+\/?$/.test(u.pathname.slice(unitPath.length)))
    .map(u => u.origin + u.pathname))];
  if (!urls.length) throw new Error('No unit links were found in the course sidebar.');

  const absolute = (value, base) => {
    try {
      const url = new URL(value, base);
      return /^https?:$/.test(url.protocol) ? url.href : null;
    } catch { return null; }
  };
  const clean = (node, base) => {
    if (!node) return '';
    const copy = node.cloneNode(true);
    copy.querySelectorAll('script,style,iframe,video,audio,source,track,form,input,button,textarea,select,svg,canvas,noscript,.modal')
      .forEach(e => e.remove());
    copy.querySelectorAll('*').forEach(e => {
      const href = e.tagName === 'A' ? absolute(e.getAttribute('href'), base) : null;
      const image = e.tagName === 'IMG' ? absolute(e.getAttribute('data-src') || e.getAttribute('src'), base) : null;
      const alt = e.tagName === 'IMG' ? e.getAttribute('alt') : null;
      [...e.attributes].forEach(a => e.removeAttribute(a.name));
      if (href) e.setAttribute('href', href);
      if (image) e.setAttribute('src', image);
      if (alt) e.setAttribute('alt', alt);
    });
    return copy.innerHTML;
  };
  const propsFrom = html => {
    const found = html.match(/window\.__INITIAL_PROPS__\s*=\s*JSON\.parse\('((?:\\.|[^'])*)'\);/s);
    if (!found) throw new Error('Course lesson metadata was not found.');
    return JSON.parse(JSON.parse('"' + found[1].replace(/\\'/g, "'") + '"'));
  };

  const result = { version: 1, course_id: courseId, collected_at: new Date().toISOString(), units: [] };
  for (const url of urls) {
    console.log('Reading unit:', url);
    const response = await fetch(url, { credentials: 'same-origin' });
    if (!response.ok || !response.url.startsWith(location.origin + coursePath + '/units/'))
      throw new Error(`Could not read course unit (${response.status}): ${url}`);
    const html = await response.text();
    const doc = new DOMParser().parseFromString(html, 'text/html');
    const props = propsFrom(html);
    if (Number(props.course?.id) !== courseId || !Array.isArray(props.videos))
      throw new Error(`Unexpected lesson metadata for ${url}`);
    const article = doc.querySelector('article.paper');
    const body = article?.querySelector('.paper__body');
    if (!body) throw new Error(`Unit content was not found: ${url}`);
    const sections = [...body.children].filter(e => e.classList.contains('section'));
    const unitNumber = Number(props.videos[0]?.video?.numUnit);
    const unit = {
      number: unitNumber,
      title: article.querySelector('h2')?.textContent.trim() || `Unit ${unitNumber}`,
      url,
      intro_html: clean(body.querySelector(':scope > .m-rich-text'), url),
      extras: sections.filter(s => !s.querySelector('li[id^="course_lesson_"]'))
        .map(s => ({ title: s.querySelector('h2')?.textContent.trim() || 'More', html: clean(s, url) })),
      lessons: props.videos.map(({ video }) => {
        const item = doc.getElementById(`course_lesson_${video.lessonId}`);
        if (!item || !video.playbackURL) throw new Error(`Missing lesson or stream: ${video.lessonId}`);
        return {
          number: Number(video.numLesson), id: Number(video.lessonId),
          title: item.querySelector('.lesson-title')?.textContent.trim() || video.title,
          duration_seconds: Number(video.duration),
          url: `${url}#course_lesson_${video.lessonId}`,
          media_url: video.playbackURL,
          transcript_html: clean(item.querySelector('.lesson-description'), url)
        };
      })
    };
    if (!unitNumber || !unit.lessons.length) throw new Error(`No video lessons found: ${url}`);
    result.units.push(unit);
    result.course_title ||= doc.querySelector('h1')?.textContent.trim() || `Domestika course ${courseId}`;
    result.expected_units ||= Number(props.course.totalNumUnits);
    result.expected_lessons ||= Number(props.course.totalNumLessons);
  }
  result.units.sort((a, b) => a.number - b.number);
  const count = result.units.reduce((n, u) => n + u.lessons.length, 0);
  if (result.units.length !== result.expected_units || count !== result.expected_lessons)
    throw new Error(`Expected ${result.expected_units} units and ${result.expected_lessons} lessons; found ${result.units.length} and ${count}.`);
  const blob = new Blob([JSON.stringify(result, null, 2)], { type: 'application/json' });
  const link = document.createElement('a');
  link.href = URL.createObjectURL(blob);
  link.download = `domestika-course-${courseId}-manifest.json`;
  link.click();
  setTimeout(() => URL.revokeObjectURL(link.href), 10000);
  console.log(`Collected ${result.units.length} units and ${count} lessons. The manifest is in your Downloads folder.`);
})().catch(error => console.error('Domestika collection failed:', error));
