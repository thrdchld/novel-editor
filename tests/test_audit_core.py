import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from audit_core import collect_files, collect_refs, scan, scan_refs


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

    def test_scan_refs_on_catatan_sungkan_fixture(self):
        fixture_root = Path(__file__).resolve().parent / "fixtures" / "catatan-sungkan-pre-fix"
        markdown_output = scan_refs(fixture_root)
        by_chapter = collect_refs(fixture_root)

        self.assertIn("## Bab 18", markdown_output)
        self.assertIn("## Bab 21", markdown_output)
        self.assertIn("## Bab 25", markdown_output)
        self.assertIn("## Bab 31", markdown_output)

        bab_18_quotes = " ".join(item["quote"] for item in by_chapter[18])
        bab_21_quotes = " ".join(item["quote"] for item in by_chapter[21])
        bab_25_quotes = " ".join(item["quote"] for item in by_chapter[25])
        bab_31_quotes = " ".join(item["quote"] for item in by_chapter[31])

        self.assertIn("Kemarin", bab_18_quotes)
        self.assertIn("warung soto", bab_21_quotes)
        self.assertIn("warung soto", bab_25_quotes)
        self.assertIn("suasana kerja di Jogja", bab_31_quotes)

        # Dialogue tag "katanya" right after closing quote must not be flagged (e.g. Bab 3, Bab 9)
        bab_03_lines = [item["line"] for item in by_chapter.get(3, [])]
        self.assertNotIn(29, bab_03_lines)
        bab_09_lines = [item["line"] for item in by_chapter.get(9, [])]
        self.assertNotIn(29, bab_09_lines)
        self.assertNotIn(65, bab_09_lines)

        # "katanya" in narration (Bab 17) and inside quotes (Bab 26, 29, 31) must still be flagged
        bab_17_quotes = " ".join(item["quote"] for item in by_chapter[17])
        bab_26_quotes = " ".join(item["quote"] for item in by_chapter[26])
        bab_29_quotes = " ".join(item["quote"] for item in by_chapter[29])
        self.assertIn("martabak telur", bab_17_quotes)
        self.assertIn("katanya nggak sabar", bab_26_quotes)
        self.assertIn("Katanya urusan di sini", bab_29_quotes)
        bab_31_line_75 = next(item for item in by_chapter[31] if item["line"] == 75)
        self.assertIn("Katanya", bab_31_line_75["terms"])

    def test_scan_refs_catatan_sungkan_bab_25_kedai_kopi(self):
        fixture_root = Path(__file__).resolve().parent / "fixtures" / "catatan-sungkan-pre-fix"
        markdown_output = scan_refs(fixture_root)
        by_chapter = collect_refs(fixture_root)

        bab_25_line_21 = next(item for item in by_chapter[25] if item["line"] == 21)
        self.assertIn("kamu sendiri yang bilang di kedai kopi", bab_25_line_21["quote"].lower())
        self.assertIn("Kamu sendiri yang bilang", bab_25_line_21["terms"])
        self.assertIn("di kedai", bab_25_line_21["terms"])

        bab_25_section = markdown_output.split("## Bab 25", 1)[1].split("## Bab ", 1)[0]
        self.assertIn("Kamu sendiri yang bilang di kedai kopi", bab_25_section)

        # Past speech/locative references in other chapters are included
        bab_28_line_29 = next(item for item in by_chapter[28] if item["line"] == 29)
        self.assertIn("dia bilang", [t.lower() for t in bab_28_line_29["terms"]])
        bab_31_line_39 = next(item for item in by_chapter[31] if item["line"] == 39)
        self.assertIn("kamu bilang", [t.lower() for t in bab_31_line_39["terms"]])
        bab_13_line_11 = next(item for item in by_chapter[13] if item["line"] == 11)
        self.assertIn("di kedai", [t.lower() for t in bab_13_line_11["terms"]])
        bab_17_line_51 = next(item for item in by_chapter[17] if item["line"] == 51)
        self.assertIn("di warung", [t.lower() for t in bab_17_line_51["terms"]])

        # Non-past uses (future "yang bilang", general/hypothetical "di warung"/"di kafe") are excluded
        bab_27_lines = [item["line"] for item in by_chapter.get(27, [])]
        self.assertNotIn(51, bab_27_lines)
        bab_09_lines = [item["line"] for item in by_chapter.get(9, [])]
        self.assertNotIn(21, bab_09_lines)
        bab_02_line_33 = next(item for item in by_chapter[2] if item["line"] == 33)
        self.assertNotIn("di kafe", [t.lower() for t in bab_02_line_33["terms"]])

    def test_prapenulisan_report_template_has_verdict_section(self):
        template_path = (
            Path(__file__).resolve().parents[1] / "templates" / "prapenulisan-report.md"
        )
        self.assertTrue(template_path.is_file())
        content = template_path.read_text(encoding="utf-8")
        self.assertIn("## Vonis", content)
        self.assertIn("LAYAK DITULIS", content)
        self.assertIn("PERBAIKI DULU", content)
        self.assertIn("PREMIS/KERANGKA DIBUANG", content)


if __name__ == "__main__":
    unittest.main()
