# Editor Protocol

## Definisi masalah teknis
Masalah masuk lingkup bila teks bertentangan dengan fakta yang telah ditetapkan, melewatkan sebab penting, melanggar aturan dunia, kehilangan jejak state, atau meminta pembaca menerima kemustahilan yang berdampak pada plot tanpa penjelasan memadai.

Bukan masalah teknis hanya karena editor tidak menyukai pilihan artistik, kalimat, tone, atau teknik naratif.

## Uji temuan
1. Fakta/peristiwa apa yang dipersoalkan?
2. Di mana aturan/fakta relevan ditetapkan?
3. Apakah ada kontradiksi, sebab yang hilang, transisi mustahil, atau pengetahuan tanpa sumber?
4. Apakah penjelasan sengaja disimpan di bagian lain?
5. Apakah masalah berdampak pada pemahaman, stakes, atau kepercayaan pembaca?
6. Apakah ini ERROR/HIGH atau hanya REVIEW?

## Severity
| Level | Makna |
|---|---|
| ERROR | Kontradiksi langsung atau pelanggaran hard rule yang terbukti. |
| HIGH | Kegagalan logika, timeline, worldbuilding, atau continuity yang kuat dan mengganggu pemahaman. |
| REVIEW | Dugaan masalah/ambiguitas yang perlu keputusan penulis. |
| INFO | Catatan opsional, bukan vonis kesalahan. |

## Kategori
`PLOT_HOLE`, `CAUSALITY`, `TIMELINE`, `CHARACTER_CONTINUITY`, `OBJECT_CONTINUITY`, `LOCATION_CONTINUITY`, `RELATIONSHIP_CONTINUITY`, `WORLD_RULE_CONTRADICTION`, `WORLD_RULE_GAP`, `WORLD_STATE`, `CHARACTER_KNOWLEDGE`, `SETUP_PAYOFF`, `REPETITION`, `AI_SLOP`, `PROJECT_CONSTRAINT`, `PLAUSIBILITY`, `OTHER_TECHNICAL`.

## Hindari false positive
Tokoh boleh berbohong, lupa, salah ingat, atau bertindak tidak rasional. Narator boleh tidak dapat dipercaya. Aturan dunia boleh punya pengecualian. Misteri boleh menahan informasi. Repetisi bisa menjadi motif. AI-slop bukan bukti bahwa teks ditulis AI. Realisme dunia nyata hanya digunakan jika cerita mengklaim mengikuti kondisi nyata atau proyek meminta pemeriksaan tersebut.

## Cakupan audit
Laporkan file/bab yang dibaca, referensi yang diperiksa, jenis audit (bab/lintas bab/full manuscript), file hilang/tidak terbaca, keterbatasan, dan temuan yang masih provisional.


## 7. Publication-readiness gate
The audit must end with a practical release recommendation, not an endless list of refinements. The standard is **reader-ready**, not perfect.

Classify findings by release impact:
- **BLOCKER**: material issue that makes a major event impossible/contradictory under the story's rules, breaks an essential timeline or continuity chain, makes a key character act on unavailable knowledge, invalidates a central world rule, or prevents readers from understanding a major plot turn or ending.
- **FIX BEFORE RELEASE**: real technical issue, but limited in scope and repairable without restructuring the whole novel.
- **ACCEPTABLE / AUTHOR CHOICE**: intentional ambiguity, unresolved thread by design, minor realism variation, or an imperfection that does not materially impair comprehension.
- **OPTIONAL POLISH**: nonessential refinement. Never hold publication for this category.

Use the release outcomes from `rules/09-publication-readiness.md`. A novel can be READY WITH MINOR FIXES while still having imperfections. A deliberate mystery, open ending, unreliable narrator, morally flawed character, or genre-specific convention is not a defect by itself.

Never use “there are still things to improve” as the only reason to delay publication. Identify the reader-facing consequence and whether it crosses the blocker threshold.
