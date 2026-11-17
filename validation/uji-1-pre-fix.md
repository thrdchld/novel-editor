# Laporan Audit Editorial Lengkap — UJI 1 (Naskah Pre-Fix: *Catatan untuk Orang Sungkan*)

- **Proyek / Naskah:** *Catatan untuk Orang Sungkan* (Versi `pre-fix`)
- **Direktori Audit:** `/tmp/uji-pre` (`$TMPDIR/uji-pre`)
- **Cakupan Dokumen yang Dibaca:** 32 bab lengkap (`chapters/bab-01.md` s.d. `chapters/bab-32.md`) dan `outline.md` (Status: TERKUNCI v1.1).
- **Dokumen yang Tidak Dibaca / Diabaikan Sesuai Instruksi:** Tidak membuka `canon.md`, `ledger.md`, `state.md`, `reports/`, `tests/fixtures/`, maupun `EXPECTED-FINDINGS.md`.
- **Pernyataan *Blind Pass* Wajib (`AGENTS.md` §7.1):** Audit ini diawali dengan **blind pass** murni terhadap 32 file bab mentah (`chapters/bab-01.md` s.d. `chapters/bab-32.md`) dan `outline.md`. Seluruh pembacaan pengalaman pembaca (*reader pass*) dan penyusunan **Tabel Rantai Sebab-Akibat** dilakukan langsung dari bukti teks di halaman naskah sebelum pemeriksaan silang mekanis lainnya.
- **Keputusan Akhir Kesiapan Publikasi (`rules/09-publication-readiness.md`):** **`NOT READY` (Kerangka Perlu Dibongkar pada Kausalitas Paruh Kedua & Perbaikan Kontinuitas/Fakta Operasional)**

---

## 1. Story Assessment dan Evaluasi Developmental (`rules/16` & `rules/15`)

### 1.1. Apa yang Sudah Bekerja
1. **Premis, Janji Cerita, dan Pembukaan (Bab 1–9):**
   - Pembukaan *in medias res* di tangga darurat (Bab 1–2) langsung memperkenalkan karakterisasi Nadia Putri (desainer grafis 26 tahun yang kronis "nggak enakan"), luka barunya (diputuskan Dimas dengan julukan "operator *customer service*"), antagonis keseharian kantor (Mbak Dinda, Riko, Dimas), serta kontras tajam dengan Saka Wijaya (editor senior 28 tahun dari Yogyakarta yang lugas dan tertib batas waktu).
   - Progresi latihan berkata "tidak" di paruh pertama bekerja secara konkret dan bertahap: dibantu Saka menolak Mbak Dinda (Bab 4), menolak menalangi ayam bakar Riko (Bab 5), menolak membuatkan *backdrop* dadakan Dimas dan Vanya (Bab 6–7), hingga berani mempertahankan tabungan papan gambar di hadapan Ibu dan Mbak Raras (Bab 10–13).
2. **Planting & Callback Visual Utama:**
   - Tiga motif utama (*tell* Saka memutar tutup botol minum hitam hingga berbunyi *klik* dua kali saat berbohong untuk menutupi perhatiannya di Bab 5, 7, 17, 31; catatan *post-it* kuning *"Bilang enggak itu nggak bikin langit runtuh"* di Bab 4, 5, 26, 32; dan pembalikan kalimat "operator *customer service*" di Bab 1 & 28) memiliki fungsi emosional yang jelas dan memberi kepuasan baca pada bab penutup.

### 1.2. Masalah Struktural dan Kausalitas Utama
1. **Runtuhnya Kausalitas dan Agensi Tokoh di Paruh Kedua (Bab 19–29):**
   - Konflik utama paruh kedua (kesalahpahaman bahwa Saka akan pulang permanen ke Yogyakarta dan kembalinya Nadia ke pelukan Dimas hingga hampir resmi balikan di Bab 27) tidak tumbuh dari rintangan nyata yang tak terelakkan, melainkan dari **rekayasa penahanan komunikasi berulang (7 titik)** dan **alasan sifat abstrak** (*"tidak tega merusak suasana"*, *"penyakit nggak enakanku"*, *"gengsi"*, *"takut sendirian"*).
   - Tokoh POV (Nadia) mengabaikan petunjuk konkret yang sudah dilihatnya sendiri di halaman sebelumnya (tab kos tahunan Cikini dan formulir kepegawaian antar-cabang di laptop Saka pada Bab 14, serta laporan Tari bahwa Saka menyerahkan map formulir ke HRD pada Bab 18).
   - Regresi karakter Nadia di Bab 25–27 merusak perkembangan yang telah dibangun di Bab 1–18: setelah sanggup menolak Mbak Raras dan Ibunya di Bab 13 demi alat kerja, Nadia justru pasrah menyetujui makan malam peresmian balikan dengan Dimas dan **sudah bersiap mengangguk menerima Dimas kembali** di Bab 27 baris 17. Kesadaran Nadia di Bab 27 tidak lahir dari keputusan aktifnya, melainkan karena kebetulan pelayan salah mengantar es jeruk yang memicu Dimas membuka topengnya sendiri dan menyuruh Nadia membolos dari peluncuran bukunya.
2. **Kerusakan Kontinuitas, Rujukan Mundur (`--refs`), dan Jadwal Prosedur Dunia Nyata:**
   - Terdapat kontradiksi langsung pada lokasi kos Saka (di belakang Stasiun Cikini pada Bab 2 vs naik KRL ke arah selatan pada Bab 16–17), lokasi cerita masa lalu Saka (Kedai Kopi Cikini di Bab 12 berubah menjadi Warung Soto di Bab 21 & 25), rincian trauma mantan Saka di Bab 25 yang tidak pernah ditanam di Bab 12, pengiriman poster Dimas di Bab 2–3 & 7, pengiriman file halaman penutup di Bab 21 & 24, liburan Mbak Raras ke Bali vs Puncak di Bab 10 & 13, belasan rujukan waktu relatif *"kemarin"* / *"minggu lalu"* yang meleset dari kalender bab, serta jadwal cetak massal buku (2,5 hari kerja) dan kereta malam Jakarta–Yogyakarta yang tidak sesuai kenyataan operasional.

---

## 2. Tabel Rantai Sebab-Akibat dan Audit Kausalitas (`rules/01-plot-and-causality.md` & `rules/05-character-knowledge.md`)

### 2.1. Tabel Rantai Sebab-Akibat (7 Kolom Wajib dari Bab Mentah)

| peristiwa | keinginan tokoh | hambatan | pilihan | akibat yang tampak di halaman | pertanyaan "kenapa tidak X?" | jawaban di halaman |
|---|---|---|---|---|---|---|
| **Bab 1–3:** Nadia memaki Dimas & Mbak Dinda di tangga darurat Senin pukul 19.30; dipergoki Saka; kabur pulang pukul 19.45 tanpa menyentuh komputer (Bab 2 baris 49–53). Selasa pagi Dimas berterima kasih atas poster yang sudah jadi (Bab 3 baris 29). | Nadia ingin segera pulang menghindari rasa malu di depan Saka dan tidak peduli lagi pada tugas titipan malam itu. | Rasa malu ekstrem setelah omelannya didengar Saka di tangga darurat; di kantor ada tekanan sosial dari rekan kerja. | Nadia mematikan monitor dan langsung pulang Senin malam (Bab 2 baris 51–53). Namun di Bab 3 baris 29 poster Dimas tahu-tahu sudah selesai, dan di Bab 7 baris 31 Nadia mengklaim mengunggahnya *"Senin malam"*. | Kontradiksi aksi langsung di halaman: poster yang ditinggalkan di Bab 2 tahu-tahu selesai dan terunggah Senin malam tanpa adegan pengerjaan. | Kenapa Nadia tidak menolak poster Dimas saat dititipkan Senin sore, dan kapan sebenarnya poster itu dikerjakan jika Senin malam ia langsung kabur pulang? | **KOSONG / KONTRADIKTIF** untuk waktu pengerjaan poster (di Bab 2 baris 51 tertulis *"Bodo amat. Malam ini aku tidak peduli lagi"*, bertentangan dengan klaim Bab 7 baris 31 *"Senin malam"*). Untuk alasan tidak menolak Senin sore: hanya label sifat *"nggak enakan kronis"* (Bab 1 baris 37). |
| **Bab 4–7:** Saka menutup meja pukul 17.01 (Bab 4), menyemangati Nadia menolak talangan ayam bakar Riko (Bab 5), dan diam bersedekap memberi ruang saat Dimas & Vanya meminta *backdrop* Jumat sore (Bab 6–7). | Nadia ingin berhenti dimanfaatkan oleh Mbak Dinda, Riko, dan Dimas tanpa memicu keributan besar. | Kebiasaan lama takut dicap mantan pendendam di depan Vanya (Bab 6 baris 49) dan rasa sungkan di depan rekan kantor. | Nadia menolak Riko dengan menunjuk stiker QRIS (Bab 5) dan menolak Dimas dengan mengarahkan ke file mentah di folder bersama (Bab 7). | Riko terpaksa membayar sendiri; Dimas & Vanya pergi ke percetakan dengan kesal; Saka memberi apresiasi es jeruk (Bab 5) dan cokelat (Bab 7) sambil memutar tutup botol dua kali *klik*. | Kenapa Dimas dan Vanya tidak langsung mengubah skala *backdrop* sendiri dari awal jika aplikasi dan file mentah sudah ada di folder pemasaran? | Terjawab di halaman (Bab 6 baris 39–41): Vanya sudah mencoba tetapi resolusinya pecah, dan mereka ingin lepas tangan agar bisa pergi mengecek katering berdua. (**Valid**) |
| **Bab 10:** Minggu siang di Rawamangun, Ibu menanyakan Dimas dan memuji Dimas sebagai calon menantu ramah; Mbak Raras meminta pinjam Rp4 juta tabungan tablet gambar Nadia untuk hotel/mobil di Bali. | Nadia ingin mempertahankan tabungan Rp4 juta untuk membeli tablet gambar kerja dan tidak ingin terus dikaitkan dengan Dimas. | Tekanan emosional Ibu (*"ngalah dulu sama kakaknya"*) dan ketakutan dianggap anak egois/durhaka sejak kecil. | Untuk uang Rp4 juta, Nadia menunda jawaban (*"cek saldo dulu nanti malam"*). Namun untuk status Dimas, Nadia berbohong bahwa Dimas sibuk acara kantor dan menyembunyikan fakta bahwa mereka sudah putus. | Ibu tetap menganggap Dimas pacar Nadia (yang kelak memicu Ibu menelepon Dimas saat sakit di Bab 22); Mbak Raras terus menagih uang Rp4 juta di hari Senin. | **Kenapa Nadia tidak memberi tahu Ibunya sejak Minggu siang itu bahwa ia dan Dimas sudah putus?** | **ALASAN ABSTRAK (Temuan `HIGH`):** Bab 10 baris 17 hanya menyebutkan *"lidahku langsung kelu tidak tega merusak suasana hatinya"*. Tidak ada ancaman konkret, krisis kesehatan Ibu, atau hambatan situasional di meja makan yang menghalangi Nadia menyampaikan bahwa mereka sudah putus. |
| **Bab 11–13:** Kabel tablet gambar Nadia rusak parah saat kerja Senin; Saka menceritakan masa lalu studionya yang bangkrut di Jogja karena tak tegas menjaga batas (Bab 12); Senin malam Nadia menelepon Ibu. | Nadia ingin membeli tablet gambar baru tanpa memutus hubungan baik dengan ibunya. | Desakan WhatsApp Mbak Raras (batas bayar hotel pukul 22.00) dan nada kecewa Ibu di telepon. | Nadia menolak meminjamkan Rp4 juta secara lembut dengan alasan alat kerjanya rusak, dan memberikan Rp500 ribu secara cuma-cuma untuk jajan Daffa. | Ibu akhirnya memaklumi, tetapi di Bab 13 baris 57 Ibu berkata *"Biar Mbakmu liburan ke Puncak aja"*, padahal di Bab 10 baris 27 Mbak Raras sudah membeli tiket pesawat ke Bali. | Kenapa Mbak Raras bisa mengganti liburan ke Puncak begitu saja jika tiket pesawat ke Bali sudah dibeli kemarin (Bab 10 baris 27)? | **KONTRADIKSI KONTINUITAS (Temuan `ERROR`):** Teks Bab 13 baris 57 mengabaikan fakta pembelian tiket pesawat ke Bali di Bab 10 baris 27. |
| **Bab 14 & Bab 18:** Nadia melihat tab *"daftar sewa kamar kos tahunan daerah Cikini dan formulir kepegawaian antar-cabang"* di laptop Saka (Bab 14 baris 17–21); Tari melaporkan Saka menyerahkan map formulir ke Mbak Sinta HRD (Bab 18 baris 39). | Saka ingin mengurus mutasi tetap ke Jakarta atas tawaran Pak Ramdan; Nadia ingin tahu mengapa Saka mencari kos tahunan di Cikini. | Saka enggan mengungkapkan rencana mutasinya sebelum SK pelepasan resmi ditandatangani Kepala Cabang Yogyakarta. | Saka berbohong bahwa info kos tahunan itu titipan teman Jogja (Bab 14 baris 21, tanpa *tell* memutar tutup botol); Nadia menanggapi info Tari dengan asumsi *"Mungkin laporan proyek buku"* (Bab 18 baris 43). | Petunjuk kuat tentang kepindahan permanen Saka ke Jakarta sudah diketahui langsung oleh Nadia sejak Bab 14 dan Bab 18. | Kenapa Saka berbohong bahwa formulir kepegawaian antar-cabang dan kos tahunan itu untuk teman Jogja, dan kenapa ia tidak memutar tutup botolnya seperti aturan *tell* internal cerita? | Di halaman Bab 14 tidak dijelaskan mengapa Saka menyembunyikannya; baru di Bab 21/31 diklaim karena Saka pantang berjanji sebelum SK resmi turun—tetapi alasan ini tidak menjelaskan kebohongan tentang *formulir kepegawaian antar-cabang* di laptopnya sendiri. |
| **Bab 19–20:** Dimas meminta maaf di pantry dan membisikkan bahwa tugas Saka hanya 5 minggu (Bab 19); Nadia menguping telepon Pak Ramdan ke Pak Bambang dan melihat amplop *"Verifikasi Masa Tugas dan Pelepasan Pegawai"* (Bab 20). | Nadia ingin kepastian apakah Saka akan tetap di Jakarta atau kembali ke Yogyakarta setelah proyek *Sela Waktu* selesai. | Kalimat Pak Ramdan di telepon terdengar seperti masa tugas Saka habis minggu depan; Saka sedang di lantai dua. | Nadia langsung menyimpulkan Saka akan pulang permanen ke Yogyakarta dan melupakan sama sekali petunjuk tab kos tahunan Cikini & formulir kepegawaian antar-cabang (Bab 14). | Nadia patah hati, merasa seluruh perhatian Saka hanya sebatas tanggung jawab editor proyek sementara, dan menggambar sketsa kursi kosong di halaman penutup. | **Kenapa Nadia sama sekali tidak mengingat atau mempertimbangkan tab kos tahunan Cikini & formulir mutasi antar-cabang yang dilihatnya sendiri di Bab 14, dan kenapa Pak Ramdan bicara di telepon seolah Saka hanya bertugas 5 minggu padahal Pak Ramdan sendiri yang menawari Saka mutasi tetap sejak awal proyek (Bab 31)?** | **KOSONG / CACAT PENGETAHUAN & KAUSALITAS (`HIGH` / `BLOCKER`):** Di Bab 20 versi `pre-fix`, Nadia mengalami amnesia naratif atas petunjuk Bab 14 (baru tiba-tiba ingat di Bab 31 baris 53). Dialog telepon Pak Ramdan di Bab 20 juga bertentangan dengan fakta Bab 31 bahwa Pak Ramdan dan Saka sudah memproses mutasi tetap sejak 3 minggu lalu. |
| **Bab 21:** Jumat pukul 17.01, Nadia memancing pertanyaan ke Saka soal rencana setelah peluncuran buku; Saka menjawab minggu depan harus ke Yogyakarta menghadap Pak Bambang membereskan surat. | Nadia ingin tahu apakah Saka akan kembali ke Jogja; Saka ingin menyelesaikan administrasi pelepasannya di Jogja lebih dulu. | SK pelepasan Pak Bambang belum ditandatangani; telepon Kepala Cabang Jogja berdering saat Saka hendak mendesak Nadia. | Saka menjawab samar (*"minggu depan saya harus balik ke Yogyakarta menghadap Pak Bambang membereskan urusan surat"*); Nadia langsung bicara baku seperti operator CS dan menolak pulang bareng. | Kesalahpahaman terkunci sepanjang akhir pekan; keduanya membisu tanpa pesan konfirmasi. | **Kenapa Saka tidak mengatakan satu kalimat faktual bahwa surat yang diurus ke Pak Bambang adalah surat pelepasan untuk mutasi tetap ke Jakarta? Dan kenapa Nadia langsung memutus percakapan dengan gaya operator CS alih-alih bertanya surat apa yang dimaksud?** | **ALASAN ABSTRAK & PENAHANAN INFORMASI SEMU (`HIGH` / `BLOCKER`):** Di halaman (Bab 21 baris 25 & 37–43), Saka menahan fakta mutasi dengan alasan *"pantang mengumbar janji sebelum ada kepastian resmi"*, padahal menyebut proses mutasi yang sedang berjalan bukanlah janji kosong; Nadia menutup diri murni karena label abstrak *"penyakit nggak enakanku"*, *"rasa malu"*, dan *"melindungi harga diri"*. |
| **Bab 22–23:** Ibu kambuh vertigo Sabtu pagi dan menelepon Dimas karena mengira mereka masih pacaran; Dimas mengantar ke klinik; sorenya Dimas mengaku ke Ibu sudah minta maaf dan Ibu membujuk Nadia kembali pada Dimas. | Nadia ingin Ibunya pulih dan tidak kecewa, tetapi hatinya masih tertuju pada Saka. | Kondisi Ibu baru pulih dari vertigo; Saka tidak menghubungi Nadia sejak Jumat sore. | Nadia diam saja saat Ibu membujuknya mempertimbangkan Dimas kembali, tidak menceritakan alasan sebenarnya Dimas memutuskannya (demi Vanya & menghina sebagai CS), lalu menyetujui janji temu Dimas di lobi kantor Senin sore. | Dimas mendapat celah masuk kembali ke kehidupan Nadia dan mengklaim restu Ibu. | **Kenapa saat kondisi Ibu sudah tenang di Sabtu sore (Bab 23), Nadia tidak mengatakan secara jujur kepada Ibu bahwa Dimas memutuskannya demi staf magang baru (Vanya), melainkan membiarkan Ibu terus tertipu oleh versi sepihak Dimas?** | **ALASAN ABSTRAK (`HIGH`):** Bab 23 baris 51 hanya menyebut *"ketakutan membuat Ibu kecewa serta kekhawatiran berakhir sendirian di perantauan"*. Padahal ketika fakta yang sama diungkap Nadia 3 hari kemudian di Bab 28, Ibu langsung marah pada Dimas dan membela Nadia! |
| **Bab 24–25:** Senin sore Saka melihat ilustrasi kursi kosong di *dummy* buku dan bertanya ke Nadia, terpotong pesan Dimas; Saka menyusul ke lobi dan melihat Dimas membawa puding untuk Ibu. | Saka ingin mengonfirmasi maksud gambar kursi kosong dan kehadiran Dimas; Nadia ingin Saka menahannya dan menunjukkan rasa cemburu. | Dering WhatsApp Dimas di Bab 24; ego/gengsi Nadia dan luka lama Saka di lobi Bab 25. | Nadia sengaja mengungkit bahwa Dimas merawat ibunya dan meminta kesempatan kedua untuk memancing Saka (Bab 25 baris 23–33); Saka justru menjawab dingin bahwa kembali pada Dimas adalah *"pilihan paling masuk akal"* lalu pergi; Nadia langsung menerima ajakan makan malam peresmian balikan Dimas. | Hubungan Nadia dan Saka membeku total di Bab 26; Nadia terjadwal makan malam peresmian balikan dengan Dimas pada Selasa malam. | **Kenapa Nadia tidak menjawab pertanyaan Saka di Bab 24/25 dengan jujur bahwa ia menggambar kursi kosong karena mengira Saka pindah ke Jogja? Dan dari mana munculnya klaim Nadia di Bab 25 baris 35 bahwa mantan Saka di Jogja memilih "laki-laki pilihan orang tua yang dianggap lebih mapan"?** | **MOTIF TIDAK DITANAM & PENGABAIAN KOMUNIKASI (`HIGH` / `BLOCKER`):** Di Bab 25 baris 35, narasi mengklaim Saka terpicu cerita di *"warung soto"* bahwa mantannya memilih *"laki-laki pilihan orang tua yang dianggap lebih mapan"*, padahal di Bab 12 (di kedai kopi!) fakta itu **tidak pernah diceritakan**! Selain itu, di Bab 21 baris 9 Saka sudah mengirim seluruh file akhir ke percetakan sebelum Nadia pulang, sehingga mustahil Saka baru melihat ilustrasi kursi kosong itu pertama kali di cetakan *dummy* Bab 24! |
| **Bab 26–28:** Selasa malam makan malam keluarga bersama Ibu dan Dimas di Rawamangun; Nadia sudah hampir mengangguk menerima ajakan balikan Dimas (Bab 27 baris 17), sebelum pelayan salah mengantar es jeruk tanpa gula dan Dimas keceplosan menyuruh Nadia membolos dari peluncuran buku *Sela Waktu*. | Nadia awalnya pasrah ingin menyenangkan hati Ibunya; setelah Dimas meremehkan bukunya, Nadia ingin mengakhiri hubungan dengan Dimas secara permanen. | Rasa bersalah pada Ibu dan keputusasaan karena mengira Saka sudah melepaskannya. | Nadia hampir mengangguk setuju balikan (Bab 27 baris 17); namun setelah Dimas meremehkan buku *Sela Waktu* dan mengklaim akan mengizinkan Nadia ke Pak Ramdan, Nadia membongkar seluruh kebenaran di depan Ibu dan menolak Dimas dengan kalimat penutup operator CS (Bab 28). | Dimas dipermalukan dan diusir secara halus oleh Ibu; Nadia melunasi seluruh biaya klinik/bensin Dimas dan bertekad meminta maaf pada Saka Rabu pagi. | **Kenapa Nadia yang sudah tumbuh berani menolak Ibu dan Mbak Raras di Bab 13 tiba-tiba nyaris menerima Dimas kembali di Bab 27 baris 17, dan hanya batal karena kebetulan pelayan salah antar es jeruk serta kecerobohan Dimas menyuruhnya membolos dari panggung peluncuran?** | **REGRESI KARAKTER & KEBETULAN ANTAGONIS (`HIGH`):** Teks membuat agensi Nadia lumpuh hingga detik terakhir di Bab 27 baris 17, sehingga titik balik klimaks tidak digerakkan oleh ketegasan internal Nadia sejak awal makan malam, melainkan oleh kebetulan es jeruk ketukar dan blunder konyol Dimas (termasuk klaim absurd staf pemasaran bisa mengizinkan ilustrator utama absen kepada Kepala Redaksi). |
| **Bab 29–31:** Rabu pagi meja Saka kosong karena Saka berangkat ke Jogja Selasa petang; nomor Saka "di luar jangkauan sinyal kereta"; Tari mengirim WhatsApp ke Saka bahwa Nadia menolak Dimas; Jumat sore Saka hadir di peluncuran buku membawa SK Mutasi Tetap. | Nadia ingin meminta maaf secara langsung kepada Saka; Saka ingin membereskan kos lama dan mengambil tanda tangan pelepasan Pak Bambang di Jogja sebelum peluncuran Jumat. | Saka berangkat Selasa malam; ponsel Saka tidak aktif saat ditelepon Rabu pagi. | Nadia menangis membaca catatan merah Saka di *dummy* buku dan menunggu hingga acara peluncuran Jumat; di Bab 31 Saka menunjukkan SK Mutasi Tetap dan memutar tutup botol dua kali saat mengelak pindah demi Nadia. | Kesalahpahaman tuntas di balkon toko buku Cikini; pada Bab 32 mereka resmi bekerja tetap semeja dan Saka ikut makan malam ke Rawamangun. | **Kenapa Nadia tidak mengirim pesan WhatsApp penjelasan kepada Saka sejak Selasa malam/Rabu pagi atau bertanya langsung kepada Pak Ramdan di kantor? Dan kenapa di Bab 31 baris 65 Saka berkata *"Begitu baca pesan dari Tari kalau kamu nolak Dimas, saya langsung beresin kos lama"*, padahal permohonan mutasi tetapnya sudah diajukan sejak 3 minggu lalu?** | **KOSONG / KONTRADIKTIF (`HIGH`):** Di Bab 29 versi `pre-fix`, tidak ada alasan mengapa Nadia tidak mengirim pesan WhatsApp langsung ke Saka (sementara Tari justru mengirim WhatsApp ke Saka!) atau bertanya pada Pak Ramdan. Selain itu, kalimat Saka di Bab 31 baris 65 bertentangan dengan fakta bahwa ia sudah mengajukan mutasi tetap 3 minggu sebelumnya dan berangkat ke Jogja Selasa sore memang untuk mengurus kepindahannya. |

---

### 2.2. Uji Pertanyaan "Kenapa Tidak X?" dan Larangan Alasan Abstrak (`rules/01-plot-and-causality.md` §2)

Sesuai aturan keras `rules/01-plot-and-causality.md` §2, alasan berupa label sifat abstrak (*"karena nggak enakan"*, *"karena gengsi"*, *"karena sungkan"*, *"karena takut merusak suasana"*) tanpa pemicu/ancaman konkret di halaman wajib dicatat sebagai temuan `CAUSALITY` / `MOTIVATION`:

1. **Bab 10 baris 17:** Nadia menyembunyikan fakta sudah putus dari Dimas selama sebulan penuh hanya dengan alasan: *"lidahku langsung kelu tidak tega merusak suasana hatinya."*
2. **Bab 21 baris 37–43:** Nadia tidak menanyakan surat apa yang diurus Saka ke Yogyakarta dan malah berbicara baku seperti operator layanan hanya karena: *"penyakit nggak enakanku langsung ikut berbisik di kepalaku"*, *"rasa malu dan takut ditinggalkan"*, serta *"untuk melindungi harga diri dan agar tidak terlihat menyedihkan"*.
3. **Bab 23 baris 51:** Nadia tidak menceritakan alasan sebenarnya Dimas memutuskannya kepada Ibu dan malah menyetujui janji temu Dimas karena: *"titik terlemah dalam diriku memang ketakutan membuat Ibu kecewa serta kekhawatiran berakhir sendirian di perantauan."*
4. **Bab 25 baris 31–33 & 55:** Nadia bukannya menjelaskan ketakutannya ditinggal Saka ke Jogja, melainkan mengungkit kebaikan Dimas dan menerima ajakan makan malam balikan karena: *"alasan bodoh... Aku ingin melihat apakah wajah tenang itu akan goyah"* dan *"Rasa gengsi dan patah hati membuat pandanganku buram"*.

---

### 2.3. Hitungan Konflik yang Bergantung pada Pengabaian Komunikasi (`rules/01-plot-and-causality.md` §3)

Berapa kali konflik utama atau kesalahpahaman di paruh kedua naskah dapat selesai hanya dengan **satu pertanyaan, satu kalimat konfirmasi, atau satu pesan singkat** yang diabaikan oleh tokoh?

1. **Pengabaian #1 (Bab 10 baris 15–17):** Satu kalimat jujur Nadia kepada Ibu bahwa ia dan Dimas sudah putus karena Dimas mendekati Vanya akan mencegah Ibu menghubungi Dimas saat vertigo di Bab 22.
2. **Pengabaian #2 (Bab 14 baris 19–21):** Satu kalimat jujur Saka saat Nadia memergoki tab kos tahunan Cikini dan formulir kepegawaian antar-cabang di laptopnya akan mencegah seluruh keraguan di Bab 19–29.
3. **Pengabaian #3 (Bab 20 baris 29–38):** Satu pertanyaan konfirmasi Nadia kepada Pak Ramdan atau Saka mengenai arti amplop *"Verifikasi Masa Tugas dan Pelepasan Pegawai"* (mengingat petunjuk tab kos tahunan Cikini di Bab 14 dan formulir HRD di Bab 18) akan langsung mengungkap bahwa Cabang Yogyakarta sedang *melepas* Saka ke Jakarta.
4. **Pengabaian #4 (Bab 21 baris 29–53):** Satu kalimat lugas dari Saka (*"Saya ke Jogja untuk mengambil tanda tangan pelepasan mutasi tetap ke Jakarta"*) atau satu pertanyaan lanjutan dari Nadia alih-alih berubah menjadi operator CS dan mengusir Saka pulang duluan akan langsung menghentikan kesalahpahaman.
5. **Pengabaian #5 (Bab 23 baris 37–50):** Satu kalimat jujur Nadia kepada Ibu pada Sabtu sore tentang alasan Dimas memutuskannya di parkiran akan langsung menghentikan bujukan Ibu saat itu juga (sebagaimana terbukti di Bab 28).
6. **Pengabaian #6 (Bab 24 baris 39–60 & Bab 25 baris 15–58):** Saat Saka menunjuk gambar kursi kosong dan bertanya *"Kamu sebenarnya mikirin apa?"* lalu menyusul ke lobi, satu kalimat jujur dari Nadia (*"Aku sedih karena mengira Mas Saka pulang selamanya ke Jogja"*) atau satu kalimat penjelasan dari Saka tentang SK Mutasi Tetap akan membatalkan pertengkaran lobi dan rencana makan malam bersama Dimas.
7. **Pengabaian #7 (Bab 29 baris 57–65):** Setelah membaca catatan tangan Saka di *dummy* buku (*"lain kali jangan suka menyimpulkan isi kepala orang sebelum bertanya sampai selesai"*), satu pesan WhatsApp langsung dari Nadia kepada Saka atau satu pertanyaan ke Pak Ramdan pada Rabu pagi akan menjernihkan situasi tanpa harus menunggu 3 hari sampai Jumat sore.

**Total Akumulasi:** **7 kali pengabaian komunikasi satu kalimat.** Sesuai `rules/01-plot-and-causality.md` §3, pengabaian berulang tanpa hambatan eksternal baru yang lebih kuat ini merupakan **cacat struktural kausalitas (`HIGH` / `BLOCKER`)**.

---

## 3. Evaluasi Lengkap Daftar Rujukan Mundur dan Waktu Relatif (`--refs` / `rules/06-setup-payoff.md`)

Berikut adalah hasil eksekusi `python3 scripts/audit_core.py --root /tmp/uji-pre --refs` beserta penilaian editorial lengkap terhadap keberadaan setup, kesamaan detail, dan ketepatan waktu relatif untuk **seluruh item** dari Bab 1 hingga Bab 32:

### Bab 1
- **Baris 7 (`dulu`):** `Kalau gue customer service, telepon lo udah gue matiin dari dulu, Dimas!"`
  - **Penilaian:** **LULUS.** Hiperbola retoris mengacu pada masa pacaran 2 tahun sebelum Bab 1.
- **Baris 17 (`waktu itu`):** `"Aku capek, Nad," katanya waktu itu sambil memegang tali helm.`
  - **Penilaian:** **LULUS.** Mengacu pada Jumat malam lalu di parkiran basement (dijelaskan langsung pada baris 15).

### Bab 2
- **Baris 33 (`kemarin lusa`):** `"Saya baru pindah ke Jakarta kemarin lusa.`
  - **Penilaian:** **LULUS.** Bab 2 berlangsung Senin malam; "kemarin lusa" berarti hari Sabtu akhir pekan sebelumnya, konsisten dengan mulai masuk kerja hari Selasa (Bab 3).

### Bab 3
- **Baris 17 (`Tadi pagi`):** `Tadi pagi jam tujuh lewat lima belas sudah saya kirim ke email Mbak Dinda," jawabku sopan...`
  - **Penilaian:** **LULUS (dengan catatan beban kerja dini hari).** Bab 3 berlangsung Selasa pagi pukul 09.00; mengacu pada Selasa pukul 07.15 pagi.
- **Baris 21 (`Kemarin`):** `Kemarin gue dengar sendiri di pantry."`
  - **Penilaian:** **LULUS.** Bab 3 adalah Selasa pagi; Tari merujuk pada hari Senin kemarin saat Mbak Dinda menitipkan revisi ke Nadia (konsisten dengan Bab 1 baris 33).
- **Baris 53 (`tadi malam`):** `Duduk semeja dengan pria yang tadi malam mendengarkan seluruh aib makianku di tangga darurat?!`
  - **Penilaian:** **LULUS.** Mengacu langsung pada adegan tangga darurat Senin malam di Bab 1–2.

### Bab 4
- **Baris 39 (`dulu`):** `Namun sebelum benda itu menyentuh mejaku, Saka sudah lebih dulu berdiri tegak di samping kursinya.`
  - **Penilaian:** **LULUS.** Urutan aksi fisik di dalam adegan ("lebih dulu").

### Bab 5
- **Baris 3 (`kemarin`):** `Setiap kali Mbak Dinda melintas di belakang mejaku sambil melempar lirikan masam karena urusan flash disk kemarin sore...`
  - **Penilaian:** **LULUS.** Bab 5 berlangsung Rabu siang; urusan *flash disk* Mbak Dinda terjadi Selasa sore di Bab 4 baris 33–56.
- **Baris 13 (`dulu`):** `"Talangin punya gue dulu dong?`
  - **Penilaian:** **LULUS.** Ungkapan percakapan ("terlebih dahulu").
- **Baris 17 (`Bulan lalu`):** `Bulan lalu saja Riko sudah tiga kali memakai alasan dompet tertinggal.`
  - **Penilaian:** **LULUS.** Latar kebiasaan Riko sebelum cerita dimulai, konsisten dengan total utang Rp90.000 (3 x Rp30.000) yang ditagih di Bab 32 baris 33.

### Bab 6
- **Baris 7 (`Kemarin`):** `Kemarin waktu staf administrasi meminta bantuan memotong dua ratus lembar kupon diskon secara manual, aku berani menolak dengan alasan sedang mengejar draf ilustrasi bab tiga.`
  - **Penilaian:** **LULUS.** Bab 6 berlangsung Jumat sore (dua hari setelah Rabu Bab 5); "kemarin" merujuk pada hari Kamis yang dilompati secara naratif.
- **Baris 15 (`Waktu itu`):** `"Buku Sela Waktu itu kan tentang orang kota yang kecapekan kerja sampai lupa waktu.`
  - **Penilaian:** **LULUS.** *False positive* pencocokan kata `Waktu itu` dari judul buku *Sela Waktu* diikuti kata *itu*.
- **Baris 35 (`dulu`):** `"Acara bincang buku besok pindah ke aula bawah," ujar Dimas dengan intonasi memohon yang dulu selalu berhasil meluluhkan hatiku.`
  - **Penilaian:** **LULUS.** Mengacu pada masa pacaran 2 tahun mereka.
- **Baris 45 (`minggu lalu`):** `...Dimas bahkan memujiku di depan Vanya menggunakan sifat sungkanku yang minggu lalu dia jadikan alasan untuk mengakhiri hubungan kami!`
  - **Penilaian:** **LULUS.** Bab 6 adalah Jumat sore Minggu 1; putus hubungan terjadi Jumat malam minggu sebelumnya (Bab 1 baris 15).
- **Baris 55 (`kemarin`):** `Berbeda dengan kejadian kemarin saat menghadapi Mbak Dinda, kali ini Saka tidak memotong pembicaraan.`
  - **Penilaian:** **TEMUAN (`ERROR` — `SETUP_PAYOFF` / `TIMELINE`).** Bab 6 terjadi pada **Jumat sore**, sedangkan adegan Saka memotong pembicaraan Mbak Dinda terjadi di **Bab 4** pada **Selasa sore** (3 hari sebelumnya, bukan "kemarin"!). Apalagi di baris 7 bab yang sama, kata "kemarin" sudah dipakai dengan benar untuk merujuk hari Kamis.

### Bab 7
- **Baris 11 (`minggu lalu`):** `Ingatan Jumat malam minggu lalu mendadak melintas di kepalaku, saat aku berdiri kaku di parkiran motor...`
  - **Penilaian:** **LULUS.** Konsisten dengan Bab 1 baris 15 dan Bab 6 baris 45.
- **Baris 29 (`kemarin`):** `"Loh, kan cuma tinggal tarik ukuran dari file poster yang kemarin, Nad," desak Dimas kesal.`
  - **Penilaian:** **LULUS (Kolokial) / CATATAN.** Mengacu pada poster acara yang dititipkan Senin sore (Bab 1 baris 11 & 29); dalam percakapan lisan "yang kemarin" sering berarti "yang tempo hari/awal minggu ini", namun pada baris 31 terdapat **kontradiksi setup** karena Nadia mengklaim *"File mentahnya sudah kuunggah ke folder bersama divisi pemasaran dari Senin malam"*, padahal di Bab 2 baris 49–53 pada Senin malam Nadia langsung mematikan monitor dan kabur pulang tanpa menyentuh kertas coretan Dimas!
- **Baris 61 (`Tadi pagi`):** `"Tadi pagi kasir minimarket depan stasiun ngasih promo beli kopi botol," jawab Saka santai.`
  - **Penilaian:** **LULUS.** Kebohongan disengaja oleh Saka pada Jumat sore (dibuktikan dengan *tell* memutar tutup botol dua kali *klik* dan ingatan Nadia di baris 67 bahwa pagi tadi Saka menyeduh kopi bubuk di dapur kantor).

### Bab 8
- **Baris 25 (`Dulu`):** `Dulu waktu masih pacaran sama Dimas, kalau kami jalan di trotoar lalu dia pindah ke sisi luar...`
  - **Penilaian:** **LULUS.** Latar masa pacaran sebelum Bab 1.
- **Baris 31 (`dulu`):** `"Di naskah kan ada bagian yang bahas bioskop tua sama toko roti zaman dulu."`
  - **Penilaian:** **LULUS.** Frasa "zaman dulu" sebagai topik isi buku.
- **Baris 35 (`Kemarin`):** `"Kemarin Dimas bilang gaya kayak gini kusam dan kurang komersial."`
  - **Penilaian:** **TEMUAN (`ERROR` / `HIGH` — `SETUP_PAYOFF` / `TIMELINE`).** Rujukan tanpa tanam dan salah waktu relatif! Bab 8 berlangsung **Sabtu siang Minggu 1**, sehingga "kemarin" berarti **Jumat (Bab 6–7)**. Di Bab 6–7, Dimas hanya meminta pembuatan *backdrop* panggung dari file poster dan **tidak pernah melihat buku sketsa Nadia atau mengkritik gaya arsiran pensil arang Nadia sebagai "kusam dan kurang komersial"**. Kritik Dimas terhadap arsiran pensil arang baru terjadi 2 minggu kemudian di Bab 14!
- **Baris 37 (`dulu`):** `Tangan Saka yang sedang menarik sebuah buku kumpulan foto Jakarta tempo dulu berhenti bergerak.`
  - **Penilaian:** **LULUS.** Frasa "tempo dulu".
- **Baris 43 (`Waktu itu`):** `"Berarti yang tahu cocok atau enggaknya gambar itu sama isi naskah Sela Waktu itu saya sama kamu, bukan dia," kata Saka lugas.`
  - **Penilaian:** **LULUS.** *False positive* judul buku *Sela Waktu* diikuti kata *itu*.

### Bab 9
- **Baris 11 & 13 (Rujukan mundur implisit `Waktu makan ayam bakar` & `Waktu makan bakso di kantin`):**
  - **Penilaian:** Rujukan *"Waktu makan ayam bakar"* cocok dengan Bab 5 (meskipun di Bab 5 detail menyisihkan seledri tidak ditampilkan secara eksplisit di halaman, masih dapat diterima sebagai observasi Saka saat adegan berlangsung). Namun rujukan *"Waktu makan bakso di kantin juga kamu minta kuah kosongan"* merujuk pada kejadian di antara Selasa–Jumat yang tidak pernah ditampilkan di halaman.
- **Baris 39 (`dulu`):** `Sebelum tanganku sempat menyambar buku sketsa itu untuk menutupnya, mata Saka sudah lebih dulu tertuju ke halaman belakang...`
  - **Penilaian:** **LULUS.** Urutan aksi fisik ("lebih dulu").

### Bab 10
- **Baris 17 (`minggu lalu`):** `Aku belum berani bilang ke Ibu bahwa hubungan dua tahunku dengan calon menantu kesayangannya itu sudah tamat sejak Jumat minggu lalu.`
  - **Penilaian:** **LULUS (Kolokial).** Bab 10 adalah Minggu siang (9 hari setelah Jumat malam putus hubungan).
- **Baris 27 (`kemarin`):** `"Iya, makanya Mbak udah pesan tiket pesawat dari kemarin," lanjut Mbak Raras santai.`
  - **Penilaian:** **TEMUAN KONTINUITAS LINTAS BAB (`ERROR` di Bab 13 baris 57).** Rujukan "kemarin" (Sabtu) di Bab 10 baris 27 ini sah, tetapi **dilanggar di Bab 13 baris 57** saat Ibu berkata *"Biar Mbakmu liburan ke Puncak aja sesuai uang yang ada"*, seolah-olah tiket pesawat ke Bali belum pernah dibeli!
- **Baris 31, 45, 53 (`dulu`):** `"Mbak pinjam tabungan kamu dulu..."`, `"ngalah dulu..."`, `"cek saldo rekeningku dulu..."`
  - **Penilaian:** **LULUS.** Penggunaan kata keterangan "terlebih dahulu/sementara".

### Bab 11
- **Baris 31 (`dulu`):** `"Teduh di situ dulu," ajak Saka...`
  - **Penilaian:** **LULUS.** Kata keterangan "terlebih dahulu".
- **Baris 49 (`kemarin`) & Baris 51 (`Kemarin`):** `Beban yang sejak kemarin sore mengganjal...` | `"Kemarin waktu pulang ke Rawamangun, Mbak Raras minta pinjam uang tabunganku,"`
  - **Penilaian:** **LULUS.** Bab 11 berlangsung Senin sore Minggu 2; "kemarin" merujuk dengan tepat pada Minggu siang/sore di Rawamangun (Bab 10).

### Bab 12
- **Baris 13 (`Dulu`), Baris 21 (`Dulu`), Baris 33 (`Dulu`):** `"Dulu waktu baru lulus kuliah di Jogja..."` | `"Dulu saya merintis studio penyuntingan kecil..."` | `Dulu kupikir dia sengaja bergaya membawa botol usang.`
  - **Penilaian:** **LULUS** pada Bab 12, tetapi menjadi dasar bukti bahwa cerita masa lalu Saka di Yogyakarta disampaikan **di Kedai Kopi Kecil dekat Stasiun Cikini** (Bab 11–12), **bukan** di warung soto (yang keliru dirujuk di Bab 21 baris 25 dan Bab 25 baris 35), dan bahwa Saka **tidak pernah** menceritakan mantannya memilih laki-laki pilihan orang tua (yang diklaim secara keliru di Bab 25 baris 35).

### Bab 13
- **Baris 25 (`Kemarin`, `dulu`):** `"Kemarin siang kan kamu bilangnya mau cek saldo dulu.`
  - **Penilaian:** **LULUS.** Bab 13 berlangsung Senin malam Minggu 2; Ibu merujuk tepat pada ucapan Nadia saat makan siang Minggu di Bab 10 baris 53.
- **Baris 67 (`ceritanya`):** `Makasih banyak ya, Mas, buat ceritanya sama tahu isinya tadi sore.`
  - **Penilaian:** **LULUS.** Mengacu tepat pada cerita Saka dan tahu isi di kedai kopi pada Bab 11–12 petang harinya.

### Bab 14
- **Baris 5 (`dulu`):** `Kedua, tumpukan map plastik warna-warni titipan warga kantor yang dulu selalu menghalangi pandanganku kini sudah punah sama sekali.`
  - **Penilaian:** **LULUS.** Mengacu pada kondisi meja Nadia di Bab 1–3.
- **Baris 7 (`kemarin`):** `Di grup WhatsApp keluarga pun, Mbak Raras masih mendiamkanku sejak malam itu, meski kemarin siang Ibu akhirnya sudah mau mengirim pesan suara menanyakan apakah papan gambar baruku sudah dipakai kerja.`
  - **Penilaian:** **TEMUAN KRONOLOGI (`HIGH` — `TIMELINE`).** Bab 14 terjadi pada hari **Kamis siang** dan dibuka dengan klaim *"Dua minggu duduk satu meja dengan Saka Wijaya"* (baris 3), lalu 4 hari kemudian pada hari Senin (Bab 18 baris 17) sudah disebut *"Memasuki minggu keempat kami duduk semeja"*. Jika Kamis Bab 14 adalah akhir Minggu ke-3 (10 hari setelah telepon Senin malam Bab 13), maka "kemarin siang" (Rabu Minggu ke-3) berarti Ibu mendiamkan Nadia selama 9 hari penuh sejak Nadia membelikan papan gambar di Minggu ke-2. Sebaliknya, jika Kamis Bab 14 adalah Minggu ke-2 (3 hari setelah telepon Senin malam Bab 13), maka Senin berikutnya (Bab 18) baru memasuki **Minggu ke-3**, bukan Minggu ke-4!
- **Baris 15 (`waktu itu`):** `Asal jangan dikasih warna hijau stabilo lagi kayak waktu itu."`
  - **Penilaian:** **LULUS.** Mengacu tepat pada Bab 11 baris 45 (*"kucing kampung jadi hijau stabilo"*).
- **Baris 27 (`kemarin`):** `Kabar burung yang beredar dari dapur kantor menyebutkan bahwa Vanya kemarin sempat ngambek dan menolak membantu Dimas menyiapkan laporan bulanan...`
  - **Penilaian:** **LULUS.** Kejadian internal kantor sehari sebelum Kamis Bab 14.
- **Baris 29 (`dulu`), Baris 41 (`Dulu`), Baris 45 (`Dulu`):** Mengacu pada masa pacaran Nadia dan Dimas sebelum putus.
  - **Penilaian:** **LULUS.**

### Bab 15
- **Baris 21 (`Dulu`):** `Dulu waktu kami masih berpacaran, setiap kali ada rapat gabungan dan ide desainku dikritik orang lain, Dimas tidak pernah sekali pun membela karyaku.`
  - **Penilaian:** **LULUS.** Latar masa lalu hubungan Nadia–Dimas.
- **Baris 23 (`dulu`) & Baris 61 (`dulu`):** `...Saka lebih dulu menggeser laptop peraknya...` | `...berjalan lebih dulu keluar pintu ruang rapat...`
  - **Penilaian:** **LULUS.** Urutan aksi fisik ("lebih dulu").

### Bab 16
- **Baris 47 (`Dulu`):** `Dulu waktu sama Dimas, baru kena gerimis dua tetes saja dia sudah sibuk menyelamatkan rambutnya sendiri pakai map kertas.`
  - **Penilaian:** **LULUS.** Perbandingan karakterisasi masa lalu.

### Bab 17
- **Baris 25 (`katanya`):** `Dan di dalam kantong plastik yang dibawa Saka sendiri, sama sekali tidak ada kotak kedua yang katanya berisi martabak telur itu.`
  - **Penilaian:** **LULUS.** Mengacu langsung pada klaim bohong Saka di baris 19 bab yang sama.

### Bab 18
- **Baris 11 (`Kemarin`):** `"Kemarin Mas Saka bilang nggak suka makanan manis," godaku sambil menahan senyum.`
  - **Penilaian:** **TEMUAN (`ERROR` — `SETUP_PAYOFF` / `TIMELINE`).** Bab 18 berlangsung pada **Senin pagi** (baris 5: *"Senin pagi pukul sembilan kurang sepuluh menit"*). Kata *"Kemarin"* berarti hari **Minggu**, padahal Saka mengatakan *"Saya kan nggak suka makanan manis"* pada **Kamis malam (malam Jumat)** di Bab 17 baris 23 (dan Jumat sore di Bab 7 baris 61)!
- **Baris 17 (`dulu`) & Baris 19 (`dulu`):** Mengacu pada hari pertama duduk di meja nomor empat (Bab 3–4).
  - **Penilaian:** **LULUS** untuk referen hari pertama, namun klaim *"Memasuki minggu keempat"* di baris 17 melompati 1 minggu kalender dari Kamis Bab 14–17.
- **Baris 29 (`Kemarin`):** `"Kemarin sore gue lihat dari jendela atas, Mas Saka balik dari stasiun buat mayungin lo jalan kaki."`
  - **Penilaian:** **TEMUAN (`ERROR` — `SETUP_PAYOFF` / `TIMELINE`).** Bab 18 berlangsung pada hari **Senin siang**. Adegan Saka berbalik dari arah stasiun untuk memayungi Nadia berjalan kaki terjadi pada **Kamis sore** (Bab 16), **bukan** "kemarin sore" (Minggu sore)!
- **Baris 39 (`Kemarin`):** `"Kemarin waktu antar berkas personalia, gue lihat Mas Saka nyerahin map formulir ke Mbak Sinta HRD."`
  - **Penilaian:** **TEMUAN (`ERROR` — `SETUP_PAYOFF` / `TIMELINE`).** Bab 18 adalah hari **Senin**; tidak mungkin Tari mengantar berkas personalia dan melihat Saka menyerahkan map formulir ke Mbak Sinta HRD di kantor pada hari Minggu ("kemarin")!
- **Baris 43 (`waktu itu`) & Baris 51 (`ceritanya`):** Mengacu pada momen percakapan dengan Tari dan cerita di balik botol minum penyok Saka (Bab 12).
  - **Penilaian:** **LULUS.**

### Bab 19
- **Baris 5 (`kemarin`):** `Sejak kemarin, suasana di divisi pemasaran agak tegang. Kata Tari, hubungan singkat antara Dimas dan Vanya sudah bubar jalan gara-gara mereka ribut besar soal pembagian tugas pameran akhir pekan lalu.`
  - **Penilaian:** **LULUS** untuk baris 5 (Bab 19 adalah Rabu sore; "sejak kemarin" = Selasa, setelah ribut pameran akhir pekan lalu). **TETAPI KONTRADIKTIF dengan baris 39** di bab yang sama: pada baris 39 Dimas berkata, *"Seminggu ini setelah Vanya pergi, aku baru sadar nggak ada orang setulus kamu, Nad."* Padahal jika mereka baru bubar gara-gara tugas pameran *akhir pekan lalu* (3–4 hari sebelum Rabu Bab 19, dan suasana baru tegang "sejak kemarin" Selasa), belum ada "seminggu" sejak Vanya pergi!
- **Baris 13 (`dulu`) & Baris 17 (`dulu`):** Mengacu pada Bab 1/6 (menyuruh buat poster) dan masa awal pacaran 2 tahun lalu.
  - **Penilaian:** **LULUS.**
- **Baris 65 (`Tadi pagi`):** `"Tadi pagi orang HRD baru aja bahas tiket kepulangan dia ke Jogja."`
  - **Penilaian:** **LULUS (Manipulasi Dialog Antagonis).** Klaim lisan Dimas pada Rabu sore untuk memanipulasi keraguan Nadia.

### Bab 20
- **Baris 5 (`dulu`):** `Waktu Pak Ramdan memperkenalkan Saka di ruang rapat pada hari pertama dulu, Pak Ramdan memang sempat menyebut bahwa kami dipasangkan duduk semeja selama lima minggu...`
  - **Penilaian:** **LULUS.** Cocok dengan Bab 3 baris 47.
- **Baris 29 (`kemarin`):** `Dan kalimat Tari kemarin pagi soal formulir di meja Mbak Sinta HRD itu ternyata memang urusan kepulangan Saka ke kantor pusatnya di Yogyakarta.`
  - **Penilaian:** **TEMUAN (`ERROR` — `SETUP_PAYOFF` / `TIMELINE`).** Bab 20 berlangsung pada **Jumat siang** (dua hari setelah Rabu Bab 19). Padahal Tari menceritakan soal formulir HRD itu pada **Bab 18**, yaitu hari **Senin siang saat jam makan siang** (4 hari sebelumnya, bukan "kemarin pagi" / Kamis pagi)!

### Bab 21
- **Baris 25 (`ceritanya`, `dulu`):** `Aku teringat ceritanya di warung soto dulu: sejak ditinggal mantannya di Yogyakarta saat studionya bangkrut, Saka paling pantang mengumbar janji kepada perempuan sebelum ada kepastian resmi yang benar-benar sudah beres di tangannya.`
  - **Penilaian:** **TEMUAN (`ERROR` — `SETUP_PAYOFF` / `LOCATION_CONTINUITY`).** Kesalahan lokasi rujukan mundur! Saka menceritakan kisah studionya yang bangkrut dan putus dari mantannya di Yogyakarta pada **Bab 12** di **Kedai Kopi Kecil dekat Stasiun Cikini** (Senin petang saat hujan deras), **bukan** di Warung Soto Kwitang (Bab 9)!

### Bab 22
- **Baris 5 (`kemarin`):** `Mbak Raras sedang berada di Bandung bersama keluarganya sejak Jumat sore kemarin.`
  - **Penilaian:** **LULUS.** Bab 22 adalah Sabtu pagi; "Jumat sore kemarin" adalah sehari sebelumnya.
- **Baris 21 (`tadi pagi`), Baris 33 (`Tadi pagi`), Baris 57 (`tadi pagi`):** Mengacu pada Sabtu pagi pukul 06.30–09.30 saat Ibu menelepon dan Dimas datang ke Rawamangun.
  - **Penilaian:** **LULUS.**
- **Baris 45 (`Dulu`):** Mengacu pada masa pacaran Nadia–Dimas.
  - **Penilaian:** **LULUS.**
- **Baris 59 (`kemarin`):** `Di saat hatiku sedang perih dan hampa karena jawaban dingin Saka kemarin sore soal kepulangannya ke Yogyakarta...`
  - **Penilaian:** **LULUS.** Bab 22 adalah Sabtu siang; jawaban Saka terjadi Jumat sore (Bab 21).

### Bab 23
- **Baris 9 (`dulu`) & Baris 17 (`waktu itu`):** Mengacu pada sikap lama Dimas dan peristiwa putus di parkiran.
  - **Penilaian:** **LULUS.**
- **Baris 41 (`minggu lalu`):** `Tak ada ketegangan kaku seperti saat kami memperdebatkan permintaan Mbak Raras minggu lalu.`
  - **Penilaian:** **TEMUAN (`ERROR` — `SETUP_PAYOFF` / `TIMELINE`).** Bab 23 terjadi pada **Sabtu akhir Minggu ke-4**, sedangkan perdebatan permintaan Mbak Raras terjadi pada **Minggu–Senin awal Minggu ke-2** (Bab 10 & Bab 13), yaitu **dua hingga tiga minggu lalu**, bukan "minggu lalu"!

### Bab 24
- **Baris 45 (`kemarin`):** `"Sejak kemarin kamu ngomong kaku banget ke saya."`
  - **Penilaian:** **TEMUAN (`REVIEW` / `FIX BEFORE RELEASE` — `TIMELINE`).** Bab 24 berlangsung pada **Senin sore**, sedangkan Nadia mulai berbicara kaku kepada Saka pada **Jumat sore** (Bab 21), bukan hari Minggu ("kemarin").

### Bab 25
- **Baris 35 (`dulu`):** `Namun aku lupa cerita Saka di warung soto dulu. Saat studionya di Yogyakarta bangkrut, mantan kekasihnya meninggalkannya demi laki-laki pilihan orang tua yang dianggap lebih mapan dan sudah jelas di depan mata.`
  - **Penilaian:** **TEMUAN GANDA (`ERROR` & `HIGH` — `SETUP_PAYOFF` / `CONTINUITY`).**
    1. **Salah lokasi:** Cerita masa lalu Saka di Yogyakarta terjadi di **Kedai Kopi Cikini** (Bab 12), bukan di **warung soto** (bahkan kontradiktif dengan ucapan Saka sendiri di Bab 25 baris 21: *"Kamu sendiri yang bilang di kedai kopi..."*).
    2. **Klaim tanpa setup (tidak pernah ditanam):** Di Bab 12 baris 27, Saka hanya mengatakan *"Hubungan saya sama pacar di Jogja juga ikut bubar karena hidup saya berantakan."* Saka **sama sekali tidak pernah menceritakan** bahwa mantannya meninggalkannya *"demi laki-laki pilihan orang tua yang dianggap lebih mapan dan sudah jelas di depan mata"*. Detail krusial yang menopang reaksi dingin Saka di lobi ini muncul mendadak tanpa tanam!

### Bab 26
- **Baris 19 (`katanya`):** `"Ibu kamu tadi udah telepon aku lagi, katanya nggak sabar mau makan ikan bakar bareng kita malam ini."`
  - **Penilaian:** **LULUS.** Klaim lisan Dimas pada Selasa siang.
- **Baris 29 (`kemarin`):** `"Waktu Ibu sakit kemarin, dia yang ngurusin semuanya, Tar," belaku pelan.`
  - **Penilaian:** **TEMUAN (`REVIEW` / `FIX BEFORE RELEASE` — `TIMELINE`).** Bab 26 adalah **Selasa siang**, sedangkan Ibu sakit dan diantar ke klinik terjadi pada **Sabtu pagi/siang** (Bab 22, tiga hari sebelumnya, bukan "kemarin").
- **Baris 37 (`kemarin`) & Baris 39 (`kemarin`):** Mengacu pada kejadian di lobi kantor pada Senin sore (Bab 25).
  - **Penilaian:** **LULUS.** (Senin sore dirujuk pada Selasa siang sebagai "kemarin sore" / "kemarin").
- **Baris 43 (`dulu`):** Cerita masa kuliah Tari.
  - **Penilaian:** **LULUS.**
- **Baris 53 (`tiga minggu lalu`):** `Kertas post-it kuning bertuliskan Bilang enggak itu nggak bikin langit runtuh yang ditempelkan Saka tiga minggu lalu...`
  - **Penilaian:** **TEMUAN (`ERROR` — `TIMELINE`).** Bab 26 terjadi pada **Selasa Minggu ke-5** (tiga hari sebelum peluncuran buku pada Jumat akhir minggu ke-5), sedangkan *post-it* kuning ditempelkan Saka pada **Selasa Minggu ke-1** (Bab 4). Jarak dari Selasa Minggu 1 ke Selasa Minggu 5 adalah **empat minggu**, bukan "tiga minggu lalu"!

### Bab 27
- **Baris 13 (`dulu`) & Baris 47 (`dulu`):** Mengacu pada masa pacaran 2 tahun dan sifat gugup Nadia di masa lalu.
  - **Penilaian:** **LULUS.**

### Bab 28
- **Baris 17 (`dulu`), Baris 23 (`waktu itu`), Baris 41 (`dulu`):** Mengacu pada peristiwa putus di parkiran (Bab 1) dan menangis di tangga darurat (Bab 1).
  - **Penilaian:** **LULUS.**
- **Baris 57 (`kemarin`):** `"Semua biaya klinik, bubur, dan bensin kemarin biar ditransfer balik sama Nadia malam ini," lanjut Ibu tegas.`
  - **Penilaian:** **TEMUAN (`REVIEW` / `FIX BEFORE RELEASE` — `TIMELINE`).** Bab 28 berlangsung pada **Selasa malam**, sedangkan kejadian ke klinik terjadi pada **Sabtu siang** (Bab 22, tiga hari sebelumnya).

### Bab 29
- **Baris 5 (`Tadi pagi`):** Mengacu pada Rabu pagi saat Nadia berjalan dari Stasiun Cikini ke kantor. (**LULUS**)
- **Baris 7 (`kemarin`), Baris 23 (`kemarin`), Baris 27 (`kemarin`), Baris 29 (`kemarin`), Baris 33 (`Katanya`), Baris 39 (`Kemarin`), Baris 61 (`Tadi malam`):**
  - **Penilaian:** Bab 29 adalah **Rabu pagi**. Rujukan ke keberangkatan Saka dan berkas naik cetak pada Selasa sore ("kemarin sore") serta pengiriman pesan ke Tari pada Selasa malam ("tadi malam") **LULUS** secara kalender; hanya frasa baris 7 (*"bicara menyakitkan di lobi gedung"* yang terjadi Senin sore, bukan Selasa/"kemarin") yang sedikit menyatukan kejadian Senin sore dan Selasa.
- **Baris 63 (`dulu`):** `"Lo tenang dulu, Nad,"` (**LULUS**).

### Bab 30
- **Baris 9 (`dulu`):** `...memulai sesi diskusi lebih dulu sambil menunggu Saka menyusul.` (**LULUS**).
- **Baris 21 (`kemarin`):** `Sejak kemarin malam aku sudah berlatih bicara berkali-kali di depan cermin kamar...`
  - **Penilaian:** **LULUS.** Bab 30 adalah Jumat sore; "kemarin malam" adalah Kamis malam, dan rujukan *"Selasa malam lalu"* cocok dengan Bab 27.
- **Baris 27 (`Dulu`):** `"Dulu saya tipe orang yang punya penyakit nggak enakan kronis."` (**LULUS**).

### Bab 31
- **Baris 21 (`kemarin`):** `"Maaf buat sikapku kemarin, dan maaf buat omonganku di lobi."`
  - **Penilaian:** **TEMUAN (`REVIEW` / `FIX BEFORE RELEASE` — `TIMELINE`).** Bab 31 berlangsung pada **Jumat sore**, sedangkan mereka terakhir bertemu pada **Selasa siang** (Bab 26) dan pertengkaran di lobi terjadi pada **Senin sore** (Bab 25), bukan hari Kamis ("kemarin").
- **Baris 41 (`Waktu itu`):** Mengacu pada Senin sore di lobi (baris 39). (**LULUS**).
- **Baris 47 (`minggu lalu`):** `Itu amplop yang sama persis dengan yang kulihat di bawah buku catatannya hari Jumat minggu lalu.`
  - **Penilaian:** **LULUS.** Bab 31 adalah Jumat akhir Minggu 5; mengacu tepat pada Jumat akhir Minggu 4 (Bab 20).
- **Baris 51 (`tiga minggu yang lalu`, `kemarin`):** `...tanggal pengajuan permohonan dari Saka sejak tiga minggu yang lalu, dan tanda tangan pelepasan resmi Kepala Cabang Yogyakarta, Pak Bambang, tertanggal hari Kamis kemarin.`
  - **Penilaian:** Rujukan *"hari Kamis kemarin"* **LULUS** (sehari sebelum Jumat Bab 31). Namun *"sejak tiga minggu yang lalu"* menimbulkan masalah kausalitas dengan telepon Pak Ramdan di Bab 20 dan kalimat Saka di baris 65.
- **Baris 53 (`dulu`):** `Pantas saja dulu aku pernah memergoki layar laptopnya membuka daftar kos tahunan di Cikini dan Tari sempat melihatnya menyerahkan formulir ke Mbak Sinta HRD!`
  - **Penilaian:** Cocok dengan Bab 14 baris 18 dan Bab 18 baris 39, tetapi membuktikan bahwa di Bab 20 Nadia sempat melupakan petunjuk ini sama sekali (`CHARACTER_KNOWLEDGE`).
- **Baris 63 (`dulu`) & Baris 67 (`kemarin`):** `"harus ke Jogja dulu..."` | `"mengejar tanda tangan Pak Bambang kemarin siang..."` (**LULUS**).
- **Baris 75 (`Katanya`, `dulu`):** `"Katanya waktu minggu pertama dulu lebih suka suasana kerja di Jogja," kataku sambil menunjuk baris tanggal pengajuan di surat itu.`
  - **Penilaian:** **TEMUAN (`ERROR` — `SETUP_PAYOFF`).** Rujukan tanpa tanam! Di seluruh bab minggu pertama (Bab 1 s.d. Bab 9), Saka **tidak pernah sekalipun** mengatakan bahwa ia lebih suka suasana kerja di Yogyakarta.
- **Baris 79 (Rujukan lokasi implisit `soto ayam tanpa seledri di warung depan gedung kantor`):**
  - **Penilaian:** **TEMUAN (`ERROR` — `LOCATION_CONTINUITY` / `SETUP_PAYOFF`).** Adegan makan soto ayam tanpa seledri di Bab 9 terjadi di **Warung Soto Kwitang dekat Halte Senen**, **bukan** di warung depan gedung kantor Cikini!

### Bab 32
- **Baris 59 (`waktu itu`):** `"Ibu malah nanyain kapan editor Jogja yang di panggung waktu itu mau mampir ke rumah."`
  - **Penilaian:** **LULUS.** Mengacu pada acara peluncuran buku 3 hari sebelumnya di Bab 30 (di mana Ibu hadir di barisan depan).

---

## 4. Verifikasi Prosedur Dunia Nyata dengan Pencarian Web (`rules/18-real-world-procedures.md` & `rules/04-worldbuilding.md`)

Seluruh prosedur operasional dan fakta dunia nyata yang menopang plot/tenggat waktu cerita telah diverifikasi menggunakan pencarian web terhadap standar industri dan pedoman resmi di Indonesia:

| No. | Prosedur Dunia Nyata di Naskah | Klaim Urutan & Durasi di Naskah (`pre-fix`) | Standar Industri / Operasional Nyata & Sumber Verifikasi | Status Verifikasi & Klasifikasi |
|---|---|---|---|---|
| 1 | **Penerbitan, Percetakan Buku Massal, dan Distribusi Toko Buku** (Bab 15, 21, 24, 26, 30, 32) | 1. **Kamis sore Minggu 3 (Bab 15 baris 51):** Sampul baru disetujui, Pak Ramdan berkata *"langsung masuk tahap cetak percobaan"* padahal tata letak bab 6 & halaman akhir baru selesai Jumat Minggu 4.<br>2. **Jumat pukul 17.01 (Bab 21 baris 9):** Seluruh file akhir dikirim ke percetakan.<br>3. **Senin pukul 16.00 (Bab 24 baris 3):** 2 eksemplar *dummy* / cetak percobaan tiba.<br>4. **Selasa pukul 10.00–11.00 (Bab 26 baris 7–9):** Persetujuan naik cetak ditandatangani & diambil kurir.<br>5. **Jumat pagi (Bab 30 baris 5):** Buku *Sela Waktu* sudah selesai cetak massal dan terbit (**hanya 2,5 hari kerja** sejak *ACC* naik cetak!).<br>6. **Senin sore, 3 hari pasca-peluncuran (Bab 32 baris 3):** Buku sudah terpajang rapi di rak depan toko-toko buku kawasan Cikini dan Matraman (**total 4 hari kerja** sejak *ACC* cetak!). | - **Pembuatan *Dummy Proof* (Digital Printing):** 1–3 hari kerja (pengiriman file Jumat sore -> *dummy* Senin sore sesuai kenyataan).<br>- **Pra-cetak Offset (Pelat CTP) + Naik Cetak Massal + *Finishing* (Lipat, Jilid Lem Panas, Pengeringan, Laminasi Cover, Potong, QC):** Membutuhkan **3–7 hari kerja** di percetakan.<br>- **Distribusi Gudang Pusat (DC) & Alokasi PPIC ke Etalase Toko Buku Mayor (seperti Gramedia Matraman):** Membutuhkan tambahan **5–14 hari kerja (1–3 minggu)**.<br>- **Sumber Verifikasi Web:**<br>  1. Standar Waktu Produksi Cetak Buku Offset & *Dummy Proof* — Percetakan Diandra Creative (`percetakandiandra.co.id` / `diandracreative.com`) & Penerbit Deepublish (`penerbitdeepublish.com`).<br>  2. Proses Pra-Cetak CTP (*Computer to Plate*) & *Finishing* Percetakan — Meridian Grup (`meridiangrup.com`) & Noken Studio (`nokenstudio.com`).<br>  3. Alur Logistik Gudang Pusat (DC) dan PPIC Distribusi Toko Buku Mayor Indonesia — Studi Rantai Pasok Penerbit Mayor / Gramedia (`umn.ac.id`). | **TEMUAN (`DOMAIN_FACTUALITY` / `TIMELINE` — `HIGH` / `FIX BEFORE RELEASE`)**<br>Mustahil menyelesaikan cetak offset massal + penjilidan hanya dalam 2,5 hari kerja (Selasa siang s.d. Jumat pagi) dan mendistribusikannya ke rak depan jaringan toko buku Matraman & Cikini dalam 3 hari akhir pekan, kecuali dijelaskan di teks bahwa cetakan peluncuran adalah cetak digital terbatas (*POD*). |
| 2 | **Transportasi Kereta Api Antarkota Jakarta–Yogyakarta & Pesan Operator Seluler** (Bab 29, 30, 31) | 1. **Selasa petang pukul 17.30 / malam (Bab 29 baris 31 & 39):** Saka berangkat ke Yogyakarta naik kereta malam.<br>2. **Rabu pagi pukul 08.15–08.30 (Bab 29 baris 3 & 59):** Saat Nadia menelepon Saka, *"suara operator hanya menjawab bahwa nomor yang kutuju sedang berada di luar jangkauan sinyal kereta."*<br>3. **Jumat pagi–sore (Bab 30 baris 9):** Saka naik kereta pagi dari Yogyakarta ke Stasiun Gambir, tertahan sinyal 20 menit sebelum Jatinegara, perjalanan Gambir–Cikini ~10 menit, tiba di Cikini sebelum pukul 17.30. | - **Waktu Tempuh KA Jakarta (Gambir/Pasar Senen) – Yogyakarta (Tugu/Lempuyangan):** Berkisar antara **6 jam hingga 7 jam 30 menit** (misal KA Taksaka ~6 jam 10 menit; KA eksekutif/reguler malam berangkat pukul 19.00–21.30 tiba di Yogyakarta pukul **01.15–04.30 dini hari**).<br>- Kereta malam yang berangkat Selasa malam sudah tiba di Yogyakarta sebelum pukul 05.00 Rabu pagi; mustahil pada pukul 08.30 Rabu pagi Saka masih berada di dalam kereta.<br>- Selain itu, tidak ada pesan otomatis operator telekomunikasi seluler di Indonesia yang menyebutkan spesifikasi lokasi *"di luar jangkauan sinyal kereta"*.<br>- Untuk perjalanan Jumat pagi (Yogyakarta–Gambir ~6,5 jam + Gambir–Cikini ~10–15 menit), jadwal tiba sore hari sesuai kenyataan.<br>- **Sumber Verifikasi Web:**<br>  1. Jadwal dan Waktu Tempuh Resmi KA Gambir–Yogyakarta (Taksaka / Argo Dwipangga / Argo Lawu) — PT Kereta Api Indonesia / Tiket KAI (`tiketkai.com`, `traveloka.com`, `detik.com`). | **TEMUAN (`DOMAIN_FACTUALITY` / `TIMELINE` — `ERROR` / `FIX BEFORE RELEASE`)** pada Bab 29 baris 59 (kereta malam Selasa tidak mungkin masih di perjalanan pada Rabu pukul 08.30 pagi & bunyi pesan operator tidak faktual).<br>**TERVERIFIKASI LULUS** untuk kereta pagi Jumat di Bab 30. |
| 3 | **Geografi Jakarta & Operasional KRL Commuter Line Jabodetabek** (Bab 2, 10, 16, 17) | 1. **Bab 2 baris 33:** Saka berkata *"Kosan saya di belakang stasiun Cikini."*<br>2. **Bab 16 baris 23 & Bab 17 baris 19:** Dari kantor di Cikini, Nadia berkata *"Kos Mas Saka kan arahnya naik kereta ke selatan, bukan ke arah gang kosku"*, dan Saka berkata *"Tadi niatnya beli martabak telur buat makan di kereta."*<br>3. **Bab 10 baris 55:** Perjalanan KRL dari Rawamangun (Stasiun Jatinegara) menuju Stasiun Cikini. | - **Geografi Stasiun Cikini & Lin Bogor:** Jika kos Saka berada di belakang Stasiun Cikini dan kantornya di Cikini, ia cukup berjalan kaki ke kos tanpa perlu naik KRL ke arah selatan (Manggarai/Tebet/Depok/Bogor).<br>- **Aturan KRL Commuter Line:** PT KAI Commuter memberlakukan larangan makan dan minum di dalam gerbong KRL Commuter Line Jabodetabek.<br>- **Rute KRL Jatinegara – Cikini:** Dilayani oleh Lin Cikarang (Jatinegara -> Matraman -> Manggarai ~5 menit) lalu transit peron ke Lin Bogor menuju Stasiun Cikini (1 stasiun dari Manggarai).<br>- **Sumber Verifikasi Web:**<br>  1. Peta Rute dan Panduan Transit KRL Lin Cikarang & Lin Bogor (Jatinegara–Manggarai–Cikini) — KAI Commuter (`keretaapikita.com`, `kabarpenumpang.com`). | **TEMUAN (`LOCATION_CONTINUITY` / `DOMAIN_FACTUALITY` — `ERROR` / `FIX BEFORE RELEASE`)** pada Bab 2 vs Bab 16–17 (kontradiksi lokasi kos Saka di belakang Stasiun Cikini vs naik kereta ke selatan).<br>**TERVERIFIKASI LULUS** untuk rute KRL Jatinegara–Cikini di Bab 10. |
| 4 | **Prosedur Medis Penanganan Vertigo Akut di Klinik Pratama** (Bab 22) | Ibu mengalami vertigo akut sejak subuh (kepala berputar saat duduk, wajah pucat), dibawa ke Klinik Pratama Rawamangun pukul 09.30 dengan kursi roda, registrasi, ruang observasi redup, injeksi obat pereda pusing/mual, menunggu obat di apotek (total ~3 jam sampai pukul 13.00), lalu istirahat di rumah dan membaik pukul 17.00. | - Sesuai **Panduan Praktik Klinis (PPK) Bagi Dokter di Fasilitas Pelayanan Kesehatan Tingkat Pertama (FKTP) IDI** dan panduan **PERDOSSI**, vertigo vestibular perifer akut tanpa tanda bahaya neurologis fokal (*red flags* vertigo sentral) ditangani di layanan primer dengan: pemberian terapi simtomatik injeksi (dimenhidrinat atau metoklopramid IM/IV), observasi di ruang tenang/redup selama 1–3 jam hingga gejala otonom mereda, dilanjutkan obat oral rawat jalan (betahistin/antihistamin) dan istirahat.<br>- **Sumber Verifikasi Web:**<br>  1. Panduan Praktik Klinis (PPK) Layanan Primer IDI & PERDOSSI — Tatalaksana Vertigo Akut (`alomedika.com`, `rspon.go.id`, `usu.ac.id`). | **TERVERIFIKASI LULUS** |
| 5 | **Administrasi Kepegawaian / HRD Mutasi Tetap Antar-Cabang** (Bab 3, 14, 18, 20, 31) | Saka editor senior dari Yogyakarta ditugaskan 5 minggu di Jakarta; mengajukan formulir kepegawaian antar-cabang ke HRD (Bab 14, 18); membutuhkan tanda tangan pelepasan Kepala Cabang Yogyakarta (Pak Bambang) untuk SK Mutasi Tetap (Bab 20, 31). Namun di Bab 20 baris 29 & 37 serta Bab 31 baris 47 & 51, Yogyakarta disebut sebagai *"Cabang Yogyakarta"* sekaligus *"Kantor Pusat Yogyakarta"* (*"Kantor Pusat Penerbit Aksara Senja Cabang Yogyakarta"*). | - Secara administrasi SDM korporat, mutasi tetap antar-cabang memang memerlukan pengajuan ke HRD, persetujuan pimpinan unit penerima, dan surat pelepasan (*release letter*) dari pimpinan unit asal.<br>- Namun secara struktur korporasi, satu entitas di Yogyakarta tidak mungkin berstatus **Kantor Pusat** sekaligus **Cabang** secara bersamaan pada kop surat yang sama (*"Kantor Pusat Penerbit Aksara Senja Cabang Yogyakarta"*). | **TEMUAN (`NAME_TERM_CONSISTENCY` / `DOMAIN_FACTUALITY` — `ERROR` / `FIX BEFORE RELEASE`)** pada kop surat dan status kantor Yogyakarta vs Jakarta di Bab 20 & Bab 31. |

---

## 5. Daftar Lengkap Temuan Editorial Beserta Severity dan Saran Perbaikan Spesifik

### Ringkasan Jumlah Temuan berdasarkan Severity
- **ERROR:** 16 temuan
- **HIGH:** 6 temuan
- **REVIEW:** 5 temuan
- **INFO:** 1 temuan

---

### A. Temuan `HIGH` dan `ERROR` yang Berdampak `BLOCKER`

#### [F-01] `HIGH` | `CAUSALITY` / `MOTIVATION` | Release Impact: `BLOCKER` | Confidence: `HIGH`
- **Lokasi:** Lintas bab paruh kedua (`chapters/bab-10.md` baris 17; `chapters/bab-21.md` baris 25–53; `chapters/bab-23.md` baris 37–55; `chapters/bab-25.md` baris 15–58; `chapters/bab-27.md` baris 17; `chapters/bab-29.md` baris 57–65)
- **Bukti Kutipan:**
  - `bab-10.md:17`: *"Setiap kali Ibu menyebut nama Dimas dengan mata berbinar karena menganggap mantan pacarku itu laki-laki paling sopan dan ramah sedunia, lidahku langsung kelu tidak tega merusak suasana hatinya."*
  - `bab-21.md:37`: *"Apalagi penyakit nggak enakanku langsung ikut berbisik di kepalaku: memangnya aku ini siapanya Saka sampai berhak menuntut penjelasan atau menahannya tetap tinggal di Jakarta?"*
  - `bab-25.md:31-33`: *"Di dalam lubuk hatiku yang paling dalam, sebenarnya ada alasan bodoh kenapa aku mengucapkan kalimat itu di depan wajahnya. Aku ingin melihat apakah wajah tenang itu akan goyah. Aku ingin mendengar dia melarangku. Satu kalimat saja darinya, aku akan menolak Dimas."*
  - `bab-27.md:17`: *"Aku sudah menundukkan dagu sedikit, bersiap menganggukkan kepalaku untuk menjawab iya."*
- **Masalah Spesifik:**
  1. Konflik utama paruh kedua novel bertahan selama 11 bab (Bab 19–29) semata-mata karena tokoh menahan komunikasi sederhana sebanyak **7 kali** (tidak memberi tahu Ibu bahwa sudah putus di Bab 10 & 23, Saka tidak menyebut bahwa surat yang diurus ke Yogyakarta adalah surat pelepasan mutasi tetap di Bab 14, 21, 25, dan Nadia memutus percakapan di Bab 21, 24, 25, 29).
  2. Sesuai `rules/01-plot-and-causality.md` §2, alasan penahanan komunikasi tersebut hanya mengandalkan label sifat abstrak (*"tidak tega merusak suasana"*, *"penyakit nggak enakanku"*, *"rasa malu"*, *"gengsi"*) tanpa hambatan eksternal atau biaya konkret di dalam adegan.
  3. Terjadi regresi karakter ekstrem pada Nadia di Bab 25–27: setelah berhasil menolak Mbak Raras dan Ibunya di Bab 13, Nadia justru pasrah menyetujui makan malam peresmian balikan dan hampir mengangguk menerima Dimas di Bab 27 baris 17, lalu hanya tersadar karena kebetulan pelayan salah mengantar es jeruk yang memicu Dimas membuka topengnya sendiri.
- **Dampak bagi Pembaca:** Pembaca merasakan konflik paruh kedua sebagai kesalahpahaman buatan (*artificial miscommunication*) yang merusak perkembangan karakter Nadia yang sudah dibangun dengan meyakinkan di Bab 1–18.
- **Keputusan Editorial (`MANUSCRIPT ERROR` & `OUTLINE ERROR`):**
  - **Saran Perbaikan Minimal:**
    1. Pada **Bab 10 baris 17**, berikan pemicu konkret di halaman mengapa Nadia menunda memberi tahu Ibu (misalnya Ibu baru saja mengeluh pusing/tekanan darah naik saat menyiapkan makan siang sehingga Nadia menahan kabar buruk).
    2. Pada **Bab 20–21**, berikan alasan konkret dan masuk akal mengapa mutasi Saka belum pasti (misalnya posisi tetap di Jakarta sedang dibekukan sementara oleh direksi pusat atau kepala cabang Yogyakarta menahan pelepasan Saka karena kekurangan editor senior, sehingga Saka memang benar-benar belum tahu apakah permohonannya akan disetujui, bukan sekadar menahan informasi yang sudah pasti).
    3. Pada **Bab 25–27**, ubah motivasi Nadia menghadiri makan malam di Bab 27: jangan buat Nadia "hampir mengangguk menjawab iya" karena pasrah, melainkan datang karena Ibu telanjur mengundang Dimas sebagai ucapan terima kasih atas bantuan klinik, di mana Nadia sejak awal masih ragu/menjaga batas dan kesombongan Dimas soal panggung peluncuran memantapkan Nadia untuk membongkar seluruh kebenaran di depan Ibu.

---

#### [F-02] `HIGH` | `CHARACTER_KNOWLEDGE` / `CAUSALITY` | Release Impact: `BLOCKER` | Confidence: `HIGH`
- **Lokasi:** `chapters/bab-14.md` baris 17–21, `chapters/bab-18.md` baris 39–43, `chapters/bab-20.md` baris 19–38, dan `chapters/bab-31.md` baris 51–59
- **Bukti Kutipan:**
  - `bab-14.md:17-18`: *"...mataku tidak sengaja menangkap tab di sudut atas layarnya yang bertuliskan daftar sewa kamar kos tahunan daerah Cikini dan formulir kepegawaian antar-cabang."*
  - `bab-18.md:39`: *"Kemarin waktu antar berkas personalia, gue lihat Mas Saka nyerahin map formulir ke Mbak Sinta HRD."*
  - `bab-20.md:19-23`: *"Soal Saka, masa perbantuannya di Jakarta memang lima minggu sampai proyek beres," lanjut Pak Ramdan. ... "Nanti biar Saka sendiri yang pulang ke Yogyakarta minta tanda tangan Pak Bambang."*
  - `bab-20.md:29`: *"Jadi Dimas tidak mengarang cerita. Surat tugas Saka di gedung Cikini ini memang hanya berlaku lima minggu."*
  - `bab-31.md:57`: *"Pak Ramdan nawarin posisi tetap pegang lini buku ilustrasi baru sejak awal proyek," jelas Saka tenang seraya tersenyum tipis.*
- **Masalah Spesifik:**
  1. **Pengabaian Petunjuk oleh Tokoh POV (`rules/05-character-knowledge.md`):** Di Bab 14, Nadia melihat langsung tab *daftar sewa kamar kos tahunan Cikini* dan *formulir kepegawaian antar-cabang* di laptop Saka. Namun di Bab 20, saat menyimpulkan Saka akan pulang ke Yogyakarta, Nadia **sama sekali tidak mengingat atau menanggapi petunjuk tersebut di halaman** (seolah-olah Bab 14 tidak pernah terjadi), lalu baru tiba-tiba mengingatnya kembali di Bab 31 baris 53!
  2. **Kontradiksi Pengetahuan Pak Ramdan (Bab 20 vs Bab 31):** Di Bab 31 baris 51 & 57, diungkap bahwa **Pak Ramdan sendiri** yang menawari Saka posisi tetap di Jakarta sejak awal proyek dan Saka sudah mengajukan permohonan mutasi itu sejak 3 minggu lalu. Namun di Bab 20 baris 19–23, Pak Ramdan berbicara di telepon dengan Pak Bambang seolah-olah masa tugas Saka di Jakarta habis minggu depan dan Saka hanya pulang ke Yogyakarta, tanpa menyinggung mutasi tetap sama sekali.
  3. **Kontradiksi Keputusan Saka di Bab 31 baris 65:** Di Bab 31 baris 65, Saka berkata: *"Begitu baca pesan dari Tari kalau kamu nolak Dimas, saya langsung beresin kos lama. Saya kejar tanda tangan Pak Bambang kemarin siang..."* Kalimat ini mengesankan Saka baru memutuskan membereskan kos lama dan mengejar tanda tangan mutasi *setelah* membaca pesan Tari di hari Rabu, padahal ia sudah mengajukan mutasi tetap 3 minggu sebelumnya dan berangkat ke Jogja Selasa sore memang untuk urusan tersebut!
- **Dampak bagi Pembaca:** Pembaca yang teliti akan menyadari bahwa kesalahpahaman di Bab 20–21 hanya bisa terjadi karena penulis membuat Nadia lupa pada apa yang dilihatnya di Bab 14 dan membuat Pak Ramdan berbicara secara menyesatkan di telepon.
- **Keputusan Editorial (`MANUSCRIPT ERROR`):**
  - **Saran Perbaikan Minimal:**
    - Di `chapters/bab-20.md` baris 23 & 29: Sesuaikan kalimat telepon Pak Ramdan agar merujuk pada proses administrasi pelepasan cabang (*"Soal status Saka selanjutnya, akhir minggu depan masa tugas perbantuannya memang habis, jadi biar Saka sendiri yang menghadap Pak Bambang di Yogyakarta untuk membereskan surat pelepasannya"*), dan tambahkan respons batin Nadia yang mengingat tab kos tahunan Cikini serta formulir HRD namun salah menafsirkannya (misalnya mengira formulir kepegawaian antar-cabang itu adalah formulir pengembalian pegawai ke cabang asal, sedangkan kos tahunan memang untuk teman Saka).
    - Di `chapters/bab-31.md` baris 65–67: Ubah kalimat Saka agar menegaskan bahwa keputusannya pindah ke Jakarta sudah bulat sejak 3 minggu lalu dan kepergiannya Selasa sore memang untuk mengambil tanda tangan Pak Bambang serta membereskan kos lama, sedangkan pesan Tari membuat hatinya tenang saat mengejar kereta pagi.

---

#### [F-03] `HIGH` | `SETUP_PAYOFF` / `CONTINUITY` | Release Impact: `BLOCKER` | Confidence: `HIGH`
- **Lokasi:** `chapters/bab-12.md` baris 27 vs `chapters/bab-21.md` baris 25 & `chapters/bab-25.md` baris 35
- **Bukti Kutipan:**
  - `bab-12.md:27` (Lokasi: Kedai Kopi dekat Stasiun Cikini): *"Sampai akhirnya tabungan saya habis dan studio tutup," lanjut Saka dengan tatapan lurus. "Teman saya lepas tangan begitu saja. Hubungan saya sama pacar di Jogja juga ikut bubar karena hidup saya berantakan."*
  - `bab-21.md:25`: *"Aku teringat ceritanya di warung soto dulu: sejak ditinggal mantannya di Yogyakarta saat studionya bangkrut, Saka paling pantang mengumbar janji kepada perempuan sebelum ada kepastian resmi yang benar-benar sudah beres di tangannya."*
  - `bab-25.md:35`: *"Namun aku lupa cerita Saka di warung soto dulu. Saat studionya di Yogyakarta bangkrut, mantan kekasihnya meninggalkannya demi laki-laki pilihan orang tua yang dianggap lebih mapan dan sudah jelas di depan mata."*
- **Masalah Spesifik:**
  1. **Kesalahan Lokasi Rujukan Mundur (`ERROR`):** Baik di Bab 21 baris 25 maupun Bab 25 baris 35, Nadia merujuk cerita masa lalu Saka di Yogyakarta sebagai cerita *"di warung soto dulu"*. Padahal di Warung Soto Kwitang (Bab 9) Saka hanya membahas seledri dan karikatur buku sketsa; cerita masa lalu Yogyakarta disampaikan di **Kedai Kopi Kecil dekat Stasiun Cikini** pada Bab 12! (Bahkan di Bab 25 baris 21 Saka sendiri menyebut *"di kedai kopi"*).
  2. **Rujukan Tanpa Tanam untuk Pemicu Klimaks (`HIGH`):** Di Bab 25 baris 35, reaksi dingin Saka yang mendorong Nadia menerima ajakan makan malam Dimas ditopang oleh klaim bahwa mantan kekasih Saka di Yogyakarta *"meninggalkannya demi laki-laki pilihan orang tua yang dianggap lebih mapan dan sudah jelas di depan mata"*. Fakta ini **tidak pernah ada di Bab 12** maupun di `outline.md` Bab 12 versi `pre-fix`!
- **Dampak bagi Pembaca:** Pembaca bingung karena lokasi adegan kunci tertukar (kedai kopi vs warung soto) dan merasa alasan psikologis Saka di Bab 25 dikarang mendadak tanpa pernah diceritakan sebelumnya.
- **Keputusan Editorial (`MANUSCRIPT ERROR` & `OUTLINE ERROR`):**
  - **Saran Perbaikan Minimal:**
    - Di `chapters/bab-12.md` baris 27 (dan `outline.md` Bab 12), tanamkan kalimat eksplisit: *"Hubungan saya sama pacar di Jogja juga ikut bubar karena hidup saya berantakan. Dia akhirnya memilih laki-laki yang direstui orang tuanya karena pekerjaannya sudah jelas dan dianggap lebih mapan."*
    - Di `chapters/bab-21.md` baris 25 dan `chapters/bab-25.md` baris 35, ganti frasa *"di warung soto dulu"* menjadi *"di kedai kopi dulu"*.

---

#### [F-04] `ERROR` | `PLOT_HOLE` / `CAUSALITY` | Release Impact: `BLOCKER` | Confidence: `HIGH`
- **Lokasi:** `chapters/bab-21.md` baris 5 & 9 vs `chapters/bab-24.md` baris 25–39
- **Bukti Kutipan:**
  - `bab-21.md:5`: *"Namun di tengah kesibukanku merapikan halaman terakhir buku Sela Waktu, tanganku sempat membuat satu gambar kecil tambahan di lembar penutup: sketsa dua meja kerja yang bersebelahan, di mana satu kursinya kosong dan hanya menyisakan bayangan sebuah botol minum hitam."*
  - `bab-21.md:9`: *"Seluruh file akhir Sela Waktu sudah saya kirim ke percetakan rekanan barusan," kata Saka sambil mencabut kabel laptopnya.*
  - `bab-24.md:29`: *"Aku baru ingat bahwa pada Jumat sore lalu, sebelum mengirimkan file terakhir ke percetakan dan sebelum bertanya soal kepulangan Saka ke Jogja, aku sempat menyelipkan satu sketsa kecil tambahan di bagian tengah halaman penutup buku itu."*
  - `bab-24.md:39`: *"Gambar kursi kosong di halaman terakhir ini... kamu bikin waktu saya turun ke lantai dua?"*
- **Masalah Spesifik:**
  - Di Bab 21 baris 9, **Saka sendiri** yang mengirimkan seluruh file akhir buku *Sela Waktu* ke percetakan dari laptopnya pada pukul 17.01 (sebelum Nadia bertanya soal kepulangan Saka dan sebelum Saka pulang).
  - Namun di Bab 24 baris 29, narasi menyatakan **Nadia** yang mengirimkan file terakhir itu ke percetakan, dan Saka baru pertama kali melihat gambar kursi kosong itu saat memeriksa buku cetak percobaan (*dummy*) pada hari Senin! Jika Saka yang mengirim file akhir di Bab 21 setelah memeriksa margin halaman terakhir bersama Nadia sepanjang sore, tidak masuk akal Saka tidak melihat ilustrasi di tengah halaman penutup itu atau Nadia yang mengklaim mengirimkannya.
- **Dampak bagi Pembaca:** Alur pengiriman naskah dan kejutan penemuan ilustrasi kursi kosong di Bab 24 menjadi kontradiktif secara logika adegan.
- **Keputusan Editorial (`MANUSCRIPT ERROR`):**
  - **Saran Perbaikan Minimal:**
    - Di `chapters/bab-21.md` baris 9: Ubah dialog Saka menjadi *"Semua file akhir Sela Waktu kecuali halaman penutup sudah saya kirim ke percetakan rekanan barusan, yang itu kamu kirim terakhir ya."*
    - Di `chapters/bab-24.md` baris 29: Ubah menjadi *"...aku sempat menyelipkan satu sketsa kecil tambahan di bagian tengah halaman penutup buku itu sebelum mengirimkan file terakhir tersebut ke percetakan setelah Saka pulang."*

---

### B. Temuan `ERROR` dan `HIGH` Kategori `FIX BEFORE RELEASE`

#### [F-05] `ERROR` | `PLOT_HOLE` / `TIMELINE` | Release Impact: `FIX BEFORE RELEASE` | Confidence: `HIGH`
- **Lokasi:** `chapters/bab-02.md` baris 49–53, `chapters/bab-03.md` baris 29, dan `chapters/bab-07.md` baris 31
- **Bukti Kutipan:**
  - `bab-02.md:49-53`: *"Layar monitorku masih menyala, map Mbak Dinda masih tergeletak bisu, dan kertas coretan Dimas masih menatapku dengan angkuh. Bodo amat. Malam ini aku tidak peduli lagi. Aku menyambar tas selempangku dari laci, mematikan sakelar monitor dengan sekali tekan, lalu melesat kabur menuju lobi bawah..."*
  - `bab-03.md:29` (Selasa pagi): *"Makasih posternya ya, Nad! Bagus banget, Vanya suka warnanya," katanya santai tanpa dosa.*
  - `bab-07.md:31`: *"File mentahnya sudah kuunggah ke folder bersama divisi pemasaran dari Senin malam, Mas," tanggapku tenang...*
- **Masalah Spesifik:** Pada Senin malam (Bab 1 baris 11 & Bab 2 baris 49–53), draf poster titipan Dimas belum dikerjakan dan Nadia langsung mematikan komputer lalu kabur pulang karena malu dipergoki Saka. Namun pada Selasa pagi (Bab 3 baris 29), poster itu tahu-tahu sudah selesai, dan di Bab 7 baris 31 Nadia mengklaim telah mengunggah file mentahnya ke folder divisi pemasaran *"dari Senin malam"*.
- **Dampak bagi Pembaca:** Pembaca bingung kapan Nadia mengerjakan dan mengunggah poster Dimas jika pada akhir Bab 2 ia meninggalkan kantor tanpa mengerjakannya.
- **Keputusan Editorial (`MANUSCRIPT ERROR`):**
  - **Saran Perbaikan Minimal:**
    - Di `chapters/bab-03.md` baris 5: Tambahkan satu kalimat jembatan bahwa karena tidak bisa tidur semalaman di kos, dini hari Selasa Nadia akhirnya membuka laptop dan menyelesaikan poster titipan Dimas.
    - Di `chapters/bab-07.md` baris 31: Ubah *"dari Senin malam"* menjadi *"dari Selasa pagi"*.

---

#### [F-06] `ERROR` | `LOCATION_CONTINUITY` / `DOMAIN_FACTUALITY` | Release Impact: `FIX BEFORE RELEASE` | Confidence: `HIGH`
- **Lokasi:** `chapters/bab-02.md` baris 33 vs `chapters/bab-16.md` baris 23 & `chapters/bab-17.md` baris 19
- **Bukti Kutipan:**
  - `bab-02.md:33`: *"Saya baru pindah ke Jakarta kemarin lusa. Kosan saya di belakang stasiun Cikini pompanya lagi dibongkar sampai jam delapan malam. Daripada nunggu di kafe berisik atau kena desak-desakan KRL jam pulang kantor, di sini lebih tenang."*
  - `bab-16.md:23`: *"Terus Mas Saka gimana? Kos Mas Saka kan arahnya naik kereta ke selatan, bukan ke arah gang kosku."*
  - `bab-17.md:19`: *"Tadi niatnya beli martabak telur buat makan di kereta," kata Saka dengan wajah lempeng.*
- **Masalah Spesifik:**
  1. Kontradiksi langsung lokasi kos Saka: Di Bab 2 baris 33, Saka menyatakan kosnya berada **di belakang Stasiun Cikini** (tidak perlu naik KRL dari kantor di Cikini, sehingga alasan menghindari "desak-desakan KRL jam pulang kantor" di Bab 2 baris 33 juga tidak logis jika kantornya di Cikini dan kosnya di belakang Stasiun Cikini!). Sebaliknya, di Bab 16 baris 23 dan Bab 17 baris 19, kos Saka disebut harus ditempuh dengan **naik kereta (KRL) ke arah selatan** dari Stasiun Cikini.
  2. Di Bab 17 baris 19, alasan Saka membeli martabak telur *"buat makan di kereta"* juga bertentangan dengan aturan operasional KRL Commuter Line yang melarang penumpang makan dan minum di dalam kereta.
- **Dampak bagi Pembaca:** Pembaca yang mengenal geografi Cikini dan KRL langsung mendeteksi kontradiksi lokasi tempat tinggal Saka.
- **Keputusan Editorial (`MANUSCRIPT ERROR`):**
  - **Saran Perbaikan Minimal:**
    - Di `chapters/bab-02.md` baris 33: Ubah *"Kosan saya di belakang stasiun Cikini"* menjadi lokasi di jalur KRL selatan dari Cikini, misalnya *"Kosan saya di Tebet"*.
    - Di `chapters/bab-17.md` baris 19: Ubah *"buat makan di kereta"* menjadi *"buat makan malam di kos"*.

---

#### [F-07] `ERROR` | `CONTINUITY` / `PLOT_HOLE` | Release Impact: `FIX BEFORE RELEASE` | Confidence: `HIGH`
- **Lokasi:** `chapters/bab-10.md` baris 23 & 27 vs `chapters/bab-13.md` baris 57
- **Bukti Kutipan:**
  - `bab-10.md:23-27`: *"Mbak sama Mas Hendra rencananya mau ajak Daffa liburan empat hari ke Bali." ... "Iya, makanya Mbak udah pesan tiket pesawat dari kemarin," lanjut Mbak Raras santai. "Cuma uang hotel sama sewa mobil di sana masih kurang empat juta nih, Nad."*
  - `bab-13.md:57`: *Ibu terdiam sejenak. "Biar Mbakmu liburan ke Puncak aja sesuai uang yang ada. Uang jajan Daffa terserah kamu transfer kapan."*
- **Masalah Spesifik:** Di Bab 10 baris 27, Mbak Raras sudah membeli tiket pesawat ke Bali dan hanya kekurangan biaya hotel serta sewa mobil. Namun di Bab 13 baris 57, ketika Nadia menolak meminjamkan Rp4 juta, Ibu berkata *"Biar Mbakmu liburan ke Puncak aja sesuai uang yang ada"*, seolah-olah tiket pesawat ke Bali belum dibeli.
- **Dampak bagi Pembaca:** Merusak konsistensi fakta dalam subplot keluarga Nadia.
- **Keputusan Editorial (`MANUSCRIPT ERROR`):**
  - **Saran Perbaikan Minimal:** Di `chapters/bab-13.md` baris 57, ubah kalimat Ibu menjadi: *"Biar Mbakmu cari penginapan yang lebih murah di Bali aja sesuai uang yang ada."*

---

#### [F-08] `HIGH` | `DOMAIN_FACTUALITY` / `TIMELINE` | Release Impact: `FIX BEFORE RELEASE` | Confidence: `HIGH`
- **Lokasi:** `chapters/bab-15.md` baris 51, `chapters/bab-21.md` baris 9, `chapters/bab-26.md` baris 7–9, `chapters/bab-30.md` baris 5, dan `chapters/bab-32.md` baris 3
- **Bukti Kutipan:**
  - `bab-15.md:51` (Kamis Minggu 3): *"Jadwal berikutnya langsung masuk tahap cetak percobaan."*
  - `bab-21.md:9` (Jumat Minggu 4 pukul 17.01): *"Seluruh file akhir Sela Waktu sudah saya kirim ke percetakan rekanan barusan. Senin sore cetak percobaan dikirim ke sini buat kita periksa. Jumat depan langsung acara peluncuran di toko buku Cikini."*
  - `bab-26.md:7-9` (Selasa Minggu 5 pukul 10.00): *"Saat menyerahkan lembar persetujuan naik cetak untuk kutandatangani pukul sepuluh pagi... Jam sebelas kurir percetakannya ambil ke sini."*
  - `bab-30.md:5` (Jumat Minggu 5): *"...memegang satu eksemplar buku Sela Waktu yang baru saja terbit pagi ini."*
  - `bab-32.md:3` (Senin Minggu 6, tiga hari setelah peluncuran): *"Tiga hari setelah acara peluncuran buku Sela Waktu yang kini sudah terpajang rapi di rak depan toko-toko buku kawasan Cikini dan Matraman..."*
- **Masalah Spesifik:**
  1. Di Bab 15 baris 51 (Kamis Minggu 3), Pak Ramdan mengatakan setelah sampul disetujui jadwal berikutnya *"langsung masuk tahap cetak percobaan"*, padahal tata letak bab 6, halaman pengantar, dan ucapan terima kasih baru diselesaikan di Bab 18–21 (Minggu 4).
  2. Sebagaimana diverifikasi melalui standar industri percetakan Indonesia (Bagian 4 laporan ini), rentang waktu **2,5 hari kerja** dari penandatanganan persetujuan naik cetak (*Selasa pukul 11.00*) hingga buku selesai dicetak massal untuk peluncuran (*Jumat pagi*), serta **3 hari akhir pekan** hingga terpajang di rak depan toko-toko buku Cikini dan Matraman (*Senin sore*), tidak realistis secara operasional untuk cetak offset massal dan alur distribusi toko buku mayor.
- **Dampak bagi Pembaca:** Jadwal produksi buku yang menjadi tulang punggung *timeline* 5 minggu terasa mustahil bagi pembaca yang memahami alur penerbitan.
- **Keputusan Editorial (`MANUSCRIPT ERROR`):**
  - **Saran Perbaikan Minimal:**
    - Di `chapters/bab-15.md` baris 51: Ubah *"tahap cetak percobaan"* menjadi *"tahap finalisasi tata letak"*.
    - Di `chapters/bab-21.md` baris 9 & `chapters/bab-26.md` baris 7: Jelaskan bahwa untuk mengejar acara peluncuran hari Jumat, percetakan mencetak *edisi peluncuran secara digital (POD) dalam jumlah terbatas*, sedangkan cetak offset massal dan distribusi reguler menyusul.
    - Di `chapters/bab-32.md` baris 3: Ubah *"kini sudah terpajang rapi di rak depan toko-toko buku kawasan Cikini dan Matraman"* menjadi *"kini edisi cetakan awalnya sudah mulai dipajang di etalase toko buku tempat peluncuran di Cikini sementara cetakan massalnya sedang didistribusikan"*.

---

#### [F-09] `ERROR` | `DOMAIN_FACTUALITY` / `TIMELINE` | Release Impact: `FIX BEFORE RELEASE` | Confidence: `HIGH`
- **Lokasi:** `chapters/bab-29.md` baris 31, 39, dan 59
- **Bukti Kutipan:**
  - `bab-29.md:31`: *"Mas Saka izin balik ke Jogja naik kereta malam buat ngurus berkas kantor."*
  - `bab-29.md:39`: *"Kemarin sore jam setengah enam."*
  - `bab-29.md:59` (Rabu pagi pukul 08.15–08.30): *"Aku buru-buru merogoh ponsel dari dalam tasku dan menekan nomor telepon Saka, namun suara operator hanya menjawab bahwa nomor yang kutuju sedang berada di luar jangkauan sinyal kereta."*
- **Masalah Spesifik:**
  1. Berdasarkan jadwal resmi PT KAI (waktu tempuh Jakarta–Yogyakarta 6 s.d. 7,5 jam), kereta malam yang berangkat dari Jakarta pada Selasa malam tiba di Stasiun Tugu Yogyakarta antara pukul **00.30 hingga 05.00 dini hari Rabu**. Mustahil pada pukul 08.30 Rabu pagi Saka masih berada di dalam perjalanan kereta api.
  2. Pesan suara operator telekomunikasi seluler tidak pernah menyebutkan frasa *"di luar jangkauan sinyal kereta"* (melainkan *"nomor yang Anda tuju sedang tidak aktif atau berada di luar jangkauan"*).
- **Dampak bagi Pembaca:** Merusak kredibilitas fakta dunia nyata pada adegan klimaks emosional Bab 29.
- **Keputusan Editorial (`MANUSCRIPT ERROR`):**
  - **Saran Perbaikan Minimal:** Di `chapters/bab-29.md` baris 31 & 59, ubah keterangan Riko menjadi *"naik kereta pagi subuh tadi"* (sehingga pukul 08.30 pagi kereta memang sedang melintas di jalur selatan Jawa Tengah yang susah sinyal), dan ubah baris 59 menjadi *"namun suara operator hanya menjawab bahwa nomor yang kutuju sedang berada di luar jangkauan"*.

---

#### [F-10] `ERROR` | `SETUP_PAYOFF` / `TIMELINE` | Release Impact: `FIX BEFORE RELEASE` | Confidence: `HIGH`
- **Lokasi:** Enam rujukan mundur waktu relatif & fakta yang keliru di `chapters/bab-06.md`, `bab-08.md`, `bab-18.md`, `bab-19.md`, `bab-20.md`, `bab-23.md`, `bab-26.md`, dan `bab-31.md`
- **Bukti Kutipan & Masalah Spesifik:**
  1. `bab-06.md:55`: *"Berbeda dengan kejadian kemarin saat menghadapi Mbak Dinda..."* — Bab 6 adalah Jumat sore; kejadian menghadapi Mbak Dinda terjadi pada **Selasa sore** (Bab 4), bukan Kamis ("kemarin").
  2. `bab-08.md:35`: *"Kemarin Dimas bilang gaya kayak gini kusam dan kurang komersial."* — Bab 8 adalah Sabtu Minggu 1; pada hari Jumat (Bab 6–7) Dimas **tidak pernah** mengatakan hal tersebut.
  3. `bab-18.md:11, 29, 39`: Tiga penggunaan kata *"Kemarin"* pada hari **Senin pagi/siang** untuk merujuk kejadian hari **Kamis sore/malam** (Bab 16–17: tidak suka makanan manis & memayungi Nadia) dan **Jumat** (mengantar berkas personalia ke HRD).
  4. `bab-19.md:5 vs 39`: Baris 5 menyebut Dimas dan Vanya baru bubar gara-gara tugas pameran *akhir pekan lalu* (3–4 hari sebelum Rabu Bab 19), tetapi baris 39 Dimas berkata *"Seminggu ini setelah Vanya pergi..."*.
  5. `bab-20.md:29`: *"Dan kalimat Tari kemarin pagi soal formulir di meja Mbak Sinta HRD..."* — Bab 20 adalah **Jumat siang**, sedangkan Tari mengatakannya pada **Senin siang** (Bab 18), bukan Kamis pagi ("kemarin pagi").
  6. `bab-23.md:41` & `bab-26.md:53`: Bab 23 (Sabtu akhir Minggu 4) menyebut perdebatan dengan Mbak Raras (Minggu–Senin awal Minggu 2) sebagai *"minggu lalu"* (seharusnya *dua minggu lalu*); Bab 26 (Selasa Minggu 5) menyebut penempelan *post-it* (Selasa Minggu 1) sebagai *"tiga minggu lalu"* (seharusnya *empat minggu lalu*).
  7. `bab-31.md:75`: *"Katanya waktu minggu pertama dulu lebih suka suasana kerja di Jogja"* — klaim tanpa setup (Saka tidak pernah mengatakan ini di Bab 1–9).
  8. `bab-31.md:79` (dan `outline.md` Bab 31): *"soto ayam tanpa seledri di warung depan gedung kantor"* — adegan makan soto ayam tanpa seledri di Bab 9 terjadi di **Warung Soto Kwitang dekat Halte Senen**, bukan di warung depan gedung kantor Cikini.
- **Dampak bagi Pembaca:** Pembaca berulang kali kehilangan orientasi kalender dan menemukan rujukan ke ucapan/peristiwa yang tidak sesuai dengan bab sebelumnya.
- **Keputusan Editorial (`MANUSCRIPT ERROR`):**
  - **Saran Perbaikan Minimal:**
    - `bab-06.md:55`: Ubah *"kejadian kemarin"* menjadi *"kejadian Selasa sore"*.
    - `bab-08.md:35`: Ubah *"Kemarin Dimas bilang"* menjadi *"Dimas pernah bilang"*.
    - `bab-18.md:11 & 29`: Ubah *"Kemarin"* / *"Kemarin sore"* menjadi *"Kamis sore"*; pada baris 39 ubah *"Kemarin waktu antar berkas"* menjadi *"Hari Jumat kemarin waktu antar berkas"*.
    - `bab-19.md:39`: Ubah *"Seminggu ini"* menjadi *"Beberapa hari ini"*.
    - `bab-20.md:29`: Ubah *"kemarin pagi"* menjadi *"Senin lalu"*.
    - `bab-23.md:41`: Ubah *"minggu lalu"* menjadi *"dua minggu lalu"*; `bab-26.md:53`: ubah *"tiga minggu lalu"* menjadi *"empat minggu lalu"*.
    - `bab-31.md:75`: Ubah menjadi *"Katanya kos tahunan itu buat teman Jogja"*.
    - `bab-31.md:79` (dan `outline.md` Bab 31): Ubah *"di warung depan gedung kantor"* menjadi *"di warung soto dekat Kwitang waktu itu"*.

---

#### [F-11] `HIGH` | `TIMELINE` | Release Impact: `FIX BEFORE RELEASE` | Confidence: `HIGH`
- **Lokasi:** Jembatan kronologi antara `chapters/bab-13.md` (Senin Minggu 2), `chapters/bab-14.md` (Kamis), dan `chapters/bab-18.md` (Senin Minggu 4)
- **Bukti Kutipan:**
  - `bab-14.md:3 & 7`: *"Dua minggu duduk satu meja dengan Saka Wijaya..."* | *"...Mbak Raras masih mendiamkanku sejak malam itu, meski kemarin siang Ibu akhirnya sudah mau mengirim pesan suara menanyakan apakah papan gambar baruku sudah dipakai kerja."*
  - `bab-18.md:3 & 17`: *"Sejak rahasia tutup botol minum hitamnya terbongkar di teras kosku malam Jumat lalu..."* | *"Memasuki minggu keempat kami duduk semeja..."*
- **Masalah Spesifik:** Bab 18 terjadi pada hari **Senin tepat setelah Kamis Bab 14–17** (terbukti dari rujukan *"malam Jumat lalu"* di Bab 18 baris 3). Namun di Bab 14 baris 3 masa kerja mereka baru disebut *"Dua minggu duduk satu meja"*, sedangkan 4 hari kemudian di Bab 18 baris 17 tiba-tiba sudah disebut *"Memasuki minggu keempat kami duduk semeja"* dan *"sebulan ini"* (baris 61). Ada satu minggu kalender yang melompat/hilang di antara Bab 13, Bab 14, dan Bab 18.
- **Dampak bagi Pembaca:** Perhitungan masa tugas 5 minggu Saka menjadi tidak sinkron sebesar satu minggu penuh.
- **Keputusan Editorial (`MANUSCRIPT ERROR`):**
  - **Saran Perbaikan Minimal:** Di `chapters/bab-14.md` baris 3, ubah *"Dua minggu duduk satu meja"* menjadi *"Hampir tiga minggu duduk satu meja"*, dan pada baris 7 ubah *"kemarin siang Ibu akhirnya sudah mau mengirim pesan suara menanyakan apakah papan gambar baruku sudah dipakai kerja"* menjadi *"beberapa hari lalu Ibu akhirnya sudah mau mengirim pesan suara menanyakan kabar kerjaku"*.

---

#### [F-12] `ERROR` | `OBJECT_CONTINUITY` / `CHARACTER_CONTINUITY` / `SCENE_BLOCKING` | Release Impact: `FIX BEFORE RELEASE` | Confidence: `HIGH`
- **Lokasi:**
  1. Tas Saka: `bab-03.md:39`, `bab-04.md:19`, `bab-07.md:71`, `bab-08.md:5`, `bab-12.md:53`, `bab-17.md:29 & 69`, `bab-18.md:7 & 31`, `bab-21.md:3 & 17`, `bab-25.md:13`, `bab-32.md:47`
  2. Kemeja Saka hari Selasa: `bab-03.md:39` vs `bab-04.md:65`
  3. Blocking tangan Saka di teras kos: `bab-17.md` baris 5, 13, 29, 31, 41, 63
- **Bukti Kutipan & Masalah Spesifik:**
  1. **Tas Kerja Saka Berubah-ubah:** Di Bab 3 baris 39 (Selasa pagi) dan Bab 18 baris 31 disebut **"ransel hitam"**, tetapi pada sore hari yang sama di Bab 4 baris 19 (serta Bab 8 baris 5, Bab 17 baris 29, Bab 21 baris 3, Bab 32 baris 47) berubah menjadi **"tas selempang kanvas hitam"**.
  2. **Kemeja Saka Berubah di Hari yang Sama (Selasa):** Di Bab 3 baris 39 (Selasa pagi) Saka mengenakan **"kemeja katun abu-abu rapi"**, tetapi pada Selasa sore pukul 17.05 di Bab 4 baris 65 tangannya merogoh **"saku kemeja flanel"**.
  3. **Blocking Fisik Tangan Saka di Bab 17:** Di Bab 4 baris 23 dan Bab 8 baris 5, botol minum hitam Saka berada di kantong samping tasnya, dan di Bab 3 baris 39 serta Bab 12 baris 53 tasnya disampirkan di bahu kiri. Namun di Bab 17 baris 13 Saka menyodorkan bungkusan martabak dengan tangan kanan sambil melipat payung basah, lalu di baris 29–63 *ibu jari tangan kirinya* memutar tutup botol minum di kantong samping tas sementara Nadia menunjuk tangan kirinya (padahal di Bab 5, 7, dan 31 kebiasaan refleks Saka selalu dilakukan dengan **ibu jari tangan kanan**).
- **Dampak bagi Pembaca:** Mengganggu imajinasi visual dan konsistensi objek ikonik tokoh utama.
- **Keputusan Editorial (`MANUSCRIPT ERROR`):**
  - **Saran Perbaikan Minimal:** Seragamkan tas Saka menjadi *"ransel kanvas hitam"*, ubah `bab-04.md:65` menjadi *"saku kemeja katun abu-abunya"*, dan ubah `bab-17.md:29, 31, 41, 63` menjadi *"tangan kanan"* (setelah Nadia menerima kantong martabak atau saat bungkusan dipegang tangan kiri).

---

#### [F-13] `ERROR` | `TIMELINE` (Internal Bab) | Release Impact: `FIX BEFORE RELEASE` | Confidence: `HIGH`
- **Lokasi:** `chapters/bab-14.md` baris 35, 55, 59 vs `chapters/bab-15.md` baris 3 (dan `outline.md` Bab 15)
- **Bukti Kutipan:**
  - `bab-14.md:35, 55, 59`: *"...rapat evaluasi Pak Ramdan jam tiga sore nanti"* | *"...di rapat jam tiga sore depan Pak Ramdan"* | *"Jam tiga nanti di ruang rapat..."*
  - `bab-15.md:3`: *"Tebakan Saka terbukti seratus persen tepat pada pukul setengah empat sore di ruang rapat redaksi."*
- **Masalah Spesifik:** Di Bab 14, jadwal rapat evaluasi sampul disebut tiga kali sebagai **pukul 15.00 (jam tiga sore)**, tetapi di Bab 15 baris 3 rapat baru dimulai pada **pukul 15.30 (setengah empat sore)** tanpa keterangan adanya penundaan rapat.
- **Dampak bagi Pembaca:** Ketidakkonsistenan penanda waktu langsung pada dua bab yang berurutan.
- **Keputusan Editorial (`MANUSCRIPT ERROR`):**
  - **Saran Perbaikan Minimal:** Ubah ketiganya di `chapters/bab-14.md` baris 35, 55, dan 59 menjadi *"jam setengah empat sore"* / *"Jam setengah empat nanti"* agar sinkron dengan Bab 15 dan `outline.md`.

---

#### [F-14] `ERROR` | `NAME_TERM_CONSISTENCY` / `DOMAIN_FACTUALITY` | Release Impact: `FIX BEFORE RELEASE` | Confidence: `HIGH`
- **Lokasi:** `chapters/bab-03.md` baris 35, `chapters/bab-20.md` baris 29 & 37, dan `chapters/bab-31.md` baris 47 & 51
- **Bukti Kutipan:**
  - `bab-03.md:35`: *"...rekan senior baru dari cabang Yogyakarta."*
  - `bab-20.md:29`: *"...urusan kepulangan Saka ke kantor pusatnya di Yogyakarta."*
  - `bab-20.md:37`: *"...logo Kantor Pusat Penerbit Aksara Senja Cabang Yogyakarta..."*
  - `bab-31.md:47 & 51`: *"...amplop cokelat panjang berlogo Kantor Pusat Yogyakarta."* | *"Surat Keputusan Mutasi Tetap Staf Redaksi Senior dari Cabang Yogyakarta ke Kantor Redaksi Jakarta."*
- **Masalah Spesifik:** Status kantor Yogyakarta bertolak belakang di dalam bab yang sama: disebut sebagai **Cabang Yogyakarta** sekaligus **Kantor Pusat Yogyakarta**, bahkan digabung secara mustahil menjadi *"Kantor Pusat Penerbit Aksara Senja Cabang Yogyakarta"* di Bab 20 baris 37.
- **Dampak bagi Pembaca:** Mengaburkan struktur organisasi penerbit tempat para tokoh bekerja.
- **Keputusan Editorial (`MANUSCRIPT ERROR` & `OUTLINE ERROR`):**
  - **Saran Perbaikan Minimal:** Tetapkan secara konsisten bahwa Yogyakarta adalah **Cabang Yogyakarta** (dan bagian SDM di sana adalah Bagian Personalia/HRD Cabang Yogyakarta), sehingga di `bab-20.md:29` menjadi *"kantor cabangnya di Yogyakarta"*, `bab-20.md:37` menjadi *"logo Penerbit Aksara Senja Cabang Yogyakarta"*, dan `bab-31.md:47` menjadi *"berlogo Cabang Yogyakarta"*.

---

#### [F-15] `ERROR` | `CAUSALITY` / `DIALOGUE_EFFECTIVENESS` | Release Impact: `FIX BEFORE RELEASE` | Confidence: `HIGH`
- **Lokasi:** `chapters/bab-27.md` baris 51 & `chapters/bab-28.md` baris 9
- **Bukti Kutipan:**
  - `bab-27.md:51`: *Dia tersenyum percaya diri. "Soal izin ke Pak Ramdan, besok biar saya yang bilang kalau Nadia nggak usah tampil."*
  - `bab-28.md:9`: *"Apanya yang nggak bisa, Nad? Tadi kan kubilang biar besok aku yang ngomong ke bos."*
- **Masalah Spesifik:** Dimas hanyalah staf divisi pemasaran yang bahkan baru saja dipermalukan di depan Pak Ramdan (Kepala Redaksi) pada rapat evaluasi Bab 15. Klaim bahwa Dimas yang akan menghadap Pak Ramdan untuk membatalkan kehadiran ilustrator utama di acara peluncuran buku redaksi sangat tidak masuk akal secara hierarki kantor.
- **Dampak bagi Pembaca:** Membuat dialog Dimas terasa terlalu konyol dan tidak kredibel dalam konteks birokrasi kantor.
- **Keputusan Editorial (`MANUSCRIPT ERROR`):**
  - **Saran Perbaikan Minimal:** Ubah `bab-27.md:51` menjadi *"Soal izin ke Pak Ramdan, besok kamu izin sendiri aja bilang ada urusan keluarga"*, dan `bab-28.md:9` menjadi *"Tadi kan kubilang tinggal izin ke bos, bilang urusan keluarga"*.

---

#### [F-16] `ERROR` | `SPELLING_TYPO` / `GRAMMAR` | Release Impact: `FIX BEFORE RELEASE` | Confidence: `HIGH`
- **Lokasi:** `chapters/bab-03.md` baris 41, `chapters/bab-07.md` baris 41, `chapters/bab-10.md` baris 41, `chapters/bab-25.md` baris 27, dan `chapters/bab-32.md` baris 11
- **Bukti Kutipan & Koreksi Minimal:**
  1. `bab-10.md:41`: `"...kasihan keponakan kamu udah telanjur dijanyiin naik pesawat."` -> **Typo** objektif (`dijanyiin`); perbaiki menjadi **`dijanjiin`** (dialog lisan).
  2. `bab-03.md:41` & `bab-25.md:27`: `"...nafasku tersendat seketika."` & `"Nafasku memburu."` -> Bentuk tidak baku di dalam narasi (di Bab 1 baris 5, Bab 9 baris 51, dan Bab 24 baris 27 sudah ditulis baku *napasku*); perbaiki menjadi **`napasku`** / **`Napasku`**.
  3. `bab-07.md:41`: `"...seluruh udara yang kutahan di dada mendadak terhembus keluar."` -> Bentuk tidak baku di narasi (bandingkan dengan Bab 31 baris 37 *berembus*); perbaiki menjadi **`terembus`**.
  4. `bab-32.md:11`: `"Nad, sore ini lo nggak ada jadwal kemana-mana kan?"` -> Penulisan kata depan *ke* yang digabung; perbaiki menjadi **`ke mana-mana`**.

---

### C. Temuan `REVIEW` dan `INFO` (`OPTIONAL POLISH` / Kontekstual)

#### [F-17] `REVIEW` | `REPETITION` / `PROSE_CLARITY` | Release Impact: `FIX BEFORE RELEASE` | Confidence: `HIGH`
- **Lokasi:**
  1. `chapters/bab-12.md` baris 5–7
  2. `chapters/bab-17.md` baris 13–15
  3. `chapters/bab-29.md` baris 33–35
- **Bukti Kutipan & Masalah Spesifik:**
  1. `bab-12.md:5-7`: Kalimat terakhir paragraf 2 (*"Namun sore ini, nada bicara dan gerak-geriknya jauh lebih tenang dari hari-hari sebelumnya saat kami bekerja di meja nomor empat."*) dan kalimat pembuka paragraf 3 (*"Namun Saka justru meraih botol minum hitamnya..."*) sama-sama diawali konjungsi pertentangan **"Namun"**, serta mengulang frasa *"di meja nomor empat"* dua kali dalam satu paragraf.
  2. `bab-17.md:13-15`: Paragraf baris 13 (*"Tangan kanannya terulur menyodorkan kantong plastik berisi kotak martabak manis yang masih hangat itu ke arahku."*) diulang lagi secara redundan pada tag dialog baris 15 (*'"Sekalian bawa masuk ini," kata Saka seraya menyodorkan bungkusan plastik hangat itu ke arahku.'*).
  3. `bab-29.md:33-35`: Dialog Riko pada baris 33 (*"Katanya urusan di sini udah nggak ada yang perlu ditunggu."*) diulang sebagai gema batin pada baris 35 dengan susunan kata yang berubah (*`Urusan di sininya udah nggak ada yang perlu ditungguin lagi.`*).
- **Saran Perbaikan Minimal:**
  - Di `bab-12.md:7`, hapus kata *"Namun"* di awal paragraf 3 menjadi *"Saka justru meraih botol minum hitamnya..."* dan ringkas akhir baris 5 menjadi *"...lebih tenang dari hari-hari sebelumnya."*
  - Di `bab-17.md:15`, ringkas tag dialog menjadi *'"Sekalian bawa masuk ini," kata Saka.'*
  - Di `bab-29.md:35`, samakan atau ringkas gema batin agar selaras dengan kalimat Riko.

---

#### [F-18] `REVIEW` | `TIMELINE` (Kolokial Lisan) | Release Impact: `OPTIONAL POLISH` | Confidence: `MEDIUM`
- **Lokasi:** `chapters/bab-24.md` baris 45, `chapters/bab-26.md` baris 29, `chapters/bab-28.md` baris 57, dan `chapters/bab-31.md` baris 21
- **Bukti Kutipan:**
  - `bab-24.md:45` (Senin sore): `"Sejak kemarin kamu ngomong kaku banget ke saya."` (Mengacu pada Jumat sore Bab 21).
  - `bab-26.md:29` & `bab-28.md:57` (Selasa): `"Waktu Ibu sakit kemarin..."` & `"Semua biaya klinik, bubur, dan bensin kemarin..."` (Mengacu pada Sabtu Bab 22).
  - `bab-31.md:21` (Jumat sore): `"Maaf buat sikapku kemarin, dan maaf buat omonganku di lobi."` (Mengacu pada Senin–Selasa Bab 24–26).
- **Masalah Spesifik & Rekomendasi:** Dalam ragam lisan bahasa Indonesia sehari-hari, kata *"kemarin"* sering digunakan secara longgar untuk merujuk "beberapa hari yang lalu / pertemuan terakhir". Namun agar orientasi waktu pembaca lebih presisi, disarankan mengubah `bab-24.md:45` menjadi *"Sejak Jumat"*, `bab-26.md:29` & `bab-28.md:57` menjadi *"hari Sabtu kemarin"* / *"akhir pekan kemarin"*, dan `bab-31.md:21` menjadi *"sikapku awal minggu ini"*.

---

#### [F-19] `INFO` | `OUTLINE_LEAKAGE` / `POV_BOUNDARY` | Release Impact: `OPTIONAL POLISH` | Confidence: `MEDIUM`
- **Lokasi:** `chapters/bab-27.md` baris 25
- **Bukti Kutipan:** *"Merasa bahwa di detik itu aku sudah resmi kembali ke dalam genggamannya dan Ibu sudah berada di pihaknya, topeng merendah yang dipakainya sejak hari Rabu lalu mulai melorot tanpa ia sadari."*
- **Analisis:** Kalimat ini menyalin penjelasan motivasi internal Dimas dari `outline.md` Bab 27 ke dalam narasi POV orang pertama Nadia. Karena masih dapat dibaca sebagai simpulan retrospektif Nadia atas perubahan gelagat Dimas, hal ini tidak menghalangi pemahaman, namun akan lebih organik jika ditambahkan penanda persepsi Nadia (*"Seolah merasa bahwa di detik itu..."*).

---

## 6. Evaluasi Delapan Gerbang Kelayakan & Vonis Kesiapan Publikasi (`rules/09-publication-readiness.md`)

### 6.1. Evaluasi Delapan Gerbang Kelayakan

| Gerbang Kelayakan | Status | Alasan & Bukti |
|---|---|---|
| **1. Fondasi dan janji cerita** | **LULUS** | Premis, fokus karakter (Nadia belajar menjaga batas diri bersama Saka), dan janji romansa kantor terbaca jelas sejak Bab 1–4. |
| **2. Struktur dan perkembangan** | **GAGAL (`BLOCKER`)** | Paruh pertama (Bab 1–18) berkembang solid, namun paruh kedua (Bab 19–29) mengalami kemunduran karakter ekstrem (Nadia hampir menerima Dimas kembali di Bab 27 baris 17) dan bergantung pada kebetulan pelayan salah antar minum. |
| **3. Kausalitas, karakter, dan konflik** | **GAGAL (`BLOCKER`)** | Tabel Rantai Sebab-Akibat memiliki temuan `HIGH`: 7 kali pengabaian komunikasi satu kalimat, alasan sifat abstrak tanpa pemicu konkret di halaman, kontradiksi telepon Pak Ramdan (Bab 20 vs Bab 31), dan trauma mantan Saka di Bab 25 yang tidak pernah ditanam di Bab 12. |
| **4. Narasi dan orientasi pembaca** | **PERLU PERBAIKAN** | Banyak penanda waktu relatif (*"kemarin"*, *"minggu lalu"*, *"tiga minggu lalu"*) dan lompatan minggu antara Bab 14 dan Bab 18 yang mengacaukan orientasi kalender pembaca. |
| **5. Adegan dan keterbacaan** | **PERLU PERBAIKAN** | Kontradiksi pengerjaan poster di Bab 2–3 & 7, pengiriman file akhir halaman penutup di Bab 21 & 24, serta *blocking* tangan dan tas Saka di Bab 3, 4, 17. |
| **6. Continuity, timeline, dan dunia cerita** | **GAGAL (`FIX BEFORE RELEASE`)** | Kontradiksi lokasi kos Saka (Cikini vs naik kereta ke selatan), lokasi cerita Jogja (kedai kopi vs warung soto), lokasi soto tanpa seledri (Kwitang vs depan kantor), tiket pesawat Bali vs Puncak (Bab 10 vs 13), status Kantor Pusat vs Cabang Yogyakarta, serta jadwal cetak massal 2,5 hari kerja dan kereta malam Selasa yang masih di perjalanan pada Rabu pukul 08.30 pagi. |
| **7. Prosa dan teknis naskah** | **PERLU PERBAIKAN** | Secara umum prosa lancar dan hangat, namun masih terdapat typo objektif (`dijanyiin`), bentuk tidak baku di narasi (`nafasku`, `terhembus`, `kemana-mana`), dan kalimat repetitif di Bab 12, 17, 29. |
| **8. Ketuntasan dan payoff** | **PERLU PERBAIKAN** | Payoff *klik* dua kali tutup botol dan *post-it* kuning bekerja manis, tetapi daftar rujukan mundur (`--refs`) masih mengandung rujukan tanpa tanam (Bab 8 baris 35, Bab 25 baris 35, Bab 31 baris 75) dan kesalahan detail lokasi. |

---

### 6.2. Keputusan Akhir Kesiapan Publikasi (`rules/09-publication-readiness.md` §D)

- **Status Final:** **`NOT READY` (Kerangka Perlu Dibongkar / Revisi Struktural Kausalitas & Perbaikan Kontinuitas)**
- **Alasan Keputusan:**
  Sesuai `rules/09-publication-readiness.md` Bagian D, sebuah naskah tidak dapat diberi status `READY TO PUBLISH` (dan harus divonis **`NOT READY`** apabila terdapat `BLOCKER` kausalitas/pengetahuan tokoh) ketika:
  1. **Tabel Rantai Sebab-Akibat (`rules/01-plot-and-causality.md`) masih memiliki temuan `HIGH` / `BLOCKER`** (konflik utama paruh kedua bertumpu pada 7 kali pengabaian komunikasi dengan alasan sifat abstrak, pengabaian petunjuk tab kos tahunan & formulir HRD oleh tokoh POV di Bab 20, kontradiksi pengetahuan Pak Ramdan di Bab 20 vs Bab 31, kontradiksi pengiriman file akhir di Bab 21 vs Bab 24, serta regresi karakter Nadia di Bab 25–27).
  2. **Prosedur Dunia Nyata (`rules/18-real-world-procedures.md`) memiliki jadwal operasional yang mustahil** (cetak massal + penjilidan buku dalam 2,5 hari kerja dan distribusi toko buku Matraman dalam 3 hari akhir pekan; kereta malam Jakarta–Yogyakarta Selasa malam yang masih berada di perjalanan pada Rabu pukul 08.30 pagi).
  3. **Daftar Rujukan Mundur (`--refs` / `rules/06-setup-payoff.md`) belum bersih** dari rujukan tanpa tanam (Bab 8 baris 35, Bab 25 baris 35, Bab 31 baris 75), perbedaan detail lokasi (warung soto vs kedai kopi di Bab 21 & 25; warung soto depan kantor vs Kwitang di Bab 31), dan kesalahan waktu relatif (Bab 6, 18, 20, 23, 26).
- **Rekomendasi Rilis:** Tahan publikasi; terapkan perbaikan struktural pada kausalitas paruh kedua ([F-01] s.d. [F-04]) serta perbaikan lokal kontinuitas, waktu relatif, prosedur dunia nyata, dan ejaan ([F-05] s.d. [F-17]) sebelum melakukan verifikasi ulang.
