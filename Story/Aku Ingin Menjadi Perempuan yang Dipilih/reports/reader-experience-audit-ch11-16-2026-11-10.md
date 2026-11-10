# Reader-Experience Audit — Bab 11–16
Tanggal audit: 10 November 2026
Naskah: `Story/Aku Ingin Menjadi Perempuan yang Dipilih/manuscript.md`
Outline: `Story/Aku Ingin Menjadi Perempuan yang Dipilih/outline.md`
Manuscript SHA saat audit: `c235875ff0f569088936c5c4dea76207b99ff774`

## Status

**NEEDS TARGETED REVISION** untuk Bab 11–16.

Audit menilai kesinambungan dari Bab 1–16, kesesuaian dengan outline, kejelasan kronologi, logika tindakan tokoh, fungsi adegan, dan pengalaman pembaca. Naskah utama tidak diubah.

Bagian ini berhasil membawa cerita dari pengkhianatan Arman menuju keruntuhan awal kehidupan Maya. Pengungkapan kebohongan, keputusan berpisah, kesepian setelah hubungan berakhir, dan kehilangan pekerjaan membentuk urutan sebab-akibat yang dapat dipahami. Namun, ada beberapa kesalahan teknis dan kontinuitas yang wajib diperbaiki, serta beberapa bagian yang masih terlalu banyak menjelaskan emosi atau kesimpulan.

## Temuan

### F01 — Bab 12 tidak memberi jangkar tanggal untuk kembali ke masa kini
- Lokasi: pembuka Bab 12
- Severity: HIGH
- Release impact: FIX BEFORE RELEASE
- Confidence: High

Bab 2 berakhir ketika sedan Arman tiba di depan kantor Maya pada 10 Januari 2025. Bab 3–11 kemudian membawa pembaca melewati kilas balik Juni 2004 hingga Desember 2024. Bab 12 kembali ke adegan di dalam mobil, tetapi tidak menyebut tanggal atau penanda bahwa waktu telah kembali ke 10 Januari 2025.

Pembaca yang mengingat Bab 2 dapat menyimpulkan bahwa ini adegan yang sama, tetapi novel sebaiknya tidak memaksa pembaca menghitung sendiri setelah jeda sepuluh bab. Penanda tanggal juga penting karena judul Bab 13 dan dialognya menyebut lima hari sejak Maya melihat foto.

**Perbaikan:** beri penanda waktu yang ringkas pada awal Bab 12, misalnya “Malam 10 Januari 2025”. Pastikan pembaca memahami bahwa adegan ini melanjutkan momen ketika sedan Arman tiba di kantor pada akhir Bab 2.

### F02 — Masa pemberitahuan kerja tidak cocok dengan tanggal hari terakhir
- Lokasi: Bab 15, isi surat PHK
- Severity: ERROR
- Release impact: BLOCKER
- Confidence: High

Bab 15 menyatakan Maya menerima pemberitahuan pada 24 Januari 2025 (dapat disimpulkan dari sembilan hari setelah putus pada 15 Januari dan tujuh hari sebelum 31 Januari). Surat menyebut hubungan kerja berakhir setelah “masa pemberitahuan empat belas hari kerja”, tetapi hari terakhirnya ditetapkan 31 Januari 2025.

Rentang 24–31 Januari hanya tujuh hari kalender dan sekitar lima hari kerja, bukan empat belas hari kerja. Ini kontradiksi hitungan waktu yang terlihat jelas.

**Perbaikan:** pertahankan tanggal kanonis 24 Januari dan 31 Januari, lalu ubah durasi pemberitahuan dalam surat agar sesuai. Jangan mengubah tanggal hari terakhir tanpa memeriksa outline dan kesinambungan Bab 16–17.

### F03 — Lama Maya bekerja di perusahaan berubah dari tiga tahun menjadi lima tahun
- Lokasi: Bab 16, paragraf setelah Maya menandatangani dokumen
- Severity: ERROR
- Release impact: FIX BEFORE RELEASE
- Confidence: High

Bab 16 menyebut laptop kantor digunakan selama tiga tahun terakhir. Pada paragraf berikutnya, penandatanganan dokumen disebut sebagai titik akhir “masa lima tahun yang bernaung di bawah rasa aman rutinitas kantor perkotaan”.

Dua keterangan ini membuat masa kerja Maya tidak konsisten. Tidak ada dasar dalam outline untuk menyimpulkan bahwa Maya bekerja lima tahun di perusahaan tersebut.

**Perbaikan:** samakan dengan masa kerja tiga tahun yang sudah disebut. Periksa juga semua penyebutan masa kerja Maya di bab lain agar tidak ada durasi berbeda.

### F04 — Dialog “cuma pindah rumah” tidak sesuai peristiwa
- Lokasi: Bab 16, dialog Maya kepada Nita
- Severity: ERROR
- Release impact: FIX BEFORE RELEASE
- Confidence: High

Saat Nita memberikan kotak kue perpisahan, Maya berkata, “Kan aku cuma pindah rumah, bukan pindah luar pulau.” Namun konteks adegan adalah hari terakhir Maya bekerja, bukan kepindahan tempat tinggal.

**Perbaikan:** ganti dengan respons yang sesuai konteks, misalnya “Aku cuma pindah tempat kerja” jika sudah ada pekerjaan baru, atau “Aku cuma berhenti kerja di sini” jika belum. Karena Maya belum mendapat pekerjaan baru, jangan membuat dialog seolah-olah ia sudah pindah ke kantor lain.

### F05 — Kepemilikan kunci cadangan tidak jelas
- Lokasi: Bab 13, dialog Maya tentang barang Arman
- Severity: REVIEW
- Release impact: FIX BEFORE RELEASE
- Confidence: High

Maya mengatakan bahwa kunci cadangan kontrakan Arman sudah dimasukkan ke amplop. Adegan berlangsung di kontrakan Maya, sementara Arman datang untuk mengambil barang-barangnya. Frasa “kunci cadangan kontrakanmu” secara tata bahasa berarti kontrakan milik Arman, bukan kunci rumah Maya yang mungkin masih dipegang Arman.

**Perbaikan:** tentukan kunci yang dimaksud. Jika itu kunci cadangan kontrakan Maya yang dipegang Arman, gunakan “kunci cadangan kontrakan ini” atau “kunci cadangan rumahku”. Jika benar kunci kontrakan Arman, jelaskan mengapa kunci itu berada di tangan Maya dan dikembalikan bersamaan dengan barang-barangnya.

### F06 — Istilah pengarsipan percakapan WhatsApp kurang tepat
- Lokasi: Bab 14, tindakan Maya terhadap chat Arman
- Severity: REVIEW
- Release impact: OPTIONAL POLISH
- Confidence: High

Naskah menyebut Maya “memindahkan kontak Arman ke dalam daftar percakapan terarsip”. Dalam aplikasi pesan, yang diarsipkan adalah percakapan/chat, bukan kontaknya.

**Perbaikan:** gunakan “mengarsipkan percakapannya dengan Arman” atau ungkapan setara. Ini koreksi teknis kecil, tetapi membantu detail digital terasa alami.

### F07 — Adegan putus menyebut percakapan “kemarin” yang tidak pernah diperlihatkan
- Lokasi: Bab 13, dialog Arman
- Severity: REVIEW
- Release impact: AUTHOR CHOICE
- Confidence: Medium

Arman berkata, “Aku sudah bilang kemarin, soal Celine itu urusan profesional dan tuntutan keluarga investor.” Namun setelah konfrontasi di mobil pada Bab 12, tidak ada adegan yang memperlihatkan percakapan mereka pada 14 Januari.

Tidak wajib menampilkan setiap kontak setelah konfrontasi. Akan tetapi, kata “kemarin” membuat pembaca bertanya apakah ada pertemuan atau percakapan penting yang terlewat. Ini juga berpengaruh pada bagaimana Arman masih mencoba mempertahankan Maya setelah kebohongannya terbongkar.

**Perbaikan:** jika memang ada percakapan pada 14 Januari, beri satu petunjuk singkat bahwa Arman terus menghubungi atau datang menemui Maya. Jika tidak ada percakapan khusus, ubah dialog agar merujuk pada pembelaan Arman di pertemuan sebelumnya, bukan “kemarin”.

### F08 — Penutup Bab 14 terlalu menyimpulkan dan mengandung frasa abstrak
- Lokasi: akhir Bab 14
- Severity: REVIEW
- Release impact: OPTIONAL POLISH
- Confidence: High

Kalimat “Rumah ini memang sepi dan hampa, tetapi untuk pertama kalinya, tidak ada lagi prasangka yang harus ia sembunyikan di sudut-sudutnya” kurang tepat secara makna. Prasangka biasanya berkaitan dengan dugaan atau penilaian terhadap orang lain; dalam konteks ini, yang Maya sembunyikan adalah kecurigaan, luka, atau kebohongan yang selama ini ia terima.

**Perbaikan:** pilih makna yang tepat dan pertimbangkan mengakhiri bab pada tindakan atau kesadaran konkret Maya. Kesepian dan dorongan menghubungi Arman sudah tergambar cukup jelas pada adegan sebelumnya.

### F09 — Beberapa bab penting terlalu pendek, tetapi jangan ditambah dengan pengisi
- Lokasi: Bab 11, 12, 14, 16
- Severity: REVIEW
- Release impact: AUTHOR CHOICE
- Confidence: High

Perkiraan panjang bab:
- Bab 11: 389 kata
- Bab 12: 559 kata
- Bab 13: 705 kata
- Bab 14: 541 kata
- Bab 15: 678 kata
- Bab 16: 553 kata

Bab 11 adalah adegan kebohongan Arman menjelang pertunangan; Bab 12 adalah konfrontasi utama; Bab 14 menunjukkan Maya menahan dorongan untuk menghubungi Arman; Bab 16 menutup fase pekerjaan lama. Beberapa bab berada di bawah standar panjang normal atau transisi pada dokumen proyek.

Panjang pendek tidak otomatis membuat bab gagal. Namun, Bab 11 dapat memberi ruang lebih bagi reaksi Maya terhadap alasan Arman, dan Bab 12 dapat memperjelas transisi waktu serta respons emosional tanpa mengulang dialog. Bab 14 dan 16 sudah memiliki fungsi yang jelas; jangan menambahkan monolog atau detail rumah/kantor hanya untuk mengejar angka.

**Perbaikan:** utamakan kelengkapan dramatik dan keterbacaan. Tambahkan hanya tindakan, respons, atau informasi yang benar-benar memperkuat perubahan adegan.

### F10 — Beberapa frasa Bab 16 perlu dirapikan secara teknis
- Lokasi: Bab 16
- Severity: REVIEW
- Release impact: OPTIONAL POLISH
- Confidence: High

Beberapa konstruksi terasa janggal:
- “Pintu lift membawa turun menuju lantai dasar” — subjek dan objeknya kurang tepat.
- “sangat ia hafal legok jalurnya” — “legok” tidak tepat untuk menggambarkan jalur koridor yang dihafal.
- “lembar pembebasan tugas” — istilah ini kurang jelas untuk dokumen akhir masa kerja/serah terima.

**Perbaikan:** gunakan konstruksi sederhana dan istilah dokumen yang sesuai dengan proses perusahaan, misalnya dokumen serah terima atau penyelesaian administrasi akhir. Jangan membuat prosedur HR baru yang bertentangan dengan adegan.

## Pemeriksaan struktur dan kontinuitas

### Yang sudah bekerja
- Bab 11 sesuai outline: Arman berbohong tentang tugas di Garut pada 20–akhir pekan Desember 2024, sementara Maya belum tahu tanggal 21 Desember adalah hari pertunangan.
- Bab 12 memperlihatkan Arman mengakui dua kebohongan utama: ia mempertahankan Maya sambil memberi tahu Celine bahwa hubungan mereka sudah berakhir sejak November.
- Bab 13 menempatkan keputusan putus pada 15 Januari 2025, lima hari setelah Maya menemukan foto pada 10 Januari. Ini sesuai judul “Lima Tahun dan Lima Hari”.
- Bab 14 memperlihatkan kesepian setelah putus dan dorongan untuk kembali menghubungi Arman, tanpa membuat Maya langsung pulih.
- Bab 15 menempatkan pemberitahuan pengurangan tenaga kerja pada 24 Januari dan hari terakhir 31 Januari, sesuai outline.
- Bab 16 menunjukkan perpisahan dari kantor pada 31 Januari.
- Bab 17 melanjutkan konsekuensi setelah Maya kehilangan pekerjaan dan menuju keadaan darurat Ratih. Ini merupakan eskalasi yang dapat dimengerti, meski penanda tanggal Bab 17 perlu diperiksa pada audit berikutnya.

### Logika karakter
- Maya tidak langsung memaafkan atau kembali kepada Arman. Ia mengembalikan barang, menetapkan batas, dan melarang kontak. Ini konsisten dengan keputusan akhir hubungan.
- Arman masih berusaha membingkai kebohongannya sebagai urusan profesional dan keadaan yang memaksanya. Ini sesuai karakter yang manipulatif tetapi tidak harus menjadi penjahat satu dimensi.
- Maya tetap menunjukkan pola menekan emosi setelah putus dan kehilangan pekerjaan. Perilaku ini konsisten dengan latar belakangnya, tetapi jangan terus-menerus menjelaskan pola tersebut lewat kalimat narator.
- Nita berfungsi sebagai dukungan yang wajar. Dialognya tidak mengubah keputusan Maya atau mengambil alih konflik.

### Transisi menuju Bab 17
Bab 16 berakhir pada 31 Januari, sementara Bab 17 membawa Maya ke UGD setelah Ratih ditemukan jatuh. Outline menetapkan kejadian Ratih pada 2 Februari 2025. Bab 17 menyebut pesangon baru cair dua hari sebelumnya, sehingga petunjuk waktunya mendukung tanggal tersebut. Namun, tanggal atau penanda “dua hari kemudian” sebaiknya disebut secara eksplisit pada awal Bab 17 agar perpindahan dari hari terakhir kerja ke keadaan darurat tidak hanya bergantung pada petunjuk saldo pesangon.

## Urutan revisi

1. Perbaiki masa pemberitahuan kerja pada Bab 15 agar cocok dengan 24–31 Januari.
2. Perjelas tanggal 10 Januari 2025 di awal Bab 12.
3. Samakan masa kerja Maya menjadi tiga tahun di Bab 16.
4. Ganti dialog “cuma pindah rumah” dengan dialog yang sesuai perpisahan kerja.
5. Perjelas kunci cadangan yang dikembalikan pada Bab 13.
6. Putuskan apakah percakapan “kemarin” pada Bab 13 perlu diberi petunjuk atau dialognya diubah.
7. Rapikan istilah pengarsipan chat, penutup Bab 14, dan frasa teknis Bab 16.
8. Jangan menambah kata secara mekanis; kembangkan hanya bagian yang memang memerlukan ruang dramatik.

## Putusan

**Bab 11–16 tidak perlu ditulis ulang.** Rangkaian dramatisnya sudah jelas dan sesuai fondasi outline. Namun, Bab 15 dan 16 memiliki kontradiksi yang wajib diperbaiki sebelum publikasi. Bab 12 perlu penanda tanggal agar pembaca kembali ke garis waktu utama dengan yakin. Selebihnya adalah perbaikan kejelasan, diksi, dan penguatan adegan.

Status ini hanya berlaku untuk Bab 11–16. Novel secara keseluruhan belum dapat dinyatakan siap terbit sebelum audit seluruh bab, kesinambungan waktu, dan pengalaman baca dari awal sampai akhir selesai.
