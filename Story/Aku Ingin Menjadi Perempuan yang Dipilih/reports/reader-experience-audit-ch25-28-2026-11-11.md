# Reader-Experience Audit — Bab 25–28

Tanggal audit: 11 November 2026  
Naskah: `Story/Aku Ingin Menjadi Perempuan yang Dipilih/manuscript.md`  
Outline: `Story/Aku Ingin Menjadi Perempuan yang Dipilih/outline.md`  
Manuscript SHA saat audit: `c235875ff0f569088936c5c4dea76207b99ff774`

## Status

**NEEDS TARGETED REVISION** untuk Bab 25–28.

Audit membaca empat bab sesuai urutan pembaca, membandingkan peristiwa dengan outline kanonis, dan memeriksa kesinambungan karakter, waktu, hubungan, serta sudut pandang. Naskah utama tidak diubah.

Secara struktur, rangkaian ini menjalankan fungsi penting: Maya mengetahui Daniel telah menikah, melihat Sarah sebagai pribadi yang utuh dan kompeten, memahami bahwa masalah rumah tangga mereka sudah ada sebelum dirinya hadir, lalu menjaga interaksi dengan Daniel tetap profesional. Bab 28 juga mengembalikan fokus ke perjalanan Maya sendiri dan menegaskan bahwa ia belum pulih sepenuhnya dari perpisahan.

Tidak ada alasan untuk menulis ulang empat bab ini. Namun, Bab 26 memiliki pelanggaran sudut pandang yang perlu diperbaiki sebelum publikasi. Ada pula ketidaktepatan orientasi waktu dan beberapa pengulangan penjelasan batas profesional.

## Temuan

### F01 — Bab 26 berpindah ke pikiran Daniel dan Sarah tanpa penanda sudut pandang
- Kategori: `POV_VIOLATION`, `NARRATIVE_CONSISTENCY`
- Severity: ERROR
- Release impact: FIX BEFORE RELEASE
- Confidence: High
- Lokasi: Bab 26, adegan di apartemen Daniel dan Sarah.
- Bukti:
  - Narasi menyatakan Daniel ingin bercerita tentang pasiennya, “tetapi ia ragu”.
  - Narasi menyatakan Sarah memilih menyimpan kelelahannya sendiri dan tidak menceritakan gejala lupusnya kepada Daniel.
  - Narasi menjelaskan kebiasaan emosional keduanya dan alasan masing-masing memendam masalah.
- Masalah: informasi tersebut masuk ke pikiran Daniel dan Sarah dalam satu adegan. Outline menetapkan orang ketiga terbatas yang dominan mengikuti Maya, melarang perpindahan pikiran antartokoh dalam satu adegan, dan mewajibkan penandaan jelas jika sebuah bab menggunakan sudut pandang Daniel atau Sarah. Bab 26 tidak memberi penanda POV, sementara adegan tersebut sekaligus mengakses pikiran dua tokoh.
- Dampak: pembaca kehilangan pegangan tentang siapa yang menjadi pusat persepsi narasi. Ini juga membuat informasi pribadi Daniel dan Sarah terasa disampaikan oleh narator serba tahu, padahal aturan novel membatasi cara informasi itu diketahui.
- Rekomendasi: pilih satu pendekatan secara konsisten:
  1. **Pertahankan POV Maya:** hapus adegan privat di apartemen atau ubah menjadi informasi yang dapat Maya ketahui secara wajar pada kesempatan lain. Maya boleh melihat perilaku publik mereka, tetapi tidak boleh mengetahui pikiran atau gejala yang tidak pernah disampaikan.
  2. **Jadikan Bab 26 bab dengan POV Daniel:** beri penanda yang jelas sejak awal bab dan batasi adegan apartemen pada persepsi Daniel. Informasi tentang kondisi Sarah hanya boleh muncul melalui apa yang Daniel lihat, dengar, atau ketahui; jangan masuk ke pikiran Sarah dalam adegan yang sama.
- Rekomendasi editorial: pendekatan pertama paling menjaga konsistensi POV dominan Maya dan menghindari perubahan teknik narasi yang tidak diperlukan. Jika adegan rumah tangga Daniel–Sarah dianggap penting untuk pembaca, pendekatan kedua dapat dipakai, tetapi harus menjadi keputusan teknik yang konsisten, bukan pengecualian tanpa penanda.
- Dependensi: periksa semua bab lain dalam audit berikutnya untuk perpindahan POV serupa.

### F02 — Orientasi waktu Bab 26 bertentangan dengan penanda “pekan lalu”
- Kategori: `TIMELINE`, `TEMPORAL_ORIENTATION`
- Severity: REVIEW
- Release impact: FIX BEFORE RELEASE
- Confidence: High
- Lokasi: pembukaan Bab 26 dan rujukan ke sarasehan Bab 25.
- Bukti:
  - Bab 25 berlangsung Sabtu, 19 April 2025.
  - Bab 26 dibuka dengan frasa “angin sore pertengahan April”.
  - Tidak lama kemudian Maya mengingat pasangan itu di sarasehan “pekan lalu”.
  - Outline menetapkan Bab 26 pada akhir April 2025.
- Masalah: jika sarasehan berlangsung 19 April dan sudah disebut terjadi pekan lalu, adegan Maya semestinya berada sekitar akhir April, bukan “pertengahan April”.
- Dampak: pembaca mendapat dua petunjuk waktu yang tidak selaras dalam satu bab.
- Rekomendasi: ganti “pertengahan April” dengan cue yang sesuai akhir April, atau hilangkan penanda pertengahan bulan dan gunakan transisi waktu yang tidak bertentangan. Tidak perlu menetapkan tanggal spesifik jika tidak dibutuhkan.

### F03 — Kondisi lupus Sarah disebut dengan frasa yang tidak tepat dan terlalu kabur
- Kategori: `CHARACTER_CONTINUITY`, `WORD_CHOICE`, `DOMAIN_CLARITY`
- Severity: REVIEW
- Release impact: FIX BEFORE RELEASE
- Confidence: High
- Lokasi: Bab 26, adegan Daniel dan Sarah di apartemen.
- Bukti: “Gejala pegal di persendian kakinya akibat kambuhnya autoimun tipis dua hari lalu...”
- Masalah:
  - “Autoimun tipis” bukan penyebutan kondisi yang jelas atau idiomatis.
  - Kanon menetapkan Sarah didiagnosis lupus pada 2021. Penyebutan kabur ini justru menghindari nama kondisi yang sudah ditetapkan.
  - Kalimat mengaitkan pegal pada persendian kaki secara langsung dengan kambuhnya penyakit tanpa konteks atau dasar yang cukup di dalam cerita.
- Dampak: pembaca dapat mengira ada kondisi baru atau tingkat penyakit yang berbeda dari kanon.
- Rekomendasi: jika adegan ini dipertahankan, gunakan istilah “lupusnya sedang kambuh” atau bentuk yang lebih natural, tanpa menambahkan gejala, komplikasi, atau detail medis baru. Jangan membuat lupus menjadi penjelasan tunggal atas masalah rumah tangga.
- Dependensi: konsistenkan penyebutan kondisi Sarah dengan profil tokoh dan bab-bab berikutnya.

### F04 — Bab 27 mengulang batas profesional dengan beberapa pernyataan yang berdekatan
- Kategori: `REPETITION`, `PACING_PROGRESSION`
- Severity: INFO
- Release impact: OPTIONAL POLISH
- Confidence: High
- Lokasi: Bab 27, bagian tengah hingga akhir.
- Bukti:
  - “Seluruh interaksi antara Maya dan Daniel berlangsung sepenuhnya melalui jalur kerja dan grup kegiatan resmi.”
  - “Maya secara sadar memagari dirinya dengan batas yang tegas.”
  - “Daniel pun bersikap sangat profesional...”
  - “Tidak ada komunikasi pribadi di luar jam kerja dan tidak ada percakapan di luar alur proyek.”
- Masalah: beberapa kalimat menyampaikan informasi yang sama: komunikasi mereka hanya untuk urusan kerja dan keduanya menjaga batas.
- Dampak: bab terasa menjelaskan status hubungan secara berulang, bukan membiarkan tindakan dan bentuk komunikasi memperlihatkannya.
- Rekomendasi: pertahankan bukti konkret berupa koordinasi melalui grup, rapat yang dihadiri tim, dan revisi materi. Ringkas satu atau dua simpulan narator. Batas profesional tetap harus jelas karena menjadi fondasi perubahan hubungan pada bab-bab selanjutnya.

### F05 — Penutup Bab 26 menggunakan foreshadowing abstrak yang tidak menambah informasi
- Kategori: `PROSE_CLARITY`, `NARRATIVE_TONE`
- Severity: INFO
- Release impact: OPTIONAL POLISH
- Confidence: Medium
- Lokasi: paragraf terakhir Bab 26.
- Bukti: “Tiga kehidupan itu berjalan di atas relnya masing-masing, belum menyadari bahwa takdir akan kembali mempertemukan lintasan mereka di bulan-bulan mendatang.”
- Masalah: kalimat memberi tahu pembaca bahwa ketiga tokoh akan dipertemukan oleh takdir, padahal alur kerja sama yayasan dan rumah sakit sudah menyediakan alasan konkret untuk pertemuan mereka. Ungkapan “takdir” dan “lintasan” juga terasa generik dibanding detail keseharian yang menjadi kekuatan bab.
- Dampak: penutup sedikit menggeser nada dari drama psikologis realistis ke foreshadowing melodramatis.
- Rekomendasi: pertimbangkan mengakhiri bab pada detail konkret kehidupan mereka atau pada kesenjangan komunikasi Daniel–Sarah, tanpa mengumumkan bahwa takdir akan mempertemukan mereka. Ini polish opsional.

### F06 — Beberapa simpulan emosional Bab 25 dan Bab 28 menjelaskan hal yang sudah terlihat
- Kategori: `EMOTIONAL_REPETITION`, `PROSE_PRECISION`
- Severity: INFO
- Release impact: OPTIONAL POLISH
- Confidence: Medium
- Lokasi: penutup Bab 25 dan dua paragraf terakhir Bab 28.
- Bukti:
  - Bab 25 menyatakan Maya menyadari Daniel memiliki “sebuah kehidupan utuh” dan kemudian menegaskan ia hadir murni untuk bekerja.
  - Bab 28 menyatakan Maya telah melewati titik terendah, memiliki pekerjaan baru, ibunya pulih, dan tidak lagi mengalah demi Arman; setelah itu kembali menjelaskan bahwa pemulihannya belum tuntas.
- Masalah: gagasan utamanya tepat, tetapi beberapa lapis simpulan muncul berurutan. Bab 28 terutama menyampaikan perkembangan yang sama melalui rangkuman, lalu mengulang bahwa Maya belum pulih sepenuhnya.
- Dampak: emosi pembaca diarahkan terlalu eksplisit, sementara detail nasi kuning, janji Arman pada ulang tahun ke-25, dan pesan yang tidak datang sudah cukup kuat untuk membawa emosi.
- Rekomendasi: pertahankan pengakuan bahwa Maya belum pulih sepenuhnya. Pangkas simpulan yang mengulang daftar pencapaian atau menjelaskan kembali makna adegan. Biarkan detail konkret menjadi pusat penutup.

## Yang sudah bekerja

- **Sarah diperkenalkan sebagai manusia, bukan antagonis.** Ia ramah kepada Maya, memiliki pekerjaan sendiri, cakap dalam bahasa, dan mampu memberi apresiasi profesional.
- **Status pernikahan Daniel dibuat jelas.** Maya mengetahui bahwa Daniel dan Sarah menikah sejak 20 Oktober 2017, jauh sebelum hubungan profesional Maya dengan Daniel berkembang.
- **Maya tidak langsung menganggap Daniel sebagai kemungkinan pasangan.** Bab 25 dan 26 menegaskan bahwa ia melihat batas tersebut; Bab 27 memperlihatkan ia benar-benar menjaga interaksi di jalur kerja.
- **Masalah rumah tangga Daniel dan Sarah tidak diletakkan sebagai akibat Maya.** Outline menyatakan masalah komunikasi sudah ada sebelum Maya hadir. Prinsip ini perlu dipertahankan, tetapi penyampaiannya harus mengikuti aturan POV.
- **Pekerjaan Maya berkembang melalui kompetensi.** Bab 27 menunjukkan ia mampu menerjemahkan istilah medis menjadi materi yang mudah dipahami, dan Daniel menghargai kontribusinya di depan tim.
- **Bab 28 mengembalikan cerita ke Maya dan Ratih.** Ulang tahun sederhana menjadi kontras yang efektif dengan rencana masa depan yang dahulu dibayangkan Maya bersama Arman.
- **Usia Maya dan Ratih konsisten.** Maya lahir 14 Mei 1997 dan berusia 28 pada 14 Mei 2025. Ratih lahir 9 Februari 1972 dan sudah berusia 53 pada tanggal tersebut.
- **Kondisi tangan Ratih masih masuk akal secara kronologi.** Bab 24 menyebut gips sudah dilepas minggu sebelumnya; Bab 28 menyebut ia sudah sebulan bebas gips dan masih bergerak sedikit lambat. Ini tidak menunjukkan kontradiksi yang perlu diubah.

## Peta kesinambungan

| Tanggal/periode | Peristiwa |
|---|---|
| 19 April 2025 | Maya diperkenalkan kepada Sarah di sarasehan yayasan dan mengetahui mereka telah menikah sejak 2017 (Bab 25). |
| Akhir April 2025 | Maya melihat gambaran publik pasangan tersebut; kehidupan pribadi mereka mulai memperlihatkan jarak emosional (Bab 26). |
| 1–13 Mei 2025 | Maya dan Daniel berinteraksi dalam urusan program melalui kanal resmi dan grup kerja (Bab 27). |
| 13 Mei 2025 | Maya merapikan draf final materi edukasi (Bab 27). |
| 14 Mei 2025 | Maya berulang tahun ke-28 dan makan sederhana bersama Ratih (Bab 28). |

## Urutan revisi

1. Perbaiki pelanggaran POV Bab 26. Pilihan yang paling konsisten adalah mempertahankan POV Maya dan menghapus/menata ulang akses ke pikiran Daniel serta Sarah.
2. Selaraskan “pertengahan April” menjadi akhir April atau hilangkan penanda yang bertentangan.
3. Jika adegan privat Daniel–Sarah dipertahankan, rapikan penyebutan lupus Sarah dan pastikan POV-nya hanya satu tokoh.
4. Ringkas pengulangan pernyataan batas profesional di Bab 27.
5. Pertimbangkan mengganti penutup abstrak Bab 26 dengan detail konkret.
6. Saat line edit terpadu, kurangi simpulan emosional yang berulang di Bab 25 dan 28.

## Putusan

**Bab 25–28 memiliki fondasi yang kuat dan tidak membutuhkan rewrite keseluruhan.** Pengenalan Sarah berhasil, batas profesional masih terjaga, dan ulang tahun Maya memberi jeda emosional yang relevan. Namun, Bab 26 harus diperbaiki karena pelanggaran POV merupakan masalah konsistensi naratif, bukan sekadar preferensi gaya. Setelah itu, sisanya merupakan perbaikan lokal dan polish.

Status ini hanya berlaku untuk Bab 25–28. Novel secara keseluruhan belum dapat dinyatakan siap terbit sebelum audit bab berikutnya dan pemeriksaan lintas bab selesai.
