# Reader-Experience Audit — Bab 17–20

Tanggal audit: 10 November 2026  
Naskah: `Story/Aku Ingin Menjadi Perempuan yang Dipilih/manuscript.md`  
Outline: `Story/Aku Ingin Menjadi Perempuan yang Dipilih/outline.md`  
Manuscript SHA saat audit: `c235875ff0f569088936c5c4dea76207b99ff774`

## Status

**NEEDS TARGETED REVISION** untuk Bab 17–20.

Audit ini membaca Bab 17–20 dalam urutan pembaca, membandingkannya dengan outline kanonis, serta memeriksa konteks Bab 15–16 dan Bab 21–24 untuk kesinambungan waktu, keadaan karakter, dan setup pertemuan Maya–Daniel. Manuskrip tidak diubah.

Rangkaian ini bekerja sebagai konsekuensi lanjutan dari kehilangan pekerjaan Maya: kecelakaan Ratih memaksa Maya mengalihkan perhatian dan sumber daya ke rumah, sementara pertemuan dengan Daniel dimulai dari relasi dokter–keluarga pasien. Konflik keluarga dan tekanan keuangan terasa relevan dengan karakter Maya. Masalah yang paling perlu ditangani adalah penempatan waktu kunjungan Daniel, durasi perawatan, dan beberapa penanda transisi yang belum jelas. Temuan ini dapat diselesaikan dengan revisi lokal; tidak ada alasan untuk menulis ulang seluruh empat bab.

## Temuan

### F01 — Pembukaan Bab 17 belum memberi jangkar waktu setelah Bab 16
- Kategori: `TEMPORAL_ORIENTATION`, `SCENE_TRANSITION`
- Severity: REVIEW
- Release impact: FIX BEFORE RELEASE
- Confidence: High
- Lokasi: transisi Bab 16 ke Bab 17; pembukaan Bab 17.
- Bukti: Bab 16 berakhir ketika Maya meninggalkan kantor pada hari terakhir kerjanya. Bab 17 langsung dibuka di UGD tanpa penanda tanggal. Petunjuk bahwa pesangon “baru cair dua hari lalu” mendukung tanggal 2 Februari 2025, tetapi pembaca harus menyimpulkannya sendiri.
- Dampak: pembaca tidak segera mengetahui berapa lama setelah hari terakhir kerja kecelakaan Ratih terjadi. Ini penting karena Bab 17 menjadi titik perubahan baru setelah dua kehilangan yang berdekatan.
- Rekomendasi: beri cue alami pada pembukaan, misalnya “Dua hari setelah hari terakhirnya bekerja, pada sore 2 Februari 2025, ...”. Tidak perlu mengulang tanggal pada setiap paragraf.
- Dependensi: pastikan tanggal ini tetap cocok dengan tanggal pencairan pesangon yang disebut pada Bab 17.

### F02 — Pertemuan Daniel di Bab 18 terjadi pada hari yang keliru menurut outline
- Kategori: `TIMELINE`, `OUTLINE_ALIGNMENT`, `SCENE_TRANSITION`
- Severity: ERROR
- Release impact: FIX BEFORE RELEASE
- Confidence: High
- Lokasi: Bab 17, paragraf perawat tentang Daniel; pembukaan dan adegan utama Bab 18.
- Bukti pembanding:
  - Outline menetapkan Ratih jatuh pada 2 Februari 2025 dan Maya bertemu Daniel pada 3 Februari 2025.
  - Di Bab 17, perawat mengatakan Daniel “akan visit” setelah Ratih dipindahkan ke ruang rawat inap.
  - Bab 18 masih menggambarkan Maya berada di UGD, Daniel datang di samping ranjang, dan mengatakan “Malam ini Ibu harus dirawat inap”. Kalimat “sejak siang tadi” juga menempatkan pertemuan itu pada hari yang sama dengan kejadian Bab 17.
- Masalah: kunjungan Daniel yang seharusnya menjadi peristiwa 3 Februari terbaca sebagai kelanjutan malam 2 Februari. Ini bukan sekadar tanggal yang tidak disebut; urutan adegan dan dialog saat ini menempatkannya pada waktu yang sama.
- Dampak: jadwal peristiwa inti berbeda dari outline kanonis, dan pembaca tidak mendapat transisi bahwa Maya telah melewati malam pertama serta berpindah ke ruang rawat inap.
- Rekomendasi: pertahankan Bab 17 sebagai 2 Februari. Pindahkan orientasi Bab 18 ke pagi/siang 3 Februari dan tempatkan pertemuan di ruang rawat inap lantai tiga, sesuai pemindahan yang sudah disiapkan pada akhir Bab 17. Ubah rujukan “malam ini” menjadi instruksi rawat inap yang sesuai waktu kunjungan. Pertahankan peran dokter ortopedi sebagai penanggung jawab fraktur; Daniel hanya mengevaluasi penyebab pingsan.
- Dependensi: periksa kembali penggunaan “besok pagi” dalam dialog Daniel setelah tanggal adegan diperjelas.

### F03 — Bab 19 belum membedakan hari perawatan secara cukup jelas
- Kategori: `TEMPORAL_ORIENTATION`, `TIMELINE`
- Severity: REVIEW
- Release impact: FIX BEFORE RELEASE
- Confidence: High
- Lokasi: pembukaan dan adegan visit Daniel di Bab 19.
- Bukti: Bab 19 tidak menyebut tanggal. Narasi menyebut biaya telah berjalan “empat puluh delapan jam”; Daniel mengatakan gejala membaik dibanding waktu di UGD “kemarin”; Maya menyebut melihat Ratih tergeletak di rumah “kemarin”. Bab ini juga berlangsung pukul delapan malam.
- Masalah: pembaca tidak dapat memastikan apakah Bab 19 berlangsung pada 3, 4, atau hari lain dalam rentang 4–6 Februari yang ditentukan outline. Jika Bab 19 ditempatkan pada 4 Februari, rujukan “kemarin” pada kondisi di UGD tidak lagi tepat untuk kejadian 2 Februari.
- Dampak: perawatan rumah sakit terasa berlangsung dalam satu malam panjang, padahal outline memberi Bab 19 rentang beberapa hari setelah pertemuan pertama Daniel.
- Rekomendasi: pilih satu hari yang jelas dalam rentang outline—4 Februari 2025 adalah pilihan paling sederhana karena cocok dengan petunjuk sekitar 48 jam setelah kejadian 2 Februari. Tambahkan jangkar waktu pada pembukaan, lalu ganti rujukan “kemarin” yang menunjuk ke kejadian 2 Februari menjadi “saat pertama kali dibawa ke UGD” atau “dua hari lalu”, sesuai konteks kalimat.
- Dependensi: sinkronkan ulang durasi sejak deposit awal, kunjungan Daniel, dan waktu Maya menghubungi Pak Dudung.

### F04 — Hari kepulangan Ratih dan lama rawat inap belum sinkron
- Kategori: `TIMELINE`, `CONTINUITY`
- Severity: REVIEW
- Release impact: FIX BEFORE RELEASE
- Confidence: High
- Lokasi: Bab 20, pembukaan dan paragraf tentang biaya rawat inap.
- Bukti pembanding:
  - Outline menetapkan Ratih pulang pada 7 Februari 2025.
  - Bab 20 tidak menyebut tanggal. Dialog Maya menyatakan “kemarin waktu mengurus administrasi kepulangan”, yang dapat dibaca sebagai administrasi kepulangan pada 6 Februari.
  - Narasi menyebut biaya “rawat inap tiga hari di rumah sakit”. Jika Ratih dirawat sejak 2 Februari dan pulang 7 Februari, tiga hari tidak cocok dengan rentang kalender yang dibangun.
- Masalah: tanggal kepulangan serta jumlah hari rawat inap tidak dapat direkonstruksi dengan yakin.
- Dampak: pembaca mungkin tidak tahu berapa lama Ratih dirawat dan kapan ia benar-benar dipulangkan.
- Rekomendasi: beri penanda bahwa Ratih pulang pada 7 Februari. Ubah “kemarin waktu mengurus administrasi kepulangan” menjadi “sebelum pulang” atau bentuk lain yang tidak mengunci urusan administrasi pada 6 Februari. Hapus angka “tiga hari” dari keterangan biaya kecuali memang ada alasan khusus bahwa angka itu hanya merujuk pada uang jaminan untuk tiga hari, bukan total masa rawat.
- Dependensi: pastikan urutan visit terakhir, evaluasi ortopedi, instruksi kontrol, dan kepulangan tidak bertentangan.

### F05 — Frasa “retak tertutup” mencampur dua istilah
- Kategori: `PROSE_CLARITY`, `DOMAIN_FACTUALITY`
- Severity: REVIEW
- Release impact: FIX BEFORE RELEASE
- Confidence: High
- Lokasi: Bab 19, penjelasan Daniel tentang hasil ortopedi.
- Bukti: “patah tulangnya tergolong retak tertutup”.
- Masalah: naskah sebelumnya menyebut kondisi itu sebagai fraktur/patah tulang. “Retak tertutup” terdengar mencampur istilah deskriptif “retak” dengan klasifikasi fraktur tertutup, sehingga makna medisnya kurang presisi.
- Dampak: pembaca dapat bertanya apakah yang dimaksud retak tulang atau fraktur tertutup.
- Rekomendasi: gunakan istilah konsisten, misalnya “fraktur tertutup” atau “patah tulang tertutup”, setelah memastikan itu sesuai hasil pemeriksaan ortopedi yang ditetapkan dalam cerita. Tidak perlu menambahkan tipe fraktur yang tidak ada di kanon.
- Dependensi: samakan istilah dengan penyebutan cedera pergelangan tangan pada Bab 17 dan 20.

### F06 — Kartu kontak klinik Daniel berpotensi terbaca sebagai akses personal
- Kategori: `CHARACTER_KNOWLEDGE`, `RELATIONSHIP_CONTINUITY`
- Severity: REVIEW
- Release impact: AUTHOR CHOICE
- Confidence: Medium
- Lokasi: Bab 20, paragraf tentang berkas kepulangan dan kartu nama.
- Bukti: “kartu nama kecil berukir nama dr. Daniel Aditya dengan nomor kontak klinik rawat jalan yang sengaja dilingkari tinta biru.”
- Masalah: kartu itu bisa dibaca sebagai informasi klinik resmi untuk kontrol pasien, tetapi penyebutan nama Daniel dan nomor yang sengaja dilingkari juga dapat memberi kesan Maya sudah menyimpan jalur kontak khusus dengannya.
- Dampak: ini berpotensi mendahului perkembangan hubungan yang dalam outline baru mulai bergeser dari profesional pada bulan-bulan berikutnya. Outline secara khusus mengarahkan pembaca agar mengingat Daniel pada fase ini sebagai dokter yang tenang, bukan calon pasangan.
- Rekomendasi: bila kartu tersebut adalah bagian rutin dari instruksi kontrol, jelaskan secara singkat bahwa itu nomor klinik/layanan rawat jalan rumah sakit untuk keperluan kontrol. Jangan memberi kesan bahwa Daniel menyerahkan nomor pribadi atau membuka komunikasi personal. Jika detail kartu tidak memiliki fungsi lanjutan, detail tersebut dapat dihilangkan.
- Dependensi: periksa kembali Bab 24 dan awal komunikasi pribadi pada Bab 25–32 agar tidak muncul seolah hubungan pribadi sudah dimulai saat perawatan Ratih.

### F07 — Efek ketenangan Daniel diulang dengan fungsi yang hampir sama
- Kategori: `REPETITION`, `PACING_PROGRESSION`
- Severity: REVIEW
- Release impact: OPTIONAL POLISH
- Confidence: High
- Lokasi: akhir Bab 18; bagian tengah dan akhir Bab 19.
- Bukti: Bab 18 menyebut cara Daniel menjelaskan kondisi dengan tenang meninggalkan kesan mendalam dan menjadi “embun sejuk”. Bab 19 kembali menyatakan penjelasannya tertata dan mudah dipahami serta menjadi “pegangan yang kokoh”, lalu penutup kembali menyebut sikap tenangnya memberi Maya ruang bernapas.
- Masalah: dalam dua bab berurutan, tiga simpulan narator menyampaikan perubahan rasa yang hampir sama. Peristiwa baru di Bab 19—hasil pemeriksaan membaik dan perhatian Daniel kepada penunggu pasien—sebenarnya sudah dapat memberi perkembangan tersendiri.
- Dampak: pembaca menerima kesimpulan emosional yang sama lebih dari sekali, sehingga akhir Bab 19 sedikit kehilangan daya.
- Rekomendasi: pertahankan satu simpulan utama. Biarkan bagian lain menambahkan informasi atau respons baru, misalnya kelegaan setelah hasil pemeriksaan, tanpa kembali menjelaskan bahwa Daniel adalah sosok yang menenangkan. Ini polish opsional, bukan syarat kelayakan.
- Dependensi: jaga agar tahap ini tetap berupa rasa aman kepada dokter yang kompeten, bukan ketertarikan romantis yang sudah matang.

## Yang sudah bekerja

- **Eskalasi cerita masuk akal.** Setelah kehilangan pekerjaan, Maya menerima kabar bahwa Ratih jatuh dan harus dirawat. Ancaman terhadap sumber penghasilan Ratih membuat krisis ini terasa memiliki konsekuensi praktis, bukan hanya menjadi peristiwa dramatis.
- **Peran tokoh sekitar berfungsi.** Pak Dudung dan warga membantu membawa Ratih ke rumah sakit; bantuan ini memperlihatkan jaringan sosial yang nyata. Maya ingin segera mengganti biaya, sesuai kebiasaan tidak ingin merepotkan orang lain.
- **Karakter Ratih konsisten.** Meski baru jatuh dan tangannya patah, pikirannya tetap tertuju pada jahitan tetangga. Ini sejalan dengan pekerjaannya sebagai sumber penghasilan dan identitas sehari-hari.
- **Reaksi Maya dapat dipahami.** Ia mengalihkan dana, mengurus pengembalian bahan dan uang muka, serta menyembunyikan tekanan keuangan dari ibunya. Ini meneruskan pola Maya yang menanggung beban sendiri; bukan kontradiksi karakter.
- **Daniel diperkenalkan secara profesional.** Ia berbicara tentang hasil pemeriksaan, menegaskan kebutuhan rawat inap, dan memantau kondisi Ratih. Kehadirannya tidak memerlukan rayuan atau tindakan khusus di luar tugas dokter.
- **Bab 20 punya fungsi tematik.** Catatan jahitan Ratih menghubungkan masa kecil Maya dengan krisis sekarang. Maya mulai melihat dukungan ibunya bukan sekadar latar belakang, tetapi sesuatu yang nyata yang dapat ia balas melalui tindakan.
- **Tidak diperlukan rewrite besar.** Keempat bab punya fungsi yang jelas dan bergerak dari kecelakaan, penanganan, masa tunggu, hingga kepulangan.

## Peta kesinambungan yang disarankan

| Tanggal | Peristiwa yang seharusnya terbaca |
|---|---|
| 31 Januari 2025 | Hari terakhir Maya bekerja di kantor (Bab 16). |
| 2 Februari 2025 | Ratih pingsan dan jatuh; Maya datang ke UGD (Bab 17). |
| 3 Februari 2025 | Maya bertemu Daniel sebagai dokter penyakit dalam; evaluasi berlangsung profesional di ruang rawat (Bab 18). |
| 4 Februari 2025 | Maya mengurus biaya dan menunggu perkembangan; Daniel memberi pembaruan medis (Bab 19, dapat diperluas dalam rentang outline 4–6 Februari). |
| 7 Februari 2025 | Ratih pulang setelah kondisinya stabil dan instruksi kontrol tersedia (Bab 20). |

Tanggal 4 Februari untuk adegan inti Bab 19 merupakan rekomendasi penataan yang paling sederhana, bukan fakta yang tertulis saat ini. Penulis/editor dapat memilih tanggal lain dalam rentang 4–6 Februari selama semua rujukan relatif diselaraskan.

## Urutan revisi prioritas

1. Tetapkan dan tampilkan tanggal 2 Februari pada Bab 17.
2. Selaraskan Bab 18 ke 3 Februari dan pindahkan orientasi adegannya ke ruang rawat inap setelah pemindahan dari UGD.
3. Pilih tanggal dalam rentang 4–6 Februari untuk Bab 19 dan rapikan semua rujukan “kemarin”/“48 jam”.
4. Tegaskan kepulangan 7 Februari pada Bab 20; hapus atau jelaskan angka “tiga hari” agar tidak berlawanan dengan rentang rawat.
5. Rapikan istilah “retak tertutup”.
6. Pastikan kartu kontak Daniel merupakan kontak layanan klinik resmi, bukan nomor pribadi.
7. Bila melakukan line polish, kurangi satu pengulangan penjelasan tentang ketenangan Daniel.

## Putusan

**Bab 17–20 tidak perlu ditulis ulang.** Perkembangan cerita dan fungsi emosionalnya sudah bekerja. Namun, konflik waktu antara Bab 17 dan Bab 18, durasi yang belum sinkron menuju Bab 20, dan beberapa frasa yang ambigu perlu dibereskan sebelum publikasi. Bab 18 juga paling membutuhkan perbaikan orientasi lokasi/waktu, bukan penambahan panjang secara artifisial.

Status ini hanya berlaku untuk Bab 17–20. Ini bukan sertifikasi bahwa seluruh naskah sudah siap terbit; audit bab berikutnya dan pembacaan akhir lintas bab tetap diperlukan.
