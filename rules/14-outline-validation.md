# Outline Validation, Repair, and Approval

## Tujuan dan batas

Outline adalah rancangan kerja yang sudah melewati proses kreatif. Novel Editor tidak mengambil alih penciptaan cerita, mengganti selera kreatif, menilai keindahan ide, atau memaksakan formula genre. Tugasnya memastikan rancangan cukup lengkap, konsisten, logis menurut aturan cerita, dan dapat dipakai AI penulis tanpa harus mengarang mata rantai cerita inti.

Pemeriksaan outline adalah gerbang teknis sebelum penulisan manuskrip. Terapkan bersama `AGENTS.md`, `EDITOR-PROTOCOL.md`, `rules/13-editorial-decision-making.md`, serta template/panduannya.

## Format-agnostic

- Outline dapat berupa Markdown, dokumen dengan heading berbeda, tabel, atau gabungan beberapa file.
- Jangan menganggap outline salah hanya karena tidak mengikuti `templates/outline-template.md`.
- Pertama, inventarisasi semua dokumen yang tersedia dan buat peta silang ke kategori informasi template.
- Tawarkan/terapkan konversi ke template hanya jika meningkatkan kelengkapan, keterbacaan, auditabilitas, atau handoff antarmodel.
- Pertahankan catatan bebas pembuat outline. Catatan tersebut dapat menjelaskan maksud, alternatif, dan keputusan yang tidak tampak dari struktur utama.
- Bedakan catatan internal, fakta kanonis, asumsi, keputusan fleksibel, dan informasi yang memang harus muncul di manuskrip.

## Area audit wajib

### 1. Identitas dan cakupan
Pastikan judul/identitas proyek, premis, fokus, POV/tense jika ditetapkan, jumlah/rentang bab, status versi, dan hard constraints diketahui atau ditandai terbuka. Ketiadaan metadata kosmetik bukan blocker.

### 2. Kelengkapan cerita utuh
Pastikan outline menjelaskan awal, perkembangan, titik perubahan relevan, krisis/puncak sesuai bentuk cerita, ending, dan keadaan akhir. Ending tidak boleh hanya disebut tanpa sebab dan konsekuensi.

### 3. Integritas sebab-akibat
Periksa pemicu, keputusan, tindakan, hambatan, hasil, dan konsekuensi. Cari kejadian inti yang hanya terjadi karena kebetulan tanpa dukungan, solusi yang muncul mendadak, motivasi yang tidak cukup, dan konflik yang tidak memiliki mekanisme penyelesaian.

### 4. Konsistensi tokoh dan relasi
Periksa identitas, usia, latar, tujuan, motivasi, kemampuan, batas, hubungan, keputusan, perubahan, dan status akhir. Tokoh pendukung tidak harus memiliki profil panjang jika tidak memengaruhi cerita.

### 5. Timeline dan kronologi
Uji tanggal, hari, usia, durasi, urutan, jarak antarperistiwa, perjalanan, deadline, masa pemulihan, dan flashback. Hitung ulang dari jangkar yang eksplisit. Jangan mengarang tanggal pasti jika urutan relatif sudah memadai.

### 6. Dunia dan aturan internal
Periksa aturan yang memengaruhi plot, prasyarat, batas, biaya, pengecualian, institusi, geografi, teknologi, kemampuan, dan konsekuensi. Kedalaman pemeriksaan proporsional terhadap cerita; tidak semua novel memerlukan world bible terpisah.

### 7. Character knowledge dan aliran informasi
Pastikan setiap tokoh mengetahui fakta melalui pengalaman, dialog, dokumen, pengamatan, atau saluran lain yang tersedia. Periksa rahasia, kebohongan, informasi keliru, POV, dan waktu pengungkapan.

### 8. Benda, sumber daya, dan state
Lacak objek/dokumen/uang/akses/cedera/kondisi/kemampuan penting bila memengaruhi plot. Periksa kepemilikan, lokasi, perpindahan, jumlah, dan status akhir.

### 9. Setup, payoff, dan janji cerita
Periksa petunjuk, janji, misteri, konflik, dan subplot yang secara nyata dibangun. Tidak semua detail harus punya payoff; jangan menciptakan kewajiban yang tidak ditetapkan cerita.

### 10. Kesiapan outline per bab
Setiap bab harus cukup jelas untuk dieksekusi: keadaan awal, kejadian/tindakan utama, alasan atau pemicu, informasi yang tersedia, hasil/perubahan, dan konsekuensi/transisi bila relevan. Jangan menuntut jumlah kolom tertentu atau satu adegan per bab.

### 11. Keterpahaman lintas model
Pastikan rujukan nama/istilah/ID stabil, tidak ada ketergantungan pada chat yang tidak disertakan, singkatan penting dijelaskan, dan catatan tambahan tidak bertentangan dengan outline utama.

## Status temuan

Gunakan severity dan release impact yang ada. Untuk outline, gunakan klasifikasi tambahan:
- `OUTLINE BLOCKER`: rancangan tidak dapat ditulis secara koheren karena kontradiksi inti, ending tidak memiliki rantai sebab-akibat, aturan inti saling meniadakan, atau informasi penting tidak dapat ditentukan.
- `NEEDS REPAIR`: kesalahan/ketidaklengkapan teknis yang dapat diperbaiki dengan bukti internal.
- `OPEN AUTHOR DECISION`: pilihan kreatif material belum ditetapkan dan tidak dapat disimpulkan tanpa mengarang niat.
- `ACCEPTABLE FLEXIBILITY`: detail sengaja fleksibel dan tidak menghalangi penulisan.
- `READY`: tidak ada blocker teknis yang belum terselesaikan.

## Mode A: Automatic repair (default)

Outline Editor bekerja otomatis, bukan hanya membuat daftar kritik.

1. Baca outline secara keseluruhan beserta seluruh catatan dan dokumen referensi.
2. Inventarisasi struktur, bab, fakta, tokoh, timeline, aturan, dan keputusan yang sudah dikunci.
3. Bangun fact ledger sementara.
4. Identifikasi dan buktikan masalah dengan rujukan internal.
5. Tentukan apakah yang perlu diperbaiki adalah outline, timeline, bible, atau dokumen pendukung.
6. Terapkan koreksi teknis paling kecil jika jawabannya dapat disimpulkan dari bukti dan tidak mengubah maksud kreatif.
7. Perbarui semua referensi/ID/dependensi yang terdampak.
8. Pertahankan keputusan LOCKED. Jangan retcon diam-diam.
9. Jika dua alternatif kreatif tetap sama kuat dan berdampak material, jangan memilih secara acak. Catat `OPEN AUTHOR DECISION`, berikan alternatif, bukti, rekomendasi, confidence, dan konsekuensi.
10. Audit ulang seluruh area yang terdampak dan lakukan cross-check keseluruhan outline.
11. Simpan laporan dan status.

Contoh perbaikan otomatis: usia yang salah hitung, tanggal yang tidak cocok dengan usia/timeline, nama yang berubah karena typo, nomor bab duplikat, referensi bab salah, urutan kejadian yang bertentangan dengan fakta locked, atau perpindahan benda yang tidak mungkin.

Contoh yang bukan kewenangan otomatis: mengganti siapa pasangan akhir, mengubah kematian menjadi hidup, mengubah motivasi inti, memilih salah satu dari dua ending kreatif yang sama-sama mungkin, atau menciptakan subplot baru untuk menutup kekosongan kreatif.

## Mode B: Approval gate

Outline hanya dapat diberi status `APPROVED FOR DRAFTING` jika:
- seluruh bagian/bab dalam cakupan telah dibaca;
- tidak ada OUTLINE BLOCKER atau NEEDS REPAIR yang terbuka;
- semua OPEN AUTHOR DECISION yang material telah diselesaikan penulis atau dinyatakan tidak menghalangi tahap penulisan;
- timeline, karakter, aturan, pengetahuan, dan sebab-akibat utama saling sinkron;
- setiap bab cukup jelas untuk ditulis tanpa menciptakan peristiwa inti baru;
- keterbatasan bukti dicatat.

Status:
- `APPROVED FOR DRAFTING`: outline cukup solid untuk mulai ditulis.
- `APPROVED WITH TRACKED FLEXIBILITY`: ada detail yang sengaja fleksibel tetapi tidak menghalangi penulisan.
- `REPAIR REQUIRED`: masih ada masalah teknis yang perlu diperbaiki.
- `AUTHOR DECISION REQUIRED`: ada keputusan kreatif material yang tidak dapat disimpulkan.
- `INSUFFICIENT EVIDENCE`: dokumen atau bagian penting tidak tersedia.

Jangan menahan outline karena optional polish, metadata kosmetik, atau detail yang memang boleh ditentukan saat penulisan.

## Format laporan

Laporan outline minimal memuat:
1. cakupan file dan versi;
2. format/struktur yang ditemukan;
3. kelengkapan informasi dan bagian yang tidak relevan;
4. temuan dengan ID, lokasi, bukti, severity, release impact, confidence;
5. koreksi yang diterapkan dan file yang berubah;
6. keputusan OPEN AUTHOR DECISION jika ada;
7. hasil verifikasi ulang;
8. status approval dan apakah penulisan boleh dimulai.

## Batas penting

- Jangan menilai gaya, voice, tone, keindahan, daya jual, atau kesesuaian formula genre.
- Jangan mengubah isi kreatif yang sudah dipilih hanya agar lebih konvensional.
- Jangan menganggap outline harus persis sama dengan template.
- Jangan menyatakan outline siap hanya karena semua heading terisi.
- Jangan mengklaim semua masalah teratasi jika ada bagian yang tidak dibaca.
- Outline approved adalah kesiapan teknis untuk drafting, bukan jaminan novel akhir otomatis bagus atau diterima pasar.
