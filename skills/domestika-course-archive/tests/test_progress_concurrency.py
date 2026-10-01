import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))

import reading_copy as rc  # noqa: E402


class ProgressConcurrencyTests(unittest.TestCase):
    def test_parallel_lesson_updates_preserve_every_entry(self):
        with tempfile.TemporaryDirectory() as tmp:
            workdir = Path(tmp)
            rc.save_progress(workdir, {'existing': {'state': 'prepared'}})
            start = workdir / 'start'
            worker = '''
import sys
import time
from pathlib import Path
sys.path.insert(0, sys.argv[1])
import reading_copy as rc
workdir, start, lesson = Path(sys.argv[2]), Path(sys.argv[3]), sys.argv[4]
while not start.exists():
    time.sleep(0.005)
with rc.progress_transaction(workdir) as progress:
    progress[lesson] = {'state': 'checked'}
    time.sleep(0.02)
'''
            processes = [
                subprocess.Popen([
                    sys.executable, '-c', worker, str(rc.HERE), str(workdir), str(start), str(lesson),
                ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                for lesson in range(12)
            ]
            try:
                start.touch()
                results = [process.communicate(timeout=45) for process in processes]
                failures = [f'exit={process.returncode}, stdout={out!r}, stderr={err!r}'
                            for process, (out, err) in zip(processes, results) if process.returncode]
                self.assertEqual(failures, [])
            finally:
                for process in processes:
                    if process.poll() is None:
                        process.kill()
                        process.communicate()

            progress = json.loads(rc.progress_path(workdir).read_text(encoding='utf-8'))
            self.assertEqual(set(progress), {'existing', *(str(lesson) for lesson in range(12))})
            self.assertEqual(progress['existing'], {'state': 'prepared'})
            self.assertTrue(all(progress[str(lesson)] == {'state': 'checked'} for lesson in range(12)))

    def test_malformed_existing_progress_raises(self):
        with tempfile.TemporaryDirectory() as tmp:
            workdir = Path(tmp)
            path = rc.progress_path(workdir)
            path.parent.mkdir(parents=True)
            path.write_text('{broken', encoding='utf-8')
            with self.assertRaises(json.JSONDecodeError):
                rc.load_progress(workdir)


if __name__ == '__main__':
    unittest.main()
