import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))

import reading_copy as rc  # noqa: E402


VALID_LESSON = '''---
lesson_id: 42
native_language: es
---
## Why contrast matters [00:05–01:30]
Contrast tells the viewer where to look first, and it sets the emotional temperature of the image.
Warm light against a cool shadow separates the subject from the background.

::: figure 00:40 F0040.jpg
On screen: "CONTRASTE"
Shows: A slide with one warm and one cool swatch.
:::

## Applying it [01:30–03:00]
Choose the focal point, then push contrast there and lower it everywhere else in the frame.

### Key points (derived)
- Contrast directs attention.
'''


class LessonFixture:
    def __init__(self, root: Path, text: str = VALID_LESSON, native_words: int = 40):
        self.dir = root / 'reading' / 'U01' / 'L02'
        (self.dir / 'frames').mkdir(parents=True)
        (self.dir / 'lesson.json').write_text(json.dumps({
            'course_id': 1, 'unit': 1, 'lesson': 2, 'lesson_id': 42, 'title': 'Contrast',
            'duration_seconds': 180, 'native_language': 'es', 'native_words': native_words,
            'file': 'x.mp4', 'url': 'https://www.domestika.org/x'}))
        (self.dir / 'frames' / 'F0040.jpg').write_bytes(b'jpg')
        (self.dir / 'frames.json').write_text(json.dumps({'F0040.jpg': 40.2}))
        (self.dir / 'lesson.md').write_text(text)


class CaptionTests(unittest.TestCase):
    def test_rolling_and_duplicate_cues_collapse(self):
        with tempfile.TemporaryDirectory() as tmp:
            vtt = Path(tmp) / 'a.es.vtt'
            vtt.write_text('WEBVTT\n\n1\n00:00:01.000 --> 00:00:02.000\nHola\n\n'
                           '2\n00:00:02.000 --> 00:00:03.000\nHola a todos\n\n'
                           '3\n00:00:03.000 --> 00:00:04.000\nHola a todos\n\n'
                           '4\n00:00:04.000 --> 00:00:05.000\n<c.yellow>Otra</c> frase\n')
            cues = rc.read_vtt(vtt)
            self.assertEqual([c[2] for c in cues], ['Hola a todos', 'Otra frase'])
            self.assertEqual(cues[0][:2], (1.0, 4.0))

    def test_native_language_prefers_recorded_default(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            (folder / 'l.download.json').write_text(json.dumps(
                {'caption_languages': ['en', 'es'], 'default_language': 'pt'}))
            self.assertEqual(rc.native_language(folder, 'l'), 'pt')

    def test_native_language_falls_back_to_last_caption_language(self):
        with tempfile.TemporaryDirectory() as tmp:
            folder = Path(tmp)
            (folder / 'l.download.json').write_text(json.dumps({'caption_languages': ['en', 'es']}))
            self.assertEqual(rc.native_language(folder, 'l'), 'es')
            (folder / 'l.download.json').write_text(json.dumps({'caption_languages': ['en']}))
            self.assertEqual(rc.native_language(folder, 'l'), 'en')
            (folder / 'l.download.json').write_text(json.dumps({'caption_languages': []}))
            with self.assertRaises(RuntimeError):
                rc.native_language(folder, 'l')


class CheckTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.rules = rc.load_rules(1)

    def tearDown(self):
        self.tmp.cleanup()

    def errors(self, text=VALID_LESSON, native_words=40):
        return rc.check_lesson(LessonFixture(self.root, text, native_words).dir, self.rules)

    def test_valid_lesson_passes(self):
        self.assertEqual(self.errors(), [])

    def test_overlapping_range_fails(self):
        text = VALID_LESSON.replace('[01:30–03:00]', '[01:00–03:00]')
        self.assertTrue(any('overlaps' in e for e in self.errors(text)))

    def test_missing_frame_fails(self):
        text = VALID_LESSON.replace('F0040.jpg', 'F0099.jpg')
        self.assertTrue(any('not extracted' in e for e in self.errors(text)))

    def test_missing_on_screen_fails(self):
        text = VALID_LESSON.replace('On screen: "CONTRASTE"\n', '')
        self.assertTrue(any('On screen' in e for e in self.errors(text)))

    def test_short_prose_fails_without_note(self):
        self.assertTrue(any('words' in e for e in self.errors(native_words=400)))

    def test_short_prose_passes_with_compression_note(self):
        text = VALID_LESSON.replace('native_language: es\n', 'native_language: es\ncompression_note: long silent demo\n')
        self.assertEqual(self.errors(text, native_words=400), [])

    def test_uncovered_tail_fails(self):
        text = VALID_LESSON.replace('[01:30–03:00]', '[01:30–01:50]')
        self.assertTrue(any('Last section' in e for e in self.errors(text)))


class CleanTests(unittest.TestCase):
    MANIFEST_HTML = '''<h2>Tasks</h2><ul>
<li><div><a href="https://www.domestika.org/en/courses/7/units/1/tasks/9/complete"></a>
<h3>present yourself <span>Practice exercise 1.1</span></h3>
<div><p>Tell me who you are.</p></div></div></li>
<li><div><a href="https://www.domestika.org/en/courses/7/units/1/tasks/10/complete"></a>
<h3>Create images with different moods</h3>
<div><p>Change the mood using only colour and value.</p>
<p>Download the <a href="https://www.domestika.org/en/courses/7/files/55">PSD</a>.</p>
<div><a href="https://www.domestika.org/en/courses/7-x/community/forum/topics/1-y">Share on the forum</a></div>
</div></div></li>
<li><h3>Follow me!</h3><div><p>My social networks are here.</p></div></li>
<li><h3>Studio binder</h3><div><p>Read <a href="https://www.domestika.org/en/courses/99-other">this other course</a> too.</p></div></li>
</ul>'''

    def test_manifest_cleaning(self):
        rules = rc.load_rules(7)
        log = rc.Removals()
        out = rc.clean_html(self.MANIFEST_HTML, rules, 'U01/Tasks', log)
        self.assertNotIn('present yourself', out)
        self.assertNotIn('Follow me', out)
        self.assertNotIn('Share on the forum', out)
        self.assertNotIn('courses/99-other', out)
        self.assertIn('this other course', out)
        self.assertIn('Create images with different moods', out)
        self.assertIn('https://www.domestika.org/en/courses/7/files/55', out)
        self.assertNotIn('/complete', out)
        self.assertGreaterEqual(len(log.rows), 3)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / 'removed.log'
            log.write(path)
            written = path.read_text()
            self.assertIn('present yourself', written)
            self.assertIn('Share on the forum', written)

    def test_prose_cleaning_keeps_lists(self):
        rules = rc.load_rules(7)
        log = rc.Removals()
        text = 'Contrast guides the eye. Follow me on Instagram for more.\n\n- One\n- Two'
        out = rc.clean_prose(text, rules, 'U01/L02', log)
        self.assertEqual(out, 'Contrast guides the eye.\n\n- One\n- Two')
        self.assertEqual(len(log.rows), 1)

    def test_heading_only_extra_is_empty(self):
        self.assertFalse(rc.has_content({'title': 'Tasks', 'html': '<h2>Tasks</h2><ul></ul>'}))
        self.assertTrue(rc.has_content({'title': 'Tasks', 'html': '<h2>Tasks</h2><p>Paint it.</p>'}))

    def test_spoken_course_plugs_are_removed(self):
        rules = rc.load_rules(7)
        log = rc.Removals()
        text = ('Values set the mood. For that you can see my other courses on Domestika, which are good. '
                'Remember you are part of the great Domestika community.')
        self.assertEqual(rc.clean_prose(text, rules, 'U03/L08', log), 'Values set the mood.')
        self.assertEqual(len(log.rows), 2)

    def test_only_the_promotional_clause_is_removed(self):
        rules = rc.load_rules(7)
        log = rc.Removals()
        text = 'Yes, we can, if the shapes are right; for that, I invite you to see my courses on this.'
        self.assertEqual(rc.clean_prose(text, rules, 'U04/L14', log), 'Yes, we can, if the shapes are right.')

    def test_intro_lessons(self):
        rules = rc.load_rules(7)
        self.assertTrue(rc.is_intro_lesson('Presentation (Who am I)', rules))
        self.assertFalse(rc.is_intro_lesson('Influences', rules))
        self.assertFalse(rc.is_intro_lesson('What will we do in the course?', rules))


class CandidateTests(unittest.TestCase):
    def test_candidates_take_segment_ends_and_long_segment_samples(self):
        times = rc.candidate_times([10.0, 100.0], [(20.0, 26.0)], 120.0)
        self.assertIn(9.5, times)
        self.assertIn(99.5, times)
        self.assertIn(40.0, times)
        self.assertEqual(times, sorted(times))


if __name__ == '__main__':
    unittest.main()
