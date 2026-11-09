"""Mechanical manuscript checks. Semantic story and language review require contextual reading."""
import argparse
import re
from pathlib import Path

def load_config(root):
    config_path = root / "project.yaml"
    if not config_path.exists():
        return {}
    try:
        import yaml
        return yaml.safe_load(config_path.read_text(encoding="utf-8")) or {}
    except ImportError:
        return {"_warning": "PyYAML is not installed; project.yaml was not parsed."}
    except Exception as exc:
        return {"_warning": f"Could not parse project.yaml: {exc}"}

def collect_files(root, config):
    manuscript = config.get("manuscript", {})
    includes = manuscript.get("include", ["**/*.md", "**/*.txt"])
    excludes = manuscript.get("exclude", [])
    found = set()
    for pattern in includes:
        for path in root.glob(pattern):
            if path.is_file() and not any(path.relative_to(root).match(x) for x in excludes):
                found.add(path)
    return sorted(found)

def chapter_sections(text, heading_pattern):
    try:
        pattern = re.compile(heading_pattern, re.I)
    except re.error as exc:
        return [], f"Invalid chapter_heading_regex in project.yaml: {exc}"
    lines = text.splitlines()
    matches = []
    for index, line in enumerate(lines):
        match = pattern.search(line)
        if match:
            try:
                matches.append((index, int(match.group(1))))
            except (IndexError, ValueError):
                continue
    sections = []
    for position, (start, number) in enumerate(matches):
        end = matches[position + 1][0] if position + 1 < len(matches) else len(lines)
        sections.append((number, start + 1, "\n".join(lines[start:end])))
    return sections, None

def count_words(text):
    text = re.sub(r"(?m)^#{1,6}.*$", "", text)
    text = re.sub(r"(?m)^\s*[-*_]{3,}\s*$", " ", text)
    text = re.sub(r"[*_~]", "", text)
    return len(re.findall(r"[\w]+(?:['’-][\w]+)*", text, flags=re.UNICODE))

def scan(path, constraints):
    source = path.read_text(encoding="utf-8", errors="replace")
    lines = source.splitlines()
    findings = []
    markdown = constraints.get("markdown_format", {})

    if constraints.get("em_dash_forbidden"):
        for number, line in enumerate(lines, 1):
            if "—" in line:
                findings.append({
                    "severity": "ERROR", "category": "PROJECT_CONSTRAINT",
                    "title": "Em dash dilarang oleh konfigurasi", "file": str(path),
                    "line": number, "quote": line.strip(),
                    "problem": "em_dash_forbidden aktif di project.yaml."
                })

    heading_pattern = markdown.get(
        "chapter_heading_regex",
        r"^\s{0,3}#{1,6}\s+\*{0,3}BAB\s+(\d+)\b"
    )
    sections = []
    if markdown.get("enabled"):
        if markdown.get("check_unclosed_fences", True):
            fence_lines = [
                i for i, line in enumerate(lines, 1)
                if re.match(r"^\s{0,3}(?:\x60{3,}|~{3,})", line)
            ]
            if len(fence_lines) % 2:
                n = fence_lines[-1]
                findings.append({
                    "severity": "HIGH", "category": "MARKDOWN_FORMAT",
                    "title": "Code fence tidak tertutup", "file": str(path),
                    "line": n, "quote": lines[n - 1].strip(),
                    "problem": "Jumlah pembuka/penutup code fence tidak berpasangan."
                })

        sections, error = chapter_sections(source, heading_pattern)
        if error:
            findings.append({
                "severity": "REVIEW", "category": "PROJECT_CONSTRAINT",
                "title": "Konfigurasi heading bab tidak valid", "file": str(path),
                "line": None, "quote": heading_pattern, "problem": error
            })

        if markdown.get("check_chapter_sequence") and sections:
            numbers = [n for n, _, _ in sections]
            duplicates = sorted({n for n in numbers if numbers.count(n) > 1})
            for duplicate in duplicates:
                n = next(line_no for number, line_no, _ in sections if number == duplicate)
                findings.append({
                    "severity": "ERROR", "category": "DOCUMENT_STRUCTURE",
                    "title": f"Nomor bab duplikat: BAB {duplicate}", "file": str(path),
                    "line": n, "quote": lines[n - 1].strip(),
                    "problem": "Nomor bab muncul lebih dari satu kali."
                })
            missing = [n for n in range(min(numbers), max(numbers) + 1) if n not in set(numbers)]
            if missing:
                findings.append({
                    "severity": "REVIEW", "category": "DOCUMENT_STRUCTURE",
                    "title": "Nomor bab hilang", "file": str(path), "line": None,
                    "quote": ", ".join(map(str, missing)),
                    "problem": "Ada celah nomor bab; pastikan bukan penomoran yang memang disengaja."
                })

        for pattern_text in markdown.get("stray_note_patterns", []):
            try:
                pattern = re.compile(pattern_text)
            except re.error as exc:
                findings.append({
                    "severity": "REVIEW", "category": "PROJECT_CONSTRAINT",
                    "title": "Pola catatan editor tidak valid", "file": str(path),
                    "line": None, "quote": pattern_text,
                    "problem": f"Regex tidak dapat dikompilasi: {exc}"
                })
                continue
            for n, line in enumerate(lines, 1):
                if pattern.search(line):
                    findings.append({
                        "severity": "REVIEW", "category": "EDITORIAL_ARTIFACT",
                        "title": "Kemungkinan catatan/placeholder tertinggal",
                        "file": str(path), "line": n, "quote": line.strip(),
                        "problem": f"Baris cocok dengan pola {pattern_text!r}; verifikasi konteks sebelum menghapus."
                    })

    word_config = constraints.get("word_count", {})
    if word_config.get("enabled"):
        if not sections:
            sections, error = chapter_sections(source, heading_pattern)
        if error or not sections:
            findings.append({
                "severity": "REVIEW", "category": "PROJECT_CONSTRAINT",
                "title": "Jumlah kata per bab tidak dapat dihitung", "file": str(path),
                "line": None, "quote": "",
                "problem": error or "Heading bab tidak ditemukan dengan chapter_heading_regex."
            })
        else:
            minimum = word_config.get("min_per_chapter")
            maximum = word_config.get("max_per_chapter")
            for number, line_no, chapter_text in sections:
                total = count_words(chapter_text)
                if minimum is not None and total < minimum:
                    findings.append({
                        "severity": "REVIEW", "category": "PROJECT_CONSTRAINT",
                        "title": f"BAB {number} di bawah batas jumlah kata", "file": str(path),
                        "line": line_no, "quote": f"{total} kata",
                        "problem": f"Jumlah kata {total}; minimum yang dikonfigurasi {minimum}."
                    })
                if maximum is not None and total > maximum:
                    findings.append({
                        "severity": "REVIEW", "category": "PROJECT_CONSTRAINT",
                        "title": f"BAB {number} melebihi batas jumlah kata", "file": str(path),
                        "line": line_no, "quote": f"{total} kata",
                        "problem": f"Jumlah kata {total}; maksimum yang dikonfigurasi {maximum}."
                    })

    for n, line in enumerate(lines, 1):
        if re.search(r"\b(\w+)(?:\s+\1){1,}\b", line, re.I):
            findings.append({
                "severity": "REVIEW", "category": "REPETITION",
                "title": "Kata berulang berdekatan", "file": str(path),
                "line": n, "quote": line.strip(),
                "problem": "Indikasi mekanis; bisa typo atau penekanan disengaja."
            })
    return findings

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    config = load_config(root)
    if config.get("_warning"):
        print("WARNING:", config["_warning"])
    files = collect_files(root, config)
    print(f"Manuscript files inspected: {len(files)}")
    if not files:
        print("WARNING: No manuscript files matched manuscript.include. Check project.yaml.")
        return
    findings = []
    for path in files:
        print(f" - {path.relative_to(root).as_posix()}")
        findings.extend(scan(path, config.get("constraints", {})))
    print(f"Mechanical findings: {len(findings)}")
    for index, finding in enumerate(findings, 1):
        print(f"\n[{index}] {finding['severity']} {finding['category']} — {finding['title']}")
        print(f"{finding['file']}:{finding.get('line') or '?'}")
        if finding.get("quote"):
            print("Evidence:", finding["quote"])
        print("Problem:", finding["problem"])
    print("\nMechanical scan does not replace contextual story, spelling, or grammar review.")
    print("Use AGENTS.md, EDITOR-PROTOCOL.md, and rules/ for the full audit.")

if __name__ == "__main__":
    main()
