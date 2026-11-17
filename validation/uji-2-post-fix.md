# Laporan Audit Editorial Lengkap — UJI 2 (Naskah Post-Fix / Terbaru: *Catatan untuk Orang Sungkan*)

- **Proyek / Naskah:** *Catatan untuk Orang Sungkan* (Versi terbaru / `post-fix` dari branch utama `novel-metropop`)
- **Direktori Audit:** `/tmp/uji-post` (`$TMPDIR/uji-post`)
- **Cakupan Dokumen yang Dibaca:** 32 bab lengkap (`chapters/bab-01.md` s.d. `chapters/bab-32.md`) dan `outline.md` (Status: TERKUNCI v1.1).
- **Dokumen yang Tidak Dibaca / Diabaikan Sesuai Instruksi:** Tidak membuka `canon.md`, `ledger.md`, `state.md`, `reports/`, `tests/fixtures/`, maupun `EXPECTED-FINDINGS.md`.
- **Pernyataan *Blind Pass* Wajib (`AGENTS.md` §7.1):** Audit ini diawali dengan **blind pass** murni terhadap 32 file bab mentah (`chapters/bab-01.md` s.d. `chapters/bab-32.md`) dan `outline.md` di `/tmp/uji-post`. Seluruh pembacaan pengalaman pembaca (*reader pass*) dan penyusunan **Tabel Rantai Sebab-Akibat** dilakukan langsung dari bukti teks di halaman naskah.
- **Keputusan Akhir Kesiapan Publikasi (`rules/09-publication-readiness.md`):** **`NOT READY` (Masih Terdapat Cacat Struktural Kausalitas `HIGH` / `BLOCKER` pada Paruh Kedua serta Sisa Kesalahan Rujukan Mundur `--refs`, Prosedur Dunia Nyata, dan Teknis Naskah)**

---

## 1. Story Assessment dan Evaluasi Developmental (`rules/16` & `rules/15`)

### 1.1. Apa yang Sudah Bekerja dan Perbaikan yang Telah Diterapkan pada Versi Terbaru
1. **Kekuatan Cerita & Karakterisasi Paruh Pertama (Bab 1–18):**
   - Pembukaan *in medias res* di tangga darurat (Bab 1–2) serta progresi latihan berkata "tidak" (Bab 4–15) berjalan efektif, hangat, dan mudah diikuti pembaca.
   - Sejumlah lubang kontinuitas dari draf lama telah ditambal pada versi terbaru ini, antara lain:
     - Lokasi kos sementara Saka telah diselaraskan menjadi di **Tebet** (Bab 2 baris 33), sehingga cocok dengan arah naik KRL ke selatan dari Stasiun Cikini (Bab 16 baris 23).
     - Pengerjaan poster titipan Dimas telah dijembatani pada Bab 3 baris 5 (dikerjakan dini hari Selasa di kos dan diunggah Selasa pagi di Bab 7 baris 31).
     - Konsistensi benda tas Saka (*"ransel kanvas hitam"*), kemeja Selasa (*"kemeja katun abu-abunya"* di Bab 4 baris 65), tangan kanan pemutar tutup botol di Bab 17, serta jam rapat evaluasi sampul (*"jam setengah empat sore"* di Bab 14 & 15) telah diselaraskan.
     - Penanaman detail masa lalu Saka di Bab 12 baris 27 (*"Dia akhirnya memilih laki-laki yang direstui orang tuanya karena pekerjaannya sudah jelas dan dianggap lebih mapan"*) dan lokasi rujukan *"di kedai kopi dulu"* (Bab 21 baris 25 & Bab 25 baris 35) telah diperbaiki.
     - Alur pengiriman halaman penutup oleh Nadia setelah Saka pulang (Bab 21 baris 9 & Bab 24 baris 29) serta pencetakan digital terbatas untuk edisi peluncuran (Bab 21, 26, 30) telah ditambahkan.
     - Tanggapan batin Nadia terhadap petunjuk tab kos tahunan Cikini (Bab 20 baris 29) dan monolog menghapus pesan WhatsApp di Bab 29 baris 61 telah disisipkan.

### 1.2. Mengapa Tambalan Kosmetik Belum Menyelesaikan Masalah Struktural dan Fakta Operasional
Meskipun tambalan kalimat tunggal di atas memperbaiki sejumlah kontradiksi permukaan, pengujian ketat menggunakan `rules/01-plot-and-causality.md`, `rules/05-character-knowledge.md`, `rules/06-setup-payoff.md`, dan `rules/18-real-world-procedures.md` menunjukkan bahwa **fondasi kausalitas paruh kedua (Bab 10–30) masih cacat secara struktural**, disertai beberapa kesalahan rujukan mundur (`--refs`), prosedur dunia nyata, dan teknis yang belum tertangani:
1. **Konflik Utama Paruh Kedua Masih Bergantung pada 6–7 Kali Pengabaian Komunikasi dan Alasan Sifat Abstrak (`HIGH` / `BLOCKER`):**
   - Tambalan monolog di Bab 20 baris 29 dan Bab 29 baris 61 tidak mengubah fakta bahwa seluruh konflik Bab 19–29 hanya bertahan karena tokoh berulang kali menahan satu kalimat konfirmasi dengan alasan label sifat abstrak (*"tidak tega merusak suasana"*, *"penyakit nggak enakanku"*, *"rasa malu"*, *"gengsi"*, *"terlalu takut mendengar jawaban"*).
   - Di Bab 20 baris 29, alasan Nadia menepis petunjuk Bab 14 (bahwa info kos tahunan Cikini itu cuma buat teman Jogja Saka) **gagal menjelaskan petunjuk kedua yang dilihat Nadia pada tab yang sama di Bab 14 baris 18**, yaitu **"formulir kepegawaian antar-cabang"**, serta laporan Tari di Bab 18 baris 39 bahwa Saka menyerahkan map formulir ke HRD! Tidak masuk akal jika formulir kepegawaian internal antar-cabang di laptop Saka dan di meja HRD dianggap milik "teman Jogja".
   - Kontradiksi percakapan telepon Pak Ramdan dengan Pak Bambang di Bab 20 baris 19–23 vs fakta Bab 31 baris 57–59 (bahwa Pak Ramdan sendiri yang menawari Saka mutasi tetap sejak awal proyek dan keputusan pindah Saka sudah bulat sejak 3 minggu lalu) masih belum diperbaiki.
   - Regresi karakter Nadia di Bab 25–27 masih utuh: Nadia tetap bersiap mengangguk menerima Dimas kembali di Bab 27 baris 17 dan hanya batal karena kebetulan pelayan salah mengantar es jeruk yang memicu Dimas membuka topengnya sendiri.
2. **Sisa Kesalahan Rujukan Mundur (`--refs`) dan Prosedur Dunia Nyata:**
   - Rujukan waktu relatif yang salah masih tertinggal di Bab 6 baris 55 (*"kejadian kemarin"* untuk Selasa sore pada hari Jumat), Bab 18 baris 39 (*"Kemarin hari Jumat"* pada hari Senin + lompatan 1 minggu kalender antara Bab 14 dan Bab 18), Bab 26 baris 29, Bab 28 baris 57, Bab 31 baris 21, serta kesalahan lokasi warung soto tanpa seledri di Bab 31 baris 75 (*"warung depan gedung kantor"* padahal di Kwitang pada Bab 9).
   - Pada prosedur dunia nyata, masih terdapat klaim mustahil di Bab 29 baris 31 & 59 (kereta malam Jakarta–Yogyakarta yang berangkat Selasa petang masih berada di perjalanan/"di luar jangkauan sinyal kereta" pada Rabu pukul 08.30 pagi), Bab 32 baris 3 (buku yang cetak offset-nya baru "menyusul" sudah terpajang rapi di rak depan toko-toko buku Cikini dan Matraman hanya 3 hari setelah peluncuran Jumat), dan Bab 20 & 31 (kop surat *"Kantor Pusat Penerbit Aksara Senja Cabang Yogyakarta"*).

---

## 2. Tabel Rantai Sebab-Akibat dan Audit Kausalitas (`rules/01-plot-and-causality.md` & `rules/05-character-knowledge.md`)

### 2.1. Tabel Rantai Sebab-Akibat (7 Kolom Wajib dari Bab Mentah)

| peristiwa | keinginan tokoh | hambatan | pilihan | akibat yang tampak di halaman | pertanyaan "kenapa tidak X?" | jawaban di halaman |
|---|---|---|---|---|---|---|
| **Bab 1–3:** Nadia memaki Dimas & Mbak Dinda di tangga darurat Senin pukul 19.30; dipergoki Saka; kabur pulang pukul 19.45 (Bab 2); dini hari Selasa mengerjakan poster Dimas di kos karena susah tidur (Bab 3 baris 5) dan mengunggahnya Selasa pagi (Bab 7 baris 31). | Nadia ingin segera keluar dari rasa malu di tangga darurat, namun masih terikat kebiasaan tidak berani menolak tugas titipan. | Rasa malu ekstrem setelah dipergoki Saka dan kebiasaan lama selalu mengiyakan permintaan orang. | Nadia kabur pulang Senin malam, lalu menyelesaikan poster Dimas dini hari Selasa di kos sebelum berangkat kerja. | Poster selesai Selasa pagi dan diunggah ke folder pemasaran; Mbak Dinda dan Dimas berterima kasih tanpa tahu Nadia memaki mereka semalam. | Kenapa Nadia tetap mengerjakan poster Dimas pada Selasa dini hari padahal di akhir Bab 2 ia sudah bertekad *"Bodo amat. Malam ini aku tidak peduli lagi"*? | Dijelaskan di halaman (Bab 3 baris 5): karena tidak bisa tidur semalaman memikirkan kalimat Saka dan belum punya keberanian menolak langsung di hari pertama. (**Valid**) |
| **Bab 4–7:** Saka menutup meja pukul 17.01 (Bab 4), menyemangati Nadia menolak talangan ayam bakar Riko (Bab 5), dan diam bersedekap memberi ruang saat Dimas & Vanya meminta *backdrop* Jumat sore (Bab 6–7). | Nadia ingin berhenti dimanfaatkan oleh Mbak Dinda, Riko, dan Dimas. | Kebiasaan lama takut dicap mantan pendendam di depan Vanya (Bab 6 baris 49) dan rasa sungkan di depan rekan kantor. | Nadia menolak Riko dengan menunjuk stiker QRIS (Bab 5) dan menolak Dimas dengan mengarahkan ke file mentah di folder bersama (Bab 7). | Riko terpaksa membayar sendiri; Dimas & Vanya pergi ke percetakan dengan kesal; Saka memberi apresiasi es jeruk (Bab 5) dan cokelat (Bab 7) sambil memutar tutup botol dua kali *klik*. | Kenapa Dimas dan Vanya tidak langsung mengubah skala *backdrop* sendiri dari awal jika aplikasi dan file mentah sudah ada di folder pemasaran? | Terjawab di halaman (Bab 6 baris 39–41): Vanya sudah mencoba tetapi resolusinya pecah, dan mereka ingin lepas tangan agar bisa pergi mengecek katering berdua. (**Valid**) |
| **Bab 10:** Minggu siang di Rawamangun, Ibu menanyakan Dimas dan memuji Dimas sebagai calon menantu ramah; Mbak Raras meminta pinjam Rp4 juta tabungan tablet gambar Nadia untuk hotel/mobil di Bali. | Nadia ingin mempertahankan tabungan Rp4 juta untuk membeli tablet gambar kerja dan tidak ingin terus dikaitkan dengan Dimas. | Tekanan emosional Ibu (*"ngalah dulu sama kakaknya"*) dan ketakutan dianggap anak egois/durhaka sejak kecil. | Untuk uang Rp4 juta, Nadia menunda jawaban (*"cek saldo dulu nanti malam"*). Namun untuk status Dimas, Nadia berbohong bahwa Dimas sibuk acara kantor dan menyembunyikan fakta bahwa mereka sudah putus. | Ibu tetap menganggap Dimas pacar Nadia (yang kelak memicu Ibu menelepon Dimas saat sakit di Bab 22); Mbak Raras terus menagih uang Rp4 juta di hari Senin. | **Kenapa Nadia tidak memberi tahu Ibunya sejak Minggu siang itu bahwa ia dan Dimas sudah putus?** | **ALASAN ABSTRAK (Temuan `HIGH`):** Bab 10 baris 17 hanya menyebutkan *"lidahku langsung kelu tidak tega merusak suasana hatinya"*. Tidak ada ancaman konkret, krisis kesehatan Ibu, atau hambatan situasional di meja makan yang menghalangi Nadia menyampaikan bahwa mereka sudah putus. |
| **Bab 11–13:** Kabel tablet gambar Nadia rusak parah saat kerja Senin; Saka menceritakan masa lalu studionya yang bangkrut di Jogja dan mantannya yang memilih pria pilihan orang tua yang lebih mapan (Bab 12 baris 27); Senin malam Nadia menelepon Ibu. | Nadia ingin membeli tablet gambar baru tanpa memutus hubungan baik dengan ibunya. | Desakan WhatsApp Mbak Raras (batas bayar hotel pukul 22.00) dan nada kecewa Ibu di telepon. | Nadia menolak meminjamkan Rp4 juta secara lembut dengan alasan alat kerjanya rusak, dan memberikan Rp500 ribu secara cuma-cuma untuk jajan Daffa. | Ibu akhirnya memaklumi dan menyuruh Mbak Raras mencari penginapan yang lebih murah di Bali sesuai uang yang ada (Bab 13 baris 57). | Kenapa Nadia baru berani menolak pada Senin malam lewat telepon, bukan saat makan siang Minggu di Bab 10? | Terjawab di halaman (Bab 11–12): kabel tablet gambarnya kumat parah saat kerja Senin dan cerita masa lalu Saka di kedai kopi memberinya keberanian dan argumen logis. (**Valid**) |
| **Bab 14 & Bab 18:** Nadia melihat tab *"daftar sewa kamar kos tahunan daerah Cikini dan formulir kepegawaian antar-cabang"* di laptop Saka (Bab 14 baris 17–21); Tari melaporkan Saka menyerahkan map formulir ke Mbak Sinta HRD (Bab 18 baris 39). | Saka ingin mengurus mutasi tetap ke Jakarta atas tawaran Pak Ramdan; Nadia ingin tahu mengapa Saka mencari kos tahunan di Cikini. | Saka enggan mengungkapkan rencana mutasinya sebelum SK pelepasan resmi ditandatangani Kepala Cabang Yogyakarta. | Saka berbohong bahwa info kos tahunan itu titipan teman Jogja (Bab 14 baris 21, tanpa *tell* memutar tutup botol); Nadia menanggapi info Tari dengan asumsi *"Mungkin laporan proyek buku"* (Bab 18 baris 43). | Petunjuk kuat tentang kepindahan permanen Saka ke Jakarta sudah diketahui langsung oleh Nadia sejak Bab 14 dan Bab 18. | **Kenapa Saka berbohong bahwa kos tahunan Cikini dan formulir kepegawaian antar-cabang itu untuk teman Jogja, dan kenapa ia tidak memutar tutup botolnya seperti aturan *tell* internal cerita?** | **MOTIF PENAHANAN INFORMASI LEMAH (`REVIEW` / `HIGH`):** Di Bab 14 tidak ada alasan mengapa Saka harus berbohong tentang formulir kepegawaian yang sudah ia ajukan secara bulat sejak minggu kedua (Bab 31 baris 59). |
| **Bab 19–20:** Dimas meminta maaf di pantry dan membisikkan bahwa tugas Saka hanya 5 minggu (Bab 19); Nadia menguping telepon Pak Ramdan ke Pak Bambang dan melihat amplop *"Verifikasi Masa Tugas dan Pelepasan Pegawai"* (Bab 20). | Nadia ingin kepastian apakah Saka akan tetap di Jakarta atau kembali ke Yogyakarta setelah proyek *Sela Waktu* selesai. | Kalimat Pak Ramdan di telepon terdengar seperti masa tugas Saka habis minggu depan; Saka sedang di lantai dua. | Nadia sempat teringat tab kos tahunan Cikini dan formulir kepegawaian antar-cabang di laptop Saka, namun langsung menepisnya karena percaya ucapan Saka bahwa info kos itu untuk temannya dari Jogja (Bab 20 baris 29). | Nadia patah hati, merasa seluruh perhatian Saka hanya sebatas tanggung jawab editor proyek sementara, dan menggambar sketsa kursi kosong di halaman penutup. | **1) Kenapa Nadia menepis petunjuk *"formulir kepegawaian antar-cabang"* di laptop Saka (Bab 14) dan penyerahan formulir ke HRD (Bab 18) dengan alasan info kos itu buat teman Jogja—memangnya teman Jogja Saka memakai formulir kepegawaian internal Aksara Senja?<br>2) Kenapa Pak Ramdan bicara di telepon kepada Pak Bambang seolah Saka hanya bertugas sementara 5 minggu dan pulang ke Jogja, padahal Pak Ramdan sendiri yang menawari Saka mutasi tetap sejak awal proyek dan permohonannya sudah diajukan 3 minggu lalu (Bab 31)?** | **KONTRADIKSI PENGETAHUAN & KAUSALITAS (`HIGH` / `BLOCKER`):**<br>1) Tambalan di Bab 20 baris 29 hanya menjawab soal *info kos*, tetapi tidak masuk akal untuk menepis *formulir kepegawaian antar-cabang* dan amplop *Pelepasan Pegawai* Cabang Yogyakarta.<br>2) Dialog telepon Pak Ramdan di Bab 20 baris 19–23 bertentangan langsung dengan fakta Bab 31 baris 57–59 bahwa Pak Ramdan dan Saka sudah mengurus mutasi tetap ke Jakarta sejak 3 minggu lalu. |
| **Bab 21:** Jumat pukul 17.01, Nadia memancing pertanyaan ke Saka soal rencana setelah peluncuran buku; Saka menjawab minggu depan harus ke Yogyakarta menghadap Pak Bambang membereskan surat. | Nadia ingin tahu apakah Saka akan kembali ke Jogja; Saka ingin menyelesaikan administrasi pelepasannya di Jogja lebih dulu. | SK pelepasan Pak Bambang belum ditandatangani; telepon Kepala Cabang Jogja berdering saat Saka hendak mendesak Nadia. | Saka menjawab samar (*"minggu depan saya harus balik ke Yogyakarta menghadap Pak Bambang membereskan urusan surat"*); Nadia langsung bicara baku seperti operator CS dan menolak pulang bareng. | Kesalahpahaman terkunci sepanjang akhir pekan; keduanya membisu tanpa pesan konfirmasi. | **Kenapa Saka yang keputusannya pindah ke Jakarta sudah bulat sejak 3 minggu lalu (Bab 31 baris 59) tidak mengatakan satu kalimat faktual bahwa surat yang diurus ke Pak Bambang adalah surat pelepasan mutasi tetap ke Jakarta? Dan kenapa Nadia langsung memutus percakapan dengan gaya operator CS alih-alih bertanya surat apa yang dimaksud?** | **ALASAN ABSTRAK & PENAHANAN INFORMASI SEMU (`HIGH` / `BLOCKER`):** Mengatakan fakta administratif bahwa ia sedang mengurus surat pelepasan mutasi ke Jakarta bukanlah "janji kosong". Sementara itu, keputusan Nadia menutup diri dan menolak pulang bareng murni didasarkan pada label sifat abstrak: *"penyakit nggak enakanku"*, *"rasa malu dan takut ditinggalkan"*, serta *"melindungi harga diri"* (Bab 21 baris 37–43). |
| **Bab 22–23:** Ibu kambuh vertigo Sabtu pagi dan menelepon Dimas karena mengira mereka masih pacaran; Dimas mengantar ke klinik; sorenya Dimas mengaku ke Ibu sudah minta maaf dan Ibu membujuk Nadia kembali pada Dimas. | Nadia ingin Ibunya pulih dan tidak kecewa, tetapi hatinya masih tertuju pada Saka. | Kondisi Ibu baru pulih dari vertigo; Saka tidak menghubungi Nadia sejak Jumat sore. | Nadia diam saja saat Ibu membujuknya mempertimbangkan Dimas kembali, tidak menceritakan alasan sebenarnya Dimas memutuskannya (demi Vanya & menghina sebagai CS), lalu menyetujui janji temu Dimas di lobi kantor Senin sore. | Dimas mendapat celah masuk kembali ke kehidupan Nadia dan mengklaim restu Ibu. | **Kenapa saat kondisi Ibu sudah tenang di Sabtu sore (Bab 23), Nadia tidak mengatakan secara jujur kepada Ibu bahwa Dimas memutuskannya demi staf magang baru (Vanya), melainkan membiarkan Ibu terus tertipu oleh versi sepihak Dimas?** | **ALASAN ABSTRAK (`HIGH`):** Bab 23 baris 51 hanya menyebut *"ketakutan membuat Ibu kecewa serta kekhawatiran berakhir sendirian di perantauan"*. Padahal ketika fakta yang sama diungkap Nadia 3 hari kemudian di Bab 28, Ibu langsung marah pada Dimas dan membela Nadia! |
| **Bab 24–25:** Senin sore Saka melihat ilustrasi kursi kosong di *dummy* buku dan bertanya ke Nadia, terpotong pesan Dimas; Saka menyusul ke lobi dan melihat Dimas membawa puding untuk Ibu. | Saka ingin mengonfirmasi maksud gambar kursi kosong dan kehadiran Dimas; Nadia ingin Saka menahannya dan menunjukkan rasa cemburu. | Dering WhatsApp Dimas di Bab 24; ego/gengsi Nadia dan luka lama Saka di lobi Bab 25. | Nadia sengaja mengungkit bahwa Dimas merawat ibunya dan meminta kesempatan kedua untuk memancing Saka (Bab 25 baris 23–33); Saka justru menjawab dingin bahwa kembali pada Dimas adalah *"pilihan paling masuk akal"* lalu pergi; Nadia langsung menerima ajakan makan malam peresmian balikan Dimas. | Hubungan Nadia dan Saka membeku total di Bab 26; Nadia terjadwal makan malam peresmian balikan dengan Dimas pada Selasa malam. | **Kenapa Nadia tidak menjawab pertanyaan Saka di Bab 24/25 dengan jujur bahwa ia menggambar kursi kosong karena mengira Saka pindah ke Jogja? Dan kenapa Saka tidak mengatakan bahwa keputusannya pindah ke Jakarta sudah bulat sejak 3 minggu lalu?** | **ALASAN ABSTRAK & PENGABAIAN KOMUNIKASI (`HIGH` / `BLOCKER`):** Nadia memancing kecemburuan Saka karena *"alasan bodoh... ingin melihat apakah wajah tenang itu akan goyah"* dan menerima ajakan makan malam Dimas karena *"rasa gengsi dan patah hati"* (Bab 25 baris 31 & 55). |
| **Bab 26–28:** Selasa malam makan malam keluarga bersama Ibu dan Dimas di Rawamangun; Nadia sudah hampir mengangguk menerima ajakan balikan Dimas (Bab 27 baris 17), sebelum pelayan salah mengantar es jeruk tanpa gula dan Dimas keceplosan menyuruh Nadia izin membolos dari peluncuran buku *Sela Waktu*. | Nadia awalnya pasrah ingin menyenangkan hati Ibunya; setelah Dimas meremehkan bukunya, Nadia ingin mengakhiri hubungan dengan Dimas secara permanen. | Rasa bersalah pada Ibu dan keputusasaan karena mengira Saka sudah melepaskannya. | Nadia hampir mengangguk setuju balikan (Bab 27 baris 17); namun setelah Dimas meremehkan buku *Sela Waktu* dan menyuruhnya berbohong izin urusan keluarga ke Pak Ramdan, Nadia membongkar seluruh kebenaran di depan Ibu dan menolak Dimas dengan kalimat penutup operator CS (Bab 28). | Dimas dipermalukan dan diusir secara halus oleh Ibu; Nadia melunasi seluruh biaya klinik/bensin Dimas dan bertekad meminta maaf pada Saka Rabu pagi. | **Kenapa Nadia yang sudah tumbuh berani menolak Ibu dan Mbak Raras di Bab 13 tiba-tiba nyaris menerima Dimas kembali di Bab 27 baris 17, dan hanya batal karena kebetulan pelayan salah antar es jeruk serta kecerobohan Dimas menyuruhnya membolos dari panggung peluncuran?** | **REGRESI KARAKTER & KEBETULAN ANTAGONIS (`HIGH`):** Agensi Nadia lumpuh hingga detik terakhir di Bab 27 baris 17; titik balik klimaks tidak lahir dari ketegasan aktif Nadia sejak awal makan malam, melainkan karena kebetulan es jeruk tertukar yang memicu blunder konyol Dimas. |
| **Bab 29–31:** Rabu pagi meja Saka kosong karena Saka berangkat ke Jogja Selasa petang; nomor Saka "di luar jangkauan sinyal kereta"; Nadia mengetik pesan panjang lalu menghapusnya dan takut bertanya ke Pak Ramdan; Jumat sore Saka hadir di peluncuran buku membawa SK Mutasi Tetap. | Nadia ingin meminta maaf secara langsung kepada Saka; Saka mengambil tanda tangan pelepasan Pak Bambang dan membereskan kos lama di Jogja sebelum peluncuran Jumat. | Saka berada di Yogyakarta Rabu–Kamis; rasa takut Nadia sendiri. | Nadia menghapus pesan WhatsApp yang sudah diketik dan mengurungkan niat bertanya ke Pak Ramdan (Bab 29 baris 61), sehingga menunggu hingga acara peluncuran Jumat; di Bab 31 Saka menunjukkan SK Mutasi Tetap dan memutar tutup botol dua kali saat mengelak pindah demi Nadia. | Kesalahpahaman tuntas di balkon toko buku Cikini; pada Bab 32 mereka resmi bekerja tetap semeja dan Saka ikut makan malam ke Rawamangun. | **Kenapa Nadia menghapus pesan WhatsApp klarifikasi kepada Saka dan tidak berani bertanya kepada Pak Ramdan di kantor pada Rabu pagi?** | **ALASAN ABSTRAK (`HIGH`):** Bab 29 baris 61 menyatakan Nadia menghapus pesan karena ingin bicara langsung dan tidak bertanya ke Pak Ramdan *"karena terlalu takut mendengar jawaban yang memastikan Saka sudah pergi untuk selamanya"*. Penundaan 3 hari dari Rabu ke Jumat tetap bertumpu pada keengganan bertanya. |

---

### 2.2. Uji Pertanyaan "Kenapa Tidak X?" dan Hitungan Pengabaian Komunikasi (`rules/01-plot-and-causality.md` §2 & §3)

1. **Penggunaan Label Sifat Abstrak sebagai Penggerak Plot (`rules/01-plot-and-causality.md` §2):**
   - **Bab 10 baris 17:** *"lidahku langsung kelu tidak tega merusak suasana hatinya"* (tanpa pemicu/ancaman konkret di meja makan).
   - **Bab 21 baris 37–43:** *"penyakit nggak enakanku langsung ikut berbisik"*, *"rasa malu dan takut ditinggalkan"*, *"melindungi harga diri dan agar tidak terlihat menyedihkan"*.
   - **Bab 23 baris 51:** *"ketakutan membuat Ibu kecewa serta kekhawatiran berakhir sendirian di perantauan"*.
   - **Bab 25 baris 31 & 55:** *"alasan bodoh... ingin melihat apakah wajah tenang itu akan goyah"*, *"rasa gengsi dan patah hati"*.
   - **Bab 29 baris 61:** *"terlalu takut mendengar jawaban yang memastikan Saka sudah pergi untuk selamanya"*.

2. **Hitungan Konflik yang Bergantung pada Pengabaian Komunikasi Satu Kalimat (`rules/01-plot-and-causality.md` §3):**
   - Sama seperti versi sebelumnya, konflik utama paruh kedua masih bergantung pada **7 kali pengabaian komunikasi satu kalimat**:
     1. **Bab 10 baris 15–17:** Nadia tidak memberi tahu Ibu bahwa ia sudah putus dari Dimas.
     2. **Bab 14 baris 19–21:** Saka berbohong soal tab kos tahunan Cikini & formulir kepegawaian antar-cabang.
     3. **Bab 20 baris 29–38:** Nadia tidak mengonfirmasi maksud amplop *"Pelepasan Pegawai"* dan menepis petunjuk *formulir kepegawaian antar-cabang* dengan alasan tidak logis (menganggapnya milik teman Jogja Saka).
     4. **Bab 21 baris 29–53:** Saka tidak menyebut bahwa surat yang diurus ke Pak Bambang adalah pelepasan mutasi tetap ke Jakarta, dan Nadia langsung memutus obrolan dengan gaya operator CS.
     5. **Bab 23 baris 37–50:** Nadia tidak memberi tahu Ibu alasan sebenarnya Dimas memutuskannya saat Ibu membujuknya balikan pada Sabtu sore.
     6. **Bab 24 baris 39–60 & Bab 25 baris 15–58:** Nadia tidak menjawab jujur pertanyaan Saka soal gambar kursi kosong di meja maupun di lobi, dan Saka tidak menyebut proses mutasinya.
     7. **Bab 29 baris 61:** Nadia menghapus pesan WhatsApp yang sudah diketik untuk Saka dan sengaja tidak bertanya kepada Pak Ramdan.
   - **Kesimpulan Kausalitas:** Dengan **7 titik pengabaian komunikasi** tanpa hambatan eksternal yang memadai, Tabel Rantai Sebab-Akibat masih memiliki temuan **`HIGH` / `BLOCKER`**.

---

## 3. Evaluasi Lengkap Daftar Rujukan Mundur dan Waktu Relatif (`--refs` / `rules/06-setup-payoff.md`)

Berikut adalah hasil eksekusi `python3 scripts/audit_core.py --root /tmp/uji-post --refs` beserta penilaian editorial lengkap terhadap keberadaan setup, kesamaan detail, dan ketepatan waktu relatif untuk **seluruh item** dari Bab 1 hingga Bab 32:

### Bab 1
- **Baris 7 (`dulu`):** `Kalau gue customer service, telepon lo udah gue matiin dari dulu, Dimas!"` -> **LULUS.**
- **Baris 17 (`waktu itu`):** `"Aku capek, Nad," katanya waktu itu sambil memegang tali helm.` -> **LULUS** (mengacu pada Jumat malam lalu di baris 15).

### Bab 2
- **Baris 33 (`kemarin lusa`):** `"Saya baru pindah ke Jakarta kemarin lusa.` -> **LULUS** (Sabtu sebelum Senin Bab 1–2).

### Bab 3
- **Baris 17 (`Tadi pagi`):** `Tadi pagi jam tujuh lewat lima belas sudah saya kirim ke email Mbak Dinda," jawabku sopan...` -> **LULUS.**
- **Baris 21 (`Kemarin`):** `Kemarin gue dengar sendiri di pantry."` -> **LULUS** (Senin kemarin).
- **Baris 53 (`tadi malam`):** `Duduk semeja dengan pria yang tadi malam mendengarkan seluruh aib makianku di tangga darurat?!` -> **LULUS** (Senin malam Bab 1–2).

### Bab 4
- **Baris 39 (`dulu`):** `Namun sebelum benda itu menyentuh mejaku, Saka sudah lebih dulu berdiri tegak di samping kursinya.` -> **LULUS.**

### Bab 5
- **Baris 3 (`kemarin`):** `...melempar lirikan masam karena urusan flash disk kemarin sore...` -> **LULUS** (Rabu Bab 5 merujuk Selasa sore Bab 4).
- **Baris 13 (`dulu`):** `"Talangin punya gue dulu dong?` -> **LULUS.**
- **Baris 17 (`Bulan lalu`):** `Bulan lalu saja Riko sudah tiga kali memakai alasan dompet tertinggal.` -> **LULUS** (konsisten dengan utang Rp90.000 di Bab 32).

### Bab 6
- **Baris 7 (`Kemarin`):** `Kemarin waktu staf administrasi meminta bantuan memotong dua ratus lembar kupon diskon secara manual...` -> **LULUS** (Jumat Bab 6 merujuk Kamis).
- **Baris 15 (`Waktu itu`):** `"Buku Sela Waktu itu kan tentang orang kota..."` -> **LULUS** (*false positive* judul buku).
- **Baris 35 (`dulu`):** `"...intonasi memohon yang dulu selalu berhasil meluluhkan hatiku."` -> **LULUS.**
- **Baris 45 (`minggu lalu`):** `"...sifat sungkanku yang minggu lalu dia jadikan alasan untuk mengakhiri hubungan kami!"` -> **LULUS** (Jumat malam minggu sebelumnya).
- **Baris 55 (`kemarin`):** `Berbeda dengan kejadian kemarin saat menghadapi Mbak Dinda, kali ini Saka tidak memotong pembicaraan.`
  - **Penilaian:** **TEMUAN (`ERROR` — `SETUP_PAYOFF` / `TIMELINE`).** Belum diperbaiki di versi `post-fix`! Bab 6 berlangsung pada **Jumat sore**, sedangkan adegan Saka memotong pembicaraan Mbak Dinda terjadi di **Bab 4** pada **Selasa sore** (3 hari sebelumnya, bukan "kemarin" / Kamis).

### Bab 7
- **Baris 11 (`minggu lalu`):** `Ingatan Jumat malam minggu lalu mendadak melintas di kepalaku...` -> **LULUS.**
- **Baris 29 (`kemarin`):** `"Loh, kan cuma tinggal tarik ukuran dari file poster yang kemarin, Nad," desak Dimas kesal.` -> **LULUS (Kolokial)**, dan baris 31 kini sudah diperbaiki menjadi *"dari Selasa pagi"* (cocok dengan Bab 3 baris 5).
- **Baris 61 (`Tadi pagi`):** `"Tadi pagi kasir minimarket depan stasiun ngasih promo beli kopi botol," jawab Saka santai.` -> **LULUS** (alasan bohong Saka dengan *tell* dua kali *klik*).

### Bab 8
- **Baris 25 (`Dulu`), Baris 31 (`dulu`), Baris 37 (`dulu`), Baris 43 (`Waktu itu`):** -> **LULUS.**
- **Baris 35 (`pernah bilang`):** `"Dimas pernah bilang gaya kayak gini kusam dan kurang komersial."`
  - **Penilaian:** **LULUS.** Telah diperbaiki dari *"Kemarin Dimas bilang"* menjadi *"Dimas pernah bilang"* (mengacu pada masa pacaran 2 tahun mereka sebagaimana dijelaskan pada baris 47).

### Bab 9
- **Baris 11 & 13 (Rujukan implisit `Waktu makan ayam bakar` & `Waktu makan bakso di kantin`):** Rujukan ayam bakar cocok dengan Bab 5; makan bakso di kantin merupakan kejadian rutin di luar layar pada minggu pertama.
- **Baris 39 (`dulu`):** `...mata Saka sudah lebih dulu tertuju ke halaman belakang...` -> **LULUS.**

### Bab 10
- **Baris 17 (`minggu lalu`):** `...sudah tamat sejak Jumat minggu lalu.` -> **LULUS.**
- **Baris 27 (`kemarin`):** `"Iya, makanya Mbak udah pesan tiket pesawat dari kemarin,"` -> **LULUS** (dan kini sudah konsisten dengan Bab 13 baris 57 yang tetap ke Bali).
- **Baris 31, 45, 53 (`dulu`):** -> **LULUS.**

### Bab 11
- **Baris 31 (`dulu`):** `"Teduh di situ dulu,"` -> **LULUS.**
- **Baris 49 (`kemarin`) & Baris 51 (`Kemarin`):** Mengacu dari Senin sore (Bab 11) ke Minggu siang/sore di Rawamangun (Bab 10). -> **LULUS.**

### Bab 12
- **Baris 13 (`Dulu`), Baris 21 (`Dulu`), Baris 33 (`Dulu`):** Mengacu pada masa lalu Saka di Yogyakarta (kini sudah mencakup kalimat tentang mantan kekasihnya yang memilih pria pilihan orang tua pada baris 27). -> **LULUS.**

### Bab 13
- **Baris 25 (`Kemarin`, `dulu`):** `"Kemarin siang kan kamu bilangnya mau cek saldo dulu.` -> **LULUS** (Senin malam merujuk Minggu siang Bab 10).
- **Baris 67 (`ceritanya`):** `Makasih banyak ya, Mas, buat ceritanya sama tahu isinya tadi sore.` -> **LULUS** (merujuk Bab 11–12).

### Bab 14
- **Baris 5 (`dulu`), Baris 15 (`waktu itu`), Baris 27 (`kemarin`), Baris 29 (`dulu`), Baris 41 (`Dulu`), Baris 45 (`Dulu`):** -> **LULUS.**
- **Baris 7 (`kemarin`):** `Di grup WhatsApp keluarga pun, Mbak Raras masih mendiamkanku sejak malam itu, meski kemarin siang Ibu akhirnya sudah mau mengirim pesan suara menanyakan apakah papan gambar baruku sudah dipakai kerja.`
  - **Penilaian:** **TEMUAN KRONOLOGI (`HIGH` — `TIMELINE`).** Belum diperbaiki di versi `post-fix`! Bab 14 dibuka dengan *"Dua minggu duduk satu meja dengan Saka Wijaya"* pada hari **Kamis siang**, namun pada hari **Senin pagi berikutnya** (Bab 18 baris 3 & 17, empat hari setelah Kamis Bab 14–17) tiba-tiba sudah disebut *"Memasuki minggu keempat kami duduk semeja"*. Jika Bab 14 adalah Kamis akhir Minggu ke-3 (10 hari setelah telepon Senin malam Bab 13), maka Ibu mendiamkan Nadia selama 9 hari penuh sebelum bertanya pada hari Rabu ("kemarin siang"). Sebaliknya, jika Bab 14 adalah Kamis Minggu ke-2, maka Senin berikutnya (Bab 18) baru memasuki Minggu ke-3, bukan Minggu ke-4!

### Bab 15
- **Baris 21 (`Dulu`), Baris 23 (`dulu`), Baris 61 (`dulu`):** -> **LULUS.**

### Bab 16
- **Baris 47 (`Dulu`):** -> **LULUS.**

### Bab 17
- **Baris 25 (`katanya`):** -> **LULUS.**

### Bab 18
- **Baris 11 & 29 (`Kamis sore`):** Telah diperbaiki dari *"Kemarin"* menjadi *"Kamis sore"* (merujuk Bab 16–17). -> **LULUS.**
- **Baris 17 (`dulu`) & Baris 19 (`dulu`):** Mengacu pada hari pertama kerja semeja, namun klaim *"Memasuki minggu keempat"* di baris 17 masih melompati 1 minggu kalender dari Bab 14 baris 3 (*"Dua minggu duduk satu meja"*).
- **Baris 39 (`Kemarin`):** `"Kemarin hari Jumat waktu antar berkas personalia, gue lihat Mas Saka nyerahin map formulir ke Mbak Sinta HRD."`
  - **Penilaian:** **TEMUAN (`REVIEW` / `FIX BEFORE RELEASE` — `GRAMMAR` / `TIMELINE`).** Konstruksi *"Kemarin hari Jumat"* yang diucapkan pada hari **Senin siang** tidak tepat secara bahasa Indonesia (pada hari Senin, "kemarin" adalah hari Minggu; seharusnya ditulis *"Hari Jumat kemarin"* atau *"Jumat lalu"*).
- **Baris 43 (`waktu itu`) & Baris 51 (`ceritanya`):** -> **LULUS.**

### Bab 19
- **Baris 5 (`kemarin`):** `Sejak kemarin, suasana di divisi pemasaran agak tegang.` -> **LULUS** (dan baris 39 kini sudah diperbaiki menjadi *"Beberapa hari ini setelah Vanya pergi"*).
- **Baris 13 (`dulu`), Baris 17 (`dulu`), Baris 65 (`tadi pagi`):** -> **LULUS.**

### Bab 20
- **Baris 5 (`dulu`):** -> **LULUS.**
- **Baris 29 (`waktu itu` & `Senin lalu`):** `Aku sempat teringat tab kos tahunan Cikini dan formulir kepegawaian antar-cabang di layar laptopnya waktu itu. ... Kalimat Tari Senin lalu soal formulir di meja Mbak Sinta HRD itu...`
  - **Penilaian:** Secara waktu relatif (`waktu itu` mengacu Bab 14 dan `Senin lalu` mengacu Bab 18) **LULUS**, tetapi secara logika pengetahuan tokoh (`CHARACTER_KNOWLEDGE`) gagal karena alasan Nadia menepis petunjuk tersebut (*"info kos tersebut cuma buat temannya dari Jogja"*) tidak menjelaskan mengapa Saka membuka **formulir kepegawaian antar-cabang** dan menyerahkan map formulir ke HRD.

### Bab 21
- **Baris 25 (`ceritanya`, `dulu`):** `Aku teringat ceritanya di kedai kopi dulu...` -> **LULUS** (telah diperbaiki dari *"warung soto"* menjadi *"kedai kopi"*).

### Bab 22
- **Baris 5 (`kemarin`), Baris 21 (`tadi pagi`), Baris 33 (`Tadi pagi`), Baris 45 (`Dulu`), Baris 57 (`tadi pagi`), Baris 59 (`kemarin`):** -> **LULUS.**

### Bab 23
- **Baris 9 (`dulu`) & Baris 17 (`waktu itu`):** -> **LULUS.**
- **Baris 41 (`dua minggu lalu`):** `Tak ada ketegangan kaku seperti saat kami memperdebatkan permintaan Mbak Raras dua minggu lalu.` -> **LULUS** (telah diperbaiki dari *"minggu lalu"*).

### Bab 24
- **Baris 45 (`Sejak Jumat`):** Telah diperbaiki dari *"Sejak kemarin"* menjadi *"Sejak Jumat"*. -> **LULUS.**

### Bab 25
- **Baris 35 (`dulu`):** `Namun aku lupa cerita Saka di kedai kopi dulu.` -> **LULUS** (telah diperbaiki dari *"warung soto"* menjadi *"kedai kopi"* dan detailnya telah ditanam di Bab 12 baris 27).

### Bab 26
- **Baris 19 (`katanya`), Baris 37 (`kemarin`), Baris 39 (`kemarin`), Baris 43 (`dulu`):** -> **LULUS.**
- **Baris 29 (`kemarin`):** `"Waktu Ibu sakit kemarin, dia yang ngurusin semuanya, Tar," belaku pelan.`
  - **Penilaian:** **TEMUAN (`REVIEW` / `FIX BEFORE RELEASE` — `TIMELINE`).** Belum diperbaiki di `post-fix`! Bab 26 berlangsung pada **Selasa siang**, sedangkan Ibu sakit dan diantar ke klinik terjadi pada **Sabtu pagi/siang** (Bab 22, tiga hari sebelumnya, bukan "kemarin").
- **Baris 53 (`empat minggu lalu`):** `Kertas post-it kuning bertuliskan Bilang enggak itu nggak bikin langit runtuh yang ditempelkan Saka empat minggu lalu...` -> **LULUS** untuk jarak Selasa Minggu 1 ke Selasa Minggu 5 (namun tetap meninggalkan celah lompatan 1 minggu antara Bab 14 dan Bab 18).

### Bab 27
- **Baris 13 (`dulu`) & Baris 47 (`dulu`):** -> **LULUS.**

### Bab 28
- **Baris 17 (`dulu`), Baris 23 (`waktu itu`), Baris 41 (`dulu`):** -> **LULUS.**
- **Baris 57 (`kemarin`):** `"Semua biaya klinik, bubur, dan bensin kemarin biar ditransfer balik sama Nadia malam ini," lanjut Ibu tegas.`
  - **Penilaian:** **TEMUAN (`REVIEW` / `FIX BEFORE RELEASE` — `TIMELINE`).** Belum diperbaiki di `post-fix`! Bab 28 berlangsung pada **Selasa malam**, sedangkan kejadian ke klinik terjadi pada **Sabtu siang** (Bab 22, tiga hari sebelumnya).

### Bab 29
- **Baris 5 (`Tadi pagi`), Baris 7 (`kemarin`), Baris 23 (`kemarin`), Baris 27 (`kemarin`), Baris 29 (`kemarin`), Baris 33 (`Katanya`), Baris 39 (`Kemarin`), Baris 63 (`Tadi malam`), Baris 65 (`dulu`):** -> **LULUS** (mengacu dari Rabu pagi ke Selasa sore/malam, dengan catatan kecil baris 7 menyatukan lobi Senin sore dan goyah Selasa ke dalam kata *"kemarin"*).

### Bab 30
- **Baris 9 (`dulu`), Baris 21 (`kemarin`), Baris 27 (`Dulu`):** -> **LULUS.**

### Bab 31
- **Baris 21 (`kemarin`):** `"Maaf buat sikapku kemarin, dan maaf buat omonganku di lobi."`
  - **Penilaian:** **TEMUAN (`REVIEW` / `FIX BEFORE RELEASE` — `TIMELINE`).** Belum diperbaiki di `post-fix`! Bab 31 adalah **Jumat sore**, sedangkan sikap dingin Nadia dan pertengkaran di lobi terjadi pada **Senin–Selasa** (Bab 24–26), bukan hari Kamis ("kemarin").
- **Baris 41 (`Waktu itu`), Baris 47 (`minggu lalu`), Baris 51 (`tiga minggu yang lalu`, `kemarin`), Baris 53 (`dulu`), Baris 59 (`tiga minggu lalu`), Baris 63 (`kemarin`), Baris 71 (`Katanya`):** -> **LULUS** secara kesesuaian rujukan (baris 71 telah diperbaiki menjadi *"Katanya kos tahunan itu buat teman Jogja"* mengacu Bab 14 baris 21).
- **Baris 75 (Rujukan lokasi implisit `soto ayam tanpa seledri di warung depan gedung kantor`):**
  - **Penilaian:** **TEMUAN (`ERROR` — `LOCATION_CONTINUITY` / `SETUP_PAYOFF`).** Belum diperbaiki di `post-fix`! Adegan makan soto ayam tanpa seledri di Bab 9 terjadi di **Warung Soto Kwitang dekat Halte Senen**, **bukan** di warung depan gedung kantor Cikini!

### Bab 32
- **Baris 59 (`waktu itu`):** `"Ibu malah nanyain kapan editor Jogja yang di panggung waktu itu mau mampir ke rumah."` -> **LULUS.**

---

## 4. Verifikasi Prosedur Dunia Nyata dengan Pencarian Web (`rules/18-real-world-procedures.md` & `rules/04-worldbuilding.md`)

Seluruh prosedur dunia nyata di naskah `post-fix` telah diverifikasi menggunakan pencarian web terhadap standar industri dan operasional di Indonesia:

| No. | Prosedur Dunia Nyata di Naskah | Klaim Urutan & Durasi di Naskah (`post-fix`) | Standar Industri / Operasional Nyata & Sumber Verifikasi | Status Verifikasi & Klasifikasi |
|---|---|---|---|---|
| 1 | **Penerbitan, Percetakan Buku (Digital vs Offset), dan Distribusi Toko Buku** (Bab 15, 21, 24, 26, 30, 32) | 1. **Jumat pukul 17.01 (Bab 21 baris 9):** File akhir dikirim; *"Edisi peluncurannya dicetak digital dalam jumlah terbatas supaya keburu, cetak offset menyusul."*<br>2. **Senin pukul 16.00 (Bab 24 baris 3):** 2 eksemplar *dummy* tiba.<br>3. **Selasa pukul 10.00–11.00 (Bab 26 baris 7–9):** Persetujuan naik cetak terbatas edisi peluncuran ditandatangani & diambil kurir.<br>4. **Jumat pagi (Bab 30 baris 5):** Buku edisi pertama cetak terbatas tiba dari percetakan untuk acara peluncuran.<br>5. **Senin sore, 3 hari pasca-peluncuran (Bab 32 baris 3):** *"Tiga hari setelah acara peluncuran buku Sela Waktu yang kini sudah terpajang rapi di rak depan toko-toko buku kawasan Cikini dan Matraman dengan sambutan hangat dari para pembaca..."* | - **Cetak Digital Terbatas (*POD*) untuk Peluncuran (Selasa siang -> Jumat pagi = 2,5 hari kerja):** Masuk akal untuk pencetakan digital terbatas 50–100 eksemplar.<br>- **Cetak Offset Massal + Distribusi ke Jaringan Toko Buku Kawasan Cikini & Matraman:** Di Bab 21 baris 9 & Bab 26 baris 7 dinyatakan bahwa yang disetujui Selasa siang baru *cetak digital terbatas edisi peluncuran* sedangkan *cetak offset menyusul*. Dalam industri penerbitan Indonesia, proses pra-cetak pelat CTP (1–2 hari kerja), cetak offset massal & penjilidan/QC (2–5 hari kerja), pengiriman ke Gudang Distribusi Pusat / DC (1–2 hari kerja), serta alokasi PPIC dan pemajangan di etalase cabang toko buku mayor (seperti Gramedia Matraman) membutuhkan total **1 hingga 3 minggu (minimal 8–15 hari kerja)**.<br>- Mustahil hanya dalam **3 hari akhir pekan (Jumat sore ke Senin sore)** buku yang cetak offset-nya baru "menyusul" sudah selesai dicetak massal, melewati gudang distribusi, dan *"terpajang rapi di rak depan toko-toko buku kawasan Cikini dan Matraman"*.<br>- **Sumber Verifikasi Web:**<br>  1. Standar Waktu Produksi Cetak Buku Offset, CTP, & *Digital Printing* — Percetakan Diandra Creative (`percetakandiandra.co.id` / `diandracreative.com`), Penerbit Deepublish (`penerbitdeepublish.com`), Meridian Grup (`meridiangrup.com`), & Noken Studio (`nokenstudio.com`).<br>  2. Alur Logistik Gudang Pusat (DC) dan PPIC Distribusi Toko Buku Mayor Indonesia — Studi Rantai Pasok Penerbit Mayor / Gramedia (`umn.ac.id`). | **TERVERIFIKASI LULUS** untuk cetak digital terbatas edisi peluncuran (Bab 21–30).<br>**TEMUAN (`DOMAIN_FACTUALITY` / `TIMELINE` — `HIGH` / `FIX BEFORE RELEASE`)** pada **Bab 32 baris 3** (distribusi ke rak depan toko-toko buku Cikini & Matraman pada hari Senin, 3 hari setelah peluncuran, masih mustahil secara operasional). |
| 2 | **Transportasi Kereta Api Antarkota Jakarta–Yogyakarta & Pesan Operator Seluler** (Bab 29, 30, 31) | 1. **Selasa petang pukul 17.30 / malam (Bab 29 baris 31 & 39):** Saka berangkat ke Yogyakarta naik kereta malam.<br>2. **Rabu pagi pukul 08.15–08.30 (Bab 29 baris 3 & 59):** Saat Nadia menelepon Saka, *"suara operator hanya menjawab bahwa nomor yang kutuju sedang berada di luar jangkauan sinyal kereta."*<br>3. **Bab 31 baris 63:** Saka berkata *"Pesan Tari di kereta nggak mengubah keputusan itu..."* (mengonfirmasi ia masih di kereta pada Rabu pagi saat Tari mengirim pesan).<br>4. **Jumat pagi–sore (Bab 30 baris 9):** Saka naik kereta pagi dari Yogyakarta ke Stasiun Gambir, tertahan sinyal 20 menit sebelum Jatinegara, perjalanan Gambir–Cikini ~10 menit, tiba di Cikini sebelum pukul 17.30. | - **Waktu Tempuh KA Jakarta (Gambir/Pasar Senen) – Yogyakarta (Tugu/Lempuyangan):** Berkisar antara **6 jam hingga 7 jam 30 menit** (KA Taksaka ~6 jam 10 menit; KA malam yang berangkat dari Jakarta pukul 19.00–21.30 tiba di Yogyakarta pukul **01.15–04.30 dini hari**).<br>- Kereta malam yang berangkat Selasa malam sudah tiba di Yogyakarta sebelum pukul 05.00 Rabu pagi; **mustahil pada pukul 08.30 Rabu pagi Saka masih berada di dalam kereta menuju Yogyakarta**.<br>- Selain itu, operator telekomunikasi seluler di Indonesia tidak memiliki pesan suara otomatis yang berbunyi *"sedang berada di luar jangkauan sinyal kereta"*.<br>- **Sumber Verifikasi Web:**<br>  1. Jadwal dan Waktu Tempuh Resmi KA Gambir–Yogyakarta — PT Kereta Api Indonesia / Tiket KAI (`tiketkai.com`, `traveloka.com`, `detik.com`). | **TEMUAN (`DOMAIN_FACTUALITY` / `TIMELINE` — `ERROR` / `FIX BEFORE RELEASE`)** pada **Bab 29 baris 31 & 59** serta **Bab 31 baris 63** (belum diperbaiki di versi `post-fix`).<br>**TERVERIFIKASI LULUS** untuk kereta pagi Jumat di Bab 30. |
| 3 | **Geografi Jakarta & Operasional KRL Commuter Line Jabodetabek** (Bab 2, 10, 16, 17) | 1. **Bab 2 baris 33:** Saka berkata *"Kosan saya di Tebet."*<br>2. **Bab 16 baris 23:** Nadia berkata *"Kos Mas Saka kan arahnya naik kereta ke selatan."*<br>3. **Bab 17 baris 19:** Saka beralasan *"Tadi niatnya beli martabak telur buat makan di kereta."*<br>4. **Bab 10 baris 55:** Perjalanan KRL dari Stasiun Jatinegara menuju Stasiun Cikini. | - **Rute KRL Cikini – Tebet:** Dilayani langsung oleh KRL Lin Bogor ke arah selatan (Cikini -> Manggarai -> Tebet, ~8–10 menit). Lokasi kos di Tebet sudah konsisten.<br>- **Aturan KRL Commuter Line:** PT KAI Commuter melarang penumpang makan dan minum di dalam gerbong KRL (namun karena kalimat Saka di Bab 17 baris 19 adalah alasan bohong spontan yang langsung dibongkar Nadia, hal ini hanya menjadi kejanggalan kecil dalam alasan bohong Saka).<br>- **Rute KRL Jatinegara – Cikini:** Lin Cikarang ke Manggarai (~5 menit) lalu transit Lin Bogor ke Cikini (1 stasiun).<br>- **Sumber Verifikasi Web:**<br>  1. Peta Rute dan Aturan KRL Commuter Line Jabodetabek — KAI Commuter (`keretaapikita.com`, `kabarpenumpang.com`). | **TERVERIFIKASI LULUS** (dengan catatan minor pada alasan bohong makan di KRL di Bab 17 baris 19). |
| 4 | **Prosedur Medis Penanganan Vertigo Akut di Klinik Pratama** (Bab 22) | Ibu mengalami vertigo akut sejak subuh, dibawa ke Klinik Pratama Rawamangun pukul 09.30 dengan kursi roda, observasi di ruang redup, injeksi obat pereda pusing/mual, penebusan obat di apotek (total ~3 jam sampai pukul 13.00), lalu istirahat di rumah dan membaik pukul 17.00. | - Sesuai **Panduan Praktik Klinis (PPK) Layanan Primer IDI** dan panduan **PERDOSSI**, penanganan vertigo perifer akut di FKTP/Klinik Pratama meliputi triase tanda bahaya, injeksi simtomatik (dimenhidrinat/metoklopramid), observasi di ruang tenang/redup selama 1–3 jam, serta obat pulang oral (betahistin).<br>- **Sumber Verifikasi Web:**<br>  1. Panduan Praktik Klinis (PPK) Layanan Primer IDI & PERDOSSI — Tatalaksana Vertigo Akut (`alomedika.com`, `rspon.go.id`, `usu.ac.id`). | **TERVERIFIKASI LULUS** |
| 5 | **Administrasi Kepegawaian / HRD Mutasi Tetap Antar-Cabang** (Bab 3, 14, 18, 20, 31) | Di Bab 3 baris 35 dan Bab 31 baris 51 Yogyakarta disebut *"Cabang Yogyakarta"*, tetapi di Bab 20 baris 29 disebut *"kantor pusatnya di Yogyakarta"*, di Bab 20 baris 37 tertulis *"logo Kantor Pusat Penerbit Aksara Senja Cabang Yogyakarta"*, dan di Bab 31 baris 47 tertulis *"berlogo Kantor Pusat Yogyakarta"*. | - Secara tata kelola organisasi dan administrasi surat-menyurat perusahaan, satu unit kerja tidak dapat berstatus **Kantor Pusat** sekaligus **Cabang** secara bersamaan pada kop surat yang sama (*"Kantor Pusat Penerbit Aksara Senja Cabang Yogyakarta"*). | **TEMUAN (`NAME_TERM_CONSISTENCY` / `DOMAIN_FACTUALITY` — `ERROR` / `FIX BEFORE RELEASE`)** pada Bab 20 baris 29 & 37 serta Bab 31 baris 47 (belum diperbaiki di versi `post-fix`). |

---

## 5. Daftar Lengkap Temuan Editorial pada Versi `post-fix` Beserta Severity dan Saran Perbaikan Spesifik

### Ringkasan Jumlah Temuan Terbuka pada Versi `post-fix`
- **ERROR:** 6 temuan
- **HIGH:** 4 temuan
- **REVIEW:** 3 temuan
- **INFO:** 1 temuan

---

### A. Temuan `HIGH` yang Berdampak `BLOCKER`

#### [F-01] `HIGH` | `CAUSALITY` / `MOTIVATION` | Release Impact: `BLOCKER` | Confidence: `HIGH`
- **Lokasi:** Lintas bab paruh kedua (`chapters/bab-10.md` baris 17; `chapters/bab-21.md` baris 29–53; `chapters/bab-23.md` baris 37–55; `chapters/bab-25.md` baris 15–58; `chapters/bab-27.md` baris 17; `chapters/bab-29.md` baris 61)
- **Bukti Kutipan:**
  - `bab-10.md:17`: *"...lidahku langsung kelu tidak tega merusak suasana hatinya."*
  - `bab-21.md:37`: *"Apalagi penyakit nggak enakanku langsung ikut berbisik di kepalaku: memangnya aku ini siapanya Saka sampai berhak menuntut penjelasan atau menahannya tetap tinggal di Jakarta?"*
  - `bab-25.md:31-33`: *"Di dalam lubuk hatiku yang paling dalam, sebenarnya ada alasan bodoh kenapa aku mengucapkan kalimat itu di depan wajahnya. Aku ingin melihat apakah wajah tenang itu akan goyah. Aku ingin mendengar dia melarangku."*
  - `bab-27.md:17`: *"Aku sudah menundukkan dagu sedikit, bersiap menganggukkan kepalaku untuk menjawab iya."*
  - `bab-29.md:61`: *"Jemariku sempat beralih membuka ruang obrolan dan mengetik pesan permintaan maaf yang panjang lebar untuknya. Namun sebelum menekan tombol kirim, kuhapus kembali seluruh teks itu huruf demi huruf. ... Aku pun mengurungkan niat bertanya ke ruangan Pak Ramdan karena terlalu takut mendengar jawaban yang memastikan Saka sudah pergi untuk selamanya."*
- **Masalah Spesifik:**
  1. Sesuai `rules/01-plot-and-causality.md` §2 & §3, konflik utama paruh kedua (Bab 19–29) masih bertumpu pada **7 kali pengabaian komunikasi satu kalimat** yang hanya didorong oleh label sifat abstrak (*"tidak tega merusak suasana"*, *"penyakit nggak enakanku"*, *"rasa malu"*, *"gengsi"*, *"terlalu takut mendengar jawaban"*) tanpa hambatan situasional konkret.
  2. Tambalan di Bab 29 baris 61 (mengetik pesan lalu menghapusnya dan takut bertanya ke Pak Ramdan) justru memperlihatkan secara telanjang bahwa penulis sengaja menahan komunikasi agar kesalahpahaman bertahan sampai hari Jumat (Bab 30–31).
  3. Regresi karakter Nadia di Bab 25–27 masih belum diperbaiki: setelah berani menolak permintaan uang Rp4 juta dari Mbak Raras dan Ibunya di Bab 13, Nadia justru pasrah menghadiri makan malam peresmian balikan dan **sudah bersiap mengangguk menjawab iya** kepada Dimas di Bab 27 baris 17, lalu hanya tersadar karena kebetulan pelayan salah mengantar es jeruk yang memicu Dimas menyuruhnya membolos dari panggung peluncuran buku.
- **Dampak bagi Pembaca:** Konflik paruh kedua terasa dipaksakan dan merusak perkembangan karakter Nadia yang sudah dibangun dengan kuat di paruh pertama.
- **Keputusan Editorial (`MANUSCRIPT ERROR` & `OUTLINE ERROR`):**
  - **Saran Perbaikan Minimal:**
    1. Berikan hambatan situasional nyata saat Nadia hendak memberi tahu Ibu soal putus dengan Dimas di Bab 10 (misalnya Ibu mengeluh pusing/tensi naik di meja makan) dan di Bab 23 (misalnya Ibu masih lemah pasca-serangan vertigo dan dokter melarang beban pikiran berat).
    2. Buat status mutasi Saka di Bab 20–25 memang belum pasti secara eksternal (misalnya Kepala Cabang Yogyakarta menahan pelepasan Saka karena belum ada pengganti di Jogja, sehingga Saka harus berangkat ke Jogja untuk bernegosiasi langsung dengan Pak Bambang), bukan karena Saka sudah bulat dan tinggal menyembunyikan informasi dari Nadia.
    3. Di Bab 27 baris 17, hapus kalimat bahwa Nadia sudah bersiap mengangguk menjawab iya; buat Nadia datang ke makan malam itu dengan niat menolak secara baik-baik setelah kondisi Ibu pulih, lalu sikap meremehkan Dimas soal panggung peluncuran buku mengubah penolakan halus Nadia menjadi pembongkaran kebenaran secara tegas di depan Ibu.

---

#### [F-02] `HIGH` | `CHARACTER_KNOWLEDGE` / `CAUSALITY` | Release Impact: `BLOCKER` | Confidence: `HIGH`
- **Lokasi:** `chapters/bab-14.md` baris 17–21, `chapters/bab-18.md` baris 39–43, `chapters/bab-20.md` baris 19–29 & 37, dan `chapters/bab-31.md` baris 57–59
- **Bukti Kutipan:**
  - `bab-14.md:17-18`: *"...mataku tidak sengaja menangkap tab di sudut atas layarnya yang bertuliskan daftar sewa kamar kos tahunan daerah Cikini dan formulir kepegawaian antar-cabang."*
  - `bab-20.md:19-23`: *"Soal Saka, masa perbantuannya di Jakarta memang lima minggu sampai proyek beres," lanjut Pak Ramdan. "Berarti akhir minggu depan masa tugas sementaranya sudah habis. Nanti biar Saka sendiri yang pulang ke Yogyakarta minta tanda tangan Pak Bambang."*
  - `bab-20.md:29`: *"Aku sempat teringat tab kos tahunan Cikini dan formulir kepegawaian antar-cabang di layar laptopnya waktu itu. Namun ingatan itu langsung kutepis karena Saka sendiri sudah bilang bahwa info kos tersebut cuma buat temannya dari Jogja."*
  - `bab-31.md:57-59`: *"Pak Ramdan nawarin posisi tetap pegang lini buku ilustrasi baru sejak awal proyek," jelas Saka tenang seraya tersenyum tipis. "Keputusan saya pindah sudah bulat sejak pengajuan itu," kata Saka menunjuk tanggal tiga minggu lalu di suratnya.*
- **Masalah Spesifik:**
  1. **Alasan Menepis Petunjuk Tidak Logis (`rules/05-character-knowledge.md`):** Tambalan di Bab 20 baris 29 mencoba menjelaskan mengapa Nadia menepis petunjuk Bab 14, tetapi alasan *"karena Saka sendiri sudah bilang bahwa info kos tersebut cuma buat temannya dari Jogja"* **sama sekali tidak menjelaskan** mengapa di tab laptop Saka yang sama juga terbuka **"formulir kepegawaian antar-cabang"** dan mengapa Saka menyerahkan map formulir ke Mbak Sinta HRD (Bab 18 baris 39)! Teman Saka dari luar kantor tidak mungkin memakai formulir kepegawaian internal antar-cabang Penerbit Aksara Senja yang diserahkan Saka ke HRD. Selain itu, perihal surat pada amplop di Bab 20 baris 37 adalah *"Verifikasi Masa Tugas dan Pelepasan Pegawai"* dari Cabang Yogyakarta—secara bahasa administrasi, jika Cabang Yogyakarta melakukan *pelepasan pegawai*, berarti pegawai tersebut dilepas dari Yogyakarta ke Jakarta, bukan dipulangkan ke Yogyakarta.
  2. **Kontradiksi Telepon Pak Ramdan (Bab 20 vs Bab 31):** Jika Pak Ramdan sendiri yang menawari Saka posisi tetap di Jakarta sejak awal proyek dan keputusan pindah Saka sudah bulat diajukan sejak 3 minggu lalu (Bab 31 baris 57–59), tidak masuk akal Pak Ramdan berbicara di telepon kepada Pak Bambang pada akhir minggu ke-4 (Bab 20 baris 19–23) seolah-olah masa tugas Saka di Jakarta habis minggu depan dan Saka hanya pulang ke Yogyakarta tanpa menyebut mutasi tetap.
- **Dampak bagi Pembaca:** Pembaca tetap melihat bahwa kesalahpahaman di Bab 20 dipaksakan oleh dialog telepon Pak Ramdan yang tidak jujur dan kesimpulan Nadia yang mengabaikan arti "formulir kepegawaian antar-cabang".
- **Keputusan Editorial (`MANUSCRIPT ERROR`):**
  - **Saran Perbaikan Minimal:**
    - Di `chapters/bab-20.md` baris 29: Tambahkan alasan logis mengapa Nadia salah menafsirkan *formulir kepegawaian antar-cabang* tersebut, misalnya: *"Sedangkan formulir kepegawaian antar-cabang yang kulihat di layarnya dan diserahkan ke Mbak Sinta HRD Senin lalu kupikir adalah formulir pengembalian masa tugasnya ke cabang asal."*
    - Di `chapters/bab-20.md` baris 23 & 37: Ubah kalimat telepon Pak Ramdan menjadi *"...biar Saka sendiri yang menghadap Pak Bambang di Yogyakarta untuk membereskan tanda tangan berkas administrasinya"*, dan ubah perihal amplop di baris 37 yang separuh tertutup buku menjadi *"Verifikasi Masa Tugas dan Pengembalian..."* (atau bagian kata setelah *Masa Tugas* tertutup buku catatan sehingga Nadia mengira itu surat penarikan kembali ke Jogja).

---

### B. Temuan `ERROR` dan `HIGH` Kategori `FIX BEFORE RELEASE`

#### [F-03] `ERROR` | `DOMAIN_FACTUALITY` / `TIMELINE` | Release Impact: `FIX BEFORE RELEASE` | Confidence: `HIGH`
- **Lokasi:** `chapters/bab-29.md` baris 31, 39, 59 dan `chapters/bab-31.md` baris 63
- **Bukti Kutipan:**
  - `bab-29.md:31 & 39`: *"Mas Saka izin balik ke Jogja naik kereta malam buat ngurus berkas kantor."* | *"Kemarin sore jam setengah enam."*
  - `bab-29.md:59` (Rabu pagi pukul 08.15–08.30): *"Aku buru-buru merogoh ponsel dari dalam tasku dan menekan nomor telepon Saka, namun suara operator hanya menjawab bahwa nomor yang kutuju sedang berada di luar jangkauan sinyal kereta."*
  - `bab-31.md:63`: *"Pesan Tari di kereta nggak mengubah keputusan itu..."*
- **Masalah Spesifik:**
  1. Berdasarkan verifikasi jadwal resmi PT KAI (waktu tempuh KA Jakarta–Yogyakarta 6 s.d. 7,5 jam), kereta malam yang berangkat dari Jakarta pada Selasa malam sudah tiba di Stasiun Tugu Yogyakarta antara pukul **00.30 hingga 05.00 dini hari Rabu**. Mustahil pada pukul 08.30 Rabu pagi Saka masih berada di dalam perjalanan kereta api dan baru membaca pesan Tari di kereta.
  2. Pesan suara operator seluler di Indonesia tidak pernah berbunyi *"sedang berada di luar jangkauan sinyal kereta"*.
- **Dampak bagi Pembaca:** Kesalahan fakta dunia nyata dan jadwal transportasi yang mencolok pada Bab 29 dan Bab 31.
- **Keputusan Editorial (`MANUSCRIPT ERROR`):**
  - **Saran Perbaikan Minimal:**
    - Di `chapters/bab-29.md` baris 31: Ubah *"naik kereta malam"* menjadi *"naik kereta pagi subuh tadi"* (dan di baris 39 jelaskan bahwa Selasa sore pukul 17.30 Saka berpamitan pada Pak Ramdan serta mengemasi mejanya lebih awal sebelum berangkat naik kereta pagi Rabu subuh).
    - Di `chapters/bab-29.md` baris 59: Ubah menjadi *"namun suara operator hanya menjawab bahwa nomor yang kutuju sedang berada di luar jangkauan."*

---

#### [F-04] `HIGH` | `DOMAIN_FACTUALITY` / `TIMELINE` | Release Impact: `FIX BEFORE RELEASE` | Confidence: `HIGH`
- **Lokasi:** `chapters/bab-32.md` baris 3 (dibandingkan dengan `chapters/bab-21.md` baris 9 & `chapters/bab-26.md` baris 7)
- **Bukti Kutipan:**
  - `bab-21.md:9`: *"Edisi peluncurannya dicetak digital dalam jumlah terbatas supaya keburu, cetak offset menyusul."*
  - `bab-32.md:3` (Senin sore, 3 hari setelah peluncuran Jumat): *"Tiga hari setelah acara peluncuran buku Sela Waktu yang kini sudah terpajang rapi di rak depan toko-toko buku kawasan Cikini dan Matraman dengan sambutan hangat dari para pembaca..."*
- **Masalah Spesifik:** Di Bab 21 baris 9 dan Bab 26 baris 7 telah ditetapkan bahwa cetakan yang selesai pada hari Jumat hanyalah *cetak digital dalam jumlah terbatas untuk acara peluncuran*, sementara *cetak offset menyusul*. Namun di Bab 32 baris 3 (Senin sore, hanya melewati akhir pekan Sabtu–Minggu sejak peluncuran Jumat!), buku tersebut diklaim sudah terpajang rapi di rak depan toko-toko buku kawasan Cikini dan Matraman. Sesuai standar industri percetakan offset dan distribusi gudang pusat (DC) ke jaringan toko buku mayor (1–3 minggu), jadwal 3 hari akhir pekan ini mustahil secara operasional.
- **Dampak bagi Pembaca:** Membatalkan logika perbaikan cetak digital terbatas yang sudah ditambahkan di Bab 21 dan Bab 26.
- **Keputusan Editorial (`MANUSCRIPT ERROR`):**
  - **Saran Perbaikan Minimal:** Di `chapters/bab-32.md` baris 3, ubah menjadi: *"Tiga hari setelah acara peluncuran buku Sela Waktu yang edisi perdananya kini sudah terpajang rapi di etalase toko buku tempat peluncuran di Cikini sambil menunggu cetakan massalnya selesai didistribusikan..."*

---

#### [F-05] `ERROR` | `NAME_TERM_CONSISTENCY` / `DOMAIN_FACTUALITY` | Release Impact: `FIX BEFORE RELEASE` | Confidence: `HIGH`
- **Lokasi:** `chapters/bab-03.md` baris 35, `chapters/bab-20.md` baris 29 & 37, dan `chapters/bab-31.md` baris 47 & 51
- **Bukti Kutipan:**
  - `bab-20.md:29`: *"...urusan kepulangan Saka ke kantor pusatnya di Yogyakarta."*
  - `bab-20.md:37`: *"...logo Kantor Pusat Penerbit Aksara Senja Cabang Yogyakarta..."*
  - `bab-31.md:47 & 51`: *"...amplop cokelat panjang berlogo Kantor Pusat Yogyakarta."* | *"Surat Keputusan Mutasi Tetap Staf Redaksi Senior dari Cabang Yogyakarta ke Kantor Redaksi Jakarta."*
- **Masalah Spesifik:** Kontradiksi istilah kantor Yogyakarta (disebut *Cabang Yogyakarta* sekaligus *Kantor Pusat Yogyakarta*, bahkan digabung menjadi *"Kantor Pusat Penerbit Aksara Senja Cabang Yogyakarta"* di Bab 20 baris 37) masih belum diperbaiki pada versi `post-fix`.
- **Dampak bagi Pembaca:** Merusak konsistensi istilah institusi dan logika struktur organisasi penerbit.
- **Keputusan Editorial (`MANUSCRIPT ERROR` & `OUTLINE ERROR`):**
  - **Saran Perbaikan Minimal:** Ubah `bab-20.md:29` menjadi *"kantor cabangnya di Yogyakarta"*, `bab-20.md:37` menjadi *"logo Penerbit Aksara Senja Cabang Yogyakarta"*, dan `bab-31.md:47` menjadi *"berlogo Cabang Yogyakarta"*.

---

#### [F-06] `ERROR` | `SETUP_PAYOFF` / `TIMELINE` | Release Impact: `FIX BEFORE RELEASE` | Confidence: `HIGH`
- **Lokasi:** `chapters/bab-06.md` baris 55
- **Bukti Kutipan:** *"Berbeda dengan kejadian kemarin saat menghadapi Mbak Dinda, kali ini Saka tidak memotong pembicaraan."*
- **Masalah Spesifik:** Bab 6 berlangsung pada **Jumat sore**, sedangkan peristiwa Saka memotong pembicaraan Mbak Dinda terjadi di **Bab 4** pada **Selasa sore** (3 hari sebelumnya, bukan "kemarin" / Kamis). Apalagi pada baris 7 bab yang sama, kata *"Kemarin"* sudah dipakai untuk merujuk hari Kamis.
- **Dampak bagi Pembaca:** Ketidakkonsistenan penanda waktu relatif di dalam satu bab yang sama.
- **Keputusan Editorial (`MANUSCRIPT ERROR`):**
  - **Saran Perbaikan Minimal:** Ubah *"kejadian kemarin"* di `chapters/bab-06.md` baris 55 menjadi *"kejadian Selasa sore"*.

---

#### [F-07] `ERROR` | `LOCATION_CONTINUITY` / `SETUP_PAYOFF` | Release Impact: `FIX BEFORE RELEASE` | Confidence: `HIGH`
- **Lokasi:** `chapters/bab-31.md` baris 75 (dan `outline.md` Bab 31) vs `chapters/bab-09.md` baris 5–11
- **Bukti Kutipan:**
  - `bab-31.md:75`: *"Enggak," elak Saka seraya membuang pandang ke arah pepohonan taman. "Saya cuma telanjur cocok sama soto ayam tanpa seledri di warung depan gedung kantor."*
- **Masalah Spesifik:** Adegan makan **soto ayam tanpa seledri** yang menjadi dasar *callback* romantis ini terjadi di **Warung Soto Kwitang dekat Halte Senen** pada hari Sabtu (Bab 9: *"Karikatur di Warung Soto Kwitang"*), **bukan** di warung depan gedung kantor Cikini (warung dekat gedung kantor di Bab 5 adalah warung ayam bakar di gang belakang kantor).
- **Dampak bagi Pembaca:** Detail lokasi pada kalimat klimaks/payoff utama di Bab 31 meleset dari bab tempat detail tersebut ditanam (Bab 9).
- **Keputusan Editorial (`MANUSCRIPT ERROR` & `OUTLINE ERROR`):**
  - **Saran Perbaikan Minimal:** Ubah `chapters/bab-31.md` baris 75 (dan `outline.md` Bab 31) menjadi: *"Saya cuma telanjur cocok sama soto ayam tanpa seledri di warung soto dekat Kwitang waktu itu."*

---

#### [F-08] `HIGH` | `TIMELINE` | Release Impact: `FIX BEFORE RELEASE` | Confidence: `HIGH`
- **Lokasi:** `chapters/bab-14.md` baris 3 & 7 vs `chapters/bab-18.md` baris 3, 17, 39 vs `chapters/bab-26.md` baris 53
- **Bukti Kutipan:**
  - `bab-14.md:3 & 7` (Kamis): *"Dua minggu duduk satu meja dengan Saka Wijaya..."* | *"...meski kemarin siang Ibu akhirnya sudah mau mengirim pesan suara menanyakan apakah papan gambar baruku sudah dipakai kerja."*
  - `bab-18.md:3, 17, 39` (Senin berikutnya): *"Sejak rahasia tutup botol minum hitamnya terbongkar di teras kosku malam Jumat lalu..."* | *"Memasuki minggu keempat kami duduk semeja..."* | *"Kemarin hari Jumat waktu antar berkas personalia..."*
- **Masalah Spesifik:** Di versi `post-fix`, Bab 23 baris 41 sudah diubah menjadi *"dua minggu lalu"* dan Bab 26 baris 53 diubah menjadi *"empat minggu lalu"*, yang mengonfirmasi bahwa Bab 18–21 adalah **Minggu ke-4** dan Bab 24–31 adalah **Minggu ke-5**. Namun, Bab 14–17 (yang terjadi pada hari Kamis tepat sebelum Senin Bab 18, dibuktikan oleh frasa *"malam Jumat lalu"* dan *"Kamis sore"* di Bab 18) masih menyebut *"Dua minggu duduk satu meja"* (baris 3) dan merujuk telepon Senin malam Bab 13 (Minggu ke-2) seolah baru beberapa hari berlalu (baris 7)! Akibatnya, masih ada lompatan 1 minggu kalender yang hilang antara Bab 13, Bab 14, dan Bab 18. Selain itu, frasa *"Kemarin hari Jumat"* di Bab 18 baris 39 yang diucapkan pada hari Senin tidak tepat secara tata bahasa.
- **Dampak bagi Pembaca:** Kronologi 5 minggu tidak sinkron pada transisi paruh tengah novel.
- **Keputusan Editorial (`MANUSCRIPT ERROR`):**
  - **Saran Perbaikan Minimal:**
    - Di `chapters/bab-14.md` baris 3: Ubah *"Dua minggu duduk satu meja"* menjadi *"Hampir tiga minggu duduk satu meja"*, dan di baris 7 ubah *"kemarin siang Ibu akhirnya sudah mau mengirim pesan suara menanyakan apakah papan gambar baruku sudah dipakai kerja"* menjadi *"beberapa hari lalu Ibu akhirnya sudah mau mengirim pesan suara menanyakan kabar kerjaku"*.
    - Di `chapters/bab-18.md` baris 39: Ubah *"Kemarin hari Jumat"* menjadi *"Hari Jumat kemarin"*.

---

#### [F-09] `ERROR` | `SPELLING_TYPO` / `GRAMMAR` | Release Impact: `FIX BEFORE RELEASE` | Confidence: `HIGH`
- **Lokasi:** `chapters/bab-03.md` baris 41, `chapters/bab-07.md` baris 41, `chapters/bab-10.md` baris 41, `chapters/bab-25.md` baris 27, dan `chapters/bab-32.md` baris 11
- **Bukti Kutipan & Koreksi Minimal (Belum Diperbaiki di Versi `post-fix`):**
  1. `bab-10.md:41`: `"...kasihan keponakan kamu udah telanjur dijanyiin naik pesawat."` -> **Typo** objektif (`dijanyiin`); perbaiki menjadi **`dijanjiin`**.
  2. `bab-03.md:41` & `bab-25.md:27`: `"...nafasku tersendat seketika."` & `"Nafasku memburu."` -> Bentuk tidak baku di narasi (tidak konsisten dengan *napasku* di bab lain); perbaiki menjadi **`napasku`** / **`Napasku`**.
  3. `bab-07.md:41`: `"...mendadak terhembus keluar."` -> Bentuk tidak baku di narasi; perbaiki menjadi **`terembus`**.
  4. `bab-32.md:11`: `"Nad, sore ini lo nggak ada jadwal kemana-mana kan?"` -> Penulisan kata depan *ke* yang digabung; perbaiki menjadi **`ke mana-mana`**.

---

### C. Temuan `REVIEW` dan `INFO` (`FIX BEFORE RELEASE` Lokal / `OPTIONAL POLISH`)

#### [F-10] `REVIEW` | `REPETITION` / `PROSE_CLARITY` | Release Impact: `FIX BEFORE RELEASE` | Confidence: `HIGH`
- **Lokasi:** `chapters/bab-12.md` baris 5–7 dan `chapters/bab-17.md` baris 13–15
- **Bukti Kutipan & Masalah Spesifik:**
  1. `bab-12.md:5-7`: Dua kalimat berurutan di akhir paragraf 2 dan awal paragraf 3 sama-sama diawali kata **"Namun"**, serta mengulang frasa *"di meja nomor empat"* dua kali dalam satu paragraf.
  2. `bab-17.md:13-15`: Deskripsi menyodorkan bungkusan martabak hangat pada baris 13 diulang lagi secara identik pada tag dialog baris 15 (*'"Sekalian bawa masuk ini," kata Saka seraya menyodorkan bungkusan plastik hangat itu ke arahku.'*).
- **Saran Perbaikan Minimal:** Hapus kata *"Namun"* di awal `bab-12.md:7` dan ringkas tag dialog di `bab-17.md:15` menjadi *'"Sekalian bawa masuk ini," kata Saka.'*

---

#### [F-11] `REVIEW` | `TIMELINE` (Kolokial Lisan) | Release Impact: `OPTIONAL POLISH` | Confidence: `MEDIUM`
- **Lokasi:** `chapters/bab-26.md` baris 29, `chapters/bab-28.md` baris 57, dan `chapters/bab-31.md` baris 21
- **Bukti Kutipan:**
  - `bab-26.md:29` & `bab-28.md:57` (Selasa): `"Waktu Ibu sakit kemarin..."` & `"Semua biaya klinik, bubur, dan bensin kemarin..."` (Mengacu pada hari Sabtu Bab 22, tiga hari sebelumnya).
  - `bab-31.md:21` (Jumat sore): `"Maaf buat sikapku kemarin, dan maaf buat omonganku di lobi."` (Mengacu pada Senin–Selasa Bab 24–26).
- **Saran Perbaikan Minimal:** Ubah menjadi *"hari Sabtu kemarin"* / *"akhir pekan kemarin"* di Bab 26 & 28, dan *"sikapku awal minggu ini"* di Bab 31 baris 21 agar waktu relatif tidak membingungkan pembaca.

---

#### [F-12] `REVIEW` | `DOMAIN_FACTUALITY` | Release Impact: `OPTIONAL POLISH` | Confidence: `MEDIUM`
- **Lokasi:** `chapters/bab-17.md` baris 19
- **Bukti Kutipan:** *"Tadi niatnya beli martabak telur buat makan di kereta," kata Saka dengan wajah lempeng.*
- **Analisis:** Karena kos Saka berada di Tebet (Bab 2 baris 33), kereta yang dinaikinya dari Stasiun Cikini adalah KRL Commuter Line Jabodetabek (waktu tempuh ~8–10 menit) yang melarang keras penumpang makan dan minum di dalam gerbong. Meskipun kalimat ini adalah kebohongan Saka, menggantinya menjadi *"buat makan malam di kos"* akan lebih natural bagi seorang pengguna rutin KRL.

---

#### [F-13] `INFO` | `OUTLINE_LEAKAGE` / `POV_BOUNDARY` | Release Impact: `OPTIONAL POLISH` | Confidence: `MEDIUM`
- **Lokasi:** `chapters/bab-27.md` baris 25
- **Bukti Kutipan:** *"Merasa bahwa di detik itu aku sudah resmi kembali ke dalam genggamannya dan Ibu sudah berada di pihaknya, topeng merendah yang dipakainya sejak hari Rabu lalu mulai melorot tanpa ia sadari."*
- **Analisis:** Ringkasan motivasi internal Dimas dari `outline.md` Bab 27; disarankan menambahkan penanda persepsi POV Nadia (*"Seolah merasa bahwa di detik itu..."*).

---

## 6. Evaluasi Delapan Gerbang Kelayakan & Vonis Kesiapan Publikasi (`rules/09-publication-readiness.md`)

### 6.1. Evaluasi Delapan Gerbang Kelayakan

| Gerbang Kelayakan | Status | Alasan & Bukti |
|---|---|---|
| **1. Fondasi dan janji cerita** | **LULUS** | Premis, fokus karakter, dan janji cerita tersampaikan dengan jelas dan hangat sejak pembukaan. |
| **2. Struktur dan perkembangan** | **GAGAL (`BLOCKER`)** | Paruh kedua (Bab 19–29) masih mengalami regresi karakter ekstrem pada Nadia (hampir mengangguk menerima Dimas kembali di Bab 27 baris 17) dan resolusi makan malam masih bertumpu pada kebetulan pelayan salah antar minum. |
| **3. Kausalitas, karakter, dan konflik** | **GAGAL (`BLOCKER`)** | Tabel Rantai Sebab-Akibat masih memiliki temuan `HIGH`: 7 kali pengabaian komunikasi satu kalimat dengan alasan sifat abstrak, alasan menepis petunjuk *formulir kepegawaian antar-cabang* di Bab 20 baris 29 yang tidak logis, serta kontradiksi telepon Pak Ramdan di Bab 20 vs fakta mutasi 3 minggu lalu di Bab 31. |
| **4. Narasi dan orientasi pembaca** | **PERLU PERBAIKAN** | Sebagian penanda waktu relatif telah diperbaiki, tetapi masih tersisa kesalahan di Bab 6 baris 55, Bab 18 baris 39, lompatan 1 minggu antara Bab 14 dan Bab 18, serta Bab 26, 28, 31. |
| **5. Adegan dan keterbacaan** | **LULUS** | Kontradiksi pengerjaan poster (Bab 3 & 7), pengiriman halaman penutup (Bab 21 & 24), dan *blocking* fisik tangan/tas Saka (Bab 3, 4, 17) telah diperbaiki dengan baik pada versi ini. |
| **6. Continuity, timeline, dan dunia cerita** | **GAGAL (`FIX BEFORE RELEASE`)** | Masih terdapat jadwal kereta malam Selasa yang mustahil masih di perjalanan pada Rabu pukul 08.30 pagi (Bab 29 baris 59 & Bab 31 baris 63), distribusi cetak massal ke toko buku Cikini & Matraman dalam 3 hari akhir pekan (Bab 32 baris 3), lokasi warung soto tanpa seledri yang salah di Bab 31 baris 75, dan kop surat *"Kantor Pusat Penerbit Aksara Senja Cabang Yogyakarta"* di Bab 20 & 31. |
| **7. Prosa dan teknis naskah** | **PERLU PERBAIKAN** | Masih terdapat typo objektif (`dijanyiin` di Bab 10 baris 41), bentuk tidak baku di narasi (`nafasku`, `terhembus`, `kemana-mana`), dan kalimat repetitif di Bab 12 & 17. |
| **8. Ketuntasan dan payoff** | **PERLU PERBAIKAN** | Sebagian besar *planting & callback* telah sinkron, namun rujukan lokasi warung soto pada *payoff* dialog utama di Bab 31 baris 75 dan rujukan waktu relatif di Bab 6 baris 55 masih meleset. |

---

### 6.2. Keputusan Akhir Kesiapan Publikasi (`rules/09-publication-readiness.md` §D)

- **Status Final:** **`NOT READY` (Kerangka Kausalitas Paruh Kedua Perlu Dibongkar & Perbaikan Lokal Rujukan/Prosedur)**
- **Alasan Keputusan:**
  Berdasarkan syarat mutlak pada `rules/09-publication-readiness.md` Bagian D, status `READY TO PUBLISH` hanya boleh diberikan apabila:
  1. **Tabel Rantai Sebab-Akibat (`rules/01-plot-and-causality.md`) tidak memiliki temuan `HIGH`** — *Belum terpenuhi* ([F-01] dan [F-02]: konflik paruh kedua masih bertumpu pada 7 kali pengabaian komunikasi dengan alasan sifat abstrak, penolakan petunjuk *formulir kepegawaian antar-cabang* di Bab 20 baris 29 tidak masuk akal, telepon Pak Ramdan di Bab 20 bertentangan dengan Bab 31, dan Nadia masih regresi hingga hampir menerima Dimas kembali di Bab 27 baris 17).
  2. **Proses Dunia Nyata (`rules/18-real-world-procedures.md`) semuanya terverifikasi tanpa jadwal mustahil** — *Belum terpenuhi* ([F-03] kereta malam Selasa petang dari Jakarta yang masih berada di perjalanan/"di luar jangkauan sinyal kereta" pada Rabu pukul 08.30 pagi di Bab 29 & 31; [F-04] distribusi buku ke rak depan toko-toko buku Cikini & Matraman hanya 3 hari setelah peluncuran edisi cetak digital terbatas di Bab 32; serta [F-05] kop surat Kantor Pusat vs Cabang Yogyakarta di Bab 20 & 31).
  3. **Daftar Rujukan Mundur (`--refs` / `rules/06-setup-payoff.md`) bebas dari perbedaan detail atau waktu relatif yang salah** — *Belum terpenuhi* ([F-06] Bab 6 baris 55 *"kejadian kemarin"* untuk Selasa sore pada hari Jumat; [F-07] Bab 31 baris 75 lokasi warung soto depan kantor vs Kwitang; [F-08] lompatan minggu Bab 14 ke Bab 18 dan konstruksi *"Kemarin hari Jumat"* pada hari Senin).
- **Rekomendasi Rilis:** Meskipun versi `post-fix` telah menyelesaikan ~15 kesalahan kontinuitas permukaan dari draf sebelumnya, tambalan yang dilakukan belum menyentuh akar masalah kausalitas paruh kedua dan masih menyisakan kesalahan faktual operasional serta rujukan mundur. Selesaikan perbaikan struktural kausalitas ([F-01], [F-02]) dan perbaikan lokal ([F-03] s.d. [F-10]) sebelum rilis.
