# Reader-Experience Audit — Bab 21–24

Tanggal audit: 11 November 2026  
Naskah: `Story/Aku Ingin Menjadi Perempuan yang Dipilih/manuscript.md`  
Outline: `Story/Aku Ingin Menjadi Perempuan yang Dipilih/outline.md`  
Manuscript SHA saat audit: `c235875ff0f569088936c5c4dea76207b99ff774`

## Status

**NEEDS MINOR TARGETED REVISION** untuk Bab 21–24.

Audit dilakukan dengan membaca Bab 21–24 dalam urutan pembaca, membandingkan peristiwa dan tanggalnya dengan outline kanonis, serta memeriksa kesinambungan dari Bab 20 dan setup menuju Bab 25. Manuskrip tidak diubah.

Rangkaian ini bekerja secara struktural. Bab 21 menunjukkan konsekuensi kehilangan pekerjaan dan biaya perawatan Ratih; Bab 22–23 memberi jalan keluar yang berasal dari kompetensi dan usaha Maya sendiri; Bab 24 mempertemukan kembali Maya dan Daniel melalui kerja sama resmi yayasan dengan rumah sakit. Ini menjaga prinsip penting cerita: Daniel tidak membantu Maya memperoleh pekerjaan dan hubungan mereka belum menjadi personal.

Tidak ditemukan masalah yang membutuhkan rewrite bab atau perubahan struktur. Temuan utama berkaitan dengan jangkar waktu, satu durasi emosional yang terasa terlalu panjang, dan pilihan frasa.

## Temuan

### F01 — Tanggal Bab 22 belum terlihat jelas dalam pengalaman membaca
- Kategori: `TEMPORAL_ORIENTATION`, `SCENE_TRANSITION`
- Severity: REVIEW
- Release impact: FIX BEFORE RELEASE
- Confidence: High
- Lokasi: pembukaan Bab 22.
- Bukti pembanding:
  - Outline menetapkan Bab 22 pada 3 Maret 2025.
  - Bab 21 berlangsung dalam rentang 10–28 Februari 2025.
  - Bab 22 dibuka dengan “Empat puluh lima menit sebelum matahari terbenam...” dan menyebut penolakan lamaran “sepanjang bulan Februari”, tetapi tidak memberi tanggal atau penanda bahwa cerita sudah masuk awal Maret.
- Masalah: urutan peristiwanya masih dapat dipahami, tetapi pembaca harus menyimpulkan sendiri bahwa bab berpindah dari rentang Februari ke 3 Maret.
- Dampak: kecil, tetapi penanda waktu akan membuat perkembangan pencarian kerja dan proses perekrutan lebih mudah diikuti.
- Rekomendasi: tambahkan cue alami pada pembukaan, misalnya “Sore 3 Maret 2025...” Tidak perlu mengulang tanggal pada paragraf berikutnya.
- Dependensi: pertahankan tanggal wawancara 6 Maret, penawaran 10 Maret, dan mulai bekerja 17 Maret dalam Bab 23.

### F02 — Bab 23 belum mengunci tanggal wawancara pada saat adegan dimulai
- Kategori: `TEMPORAL_ORIENTATION`
- Severity: INFO
- Release impact: OPTIONAL POLISH
- Confidence: High
- Lokasi: pembukaan Bab 23.
- Bukti pembanding:
  - Outline menetapkan wawancara pada 6 Maret 2025.
  - Manuskrip membuka adegan wawancara tanpa tanggal, kemudian menyatakan “Empat hari kemudian, pada sepuluh Maret” Maya menerima kabar diterima.
- Masalah: pembaca dapat menghitung bahwa wawancara berlangsung 6 Maret, jadi ini bukan kebingungan kronologi. Namun, tanggal adegan baru dapat diketahui setelah pembaca mencapai bagian telepon.
- Rekomendasi: bila jangkar tanggal ditambahkan pada Bab 22 dan 24, pertimbangkan juga cue singkat “Pada 6 Maret...” di pembukaan Bab 23 agar urutan proses rekrutmen terbaca langsung. Tidak wajib bila ritme narasi lebih baik tanpa tanggal eksplisit.

### F03 — Bab 24 belum memberi penanda tanggal setelah lompatan dari masa orientasi kerja
- Kategori: `TEMPORAL_ORIENTATION`, `SCENE_TRANSITION`
- Severity: REVIEW
- Release impact: FIX BEFORE RELEASE
- Confidence: High
- Lokasi: pembukaan Bab 24.
- Bukti pembanding:
  - Bab 23 menempatkan hari pertama Maya bekerja pada 17 Maret 2025.
  - Outline menetapkan kegiatan edukasi dan pertemuan kembali dengan Daniel pada 12 April 2025.
  - Bab 24 hanya menyebut “Sabtu pertamanya bertugas memimpin dokumentasi dan publikasi kegiatan lapangan” tanpa tanggal atau cue bahwa hampir empat minggu telah berlalu sejak hari pertama bekerja.
- Masalah: pembaca mengetahui Maya sudah bekerja dan telah menyiapkan materi selama dua minggu, tetapi tidak mendapat ukuran lompatan waktu yang jelas.
- Dampak: tidak merusak pemahaman adegan, tetapi membuat ritme transisi dari karyawan baru menjadi petugas kegiatan lapangan kurang terukur.
- Rekomendasi: beri jangkar waktu sederhana, misalnya “Sabtu pagi, 12 April 2025”. Frasa “Sabtu pertamanya bertugas” dapat dipertahankan bila maksudnya adalah tugas lapangan Sabtu pertamanya, bukan hari Sabtu pertama sejak ia mulai bekerja.
- Dependensi: tanggal ini harus tetap cocok dengan perkenalan Sarah pada 19 April di Bab 25.

### F04 — Ungkapan “selama dua bulan terakhir” berpotensi melebihkan durasi tekanan keuangan
- Kategori: `TEMPORAL_CONTINUITY`, `PROSE_PRECISION`
- Severity: REVIEW
- Release impact: OPTIONAL POLISH
- Confidence: Medium
- Lokasi: Bab 23, setelah Maya menerima kabar diterima di yayasan.
- Bukti: “...mengembuskan napas panjang yang selama dua bulan terakhir tertahan di dadanya.” Kalimat sebelumnya mengaitkan kelegaan itu dengan saldo tabungan yang menipis dan ketakutan kehilangan arah.
- Masalah: dari tanggal kehilangan pekerjaan 31 Januari sampai kabar diterima 10 Maret, durasinya sekitar lima setengah minggu, bukan dua bulan penuh. Dua bulan lebih tepat jika kalimat tersebut merujuk pada keseluruhan guncangan hidup Maya sejak 10 Januari, bukan khusus kecemasan akibat kehilangan pekerjaan dan keuangan.
- Dampak: kecil; pembaca mungkin tidak mempermasalahkannya, tetapi rujukan durasi dapat terasa tidak presisi karena konteks terdekat adalah tekanan keuangan setelah kehilangan pekerjaan.
- Rekomendasi: ubah menjadi “selama berminggu-minggu” atau “sejak awal tahun” jika yang dimaksud adalah akumulasi tekanan sejak hubungan dengan Arman berakhir. Jika yang dimaksud hanya pencarian kerja dan kondisi keuangan, gunakan durasi yang lebih dekat dengan satu bulan.
- Dependensi: jangan mengubah kronologi kehilangan pekerjaan pada 31 Januari atau tanggal penerimaan kerja 10 Maret.

### F05 — “Uang tebusan obat rawat jalan” bukan pilihan frasa yang tepat
- Kategori: `WORD_CHOICE`, `PROSE_CLARITY`
- Severity: REVIEW
- Release impact: OPTIONAL POLISH
- Confidence: High
- Lokasi: Bab 21, paragraf perhitungan sisa tabungan.
- Bukti: “...biaya jaminan rawat inap Ratih di Rumah Sakit Cakrawala, uang tebusan obat rawat jalan...”
- Masalah: “uang tebusan obat” terdengar tidak idiomatis untuk pengeluaran obat setelah pasien pulang. Kata “tebus” lebih lazim dipakai untuk mengambil obat berdasarkan resep, tetapi konstruksi “uang tebusan” mengaburkan apakah yang dimaksud biaya obat, resep, atau pengambilan obat.
- Rekomendasi: gunakan “biaya obat rawat jalan” atau “biaya menebus resep obat”, sesuai tindakan yang benar-benar terjadi. Tidak perlu menambahkan prosedur medis atau biaya baru.
- Dependensi: pertahankan fakta bahwa pengeluaran setelah rawat inap ikut mengurangi tabungan Maya.

### F06 — Penutup Bab 21, 23, dan 24 mengulang simpulan emosional dengan pola serupa
- Kategori: `REPETITION`, `PACING_PROGRESSION`
- Severity: INFO
- Release impact: OPTIONAL POLISH
- Confidence: Medium
- Lokasi: paragraf penutup Bab 21, Bab 23, dan Bab 24.
- Bukti:
  - Bab 21 menutup dengan Maya harus terus melangkah “tanpa bergantung pada siapapun”.
  - Bab 23 menegaskan kesempatan kerja datang dari usaha sendiri “tanpa uluran tangan atau campur tangan dari siapa pun”.
  - Bab 24 menutup dengan kesadaran bahwa kehadiran Maya “diakui secara utuh di tempatnya berdiri”.
- Masalah: ketiganya menyimpulkan perkembangan Maya melalui pernyataan reflektif yang cukup eksplisit. Bab 21 dan 23 terutama sama-sama menekankan kemandirian setelah krisis; Bab 24 kemudian menegaskan pengakuan/validasi diri.
- Dampak: bukan pengulangan plot, tetapi penekanan tema menjadi sedikit terlalu diterangkan oleh narator, padahal tindakan Maya mengelola uang, mengirim lamaran, menjalani wawancara, dan bekerja sudah memperlihatkan perkembangan tersebut.
- Rekomendasi: pertahankan satu simpulan reflektif yang paling kuat. Pada bab lain, pertimbangkan menutup dengan tindakan atau detail konkret. Jangan menghapus tema kemandirian atau pengakuan diri; cukup kurangi penjelasan yang menyatakan ulang hal yang sudah tampak.
- Dependensi: pastikan perkembangan Maya tetap terasa bertahap dan tidak berubah menjadi pemulihan instan setelah mendapat pekerjaan.

## Yang sudah bekerja

- **Bab 21 memperlihatkan konsekuensi yang konkret.** Pengeluaran rumah sakit, biaya rumah, dan kebutuhan Ratih membuat kehilangan pekerjaan tidak berhenti sebagai kesedihan abstrak.
- **Maya tetap konsisten sebagai tokoh yang bertanggung jawab.** Ia menghitung pengeluaran, mencari pekerjaan, dan berusaha melindungi Ratih dari kecemasan finansial. Kebiasaan menyembunyikan beban dari ibunya juga melanjutkan pola karakter yang sudah dibangun.
- **Bab 22 memberi transisi yang masuk akal menuju pekerjaan baru.** Pengalaman Maya dalam komunikasi dan evaluasi kampanye memang relevan dengan kebutuhan Yayasan Lentera Sehat.
- **Bab 23 menjaga proses perekrutan tetap kredibel.** Ada wawancara, penilaian kualifikasi, penawaran resmi, dan tanggal mulai kerja. Tidak ada campur tangan Daniel.
- **Hubungan yayasan dan RS Cakrawala sudah disiapkan.** Nama rumah sakit muncul sebagai mitra pada Bab 22, sehingga kemunculan Daniel di Bab 24 tidak terasa sebagai kebetulan yang sepenuhnya dibuat mendadak.
- **Pertemuan kembali dengan Daniel tetap profesional.** Dialog membahas kegiatan, pekerjaan Maya, dan kondisi Ratih. Daniel tidak membuka jalur komunikasi personal atau memberi perlakuan istimewa.
- **Maya mengingat Daniel tanpa langsung mengubah hubungan menjadi romansa.** Rasa nyaman setelah diakui sebagai rekan kerja dapat menjadi benih emosional, tetapi belum melanggar tahap perkembangan yang ditetapkan outline.
- **Bab 25 memiliki setup yang jelas.** Pengenalan Sarah pada acara berikutnya, 19 April, dapat berlangsung sebagai perkembangan alami dari kerja sama yayasan dan rumah sakit.

## Peta kesinambungan

| Tanggal | Peristiwa |
|---|---|
| 10–28 Februari 2025 | Maya mencari pekerjaan dan menata ulang keuangan (Bab 21). |
| 3 Maret 2025 | Maya menemukan dan mengirim lamaran ke Yayasan Lentera Sehat (Bab 22). |
| 6 Maret 2025 | Wawancara Maya (Bab 23). |
| 10 Maret 2025 | Maya menerima tawaran kerja (Bab 23). |
| 17 Maret 2025 | Hari pertama Maya bekerja di yayasan (Bab 23). |
| 12 April 2025 | Maya bertugas dalam kegiatan bersama RS Cakrawala dan bertemu kembali dengan Daniel (Bab 24). |
| 19 April 2025 | Maya diperkenalkan kepada Sarah (Bab 25). |

## Urutan revisi

1. Tambahkan jangkar 3 Maret pada pembukaan Bab 22.
2. Tambahkan jangkar 12 April pada pembukaan Bab 24.
3. Pertimbangkan cue 6 Maret pada pembukaan Bab 23 agar tanggal wawancara langsung terbaca.
4. Sesuaikan ungkapan “dua bulan terakhir” dengan rentang tekanan yang dimaksud.
5. Ganti “uang tebusan obat rawat jalan” dengan frasa yang idiomatis.
6. Saat revisi terpadu, kurangi simpulan reflektif yang berulang pada penutup Bab 21, 23, dan 24 jika dapat dilakukan tanpa menghilangkan perkembangan tema.

## Putusan

**Bab 21–24 bekerja dan tidak memerlukan penulisan ulang.** Alur pencarian kerja, perekrutan, dan pertemuan kembali dengan Daniel masuk akal serta sesuai kanon. Perbaikan yang disarankan bersifat lokal: memperjelas lompatan waktu, menyelaraskan durasi, dan merapikan beberapa frasa. Bab 24 khususnya sudah menjaga batas profesional Daniel dan Maya; tahap hubungan ini tidak perlu dipercepat.

Status ini hanya berlaku untuk Bab 21–24. Novel secara keseluruhan belum dapat dinyatakan siap terbit sebelum audit bab-bab berikutnya dan pemeriksaan lintas bab selesai.
