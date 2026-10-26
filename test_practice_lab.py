import tempfile
import unittest
from pathlib import Path

from practice_lab import database_demo, file_summary


class PracticeLabTests(unittest.TestCase):
    def test_file_summary_ignores_blank_lines(self):
        with tempfile.TemporaryDirectory() as folder:
            score_file = Path(folder) / "scores.txt"
            score_file.write_text("80\n\n100\n", encoding="utf-8")
            self.assertEqual(file_summary(score_file), (2, 80, 100, 90.0))

    def test_database_demo_uses_isolated_database_and_sorted_results(self):
        self.assertEqual(database_demo(), [("周", 96), ("林", 94), ("陈", 91)])


if __name__ == "__main__":
    unittest.main()
