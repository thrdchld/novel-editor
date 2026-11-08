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
