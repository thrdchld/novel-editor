# Editor Protocol

## 1. Definisi audit teknis

Masalah teknis adalah masalah yang dapat dibuktikan dari teks, dokumen referensi, atau hard constraints dan dapat mengganggu logika, konsistensi, pemahaman, atau kesiapan naskah.

Cakupannya mencakup dua lapisan yang sama-sama wajib:
1. **Teknis cerita:** plot logic, causality, timeline, continuity, worldbuilding, character knowledge, setup/payoff, dan keterbacaan faktual.
2. **Teknis naskah:** ejaan, typo, tata bahasa objektif, tanda baca, konsistensi nama/istilah, struktur bab, Markdown, format, placeholder, dan catatan internal.

Bukan masalah teknis hanya karena editor tidak menyukai pilihan artistik, tone, voice, diksi, atau cara kalimat dibunyikan.

## 2. Batas pemeriksaan bahasa

Periksa typo, ejaan baku, imbuhan, kata depan, kata ulang, bentuk gabungan, kapitalisasi, penulisan angka/tanggal jika tidak konsisten, tanda baca yang salah atau mengubah makna, tata bahasa yang secara objektif rusak hingga makna tidak jelas, rujukan kata ganti yang tidak memiliki referen, nama/istilah yang berubah-ubah, dialog yang kehilangan tanda kutip/pemisah, catatan editor, placeholder, TODO/FIXME, instruksi produksi, dan markup/format yang merusak tampilan.

Jangan perbaiki hanya karena ada sinonim yang terasa lebih bagus, kalimat terasa sederhana/panjang/pendek, tone tidak sesuai selera, metafora tidak disukai, atau editor ingin menyamakan semua kalimat ke satu gaya.

Jika tata bahasa punya lebih dari satu bentuk sah, jangan tandai sebagai ERROR. Gunakan REVIEW hanya bila ada dampak nyata pada makna atau konsistensi.

## 3. Uji temuan

1. Fakta/peristiwa/format apa yang dipersoalkan?
2. Di mana aturan/fakta relevan ditetapkan?
3. Apakah ada kontradiksi, sebab yang hilang, transisi mustahil, knowledge leak, state mismatch, atau kesalahan teknis objektif?
4. Apakah penjelasan sengaja disimpan di bagian lain?
5. Apakah masalah berdampak pada pemahaman, tampilan, stakes, atau kepercayaan pembaca?
6. Apakah ini ERROR/HIGH atau hanya REVIEW?
7. Apa koreksi terkecil yang menyelesaikan masalah tanpa mengubah gaya?

## 4. Severity

| Level | Makna |
|---|---|
| ERROR | Kontradiksi langsung, typo/fakta salah yang terbukti, atau pelanggaran hard rule yang terbukti. |
| HIGH | Kegagalan logika, timeline, worldbuilding, continuity, atau format yang kuat dan mengganggu pemahaman. |
| REVIEW | Dugaan masalah, ambiguitas, atau bentuk bahasa yang perlu verifikasi/keputusan penulis. |
| INFO | Catatan opsional, bukan vonis kesalahan. |

## 5. Release impact

| Kelas | Makna | Tindakan |
|---|---|---|
| BLOCKER | Masalah material yang merusak pemahaman, logika inti, continuity penting, timeline, aturan dunia sentral, atau membuat naskah tidak dapat dibaca secara teknis. | Wajib diperbaiki sebelum rilis. |
| FIX BEFORE RELEASE | Kesalahan teknis nyata tetapi lokal/terbatas, misalnya typo, heading rusak, catatan editor tertinggal, atau inkonsistensi faktual kecil. | Perbaiki dalam daftar singkat. |
| ACCEPTABLE / AUTHOR CHOICE | Ambiguitas disengaja, misteri, open ending, variasi realisme kecil, atau pilihan kreatif yang tidak merusak pemahaman. | Boleh dipertahankan. |
| OPTIONAL POLISH | Penyempurnaan non-esensial. | Tidak boleh menahan publikasi. |

Severity dan release impact adalah dua dimensi berbeda. Kesalahan ejaan dapat ERROR tetapi release impact-nya FIX BEFORE RELEASE, bukan otomatis BLOCKER. REVIEW tidak otomatis menahan publikasi.

## 6. Kategori

`PLOT_HOLE`, `CAUSALITY`, `TIMELINE`, `CHARACTER_CONTINUITY`, `OBJECT_CONTINUITY`, `LOCATION_CONTINUITY`, `RELATIONSHIP_CONTINUITY`, `WORLD_RULE_CONTRADICTION`, `WORLD_RULE_GAP`, `WORLD_STATE`, `CHARACTER_KNOWLEDGE`, `SETUP_PAYOFF`, `REPETITION`, `AI_SLOP`, `SPELLING_TYPO`, `GRAMMAR`, `PUNCTUATION`, `NAME_TERM_CONSISTENCY`, `MARKDOWN_FORMAT`, `DOCUMENT_STRUCTURE`, `EDITORIAL_ARTIFACT`, `PROJECT_CONSTRAINT`, `PLAUSIBILITY`, `OTHER_TECHNICAL`.

## 7. Hindari false positive

Tokoh boleh berbohong, lupa, salah ingat, atau bertindak tidak rasional. Narator boleh tidak dapat dipercaya. Aturan dunia boleh punya pengecualian. Misteri boleh menahan informasi. Repetisi bisa menjadi motif. AI-slop bukan bukti bahwa teks ditulis AI. Realisme dunia nyata hanya digunakan jika cerita mengklaim mengikuti kondisi nyata atau proyek meminta pemeriksaan tersebut.

Jangan menandai pilihan gaya sebagai kesalahan bahasa. Jangan menuntut semua detail kosmetik konsisten jika tidak relevan. Jangan menganggap ejaan tidak baku dalam dialog sebagai typo bila jelas merupakan karakterisasi/ucapan tokoh dan tidak melanggar hard constraint proyek.

## 8. Cakupan audit

Laporkan file/bab yang dibaca, referensi yang diperiksa, jenis audit (bab/lintas bab/full manuscript), file hilang/tidak terbaca, konfigurasi yang tidak valid, dan temuan provisional. Pastikan naskah yang diminta benar-benar termasuk dalam daftar file hasil inventarisasi.

## 9. Kebijakan edit

Audit biasa bersifat read-only. Jika pengguna secara eksplisit meminta penerapan revisi, editor boleh mengubah naskah. Perbaiki temuan objektif/terkonfirmasi dengan perubahan minimal. Jangan mengubah gaya, tone, voice, atau pilihan kreatif. Tandai hal yang ambigu untuk keputusan pengguna. Setelah perubahan, lakukan pemeriksaan ulang pada perubahan dan dependensi lintas bab.

## 10. Publication-readiness gate

Gunakan `rules/09-publication-readiness.md`. Standarnya reader-ready, bukan sempurna. Jangan gunakan “masih ada yang bisa diperbaiki” sebagai alasan menunda publikasi. Tunjukkan konsekuensi bagi pembaca dan apakah masalah melampaui ambang blocker.
