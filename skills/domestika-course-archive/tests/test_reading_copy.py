import json
import shutil
import subprocess
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

    def test_instagram_tagging_plug_is_removed_but_exercise_survives(self):
        rules = rc.load_rules(7)
        log = rc.Removals()
        text = ('Make three photographs with an object of your choice. '
                'If you post them on Instagram, you can tag me.')
        self.assertEqual(rc.clean_prose(text, rules, 'U02/L20', log),
                         'Make three photographs with an object of your choice.')
        self.assertEqual(len(log.rows), 1)

    def test_only_the_promotional_clause_is_removed(self):
        rules = rc.load_rules(7)
        log = rc.Removals()
        text = 'Yes, we can, if the shapes are right; for that, I invite you to see my courses on this.'
        self.assertEqual(rc.clean_prose(text, rules, 'U04/L14', log), 'Yes, we can, if the shapes are right.')

    def test_forum_prompts_are_removed_but_the_task_survives(self):
        rules = rc.load_rules(7)
        log = rc.Removals()
        text = ('Ask people what they see first to check your mission, you can also post them in the forum. '
                'Share your best copy with your peers on the forum.')
        self.assertEqual(rc.clean_prose(text, rules, 'U04/unit', log),
                         'Ask people what they see first to check your mission.')
        self.assertEqual(len(log.rows), 2)

    def test_coordinated_flag_forum_invitation_clause_is_removed(self):
        rules = rc.load_rules(7)
        log = rc.Removals()
        text = 'Viewers are asked to make their own flags and post them in the forum.'
        self.assertEqual(rc.clean_prose(text, rules, 'U02/L15', log),
                         'Viewers are asked to make their own flags.')
        self.assertEqual(len(log.rows), 1)
        self.assertEqual(log.rows[0][1:], ('U02/L15', 'and post them in the forum.'))

    def test_coordinated_palette_forum_invitation_clause_is_removed(self):
        rules = rc.load_rules(7)
        log = rc.Removals()
        text = ('When finished, classify the palettes as analogous, monochromatic, or complementary '
                'and share the observations in the forum.')
        self.assertEqual(rc.clean_prose(text, rules, 'U02/L17', log),
                         'When finished, classify the palettes as analogous, monochromatic, or complementary.')
        self.assertEqual(len(log.rows), 1)
        self.assertEqual(log.rows[0][1:], ('U02/L17', 'and share the observations in the forum.'))

    def test_standalone_forum_invitation_is_removed(self):
        rules = rc.load_rules(7)
        log = rc.Removals()
        self.assertEqual(rc.clean_prose('Share it in the forum.', rules, 'U02/L18', log), '')
        self.assertEqual(len(log.rows), 1)
        self.assertEqual(log.rows[0][1:], ('U02/L18', 'Share it in the forum.'))

    def test_forum_as_subject_of_teaching_is_kept(self):
        rules = rc.load_rules(7)
        log = rc.Removals()
        text = 'The forum of ancient Rome used a grid plan.'
        self.assertEqual(rc.clean_prose(text, rules, 'U02/L19', log), text)
        self.assertEqual(log.rows, [])

    def test_recommended_tools_are_kept(self):
        rules = rc.load_rules(7)
        html = ('<h2>Additional resources</h2><ul><li><h3>Recommended tools</h3>'
                '<p>Figma is free and runs on the web. Canva is a design tool.</p></li></ul>')
        out = rc.clean_html(html, rules, 'U02/Additional resources', rc.Removals())
        self.assertIn('Recommended tools', out)
        self.assertIn('Figma is free', out)
        self.assertIn('Canva is a design tool', out)

    def test_recommended_books_are_kept(self):
        rules = rc.load_rules(7)
        html = ('<h2>Additional resources</h2><ul><li><h3>Recommended books</h3>'
                '<p>Grid Systems in Graphic Design by Josef Müller-Brockmann.</p></li></ul>')
        out = rc.clean_html(html, rules, 'U02/Additional resources', rc.Removals())
        self.assertIn('Recommended books', out)
        self.assertIn('Grid Systems in Graphic Design', out)

    def test_intro_lessons(self):
        rules = rc.load_rules(7)
        self.assertTrue(rc.is_intro_lesson('Presentation (Who am I)', rules))
        self.assertFalse(rc.is_intro_lesson('Influences', rules))
        self.assertFalse(rc.is_intro_lesson('What will we do in the course?', rules))

    def test_intro_rules_exclude_whole_title_introductions_only(self):
        rules = rc.load_rules(5642)
        introductions = ['Presentation', 'Presentation (Who am I)', 'Presentación',
                         'Who am I?', 'Who I am?', 'About me', 'About Me']
        for title in introductions:
            self.assertTrue(rc.is_intro_lesson(title, rules), f'{title!r} should be excluded')
        for title in ['Presentation for screen 1', 'Presentation for screen 2']:
            self.assertFalse(rc.is_intro_lesson(title, rules), f'{title!r} should be kept')


class ExportTests(unittest.TestCase):
    def test_lesson_exports_as_cleaned_markdown_with_frames(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            text = VALID_LESSON.replace('in the frame.', 'in the frame. Follow me on Instagram for more.')
            lesson = LessonFixture(root, text)
            meta = json.loads((lesson.dir / 'lesson.json').read_text())
            out = root / 'out'
            log = rc.Removals()
            body, count = rc.export_lesson(meta, lesson.dir, rc.load_rules(1), log, out)
            self.assertEqual(count, 1)
            self.assertIn('Anchor: 1 · U1 · L02 · 00:05–01:30', body)
            self.assertIn('![1 · U1 · L02 · 00:40](frames/U01L02-F0040.jpg)', body)
            self.assertIn('On screen: "CONTRASTE"', body)
            self.assertIn('### Key points (derived)', body)
            self.assertNotIn('Follow me', body)
            self.assertEqual(len(log.rows), 1)
            self.assertTrue((out / 'frames' / 'U01L02-F0040.jpg').exists())

    def test_slug(self):
        self.assertEqual(rc.slug('¿Qué es la Presentación?'), 'que-es-la-presentacion')


@unittest.skipUnless(shutil.which('ffmpeg'), 'ffmpeg is required for frame extraction')
class FrameTests(unittest.TestCase):
    def test_many_subsecond_timestamps_keep_name_time_and_pixels_aligned(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            lesson = root / 'reading' / 'U01' / 'L02'
            frames = lesson / 'frames'
            frames.mkdir(parents=True)
            video = lesson / 'synthetic.mp4'
            subprocess.run([
                'ffmpeg', '-v', 'error', '-f', 'lavfi', '-i',
                'testsrc2=duration=20:size=640x360:rate=25', '-c:v', 'libx264',
                '-pix_fmt', 'yuv420p', '-an', '-y', str(video),
            ], check=True, capture_output=True, text=True)
            (lesson / 'lesson.json').write_text(json.dumps({
                'mp4': str(video), 'duration_seconds': 20,
            }), encoding='utf-8')

            # Preserve a pre-existing legacy entry while the command adds precise names.
            legacy = frames / 'F0003.jpg'
            rc.grab_frame(video, 3.25, legacy, 1600, 3)
            (lesson / 'frames.json').write_text(json.dumps({'F0003.jpg': 3.25}), encoding='utf-8')

            earlier = ['00:05.2']
            batch = ['00:17.4', '00:05.8', '00:02.13', '00:05.2', '00:14.5',
                     '00:00.4', '00:10.01', '00:01.8', '00:17.4']

            def run_frames(at_values):
                result = subprocess.run([
                    sys.executable, str(rc.HERE / 'reading_copy.py'), 'frames', str(lesson),
                    *sum((['--at', value] for value in at_values), []),
                ], check=True, capture_output=True, text=True)
                return [line.split('\t') for line in result.stdout.splitlines()]

            rows = run_frames(earlier) + run_frames(batch)
            requests = earlier + batch
            index = json.loads((lesson / 'frames.json').read_text(encoding='utf-8'))
            problems = []
            expected_dir = root / 'expected'
            expected_dir.mkdir()

            for number, (request, row) in enumerate(zip(requests, rows)):
                seconds = round(rc.parse_time(request), 2)
                total_centiseconds = round(seconds * 100)
                minutes, rest = divmod(total_centiseconds, 6000)
                whole_seconds, centiseconds = divmod(rest, 100)
                expected_name = f'F{minutes:02d}{whole_seconds:02d}.{centiseconds:02d}.jpg'
                expected_time = f'{minutes:02d}:{whole_seconds:02d}.{centiseconds:02d}'
                if len(row) != 2:
                    problems.append(f'{request}: malformed output row {row!r}')
                    continue
                name, printed_time = row
                frame_path = frames / name
                if name != expected_name:
                    problems.append(f'{request}: got ambiguous/noncanonical name {name}, expected {expected_name}')
                if printed_time != expected_time:
                    problems.append(f'{request}: printed {printed_time}, expected precise time {expected_time}')
                printed_seconds = rc.parse_time(printed_time)
                if not frame_path.exists():
                    problems.append(f'{request}: printed frame {name} does not exist')
                    continue
                if name not in index or abs(index[name] - printed_seconds) > 0.001:
                    problems.append(f'{request}: frames.json maps {name} to {index.get(name)!r}, expected {printed_seconds}')

                expected_path = expected_dir / f'{number}.jpg'
                rc.grab_frame(video, printed_seconds, expected_path, 1600, 3)
                with rc.Image.open(frame_path) as actual, rc.Image.open(expected_path) as expected:
                    if actual.convert('RGB').tobytes() != expected.convert('RGB').tobytes():
                        problems.append(f'{request}: frame pixels differ from a direct extraction at {printed_seconds:.2f}s')

            if len(rows) == len(requests) and len(rows) >= 3:
                first_same_second = frames / rows[0][0]
                second_same_second = frames / rows[2][0]
                if first_same_second.exists() and second_same_second.exists() and first_same_second.read_bytes() == second_same_second.read_bytes():
                    problems.append('the 5.2s and 5.8s samples unexpectedly contain identical image data')

            if len(rows) != len(requests):
                problems.append(f'got {len(rows)} output rows for {len(requests)} requests')
            if index.get('F0003.jpg') != 3.25 or not legacy.exists():
                problems.append('the existing frames.json entry F0003.jpg was not preserved')
            self.assertFalse(problems, '\n'.join(problems))


class CandidateTests(unittest.TestCase):
    def test_candidates_take_segment_ends_and_long_segment_samples(self):
        times = rc.candidate_times([10.0, 100.0], [(20.0, 26.0)], 120.0)
        self.assertIn(9.5, times)
        self.assertIn(99.5, times)
        self.assertIn(40.0, times)
        self.assertEqual(times, sorted(times))


if __name__ == '__main__':
    unittest.main()
