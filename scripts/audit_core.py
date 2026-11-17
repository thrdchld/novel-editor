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

DEFAULT_EXCLUDES = [
    "outline.md",
    "**/outline.md",
    "canon.md",
    "**/canon.md",
    "timeline.md",
    "**/timeline.md",
    "ledger.md",
    "**/ledger.md",
    "state.md",
    "**/state.md",
    "EXPECTED-FINDINGS.md",
    "**/EXPECTED-FINDINGS.md",
    "reports/**",
    "**/reports/**",
]

REF_REGEX = re.compile(
    r"(?<!-)\b("
    r"kemarin\s+lusa"
    r"|kemarin"
    r"|tadi\s+pagi"
    r"|tadi\s+malam"
    r"|(?:tiga|dua|empat)\s+minggu\s+(?:yang\s+)?lalu"
    r"|minggu\s+(?:yang\s+)?lalu"
    r"|bulan\s+(?:yang\s+)?lalu"
    r"|pernah\s+bilang"
    r"|kamu\s+pernah"
    r"|kamu\s+sendiri\s+yang\s+bilang"
    r"|kamu\s+bilang"
    r"|yang\s+bilang"
    r"|dia\s+bilang"
    r"|kata\s+kamu"
    r"|waktu\s+itu"
    r"|ceritanya"
    r"|katanya"
    r"|dulu"
    r"|di\s+kedai"
    r"|di\s+warung"
    r"|di\s+kafe"
    r")\b",
    re.I,
)

DIALOGUE_TAG_WORDS = {"katanya", "ujarnya", "jawabnya", "kataku"}

SPEECH_REF_PHRASES = {
    "kamu sendiri yang bilang",
    "kamu bilang",
    "yang bilang",
    "dia bilang",
    "kata kamu",
    "kamu pernah",
}

LOCATIVE_REF_PHRASES = {"di kedai", "di warung", "di kafe"}

NON_PAST_SPEECH_RE = re.compile(
    r"\b(?:"
    r"besok|lusa|nanti|ntar|kelak|suatu\s+saat|kapan-kapan"
    r"|minggu\s+depan|bulan\s+depan|tahun\s+depan|sebentar\s+lagi|bentar\s+lagi"
    r"|akan|bakal|bakalan|biar|biarkan|supaya|agar|tolong|coba|ayo|mari|silakan"
    r"|mending|lebih\s+baik|sebaiknya|suruh|jangan|tinggal|harus|mesti|perlu|wajib|hendak|mau"
    r")\b",
    re.I,
)

FUTURE_ADVERB_RE = re.compile(
    r"\b(?:besok|lusa|nanti|ntar|minggu\s+depan|bulan\s+depan|tahun\s+depan)\b",
    re.I,
)

PAST_ANCHOR_RE = re.compile(
    r"\b(?:"
    r"kemarin(?:\s+lusa)?|dulu|tadi(?:\s+(?:pagi|siang|sore|malam))?|semalam|tempo\s+hari|sebelumnya|barusan"
    r"|pernah|sempat"
    r"|(?:(?:dua|tiga|empat|lima|enam|tujuh|delapan|sembilan|sepuluh|se|beberapa|\d+)\s+)?"
    r"(?:hari|minggu|bulan|tahun|jam|menit|detik|malam|pagi|siang|sore|senin|selasa|rabu|kamis|jumat|sabtu)\s+"
    r"(?:yang\s+)?lalu"
    r"|yang\s+lalu"
    r"|(?:waktu|saat)\s+itu"
    r")\b",
    re.I,
)

LOCATIVE_PAST_CUE_RE = re.compile(
    r"\b(?:"
    r"kemarin(?:\s+lusa)?|dulu|tadi(?:\s+(?:pagi|siang|sore|malam))?|semalam|tempo\s+hari|sebelumnya|barusan"
    r"|pernah|sempat"
    r"|(?:(?:dua|tiga|empat|lima|enam|tujuh|delapan|sembilan|sepuluh|se|beberapa|\d+)\s+)?"
    r"(?:hari|minggu|bulan|tahun|jam|menit|detik|malam|pagi|siang|sore|senin|selasa|rabu|kamis|jumat|sabtu)\s+"
    r"(?:yang\s+)?lalu"
    r"|yang\s+lalu"
    r"|(?:waktu|saat)\s+itu"
    r"|(?:waktu|pas|sewaktu)\s+(?:[^,.!?]{0,30}\s+)?di\s+(?:kedai|warung|kafe)"
    r"|ingat|teringat|mengingat|keingat|inget|lupa|kelupaan|melupakan|terngiang|membekas|berputar\s+di\s+telinga\w*"
    r"|(?<!buku\s)cerita(?:nya)?|katanya|kata\s+(?:kamu|dia|aku|saya|mereka)|ngaku(?:nya)?|mengaku"
    r"|(?:kamu\s+sendiri\s+yang|kamu|yang|dia|pernah|sempat|sudah|udah|ku|kau)\s*bilang"
    r"|obrolan|percakapan|pembicaraan|pertemuan|kejadian|peristiwa|insiden|pertengkaran|perdebatan"
    r"|omongan|ucapan|perkataan|pengakuan"
    r")\b",
    re.I,
)

LOCATIVE_NON_PAST_RE = re.compile(
    r"\b(?:"
    r"besok|lusa|nanti|ntar|akan|bakal|bakalan|daripada|tolong|coba|ayo|mari|silakan|jangan"
    r"|biar|biarkan|supaya|agar|mending|sebaiknya|lebih\s+baik|suruh|tinggal|hendak"
    r"|kalau\s+(?:harus|mau|ingin|perlu)|mau\s+(?:ke|mampir|makan|minum|ketemu|nongkrong|nunggu)"
    r")\b",
    re.I,
)


def _is_dialogue_tag(line, match):
    word = re.sub(r"\s+", " ", match.group(0).strip()).lower()
    if word not in DIALOGUE_TAG_WORDS:
        return False
    prefix = line[:match.start()]
    return bool(re.search(r'\S["”\'’]\s+$', prefix))


def _is_past_reference(line, match):
    """Filter speech/locative ref candidates so future, hortative, or current-scene uses are skipped."""
    term = re.sub(r"\s+", " ", match.group(0).strip()).lower()
    if term not in SPEECH_REF_PHRASES and term not in LOCATIVE_REF_PHRASES:
        return True

    sentence, local_start = _sentence_context(line, match.span())
    before = sentence[:local_start]
    clause_before = re.split(r"[,;:—–\"“]|(?<!\w)['‘]", before)[-1]
    quote_clause_before = re.split(r"[\"“]", before)[-1]

    if term in SPEECH_REF_PHRASES:
        if term == "kamu pernah":
            return not re.search(r"\bjangan\s+sampai\b", clause_before, re.I)
        if NON_PAST_SPEECH_RE.search(clause_before):
            if PAST_ANCHOR_RE.search(clause_before):
                return True
            # Rhetorical "kenapa/kok ... harus bilang ..." reacts to something already said.
            if re.match(r"^\s*(?:kenapa|mengapa|kok)\b", clause_before.strip(), re.I) and not re.search(
                r"\b(?:besok|lusa|nanti|ntar|akan|bakal|bakalan|biar|tolong|coba|jangan)\b",
                clause_before,
                re.I,
            ):
                return True
            return False
        if FUTURE_ADVERB_RE.search(quote_clause_before) and not PAST_ANCHOR_RE.search(quote_clause_before):
            return False
        return True

    if LOCATIVE_NON_PAST_RE.search(sentence) and not PAST_ANCHOR_RE.search(sentence):
        return False
    return bool(LOCATIVE_PAST_CUE_RE.search(sentence))


def collect_files(root, config):
    manuscript = config.get("manuscript", {})
    if "include" in manuscript:
        includes = manuscript["include"]
    elif (root / "chapters").is_dir():
        includes = ["chapters/**/*.md", "chapters/**/*.txt"]
    elif (root / "manuscript.md").is_file():
        includes = ["manuscript.md"]
    else:
        includes = ["**/*.md", "**/*.txt"]
    excludes = manuscript.get("exclude", DEFAULT_EXCLUDES)
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


def _sentence_context(line, match_span):
    stripped = line.strip()
    lead = len(line) - len(line.lstrip())
    sentences = re.split(r"(?<=[.!?])\s+(?=[\"“A-Z])", stripped)
    if len(sentences) > 1:
        offset = 0
        start_idx = match_span[0] - lead
        for sent in sentences:
            pos = stripped.find(sent, offset)
            if pos != -1 and pos <= start_idx < pos + len(sent) + 1:
                return sent.strip(), max(0, start_idx - pos)
            if pos != -1:
                offset = pos + len(sent)
    return stripped, max(0, match_span[0] - lead)


def _short_quote(line, match_span):
    sentence, _ = _sentence_context(line, match_span)
    return sentence


def collect_refs(target, config=None):
    config = config or {}
    constraints = config.get("constraints", {})
    markdown = constraints.get("markdown_format", {})
    heading_pattern = markdown.get(
        "chapter_heading_regex",
        r"^\s{0,3}#{1,6}\s+\*{0,3}BAB\s+(\d+)\b",
    )
    target_path = Path(target).resolve()
    if target_path.is_file():
        files = [target_path]
    else:
        files = collect_files(target_path, config)

    by_chapter = {}
    for path in files:
        source = path.read_text(encoding="utf-8", errors="replace")
        sections, _ = chapter_sections(source, heading_pattern)
        if not sections:
            stem_match = re.search(r"bab[-_\s]*(\d+)", path.stem, re.I)
            chap_num = int(stem_match.group(1)) if stem_match else 0
            sections = [(chap_num, 1, source)]
        for chap_num, start_line, chap_text in sections:
            entries = by_chapter.setdefault(chap_num, [])
            for offset, line in enumerate(chap_text.splitlines()):
                if offset == 0 and re.search(heading_pattern, line, re.I):
                    continue
                matches = [
                    m for m in REF_REGEX.finditer(line)
                    if not _is_dialogue_tag(line, m) and _is_past_reference(line, m)
                ]
                if not matches:
                    continue
                line_no = start_line + offset
                seen_quotes = set()
                matched_terms = []
                quotes = []
                for m in matches:
                    term = re.sub(r"\s+", " ", m.group(0))
                    matched_terms.append(term)
                    q = _short_quote(line, m.span())
                    if q not in seen_quotes:
                        seen_quotes.add(q)
                        quotes.append(q)
                entries.append({
                    "chapter": chap_num,
                    "file": str(path),
                    "line": line_no,
                    "terms": matched_terms,
                    "quote": " | ".join(quotes),
                })
    return by_chapter


def scan_refs(target, config=None):
    by_chapter = collect_refs(target, config)
    out = ["# Daftar Rujukan Mundur dan Waktu Relatif"]
    for chap_num in sorted(by_chapter):
        entries = by_chapter[chap_num]
        if not entries:
            continue
        heading = f"## Bab {chap_num}" if chap_num else "## Tanpa Nomor Bab"
        out.append("")
        out.append(heading)
        for item in entries:
            terms_str = ", ".join(f"`{t}`" for t in item["terms"])
            out.append(f"- Baris {item['line']} ({terms_str}): {item['quote']}")
    return "\n".join(out)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument(
        "--refs",
        action="store_true",
        help="Hasilkan daftar markdown rujukan mundur dan kata waktu relatif per bab.",
    )
    args = parser.parse_args()
    root = Path(args.root).resolve()
    config = load_config(root)
    if config.get("_warning"):
        print("WARNING:", config["_warning"])
    if args.refs:
        print(scan_refs(root, config))
        return
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
