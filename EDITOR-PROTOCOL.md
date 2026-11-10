# Editor Protocol

## 1. Definisi audit teknis

Masalah teknis adalah masalah yang dapat dibuktikan dari teks, dokumen referensi, atau hard constraints dan dapat mengganggu logika, konsistensi, pemahaman, atau kesiapan naskah.

Cakupannya mencakup dua lapisan yang sama-sama wajib:
1. **Teknis cerita:** plot logic, causality, timeline dan orientasi waktu pembaca, continuity dan blocking adegan, worldbuilding, akurasi fakta/prosedur dunia nyata yang material, batas POV/character knowledge, setup/payoff, dan keterbacaan faktual.
2. **Teknis naskah:** ejaan, typo, tata bahasa objektif, tanda baca, konsistensi nama/istilah, struktur bab, Markdown, format, placeholder, dan catatan internal.

Bukan masalah teknis hanya karena editor tidak menyukai pilihan artistik, tone, voice, diksi, atau cara kalimat dibunyikan.

## 2. Netralitas genre

Standar ini berlaku untuk semua genre dan genre campuran. Label genre adalah konteks, bukan seperangkat aturan otomatis. Jangan mewajibkan trope, formula struktur, tipe tokoh, pola konflik, pacing, atau jenis ending berdasarkan konvensi genre. Pemeriksaan kesesuaian genre hanya dilakukan jika penulis secara eksplisit meminta evaluasi terhadap brief/target genre tertentu; nilai berdasarkan brief tersebut dan laporkan terpisah dari kesalahan teknis. Jika tidak diminta, jangan menilai apakah cerita cukup romantis, lucu, seram, fantastis, realistis, cepat, atau sesuai pasar.

## 3. Batas pemeriksaan bahasa

Periksa typo, ejaan baku, imbuhan, kata depan, kata ulang, bentuk gabungan, kapitalisasi, penulisan angka/tanggal jika tidak konsisten, tanda baca yang salah atau mengubah makna, tata bahasa yang secara objektif rusak hingga makna tidak jelas, rujukan kata ganti yang tidak memiliki referen, nama/istilah yang berubah-ubah, dialog yang kehilangan tanda kutip/pemisah, catatan editor, placeholder, TODO/FIXME, instruksi produksi, dan markup/format yang merusak tampilan.

Jangan perbaiki hanya karena ada sinonim yang terasa lebih bagus, kalimat terasa sederhana/panjang/pendek, tone tidak sesuai selera, metafora tidak disukai, atau editor ingin menyamakan semua kalimat ke satu gaya.

Jika tata bahasa punya lebih dari satu bentuk sah, jangan tandai sebagai ERROR. Gunakan REVIEW hanya bila ada dampak nyata pada makna atau konsistensi.

## 4. Uji temuan

1. Fakta/peristiwa/format apa yang dipersoalkan?
2. Di mana aturan/fakta relevan ditetapkan?
3. Apakah ada kontradiksi, sebab yang hilang, transisi mustahil, knowledge leak, state mismatch, atau kesalahan teknis objektif?
4. Apakah penjelasan sengaja disimpan di bagian lain?
5. Apakah pembaca tetap dapat mengenali waktu/tempat adegan, mengikuti blocking fisik, dan memahami batas POV? Jika ada prosedur dunia nyata yang material, apakah sudah diverifikasi?
6. Apakah masalah berdampak pada pemahaman, tampilan, stakes, atau kepercayaan pembaca?
7. Apakah ini ERROR/HIGH atau hanya REVIEW?
8. Apa koreksi terkecil yang menyelesaikan masalah tanpa mengubah gaya?

## 5. Severity

| Level | Makna |
|---|---|
| ERROR | Kontradiksi langsung, typo/fakta salah yang terbukti, atau pelanggaran hard rule yang terbukti. |
| HIGH | Kegagalan logika, timeline, worldbuilding, continuity, atau format yang kuat dan mengganggu pemahaman. |
| REVIEW | Dugaan masalah, ambiguitas, atau bentuk bahasa yang perlu verifikasi/keputusan penulis. |
| INFO | Catatan opsional, bukan vonis kesalahan. |

## 6. Release impact

| Kelas | Makna | Tindakan |
|---|---|---|
| BLOCKER | Masalah material yang merusak pemahaman, logika inti, continuity penting, timeline, aturan dunia sentral, atau membuat naskah tidak dapat dibaca secara teknis. | Wajib diperbaiki sebelum rilis. |
| FIX BEFORE RELEASE | Kesalahan teknis nyata tetapi lokal/terbatas, misalnya typo, heading rusak, catatan editor tertinggal, atau inkonsistensi faktual kecil. | Perbaiki dalam daftar singkat. |
| ACCEPTABLE / AUTHOR CHOICE | Ambiguitas disengaja, misteri, open ending, variasi realisme kecil, atau pilihan kreatif yang tidak merusak pemahaman. | Boleh dipertahankan. |
| OPTIONAL POLISH | Penyempurnaan non-esensial. | Tidak boleh menahan publikasi. |

Severity dan release impact adalah dua dimensi berbeda. Kesalahan ejaan dapat ERROR tetapi release impact-nya FIX BEFORE RELEASE, bukan otomatis BLOCKER. REVIEW tidak otomatis menahan publikasi.

## 7. Kategori

`PLOT_HOLE`, `CAUSALITY`, `TIMELINE`, `TEMPORAL_ORIENTATION`, `SCENE_BLOCKING`, `CHARACTER_CONTINUITY`, `OBJECT_CONTINUITY`, `LOCATION_CONTINUITY`, `RELATIONSHIP_CONTINUITY`, `WORLD_RULE_CONTRADICTION`, `WORLD_RULE_GAP`, `DOMAIN_FACTUALITY`, `WORLD_STATE`, `CHARACTER_KNOWLEDGE`, `POV_BOUNDARY`, `SETUP_PAYOFF`, `REPETITION`, `AI_SLOP`, `SPELLING_TYPO`, `GRAMMAR`, `PUNCTUATION`, `NAME_TERM_CONSISTENCY`, `MARKDOWN_FORMAT`, `DOCUMENT_STRUCTURE`, `EDITORIAL_ARTIFACT`, `PROJECT_CONSTRAINT`, `PLAUSIBILITY`, `OUTLINE_LEAKAGE`, `OTHER_TECHNICAL`.

## 8. Hindari false positive

Tokoh boleh berbohong, lupa, salah ingat, atau bertindak tidak rasional. Narator boleh tidak dapat dipercaya. Aturan dunia boleh punya pengecualian. Misteri boleh menahan informasi. Repetisi bisa menjadi motif. AI-slop bukan bukti bahwa teks ditulis AI. Realisme dunia nyata hanya digunakan jika cerita mengklaim mengikuti kondisi nyata atau proyek meminta pemeriksaan tersebut.

Jangan menandai pilihan gaya sebagai kesalahan bahasa. Jangan menuntut semua detail kosmetik konsisten jika tidak relevan. Jangan menganggap ejaan tidak baku dalam dialog sebagai typo bila jelas merupakan karakterisasi/ucapan tokoh dan tidak melanggar hard constraint proyek.

## 9. Cakupan audit

Laporkan file/bab yang dibaca, referensi yang diperiksa, jenis audit (bab/lintas bab/full manuscript), file hilang/tidak terbaca, konfigurasi yang tidak valid, dan temuan provisional. Pastikan naskah yang diminta benar-benar termasuk dalam daftar file hasil inventarisasi.

## 10. Kebijakan edit

Audit yang secara eksplisit diminta read-only tidak mengubah file. Namun, dalam workflow produksi Novel Editor pada folder novel, automatic technical repair adalah default yang telah diotorisasi. Perbaiki temuan objektif/terkonfirmasi dengan perubahan minimal. Jangan mengubah gaya, tone, voice, atau pilihan kreatif. Selesaikan analisis atas hal ambigu sebelum meminta keputusan. Minta keputusan penulis hanya jika alternatif material tetap sama kuat setelah prosedur rules/13-editorial-decision-making.md diterapkan. Setelah perubahan, lakukan pemeriksaan ulang pada perubahan dan dependensi lintas bab.

## 11. Editorial decision-making authority

Editor wajib mengambil keputusan berdasarkan bukti dan logika cerita, bukan sekadar melaporkan kontradiksi. Untuk setiap masalah, periksa konteks penuh, seluruh sumber canon/planning yang tersedia, versi dan status persetujuannya, urutan kejadian, sebab-akibat, state karakter, pengetahuan tokoh, serta setup/payoff lintas bab.

Pilih versi yang paling konsisten dan membutuhkan perubahan paling kecil. Tentukan secara eksplisit dokumen yang harus diperbaiki: manuskrip, outline, timeline, bible, atau canon. Klasifikasikan hasil sebagai:
- MANUSCRIPT ERROR: manuskrip menyimpang dari canon yang konsisten.
- OUTLINE ERROR: outline/timeline bertentangan dengan bukti cerita yang lebih koheren atau dengan dirinya sendiri.
- CANON CONFLICT: sumber-sumber kanonis saling bertentangan dan belum ada dasar untuk mengutamakan salah satunya.
- INTENTIONAL DEVIATION: manuskrip berbeda dari outline tetapi tetap logis dan berfungsi.
- UNRESOLVED AUTHOR CHOICE: alternatif material tetap sama kuat setelah seluruh bukti diperiksa.

Klarifikasi hanya boleh diminta untuk UNRESOLVED AUTHOR CHOICE. Sebelum bertanya, tampilkan alternatif, bukti pendukung masing-masing, analisis, rekomendasi editor, confidence, dan konsekuensi. Jangan meminta penulis memilih fakta yang dapat ditentukan melalui kronologi atau logika internal.

Jangan diam-diam mengubah canon yang disahkan. Jika canon perlu diperbarui, rekomendasikan perubahan eksplisit. Izin memperbaiki repo/editor tidak otomatis memberi izin mengubah manuskrip. Setelah setiap koreksi, verifikasi dependensi lintas bab.

Lihat rules/13-editorial-decision-making.md untuk hierarki sumber, prosedur keputusan, dan format laporan lengkap.

## 12. Publication-readiness gate

Gunakan `rules/09-publication-readiness.md`. Standarnya reader-ready, bukan sempurna. Jangan gunakan “masih ada yang bisa diperbaiki” sebagai alasan menunda publikasi. Tunjukkan konsekuensi bagi pembaca dan apakah masalah melampaui ambang blocker.

## 13. Outline leakage audit

Wajib baca dan terapkan `rules/12-outline-leakage.md` pada audit naskah. Outline, timeline, beat sheet, character bible, world bible, prompt, dan catatan penulis adalah panduan internal, bukan materi yang harus disalin ke prosa. Periksa tanggal mentah, label struktur/beat, ringkasan karakter, tujuan adegan, label arc/emosi, worldbuilding dump, foreshadowing/reveal instruction, repetisi fakta, artefak produksi, dan pola generatif mekanis. Pisahkan fakta canon dari cara penyampaiannya. Jika dokumen outline tidak tersedia, lakukan surface scan dan nyatakan keterbatasannya; jangan klaim perbandingan langsung. Setiap kandidat harus diuji berdasarkan kebutuhan pembaca, kewajaran POV/tokoh, pengulangan, dan dampak bila dihapus. Jangan menghapus informasi penting atau mengubah gaya hanya karena mirip outline.



## 14. Automatic repair workflow
Default production workflow is Mode A. When asked to run Novel Editor on a project, do not stop at findings if a correction is technically determinable. Inventory/read sources, establish canon/version and fact ledger, audit with evidence, decide the correct document to change, apply the smallest patch, update dependencies, save, reopen the saved result, re-audit affected sections and cross-chapter links, then report changes and readiness. Do not ask approval for each technical correction. Ask only for material creative choices unresolved after analysis. Preserve LOCKED canon; no silent retcons. An explicit read-only request overrides automatic repair.

## 15. Outline Gate
Before drafting, apply rules/14-outline-validation.md. Accept any readable outline structure; the universal template is a completeness reference, not a mandatory schema. Preserve freeform notes and AI-added sections. An outline is ready when technically coherent and sufficiently detailed for drafting, not when every optional field is filled. Statuses: APPROVED FOR DRAFTING, APPROVED WITH TRACKED FLEXIBILITY, REPAIR REQUIRED, AUTHOR DECISION REQUIRED, INSUFFICIENT EVIDENCE.

## 16. Multi-novel layout
Treat each Story/<Novel Title>/ as independent. Root config is generic; per-novel config overrides it. Keep reports and continuity artifacts inside the corresponding novel folder. Do not mix facts across novels unless a shared universe is explicitly configured.
