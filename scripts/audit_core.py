"""Mechanical checks only; semantic story audit requires contextual reading."""
import argparse, fnmatch, re
from pathlib import Path

def load_config(root):
    p = root / "project.yaml"
    if not p.exists(): return {}
    try:
        import yaml
        return yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    except ImportError:
        return {"_warning":"PyYAML is not installed; project.yaml was not parsed."}
    except Exception as exc:
        return {"_warning":f"Could not parse project.yaml: {exc}"}

def collect_files(root, config):
    m = config.get("manuscript", {})
    includes = m.get("include", ["**/*.md", "**/*.txt"])
    excludes = m.get("exclude", [])
    result = []
    for p in root.rglob("*"):
        if not p.is_file(): continue
        rel = p.relative_to(root).as_posix()
        if rel.startswith(".git/") or rel.startswith("novel-editor-reports/"): continue
        if any(fnmatch.fnmatch(rel, x) for x in includes) and not any(fnmatch.fnmatch(rel, x) for x in excludes):
            result.append(p)
    return sorted(result)

def scan(path, constraints):
    text = path.read_text(encoding="utf-8", errors="replace")
    out = []
    if constraints.get("em_dash_forbidden"):
        for n, line in enumerate(text.splitlines(), 1):
            if "—" in line:
                out.append({"severity":"ERROR","category":"PROJECT_CONSTRAINT","title":"Em dash dilarang oleh konfigurasi","file":str(path),"line":n,"quote":line.strip(),"problem":"em_dash_forbidden aktif di project.yaml."})
    wc = constraints.get("word_count", {})
    if wc.get("enabled"):
        count = len(re.findall(r"\b[\w'-]+\b", text, flags=re.UNICODE))
        lo, hi = wc.get("min_per_chapter"), wc.get("max_per_chapter")
        if lo is not None and count < lo:
            out.append({"severity":"REVIEW","category":"PROJECT_CONSTRAINT","title":"Jumlah kata di bawah batas","file":str(path),"line":None,"quote":"","problem":f"{count} kata; minimum {lo}."})
        if hi is not None and count > hi:
            out.append({"severity":"REVIEW","category":"PROJECT_CONSTRAINT","title":"Jumlah kata di atas batas","file":str(path),"line":None,"quote":"","problem":f"{count} kata; maksimum {hi}."})
    for n, line in enumerate(text.splitlines(), 1):
        if re.search(r"\b(\w+)(?:\s+\1){1,}\b", line, re.I):
            out.append({"severity":"REVIEW","category":"REPETITION","title":"Kata berulang berdekatan","file":str(path),"line":n,"quote":line.strip(),"problem":"Indikasi mekanis; bisa typo atau penekanan disengaja."})
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    args = ap.parse_args()
    root = Path(args.root).resolve()
    config = load_config(root)
    if config.get("_warning"): print("WARNING:", config["_warning"])
    files = collect_files(root, config)
    findings = []
    for p in files: findings.extend(scan(p, config.get("constraints", {})))
    print(f"Files inspected: {len(files)}")
    print(f"Mechanical findings: {len(findings)}")
    for i, f in enumerate(findings, 1):
        print(f"\n[{i}] {f['severity']} {f['category']} — {f['title']}")
        print(f"{f['file']}:{f.get('line') or '?'}")
        if f.get("quote"): print("Evidence:", f["quote"])
        print("Problem:", f["problem"])
    print("\nMechanical scan does not verify plot logic, worldbuilding, or semantic continuity.")
    print("Use AGENTS.md and EDITOR-PROTOCOL.md for contextual AI audit.")

if __name__ == "__main__": main()
