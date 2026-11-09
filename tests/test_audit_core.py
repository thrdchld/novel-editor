import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from audit_core import collect_files, scan


class Tests(unittest.TestCase):
    def run_scan(self, content, config):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "x.md"
            path.write_text(content, encoding="utf-8")
            return scan(path, config)

    def test_em_dash_not_forbidden_by_default(self):
        self.assertEqual(self.run_scan("Kalimat — contoh.", {}), [])

    def test_em_dash_project_rule(self):
        findings = self.run_scan("Kalimat — contoh.", {"em_dash_forbidden": True})
        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0]["severity"], "ERROR")

    def test_word_count_is_optional(self):
        findings = self.run_scan(
            "# BAB 1\nSatu dua tiga.",
            {"word_count": {"enabled": False, "min_per_chapter": 500}},
        )
        self.assertEqual(findings, [])

    def test_word_count_per_chapter(self):
        findings = self.run_scan(
            "# BAB 1\nSatu dua tiga.\n# BAB 2\nEmpat lima.",
            {
                "word_count": {
                    "enabled": True,
                    "min_per_chapter": 3,
                    "max_per_chapter": 3,
                },
                "markdown_format": {
                    "chapter_heading_regex": r"^#\s+BAB\s+(\d+)\b"
                },
            },
        )
        self.assertEqual(len(findings), 1)
        self.assertIn("BAB 2", findings[0]["title"])

    def test_duplicate_and_missing_chapter_numbers(self):
        findings = self.run_scan(
            "# BAB 1\nIsi.\n# BAB 1\nIsi.\n# BAB 3\nIsi.",
            {
                "markdown_format": {
                    "enabled": True,
                    "check_chapter_sequence": True,
                    "chapter_heading_regex": r"^#\s+BAB\s+(\d+)\b",
                }
            },
        )
        self.assertTrue(any("duplikat" in f["title"].lower() for f in findings))
        self.assertTrue(any("hilang" in f["title"].lower() for f in findings))

    def test_unclosed_fence(self):
        fence = chr(96) * 3
        findings = self.run_scan(
            fence + "python\nprint('x')",
            {"markdown_format": {"enabled": True, "check_unclosed_fences": True}},
        )
        self.assertTrue(any("fence" in f["title"].lower() for f in findings))

    def test_editorial_artifact(self):
        findings = self.run_scan(
            "Catatan Editor: periksa ini",
            {
                "markdown_format": {
                    "enabled": True,
                    "stray_note_patterns": [r"Catatan Editor"]
                }
            },
        )
        self.assertTrue(any("catatan" in f["title"].lower() for f in findings))

    def test_collect_files_includes_story_folder(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "Story").mkdir()
            (root / "rules").mkdir()
            (root / "Story" / "novel.md").write_text("isi", encoding="utf-8")
            (root / "rules" / "rule.md").write_text("rule", encoding="utf-8")
            config = {
                "manuscript": {
                    "include": ["Story/**/*.md"],
                    "exclude": []
                }
            }
            files = collect_files(root, config)
            paths = [path.relative_to(root).as_posix() for path in files]
            self.assertEqual(paths, ["Story/novel.md"])


if __name__ == "__main__":
    unittest.main()
