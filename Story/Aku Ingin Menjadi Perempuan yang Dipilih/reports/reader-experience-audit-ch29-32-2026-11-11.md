# Reader-Experience Audit — Bab 29–32

Tanggal audit: 11 November 2026  
Naskah: `Story/Aku Ingin Menjadi Perempuan yang Dipilih/manuscript.md`  
Outline: `Story/Aku Ingin Menjadi Perempuan yang Dipilih/outline.md`  
Manuscript SHA saat audit: `c235875ff0f569088936c5c4dea76207b99ff774`

## Status

**NEEDS TARGETED REVISION** untuk Bab 29–32.

Audit mencakup Bab 29–32, pembandingan dengan outline kanonis, dan pemeriksaan kesinambungan terbatas ke Bab 28 serta Bab 33. Naskah utama tidak diubah.

Rangkaian ini merupakan titik perubahan penting: komunikasi pribadi dimulai dari alasan kerja, berkembang menjadi percakapan harian, mulai diperhatikan Sarah, lalu berubah menjadi ruang curhat emosional Daniel. Secara dramaturgis, eskalasi tersebut masuk akal dan sesuai arah cerita. Maya tidak langsung melakukan tindakan romantis terang-terangan; justru rasionalisasi bahwa percakapan mereka masih sopan menjadi cara ia mengabaikan batas yang mulai dilanggar.

Namun, terdapat dua masalah kontinuitas yang perlu diperbaiki sebelum publikasi: kronologi Bab 32–33 yang terbalik dan informasi pelepasan gips Ratih yang bertentangan dengan bab sebelumnya. Selain itu, Bab 30 dan 32 mengakses pikiran Daniel tanpa penanda POV, mengulang masalah yang sudah ditemukan pada Bab 26.

## Temuan

### F01 — Bab 32 berlangsung setelah rentang waktu Bab 33
- Kategori: `TIMELINE`, `CHAPTER_ORDER`
- Severity: ERROR
- Release impact: FIX BEFORE RELEASE
- Confidence: High
- Lokasi: pembukaan Bab 32 dan Bab 33.
- Bukti:
  - Bab 32 dibuka dengan “Jumat sore di pertengahan Juli”.
  - Outline menetapkan Bab 33 berlangsung pada 1–10 Juli 2025.
  - Bab 33 secara eksplisit menyebut kebiasaan baru Maya tumbuh “sepanjang minggu pertama bulan Juli 2025”.
  - Urutan bab saat ini menempatkan Bab 32 sebelum Bab 33.
- Masalah: Bab 32 terjadi pada pertengahan Juli, tetapi Bab 33 kembali ke minggu pertama Juli. Ini membuat alur bergerak mundur tanpa penanda kilas balik.
- Dampak: pembaca dapat mengira Maya sudah mendapat curahan masalah rumah tangga Daniel sebelum kebiasaan menunggu pesan malam terbentuk, padahal Bab 33 menggambarkan kebiasaan tersebut sebagai perkembangan yang sudah berlangsung pada awal Juli.
- Rekomendasi editorial: selaraskan kronologi berdasarkan fungsi adegan, bukan sekadar mengganti tanggal secara mekanis. Pilihan paling sederhana adalah memindahkan kejadian Bab 32 ke akhir Juni atau awal Juli, sebelum rentang Bab 33, jika adegan curhat memang menjadi pemicu peningkatan komunikasi. Namun, bila adegan tersebut harus berlangsung pada pertengahan Juli, maka Bab 33 dan outline perlu dipindahkan ke rentang setelah kejadian Bab 32. Jangan mengubah urutan bab tanpa memastikan progres ketergantungan emosional tetap bertahap.
- Dependensi: cek tanggal Bab 33–40 agar eskalasi menuju 12 Agustus, 15 Agustus, dan 19 Agustus tetap konsisten.

### F02 — Bab 30 dan Bab 32 melanggar POV terbatas dengan mengakses pikiran Daniel
- Kategori: `POV_VIOLATION`, `NARRATIVE_CONSISTENCY`
- Severity: ERROR
- Release impact: FIX BEFORE RELEASE
- Confidence: High
- Lokasi: Bab 30 dan Bab 32.
- Bukti Bab 30:
  - “Bagi Daniel, menatap bilah percakapan dengan Maya menghadirkan rasa nyaman...”
  - “Di sana, ia tidak perlu memasang topeng dokter spesialis...”
- Bukti Bab 32:
  - “Sikap Maya yang tenang dan tidak menghujatnya dengan pertanyaan mengusik membuat ketegangan di dada Daniel perlahan melentur.”
  - “Binar matanya memancarkan rasa terkejut sekaligus lega yang amat dalam.”
  - “Pengertian yang diberikan Maya terasa begitu pas...”
  - Narasi menyatakan pengakuan Daniel “meluncur jujur” dan menjelaskan ruang batin yang menyiksanya selama berbulan-bulan.
- Masalah: outline menetapkan orang ketiga terbatas yang dominan mengikuti Maya. Bab 30 dan 32 tidak diberi penanda POV Daniel, tetapi narasi masuk ke pengalaman batinnya dan menyajikan penilaian atas kejujuran serta kondisi emosionalnya sebagai fakta.
- Dampak: pembaca tidak lagi dibatasi pada apa yang Maya lihat, dengar, atau simpulkan. Ini juga berisiko membuat cerita menerima keluhan Daniel tentang Sarah sebagai kebenaran objektif, padahal Maya hanya mendengar satu sisi rumah tangga mereka.
- Rekomendasi: pertahankan POV Maya. Ubah pernyataan batin Daniel menjadi perilaku yang dapat diamati Maya—misalnya jeda sebelum menjawab, bahu yang mengendur, atau cara ia memilih kata—dan biarkan Maya menafsirkan tanda-tanda tersebut tanpa narator memastikan apa yang sebenarnya dirasakan Daniel. Hindari menyatakan bahwa Daniel jujur atau bahwa Maya memahami seluruh masalah rumah tangganya.
- Dependensi: temuan ini berulang setelah Bab 26. Pada tahap revisi terpadu, audit ulang semua bab dengan POV utama Maya agar tidak ada perpindahan batin tanpa penanda.

### F03 — Waktu pelepasan gips Ratih di Bab 29 bertentangan dengan Bab 24 dan Bab 28
- Kategori: `CONTINUITY`, `MEDICAL_TIMELINE`
- Severity: ERROR
- Release impact: FIX BEFORE RELEASE
- Confidence: High
- Lokasi: Bab 29, percakapan pesan antara Maya dan Daniel.
- Bukti:
  - Bab 24 menyebut gips Ratih sudah dilepas pada minggu sebelumnya dalam konteks kegiatan 12 April.
  - Bab 28 berlangsung pada 14 Mei dan menyatakan Ratih sudah sekitar sebulan bebas gips.
  - Bab 29 berlangsung pada 2 Juni menurut outline, tetapi Maya mengatakan, “Minggu kemarin gipsnya sudah sepenuhnya lepas.”
- Masalah: jika gips sudah dilepas sekitar pertengahan April, pada 2 Juni peristiwa itu sudah berlalu sekitar enam sampai tujuh minggu, bukan minggu sebelumnya.
- Dampak: kontinuitas pemulihan Ratih menjadi tidak sinkron dan membuat pembaca yang mengingat Bab 24 atau 28 meragukan urutan perawatan.
- Rekomendasi: ubah keterangan Maya menjadi rujukan waktu yang sesuai, misalnya “sejak pertengahan April gipsnya sudah dilepas” atau cukup “gipsnya sudah dilepas beberapa minggu lalu”. Jangan menggeser tanggal pelepasan gips hanya untuk menyesuaikan dialog Bab 29 karena hal itu akan merusak kontinuitas Bab 24 dan 28.
- Dependensi: pertahankan tanggal pelepasan gips yang sudah tersirat di Bab 24 dan Bab 28.

### F04 — Saran Daniel tentang pemulihan tendon Ratih perlu diselaraskan dengan peran medisnya
- Kategori: `MEDICAL_PLAUSIBILITY`, `PROFESSIONAL_BOUNDARY`
- Severity: REVIEW
- Release impact: FIX BEFORE RELEASE
- Confidence: Medium
- Lokasi: Bab 29, pesan Daniel setelah menanyakan kondisi Ratih.
- Bukti: “Kunci pemulihan tendonnya memang ada di kesabaran” dan “Kalau ada keluhan nyeri atau kaku yang mengganggu saat latihan di rumah, Mbak Maya bisa beri tahu saya.”
- Masalah: Daniel adalah dokter spesialis penyakit dalam. Cedera pergelangan tangan Ratih dan latihan pemulihan gerak merupakan ranah tindak lanjut ortopedi atau rehabilitasi medis. Dialog ini membuat Daniel terdengar seolah menjadi penanggung jawab langsung rehabilitasi cedera tersebut. Bab sebelumnya juga sudah menetapkan peran dokter ortopedi dalam penanganan fraktur.
- Dampak: dapat menimbulkan keraguan tentang pembagian tanggung jawab medis sekaligus memberi alasan yang terlalu mudah bagi Daniel untuk membuka komunikasi personal di luar hubungan dokter-pasien.
- Rekomendasi: Daniel boleh menanyakan kabar mantan pasien yang pernah ia rawat, tetapi arahkan saran teknis mengenai latihan dan keluhan pergelangan tangan kepada dokter ortopedi atau fisioterapis yang menangani Ratih. Jika Daniel tetap menawarkan bantuan, batasi pada saran umum dan jangan menggambarkan dirinya sebagai pengganti dokter yang menangani rehabilitasi.
- Dependensi: selaraskan dengan detail fraktur, pelepasan gips, dan pemulihan Ratih di Bab 17–24.

### F05 — Bab 29 belum menandai tanggal 2 Juni dan Bab 30 belum mengunci posisi adegannya dalam rentang 3–20 Juni
- Kategori: `TEMPORAL_ORIENTATION`
- Severity: REVIEW
- Release impact: FIX BEFORE RELEASE
- Confidence: High
- Lokasi: pembukaan Bab 29 dan Bab 30.
- Bukti:
  - Outline menetapkan pesan pribadi pertama pada 2 Juni 2025.
  - Bab 29 membuka adegan dengan jam lima sore dan rapat yang baru selesai, tetapi tidak menyebut tanggal.
  - Outline menempatkan Bab 30 pada 3–20 Juni.
  - Bab 30 membuka percakapan pukul 20.20 dengan pertanyaan Daniel tentang perjalanan Maya “sore tadi”, lalu menyebut percakapan malam itu seperti malam-malam sebelumnya “sepanjang pertengahan bulan Juni 2025”.
- Masalah: pembaca tidak dapat menentukan apakah adegan awal Bab 30 berlangsung pada malam yang sama dengan pesan pertama 2 Juni atau merupakan salah satu malam pada pertengahan rentang 3–20 Juni. Frasa “sore tadi” memberi kesan adegan itu menyambung langsung dengan suatu pertemuan pada hari yang sama, sementara kalimat setelahnya menyatakan kebiasaan pesan telah berlangsung selama beberapa waktu.
- Dampak: tahap perubahan dari pesan pertama menjadi percakapan hampir setiap hari terasa dipadatkan dan penanda waktu tidak cukup presisi.
- Rekomendasi: tambahkan tanggal atau penanda waktu yang jelas di Bab 29 dan pilih satu titik representatif dalam rentang Bab 30. Pastikan pembukaan Bab 30 tidak memberi kesan bahwa kebiasaan harian sudah ada pada malam pertama. Gunakan rentang 3–20 Juni sesuai outline, lalu biarkan narasi ringkas menunjukkan bagaimana frekuensinya meningkat.
- Dependensi: tanggal 23 Juni di Bab 31 harus tetap datang setelah kebiasaan komunikasi itu berkembang.

### F06 — Narasi Bab 30 terlalu objektif menyebut komunikasi mereka tidak melanggar etika
- Kategori: `MORAL_FRAMING`, `CHARACTER_PSYCHOLOGY`
- Severity: REVIEW
- Release impact: FIX BEFORE RELEASE
- Confidence: High
- Lokasi: Bab 30, paragraf yang dimulai dengan “Kalimat-kalimat yang dipertukarkan di antara mereka...”
- Bukti: “Tidak ada kata-kata mesra yang vulgar, tidak ada rayuan yang melewati batas etika, dan tidak ada janji-janji yang dilanggar.” Setelah itu narasi menyebut intensitas dan frekuensi pesan membuat batas emosional mereka mengabur.
- Masalah: kalimat tersebut menyajikan kesopanan bahasa seolah membuktikan tidak ada pelanggaran etika. Padahal, komunikasi hampir setiap malam, pembicaraan di luar urusan kerja, dan ketergantungan emosional sudah menunjukkan batas pernikahan mulai dilanggar. Konflik utama cerita justru terletak pada kedekatan emosional yang tidak harus disertai rayuan vulgar atau hubungan fisik.
- Dampak: pembaca dapat menerima pembenaran Maya sebagai penilaian objektif narator, bukan sebagai rasionalisasi tokoh yang sedang mencari alasan untuk mempertahankan perhatian Daniel.
- Rekomendasi: pertahankan fakta bahwa pesan mereka masih sopan dan belum eksplisit romantis, tetapi tempatkan pembenaran tersebut secara jelas dalam pikiran Maya. Narasi perlu menjaga jarak kritis: kesopanan bahasa tidak otomatis membuat intensitas dan ketergantungan emosional itu netral.
- Dependensi: penting untuk menjaga konsistensi moral menuju Bab 37–45, ketika Maya dan Daniel harus mengakui bahwa kedekatan mereka memang telah melewati batas.

### F07 — Bab 31 sudah menggunakan POV Sarah dengan benar, tetapi satu kesimpulan narator perlu dilunakkan
- Kategori: `POV_PRECISION`
- Severity: INFO
- Release impact: OPTIONAL POLISH
- Confidence: Medium
- Lokasi: Bab 31, setelah Daniel menjelaskan identitas Maya dan urusan revisi.
- Bukti: “Sarah memperhatikan wajah suaminya. Tidak ada kebohongan verbal pada kalimat Daniel.”
- Masalah: Sarah dapat menilai bahwa penjelasan Daniel terdengar masuk akal, tetapi ia tidak dapat memastikan secara objektif apakah seluruh kalimatnya benar. Kalimat ini memberi pembaca kepastian yang tidak dimiliki Sarah.
- Dampak: mengurangi ketegangan kecurigaan Sarah dan sedikit menggeser narasi keluar dari POV yang sudah ditandai dengan baik.
- Rekomendasi: ubah menjadi persepsi Sarah, misalnya penjelasan Daniel terdengar masuk akal dan sesuai dengan agenda kerja yang ia ketahui. Dengan begitu, Sarah tetap belum memiliki bukti, tetapi pembaca tidak diberi jaminan objektif bahwa Daniel jujur.
- Catatan positif: penandaan “Sudut Pandang: Sarah” pada awal Bab 31 sudah tepat dan sejalan dengan aturan outline.

### F08 — Pengulangan penjelasan tentang batas dan ketergantungan emosional mulai terasa
- Kategori: `REPETITION`, `PACING`
- Severity: INFO
- Release impact: OPTIONAL POLISH
- Confidence: High
- Lokasi: akhir Bab 29, Bab 30, dan Bab 32.
- Bukti:
  - Bab 29 menyebut pesan Daniel sebagai “pintu kecil menuju ruang emosional baru”.
  - Bab 30 menyebut batas emosional mengabur dan Maya menunggu getaran ponsel setiap malam.
  - Bab 32 kembali menjelaskan Maya merasa dibutuhkan, kebutuhan untuk merasa penting dan terpilih, serta masuk lebih jauh ke ruang emosional yang bukan miliknya.
- Masalah: gagasan yang sama dijelaskan berulang dengan metafora ruang, kehangatan, dan ketergantungan. Perkembangan sebenarnya sudah terlihat melalui tindakan: Maya menunggu pesan, mengubah rutinitas, lalu menawarkan diri sebagai tempat bercerita.
- Dampak: eskalasi terasa lebih banyak diterangkan daripada diperlihatkan.
- Rekomendasi: pilih satu atau dua simpulan reflektif yang paling kuat. Pada bab lain, utamakan perubahan perilaku dan pilihan tokoh. Pertahankan motif kebutuhan Maya untuk dipilih, tetapi jangan menjelaskan maknanya dengan metafora serupa pada setiap penutup.
- Dependensi: jaga agar perkembangan ketergantungan emosional tetap bertahap menuju Bab 33–40.

## Yang sudah bekerja

- **Pemicu pesan pertama masuk akal.** Daniel memiliki alasan kerja yang konkret untuk menghubungi Maya setelah rapat dan menemukan kesalahan angka pada materi edukasi.
- **Pergeseran percakapan bertahap.** Bab 29 dimulai dari koreksi teknis, Bab 30 memperluas topik ke keseharian, dan Bab 32 menjadi momen Daniel membagikan masalah rumah tangga.
- **Maya tidak digambarkan sepenuhnya tidak sadar.** Ia tahu Daniel menikah dengan Sarah dan mulai menyadari bahwa mendengarkan masalah rumah tangga pria beristri merupakan batas yang seharusnya dijaga.
- **Sarah tidak langsung bereaksi berlebihan.** Bab 31 memperlihatkan ia mengamati perubahan perilaku Daniel tanpa menuduh berdasarkan satu notifikasi.
- **Kecurigaan Sarah berangkat dari perubahan kebiasaan, bukan kecemburuan tanpa dasar.** Ponsel yang mulai dijaga, dibawa ke kamar mandi, dan dibalik layarnya menjadi petunjuk perilaku yang masuk akal.
- **Daniel tidak menyalahkan Sarah secara terbuka.** Dalam percakapan dengan Maya, ia mengakui Sarah perempuan yang baik dan menggambarkan masalah komunikasi sebagai kebiasaan dua arah. Namun, cerita perlu menjaga agar versi Daniel tidak diperlakukan sebagai kebenaran tunggal.
- **Bab 32 memberi titik balik yang jelas.** Tawaran Maya untuk selalu ada sebagai teman cerita membuat hubungan bergeser dari percakapan rutin menjadi dukungan emosional personal.
- **Bab 31 menggunakan POV Sarah secara eksplisit.** Ini contoh yang dapat dipertahankan untuk bab-bab lain yang memang perlu mengikuti tokoh selain Maya.

## Peta kesinambungan

| Tanggal/periode | Peristiwa |
|---|---|
| 2 Juni 2025 | Pesan pribadi pertama Daniel kepada Maya setelah rapat dan koreksi materi (Bab 29). |
| 3–20 Juni 2025 | Pesan pribadi semakin sering dan topik berkembang ke rutinitas serta keseharian (Bab 30). |
| 23 Juni 2025 | Sarah melihat notifikasi pesan dari Maya dan mulai mengamati kebiasaan Daniel (Bab 31). |
| Juli 2025 | Daniel menceritakan ketegangan rumah tangganya kepada Maya; Maya menawarkan diri sebagai teman cerita (Bab 32). |
| 1–10 Juli 2025 | Outline menempatkan kebiasaan Maya menunggu pesan dan menyesuaikan rutinitas (Bab 33). |

**Catatan kronologi:** dua baris terakhir belum sinkron dengan urutan bab karena adegan Bab 32 saat ini secara eksplisit berlangsung pada pertengahan Juli, sedangkan Bab 33 berada pada 1–10 Juli.

## Urutan revisi

1. Selesaikan konflik tanggal Bab 32 dan Bab 33 terlebih dahulu. Ini menentukan urutan perkembangan ketergantungan emosional.
2. Perbaiki POV Bab 30 dan 32 agar narasi tetap mengikuti Maya; jangan mengubahnya menjadi narator serba tahu.
3. Selaraskan keterangan pelepasan gips Ratih di Bab 29 dengan Bab 24 dan 28.
4. Rapikan saran Daniel tentang pemulihan Ratih agar sesuai dengan peran spesialis penyakit dalam dan tindak lanjut ortopedi/rehabilitasi.
5. Beri jangkar waktu yang jelas pada Bab 29 dan Bab 30.
6. Ubah pembenaran moral Bab 30 menjadi rasionalisasi Maya, bukan penilaian objektif narator.
7. Lunakkan satu kalimat objektif di Bab 31 dan kurangi pengulangan simpulan emosional pada Bab 29–32.

## Putusan

**Bab 29–32 memiliki eskalasi emosional yang tepat dan tidak membutuhkan rewrite keseluruhan.** Pemicu komunikasi pribadi kredibel, Sarah mulai menangkap perubahan perilaku Daniel dengan wajar, dan Bab 32 menandai pergeseran hubungan ke dukungan emosional yang lebih intim.

Namun, sebelum publikasi, kronologi Bab 32–33, tanggal pelepasan gips Ratih, dan pelanggaran POV Bab 30 serta 32 harus diselesaikan. Temuan POV ini juga menunjukkan bahwa masalahnya bukan insiden tunggal di Bab 26; pemeriksaan lintas bab nantinya perlu mencari pola yang sama di seluruh naskah.

Status ini hanya berlaku untuk Bab 29–32. Novel secara keseluruhan belum dapat dinyatakan siap terbit sebelum audit bab-bab berikutnya dan pemeriksaan lintas bab selesai.
