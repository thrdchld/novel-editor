import sys, tempfile, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from audit_core import scan

class Tests(unittest.TestCase):
    def run_scan(self, content, config):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "x.md"
            p.write_text(content, encoding="utf-8")
            return scan(p, config)
    def test_em_dash_not_forbidden_by_default(self):
        self.assertEqual(self.run_scan("Kalimat — contoh.", {}), [])
    def test_em_dash_project_rule(self):
        f = self.run_scan("Kalimat — contoh.", {"em_dash_forbidden": True})
        self.assertEqual(len(f), 1)
        self.assertEqual(f[0]["severity"], "ERROR")
    def test_word_count_is_optional(self):
        self.assertEqual(self.run_scan("Satu dua tiga.", {"word_count":{"enabled":False,"min_per_chapter":500}}), [])

if __name__ == "__main__": unittest.main()
