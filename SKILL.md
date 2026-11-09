---
name: novel-editor
description: Audit and technically edit novels without judging tone, style, voice, or artistic diction. Checks plot logic, causality, timeline, continuity, worldbuilding, character knowledge, setup/payoff, technical language correctness, punctuation, names and terms, Markdown structure, repetition, and publication readiness. Use when reviewing, checking, proofreading, preparing, or applying technical corrections to a novel manuscript.
---

# Novel Editor Skill

Use this repository as the technical editing standard.

## Required reading

Before auditing or editing:
1. Read \`AGENTS.md\`.
2. Read \`EDITOR-PROTOCOL.md\`.
3. Read \`project.yaml\` and verify manuscript/reference coverage.
4. Read the relevant files in \`rules/\` and \`checklists/\`.
5. Use the report templates in \`templates/\`.

## Operating rules

- This standard is genre-agnostic and applies to all genres, subgenres, hybrids, and forms of fiction.
- Treat genre labels as descriptive context only. Never impose genre tropes, formulas, required arcs, pacing, or endings unless the author explicitly asks for a brief/genre-fit evaluation.
- When genre-fit evaluation is requested, compare only against the author's stated brief and report it separately from technical story errors.

- Audit all technical dimensions defined in README and AGENTS.
- Do not judge or rewrite tone, style, voice, artistic diction, humor, or aesthetic preferences.
- Check objective spelling, typo, grammar, punctuation, terminology, factual consistency, Markdown, chapter structure, and editorial artifacts.
- Separate confirmed errors from uncertain findings.
- Support every non-INFO finding with exact evidence and location.
- Audit chapters individually and then cross-chapter dependencies.
- Build and maintain a fact ledger for long manuscripts.
- Give a practical publication-readiness decision: READY TO PUBLISH, READY WITH MINOR FIXES, NOT READY, or INSUFFICIENT EVIDENCE.
- Default to read-only. Edit manuscript files only when the user explicitly asks for corrections or authorizes editing.
- When editing is authorized, make minimal technical corrections, preserve the author's style, and verify every change plus its cross-chapter effects.

## Output

Produce:
1. audit scope and limitations;
2. findings with severity, release impact, evidence, reader impact, confidence, and minimal recommendation;
3. cross-chapter continuity/timeline summary;
4. technical manuscript summary;
5. publication-readiness decision.

Never claim a complete audit when files or chapters were omitted. Never call a manuscript perfect or defect-free merely because no issue was found.
