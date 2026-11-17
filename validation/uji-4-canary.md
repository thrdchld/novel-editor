# Laporan Audit Editorial Lengkap: *Catatan untuk Orang Sungkan* (`canary`)

- **Target Audit:** `/tmp/uji-canary` (salinan dari `story/Catatan untuk Orang Sungkan/chapters` dan `outline.md` pada branch `canary` repositori `thrdchld/novel-metropop`)
- **Tanggal Audit:** 2026-11-17
- **Mode Kerja:** AUDIT (Read-Only) sesuai `AGENTS.md`
- **Cakupan Dokumen yang Dibaca:**
  - `outline.md` (Status: TERKUNCI v1.1, 32 bab)
  - `chapters/bab-01.md` s.d. `chapters/bab-32.md` (32 bab utuh, 100% cakupan naskah)

> **Pernyataan Eksplisit *Blind Pass* (`AGENTS.md` §7.1):**
> Audit ini diawali dengan ***blind pass* wajib**: editor membaca **hanya** ke-32 file bab naskah (`chapters/bab-01.md` s.d. `chapters/bab-32.md`) dan `outline.md` di `/tmp/uji-canary` dalam urutan pembaca, lalu menyusun **Tabel Rantai Sebab-Akibat** langsung dari bukti teks bab mentah tanpa membuka `canon.md`, `ledger.md`, `state.md`, laporan audit lama, folder `tests/fixtures/`, folder `validation/`, maupun branch `canary-key`.

---

## 1. Story Assessment & Evaluasi Fondasi (`rules/16-story-assessment-and-developmental-editing.md`)

### 1.1 Apa yang Sudah Bekerja
1. **Premis, Fokus, dan Janji Cerita:**
   - Cerita berfokus pada **Nadia Putri** (26 tahun), desainer grafis/ilustrator di Penerbit Aksara Senja (Cikini, Jakarta Pusat) yang mengidap kebiasaan "nggak enakan" kronis akibat pola asuh sebagai anak tengah di rumahnya (Rawamangun), serta baru diputuskan pacarnya selama dua tahun, **Dimas** (staf pemasaran di kantor yang sama), karena dianggap terlalu penurut seperti *operator customer service*.
   - *Inciting incident* bekerja secara konkret sejak Bab 1–4: Nadia kepergok mengamuk di tangga darurat oleh **Saka Wijaya** (28 tahun, editor senior pindahan cabang Yogyakarta yang tegas menjaga batas jam kerja), lalu keesokan paginya dipasangkan duduk semeja di Meja Proyek Nomor Empat selama lima minggu untuk menggarap buku esai dan ilustrasi kota *Sela Waktu*.
2. **Progresi Karakter & Eskalasi Konflik:**
   - Latihan menetapkan batasan diri (*boundary setting*) disusun bertahap dengan peningkatan risiko emosional yang jelas:
     - **Tahap 1 (Dibantu Saka):** Saka memotong titipan revisi Mbak Dinda tepat pukul 17.01 dan menempelkan *post-it* kuning *"Bilang enggak itu nggak bikin langit runtuh"* (Bab 4).
     - **Tahap 2 (Rekan Kerja Sejajar):** Nadia menolak menalangi makan siang Riko Rp30.000 dengan menunjuk kode QRIS (Bab 5).
     - **Tahap 3 (Mantan Pacar di Kantor):** Nadia menolak permintaan lembur desain *backdrop* dari Dimas dan Vanya dalam tiga detik (Bab 6–7).
     - **Tahap 4 (Akar Psikologis Keluarga):** Nadia menolak meminjamkan tabungan Rp4 juta (yang dikumpulkan 10 bulan untuk membeli tablet gambar baru) kepada kakaknya, Mbak Raras, dan ibunya melalui telepon tanpa marah-marah, serta tetap memberi Rp500.000 untuk jajan keponakannya, Daffa (Bab 10–13).
     - **Tahap 5 (Ujian Kemandirian & Goyahnya Keyakinan):** Ketika Dimas mengubah taktik menjadi lembut, merawat Ibu Nadia yang terserang vertigo akut di Rawamangun (Bab 22–23), dan menanamkan keraguan bahwa penugasan Saka hanya 5 minggu (Bab 19–21), Nadia sempat goyah hingga hampir kembali pada Dimas (Bab 23–26).
     - **Tahap 6 (Klimaks Kesadaran Diri):** Saat Dimas kelepasan meremehkan buku *Sela Waktu* dan meminta Nadia membatalkan kehadiran di panggung peluncuran demi acara makan malam manajer pemasaran (Bab 27), Nadia tersadar, membuka kebenaran di depan ibunya, dan menutup masa lalunya menggunakan balikan diksi *operator customer service* secara elegan (Bab 28).
3. **Planting & Callback Utama:**
   - Tiga motif utama (*post-it* kuning di sampul buku sketsa → bingkai monitor → buku sketsa → monitor & punggung laptop Saka; kebiasaan jempol Saka memutar tutup botol minum hitam penyok hingga berbunyi *klik* dua kali setiap berbohong menutupi perhatiannya di Bab 5, 7, 17, dan 31; serta ejekan *operator customer service* di Bab 1, 21, dan 28) tertanam dan terbayar secara organik.

### 1.2 Ringkasan Masalah Utama yang Ditemukan
Kerangka makro cerita di `outline.md` utuh dan koheren. Namun, pada teks manuskrip (`chapters/`) ditemukan **6 kesalahan objektif/struktural lokal (`ERROR` / `HIGH`)** dan **2 catatan pemeriksaan (`REVIEW`)** yang merusak kausalitas adegan, pengetahuan karakter, kontinuitas rujukan mundur, serta logika operasional dunia nyata:
1. **Anakronisme Pengetahuan Karakter & Kausalitas Terbalik di Bab 19 (`F-01`, `HIGH` / `ERROR`):** Pada Rabu sore (Bab 19 baris 69), Dimas berkata kepada Nadia: *"Aku lihat sendiri kamu sampai bikin sketsa kursi kosong di halaman penutup bukumu."* Padahal sketsa kursi kosong di halaman penutup itu **baru digambar Nadia dua hari kemudian pada Jumat sore (Bab 21 baris 5)** setelah mendengar telepon Pak Ramdan di Bab 20.
2. **Kebocoran Prematur Informasi Mutasi Tetap Saka oleh Dimas di Bab 27 (`F-02`, `HIGH` / `ERROR`):** Pada Selasa malam (Bab 27 baris 45), Dimas berkata di depan Nadia: *"toh kata anak HRD dia udah resmi pindah tetap ke Jakarta."* Klausa ini merusak logika cerita karena: (a) menghancurkan senjata manipulasi Dimas sendiri, (b) diabaikan total oleh Nadia yang dua paragraf kemudian (baris 63) dan sepanjang Bab 29–30 masih mengira Saka pindah kembali ke Yogyakarta, serta (c) bertentangan dengan fakta Bab 31 bahwa SK mutasi tetap baru ditandatangani Pak Bambang pada hari Kamis di Yogyakarta dan baru diketahui Nadia pada hari Jumat sore.
3. **Rujukan Mundur Salah Lokasi & Tanpa Tanam tentang Ucapan di Kedai Kopi pada Bab 25 (`F-03`, `ERROR`):** Pada Bab 25 baris 21, Saka berkata: *"Kamu sendiri yang bilang di kedai kopi kalau urusan kalian sudah selesai."* Di adegan kedai kopi (Bab 11–12), Nadia sama sekali tidak pernah membicarakan Dimas (hanya membahas Mbak Raras, Ibu, dan tablet gambar).
4. **Rujukan Mundur Tanpa Tanam tentang Adik Perempuan Saka di Surabaya pada Bab 26 (`F-04`, `ERROR`):** Pada Bab 26 baris 51, narasi menyebut: *"Aku sempat teringat cerita Saka tempo hari soal adik perempuannya yang kuliah di Surabaya."* Fakta ini tidak pernah ada di bab mana pun sebelumnya dan memutus alur paragraf.
5. **Kontradiksi Hari Keberangkatan Saka ke Yogyakarta pada Bab 29 (`F-05`, `ERROR`):** Pada Bab 29 baris 23 (Rabu pagi), Riko berkata: *"Mas Saka Senin sore udah pamit ke Jogja lebih awal."* Ini bertentangan langsung dengan Bab 26 (sepanjang Selasa pagi–siang Saka masih bekerja di meja nomor empat), Bab 29 baris 27, 29, dan 39 (*"Berangkat ke Jogja kemarin sore? ... Kemarin sore jam setengah enam"* = Selasa sore), serta Bab 31 baris 61 (*"Perjalanan Selasa sore itu"*).
6. **Jadwal & Durasi Kereta Api Yogyakarta–Jakarta yang Mustahil di Bab 30 (`F-06`, `ERROR` / `HIGH`):** Pada Bab 30 baris 9 disebutkan Saka naik *"kereta pagi yang berangkat dari Stasiun Tugu Yogyakarta pukul dua siang dan dijadwalkan tiba di Stasiun Gambir sebelum pukul empat sore"*. Selain kontradiksi istilah *"kereta pagi"* untuk pukul 14.00 siang, durasi perjalanan kereta api Stasiun Tugu Yogyakarta ke Stasiun Gambir Jakarta di bawah 2 jam adalah mustahil secara operasional (waktu tempuh nyata KA eksekutif adalah ±6 jam).

---

## 2. Audit Kausalitas & Tabel Rantai Sebab-Akibat (`rules/01-plot-and-causality.md` & `rules/05-character-knowledge.md`)

### 2.1 Tabel Rantai Sebab-Akibat (7 Kolom Wajib)

Berikut adalah pemetaan rantai sebab-akibat langsung dari teks bab mentah (`chapters/bab-01.md` s.d. `bab-32.md`) untuk seluruh titik balik, eskalasi konflik, dan keputusan penting:

| peristiwa | keinginan tokoh | hambatan | pilihan | akibat yang tampak di halaman | pertanyaan "kenapa tidak X?" | jawaban di halaman |
|---|---|---|---|---|---|---|
| **Bab 1–2:** Nadia lembur Senin malam (19.00–19.45) mengerjakan revisi Mbak Dinda & poster titipan Dimas, lalu memaki tembok di tangga darurat hingga dipergoki Saka. | Meluapkan frustrasi karena dimanfaatkan rekan kerja dan mantan pacar tanpa memicu konflik terbuka di kantor. | Kebiasaan kronis takut menolak (*people-pleasing*) dan posisi anak tengah yang terbiasa mengalah; rasa malu saat dipergoki orang asing. | Berteriak di tangga darurat, lalu refleks meminta maaf berlebihan dan kabur pulang meninggalkan lemburan di meja (namun dini hari menyelesaikan poster Dimas di kos, Bab 3 baris 5). | Saka menilai langsung kontradiksi antara amukan Nadia di tangga dan kepatuhannya di meja kerja; benih dinamika mentor-rekan terbentuk. | Kenapa Nadia tidak langsung menolak permintaan poster Dimas dan revisi Mbak Dinda sejak Senin sore di meja kerja? | Dijelaskan melalui kilas balik Bab 1 baris 15–21 & 37 serta akar keluarga di Bab 10: refleks otomatis meminta maaf dan ketakutan merusak suasana/dicap tidak kooperatif di kantor. |
| **Bab 3–4:** Selasa pagi Pak Ramdan memasangkan Nadia & Saka di Meja Proyek Nomor 4 untuk buku *Sela Waktu* (5 minggu); pukul 17.01 Mbak Dinda datang menitipkan *banner* web via *flash disk*. | Nadia ingin menyelesaikan pekerjaannya tanpa membuat Mbak Dinda marah; Saka ingin jadwal proyek *Sela Waktu* steril dari titipan luar dan pulang tepat pukul 17.00. | Refleks dua tahun Nadia yang sudah mengangkat tangan hendak menerima *flash disk* Mbak Dinda (Bab 4 baris 37). | Saka memotong langsung (*"Meja ini sudah tutup"*), menolak *flash disk* Mbak Dinda, menyuruh Nadia mengemas tas, dan menempelkan *post-it* kuning *"Bilang enggak itu nggak bikin langit runtuh"* di buku sketsa Nadia. | Mbak Dinda batal menitipkan kerjaan dengan kesal; Nadia pulang tepat waktu untuk pertama kalinya dalam sebulan dan menempelkan *post-it* itu di pojok monitor keesokan paginya (Bab 5 baris 3). | Kenapa Mbak Dinda tidak memaksa Nadia lagi saat itu juga di depan Saka? | Karena Saka berdiri tegak memotong dengan argumen prosedural (masukkan antrean resmi besok pagi) dan hendak mencabut colokan meja nomor empat (Bab 4 baris 39–55). |
| **Bab 5:** Rabu siang di warung ayam bakar, Riko mengaku dompet tertinggal di laci dan meminta Nadia menalangi Rp30.000. | Nadia ingin tidak dimanfaatkan lagi (utang Riko bulan lalu sudah Rp90.000 belum dibayar), tetapi canggung menolak di depan meja makan ramai. | Rasa sungkan melihat wajah memelas Riko di depan rekan-rekan redaksi (Bab 5 baris 19). | Didorong sikuan dan bisikan Saka, Nadia menutup dompetnya, menyatakan uang tunainya pas-pasan, dan menunjuk stiker QRIS di tiang tenda. | Riko terpaksa membayar sendiri memakai ponselnya; Nadia merasakan kelegaan konkret pertama; Saka menghadiahkan es jeruk peras sambil berbohong dan memutar tutup botol 2x *klik*. | Kenapa Riko tidak berkelit bahwa ponselnya juga tertinggal atau baterainya habis? | Karena ponsel Riko terlihat jelas berada di saku kemejanya dan dua staf redaksi lain serta Tari langsung ikut menoleh ke stiker QRIS (Bab 5 baris 41–45). |
| **Bab 6–7:** Jumat sore pukul 16.20, Dimas dan Vanya meminta Nadia lembur membuat desain *backdrop* 3x2 m untuk acara besok pagi. | Nadia ingin menolak karena harga dirinya diinjak di depan gebetan baru Dimas; Dimas ingin masalah desain beres cepat supaya bisa pergi mengecek katering bersama Vanya. | Ketakutan Nadia dicap sebagai mantan yang kekanak-kanakan dan pendendam di depan Vanya; Saka kali ini sengaja diam bersedekap untuk menguji Nadia. | Nadia menatap *post-it* kuning di monitor, menarik tangan, dan menolak tegas dengan alasan jam kerja habis dan akhir pekan padat untuk proyek *Sela Waktu*, serta mengarahkan mereka ke file mentah di folder bersama. | Dimas tersinggung dan pergi bersama Vanya ke percetakan; tangan Nadia gemetar tetapi ia berhasil memutus pola lama; Saka memberi cokelat susu (kembali berbohong + 2x *klik* tutup botol). | Kenapa Saka tidak langsung mengusir Dimas seperti saat ia menghadapi Mbak Dinda di Bab 4? | Di halaman Bab 6 baris 53–55 dijelaskan bahwa Saka sengaja bersedekap dalam hening untuk memberi ruang penuh kepada Nadia agar Nadia berani bersuara sendiri menghadapi mantannya. |
| **Bab 10–13:** Minggu siang di Rawamangun, Mbak Raras meminta pinjam tabungan Rp4 juta untuk liburan Daffa ke Bali dan Ibu membujuk Nadia mengalah; Senin sore Nadia curhat ke Saka di kedai kopi, lalu Senin malam menelepon Ibu. | Nadia ingin mempertahankan tabungan Rp4 juta untuk membeli tablet gambar baru karena kabel tablet lamanya sudah rusak parah. | Tekanan emosional Ibu (*"ngalah dulu sama kakaknya"*) dan ketakutan masa kecil Nadia bahwa jika ia menolak di rumah, keluarganya tidak akan menyayanginya lagi (Bab 10 baris 45–51; Bab 11 baris 61). | Minggu siang Nadia mengulur waktu (*"cek saldo nanti malam"*); setelah mendengar kisah masa lalu Saka yang bangkrut di Jogja karena tak tegaan (Bab 12), Senin malam (Bab 13) Nadia menelepon Ibu dengan lembut: menolak meminjamkan Rp4 juta karena untuk beli alat kerja, namun mentransfer Rp500.000 gratis untuk uang jajan Daffa. | Meski Mbak Raras menyindir ketus dan nada Ibu sempat dingin, Ibu akhirnya memaklumi dan menyuruh Mbak Raras mencari penginapan lebih murah; Nadia membeli tablet gambar baru (Bab 14 baris 5). | Kenapa Nadia tidak langsung menolak permintaan Rp4 juta di meja makan pada hari Minggu siang (Bab 10)? | Karena tekanan langsung Ibu + Mbak Raras secara tatap muka di meja makan memicu rasa bersalah anak tengah yang jauh lebih berat daripada menolak rekan kantor, sehingga Nadia memilih mundur taktis ke malam hari (Bab 10 baris 51–53). |
| **Bab 14–17:** Kamis Minggu 3, Dimas menyindir warna sampul *Sela Waktu* di meja nomor 4 dan menyerang draf Nadia di rapat evaluasi Pak Ramdan; sorenya Saka memayungi Nadia pulang dan memberi martabak manis di teras kos. | Dimas ingin menjatuhkan karya Nadia & Saka karena cemburu dan kesal sehabis ditolak Vanya; Saka ingin melindungi karya Nadia; Nadia ingin berterima kasih dan mengungkap kebiasaan bohong Saka. | Serangan formal Dimas di rapat redaksi dengan dalih komersialitas pemasaran. | Saka menyiapkan data penjualan triwulan pemasaran yang ditandatangani Dimas sendiri untuk membungkam Dimas di depan Pak Ramdan (Bab 15); malamnya di teras kos, Nadia membongkar kebiasaan jempol Saka memutar tutup botol 2x *klik* saat berbohong (Bab 17). | Sampul Nadia disetujui tanpa revisi; di teras kos wajah Saka memerah salah tingkah dan sejak Senin berikutnya (Bab 18) hubungan mereka di meja nomor 4 menjadi hangat tanpa alasan bohong lagi. | Kenapa di Bab 14 baris 19–21 saat Nadia memergoki tab kos tahunan Cikini & formulir antar-cabang di laptop Saka, Nadia tidak mendesak Saka lebih jauh? | Karena Saka langsung menutup tab dengan cepat dan memberi alasan yang terdengar masuk akal (*"Teman Jogja ada yang mau pindah kerja ke daerah sini bulan depan, titip dicarikan info harga"*), ditambah interupsi bunyi kamera ponsel Tari dan kedatangan Dimas (Bab 14 baris 21–25). |
| **Bab 19:** Rabu sore Minggu 4 di dapur kantor, Dimas yang sudah putus dari Vanya meminta maaf sambil berkaca-kaca dan membisikkan bahwa penugasan Saka dari Jogja hanya 5 minggu. | Dimas ingin mendapatkan kembali Nadia setelah merasakan lelahnya menghadapi Vanya; Nadia awalnya ingin menjaga batas sebagai rekan kerja biasa. | Kerentanan Nadia melihat orang yang pernah bersamanya 2 tahun tampil rapuh, ditambah ketiadaan pembicaraan dari Saka mengenai masa depan mereka setelah proyek 5 minggu usai. | Nadia menolak ajakan balikan saat itu, tetapi menyimpan kecemasan tentang kepulangan Saka ke Jogja. | Benih keraguan tertanam di pikiran Nadia menjelang akhir minggu keempat. *(Namun terdapat cacat kausalitas/anakronisme di baris 69 karena Dimas menyebut sketsa kursi kosong yang baru dibuat Nadia di Bab 21).* | Kenapa Nadia tidak langsung bertanya kepada Saka pada hari Rabu atau Kamis itu tentang masa tugas 5 minggunya? | Di Bab 20 baris 3–5 dijelaskan bahwa selama dua hari (Rabu–Kamis) Nadia masih berusaha meyakinkan dirinya bahwa ucapan Dimas cuma akal-akalan mantan yang panik dan mengira batas 5 minggu hanya durasi proyek buku, sampai ia mendengar sendiri telepon Pak Ramdan pada Jumat siang. |
| **Bab 20–21:** Jumat siang Minggu 4, Nadia tak sengaja mendengar telepon Pak Ramdan kepada Pak Bambang soal berakhirnya masa perbantuan 5 minggu Saka dan melihat amplop Cabang Yogyakarta di meja Saka; Jumat sore Nadia memancing pertanyaan ke Saka. | Nadia ingin kepastian apakah Saka akan kembali ke Yogyakarta setelah peluncuran buku; Saka ingin menyelesaikan administrasi pelepasan di Jogja lebih dulu sebelum memberi tahu Nadia. | Trauma masa lalu Saka di Jogja yang membuatnya pantang memberi janji sebelum SK resmi berada di tangan (Bab 12 baris 37; Bab 21 baris 25); rasa gengsi dan takut Nadia dianggap membebani Saka; dering telepon Kepala Cabang Jogja yang memotong percakapan (Bab 21 baris 55). | Saka menjawab datar bahwa surat tugas perbantuannya habis akhir minggu depan dan ia harus ke Yogyakarta menghadap Pak Bambang dulu sebelum bisa cerita jelas; Nadia yang terluka langsung memasang mode bicara baku (*operator CS*), menolak pulang bareng, dan menyelipkan sketsa kursi kosong di halaman penutup. | Kesalahpahaman mengunci kedua belah pihak: Nadia yakin Saka akan pulang selamanya ke Jogja, sementara Saka bingung melihat Nadia mendadak kaku tetapi terpotong telepon Pak Bambang. | Kenapa Saka tidak langsung menjelaskan bahwa amplop dan kunjungannya ke Pak Bambang adalah untuk mengurus mutasi tetap ke Jakarta? | Motif penahanan informasi Saka sudah ditanam sejak Bab 12 baris 27 & 37 dan ditegaskan kembali di Bab 21 baris 25 & Bab 31 baris 41–43: akibat trauma ditinggal mantan saat bangkrut di Jogja, Saka berprinsip keras pantang menahan orang dengan janji yang surat keputusannya belum resmi ditandatangani. |
| **Bab 22–23:** Sabtu pagi vertigo Ibu kambuh berat di Rawamangun; Ibu (yang belum tahu Nadia putus) menelepon Dimas; Dimas datang membawa mobil, mengantar ke klinik, menunggu 3 jam dengan telaten, dan meminta maaf pada Ibu; Ibu membujuk Nadia mempertimbangkan Dimas lagi. | Nadia ingin ibunya segera tertangani secara medis dan tenang; Dimas ingin memenangkan hati Ibu dan Nadia kembali. | Kondisi darurat medis Ibu yang tidak kuat terguncang, ponsel Nadia sempat mode senyap, Mbak Raras di Bandung, adik di kampus; rasa rapuh Nadia sehabis jawaban dingin Saka pada Jumat sore. | Nadia menerima bantuan mobil Dimas ke klinik, melunak melihat ketelatenan Dimas merawat Ibu, dan pada Sabtu malam menyetujui ajakan Dimas bertemu di lobi kantor hari Senin sore. | Dimas berhasil masuk kembali ke lingkaran keluarga Nadia melalui rasa berutang budi Ibu; keyakinan Nadia goyah. | Kenapa Ibu menelepon Dimas pada Sabtu pagi, dan kenapa Nadia tidak menolak bantuan Dimas saat tiba di rumah? | Karena selama sebulan Nadia belum berani memberi tahu Ibu bahwa mereka sudah putus (ditanam di Bab 10 baris 17), ponsel Nadia senyap saat Ibu menelepon pukul 06.30, dan kondisi vertigo Ibu darurat membutuhkan mobil agar bisa rebahan (Bab 22 baris 15–41). |
| **Bab 24–26:** Senin sore Minggu 5, Saka melihat sketsa kursi kosong di *dummy* buku dan hendak bertanya, tetapi terpotong pesan WA Dimas yang menunggu di lobi; di lobi Saka mengonfrontasi Nadia, dan saat Nadia menyebut Dimas merawat ibunya dan meminta kesempatan kedua, Saka menyuruh Nadia mengambil *"pilihan paling masuk akal"*; Nadia menyetujui makan malam keluarga Selasa malam. | Di lobi, Nadia sebenarnya ingin melihat Saka cemburu dan melarangnya kembali pada Dimas (Bab 25 baris 31–33); Saka ingin tahu maksud sketsa kursi kosong dan alasan Dimas kembali. | Kalimat Nadia yang membawa-bawa bantuan Dimas pada Ibu dan restu keluarga memicu langsung trauma lama Saka di Jogja (ditinggal mantan demi pria pilihan orang tua yang lebih siap di depan mata, Bab 25 baris 35–37). | Saka menutup diri dan berkata dingin bahwa jika Dimas berubah dan membuat Ibu tenang, kembali pada Dimas adalah *"pilihan paling masuk akal"*, lalu pergi; Nadia yang patah hati menerima ajakan makan malam Dimas untuk Selasa malam dan melepas *post-it* kuning dari monitor pada Selasa siang (Bab 26). | Hubungan Nadia dan Saka membeku total; Saka berangkat lebih awal ke Yogyakarta pada Selasa sore setelah berkas naik cetak selesai untuk mengurus tanda tangan pelepasan dan kos lamanya. | Kenapa Saka tidak menahan Nadia di lobi meskipun ia baru saja melihat gambar kursi kosong buatan Nadia di *dummy* buku? | Karena di detik Saka hendak menggali arti gambar itu, Dimas muncul di lobi membawa puding untuk Ibu Nadia, dan ucapan Nadia tentang Ibu langsung menghantam luka lama Saka di Jogja sementara SK mutasi tetap Saka belum turun di tangannya (Bab 25 baris 35–48; Bab 31 baris 39–43). |
| **Bab 27–28:** Selasa malam di Rumah Makan Sederhana Rasa Rawamangun, Dimas yang merasa sudah di atas angin mengejek sikap kaku Nadia ke pelayan dan meminta Nadia membatalkan kehadiran di panggung peluncuran *Sela Waktu* Jumat sore demi menemaninya ke syukuran bos pemasaran di Senayan. | Dimas ingin Nadia kembali menjadi pasangan patuh yang memprioritaskan karier Dimas di atas karya Nadia sendiri; Nadia awalnya hampir pasrah demi kebahagiaan Ibu. | Topeng manis Dimas lepas terlalu cepat karena merasa sudah menang; kalimatnya meremehkan buku *Sela Waktu* dan sifat gugup Nadia di depan Ibu. *(Namun terdapat cacat dialog di Bab 27 baris 45 saat Dimas menyebut Saka sudah resmi pindah tetap ke Jakarta).* | Nadia tersadar sepenuhnya, membatalkan niat balikan, menceritakan seluruh kebenaran kepada Ibu (alasan putus di parkiran, Vanya, disuruh lembur bikin poster), menolak Dimas secara permanen dengan kalimat penutup *operator customer service*, serta mengganti seluruh biaya klinik, bubur, dan bensin via *m-banking*. | Ibu berbalik mendukung Nadia sepenuhnya dan melarang Dimas datang ke Rawamangun lagi; konflik dengan Dimas tuntas secara permanen. | Kenapa Dimas begitu ceroboh meremehkan buku Nadia di depan Ibu sebelum Nadia mengucapkan kata sepakat secara lisan? | Karena selama 2 tahun pacaran Nadia tidak pernah sekali pun menolak kemauan Dimas, dan melihat Ibu sudah mendukung penuh serta Nadia sudah duduk menurut di sebelahnya, Dimas merasa posisinya sudah seratus persen aman (Bab 27 baris 25 & 33). |
| **Bab 29–32:** Rabu pagi Nadia mendapati meja Saka kosong karena Saka sudah berangkat ke Jogja Selasa sore; Tari mengirim pesan WA ke Saka bahwa Nadia sudah menolak Dimas; Jumat sore di peluncuran *Sela Waktu*, Nadia menyampaikan apresiasi tulus dari panggung, Saka hadir di belakang ruangan, menunjukkan SK Mutasi Tetap di balkon (Bab 31), dan Senin berikutnya mereka kembali bekerja berdampingan serta makan malam ke Rawamangun (Bab 32). | Nadia ingin meminta maaf secara langsung dan jujur tanpa kalimat baku; Saka ingin menyelesaikan tanda tangan pelepasan Pak Bambang di Jogja dan mengejar kereta ke Gambir tepat waktu untuk peluncuran buku. | Saka sudah berangkat ke Jogja Selasa sore dan ponselnya tidak terangkat saat ditelepon Rabu pagi; kereta Saka dari Yogyakarta sempat tertahan sinyal 20 menit sebelum Jatinegara. *(Terdapat kesalahan hari di Bab 29 baris 23 dan jadwal kereta mustahil di Bab 30 baris 9).* | Nadia menghapus draf pesan WA panjang karena memilih bicara tatap muka; Tari mengabari Saka lewat WA bahwa Nadia sudah menolak Dimas; Saka mengejar tanda tangan Kamis siang di Jogja, hadir di peluncuran Jumat sore, menunjukkan SK Mutasi Tetap, dan mengelak dengan lelucon soto Kwitang sambil memutar tutup botol 2x *klik*; Senin sore Nadia menempelkan *post-it* balasan di laptop Saka. | Kesalahpahaman tuntas sepenuhnya; janji cerita perubahan diri Nadia (menolak Mbak Dinda & Riko dalam 10 detik + menagih utang Rp90.000 di Bab 32) dan *payoff* romansa terpenuhi secara utuh. | Kenapa pada Rabu pagi (Bab 29 baris 61) Nadia menghapus pesan WA permintaan maafnya dan tidak bertanya langsung kepada Pak Ramdan? | Dijelaskan di Bab 29 baris 61: Nadia berkomitmen tidak lagi bersembunyi di balik layar ponsel untuk hal sepenting itu (ingin bicara langsung di depan wajah Saka), dan ia takut bertanya ke Pak Ramdan kalau-kalau jawabannya memastikan Saka pergi selamanya; sementara jembatan informasi ke Saka tetap terjaga karena Tari mengirimkan pesan WA ke Saka (baris 67). |

---

### 2.2 Uji Pertanyaan *"Kenapa Tidak X?"* dan Larangan Alasan Abstrak (`rules/01-plot-and-causality.md` §2)

Seluruh keputusan diam atau menghindar yang diambil tokoh utama memiliki pemicu situasional, relasi kuasa, atau trauma konkret di halaman, bukan sekadar tempelan label sifat abstrak:
1. **Mengapa Nadia tidak menolak Ibu secara langsung di meja makan pada Bab 10?** Diperlihatkan pemicu konkret di halaman: keroyokan halus antara tuntutan Mbak Raras yang membawa-bawa keponakan umur 4 tahun (Daffa) dan manipulasi emosional Ibu (*"Iya, Nad, ngalah dulu sama kakaknya... Masa sama keponakan sendiri nggak tega?"*) yang sejak SD membuat Nadia takut kehilangan kasih sayang keluarga (Bab 10 baris 39–51; Bab 11 baris 61).
2. **Mengapa Saka tidak langsung mengatakan sedang mengurus mutasi tetap pada Bab 21 dan Bab 25?** Ditanam secara konkret di Bab 12 baris 21–37: pengalaman traumatis saat studionya di Yogyakarta bangkrut dan pacarnya meninggalkannya demi pria yang dianggap lebih mapan oleh orang tuanya membuat Saka memegang prinsip keras untuk tidak pernah menjanjikan masa depan kepada perempuan sebelum dokumen resminya sah di tangan. Selain itu, pada Bab 21 baris 55 percakapan mereka dipotong oleh dering telepon dari Kepala Cabang Jogja, dan pada Bab 25 baris 23–37 ucapan Nadia yang membawa-bawa bantuan Dimas kepada Ibu memicu langsung memori luka lama Saka tersebut.
3. **Mengapa Nadia menghapus pesan WhatsApp di Bab 29?** Bukan karena sungkan abstrak, melainkan bentuk pertumbuhan karakter untuk menghadapi Saka secara tatap muka di acara peluncuran hari Jumat, sementara fungsi penyampaian informasi bahwa Nadia telah menolak Dimas tetap dijalankan melalui pesan WhatsApp Tari (Bab 29 baris 61–71).

---

### 2.3 Hitungan Konflik yang Bergantung pada Pengabaian Komunikasi (`rules/01-plot-and-causality.md` §3)

Selama 32 bab, konflik kesalahpahaman utama antara Nadia dan Saka (apakah Saka akan pulang selamanya ke Yogyakarta atau mutasi tetap ke Jakarta) bergantung pada penahanan/pengabaian komunikasi langsung dalam **4 momen kunci**:

1. **Bab 14 (Baris 17–21):** Nadia melihat tab daftar sewa kos tahunan Cikini dan formulir kepegawaian antar-cabang di laptop Saka. Satu kalimat jujur dari Saka dapat meniadakan misteri mutasi, tetapi Saka mengelak (*"Teman Jogja ada yang mau pindah kerja ke daerah sini bulan depan"*) karena pada Minggu 3 hubungannya dengan Nadia masih sebatas rekan proyek dan SK-nya belum turun. **(Alasan situasional tampak di halaman; wajar sesuai premis *slow-burn*).**
2. **Bab 21 (Baris 21–57):** Pada Jumat sore Minggu 4, Nadia bertanya apakah Saka akan kembali ke cabang Yogyakarta setelah peluncuran buku. Satu kalimat penjelasan dari Saka bahwa ia sedang mengajukan mutasi tetap ke Jakarta akan langsung menghentikan krisis Bab 21–26. Namun, di halaman terdapat dua penghalang konkret: (a) prinsip Saka sejak trauma Jogja untuk tidak berjanji sebelum tanda tangan Pak Bambang turun (*"Nanti kalau tanda tangannya sudah turun, baru saya bisa cerita jelas ke kamu"*), (b) refleks pertahanan diri Nadia yang langsung menutup obrolan dengan bahasa baku operator CS karena malu dan takut membebani, serta (c) interupsi telepon Kepala Cabang Jogja pada baris 55. **(Alasan situasional tampak di halaman dan meningkatkan taruhan emosional).**
3. **Bab 24–25 (Bab 24 baris 39–60 & Bab 25 baris 15–59):** Pada Senin sore Minggu 5, Saka menemukan sketsa kursi kosong di *dummy* buku dan sudah bertanya langsung (*"Sekarang ada gambar meja saya kosong. Kamu sebenarnya mikirin apa?"*). Satu jawaban jujur dari Nadia (*"Aku sedih karena mengira Mas Saka bakal balik ke Jogja selamanya"*) dapat menyelesaikan konflik saat itu juga. Namun, tepat pada detik itu ponsel Nadia bergetar menampilkan pesan Dimas di lobi (Bab 24 baris 49–55), dan saat dikonfrontasi di lobi (Bab 25), Nadia yang terluka sekaligus ingin memancing kecemburuan Saka justru berkata bahwa Dimas sudah merawat ibunya dan meminta kesempatan kedua—yang langsung memicu trauma masa lalu Saka di Jogja. **(Eskalasi biaya pengabaian meningkat tajam: meja kerja membeku di Bab 26 dan Nadia nyaris terjebak kembali dengan Dimas di Bab 27).**
4. **Bab 29 (Baris 59–61):** Pada Rabu pagi, Nadia menelepon Saka (tidak diangkat karena Saka sedang dalam perjalanan/mengurus berkas di Jogja) lalu mengetik pesan permintaan maaf panjang tetapi menghapusnya untuk berbicara langsung di hari Jumat. Pengabaian pesan ini tidak memperpanjang kesalahpahaman secara artifisial karena pada baris 67 Tari sudah mengirim pesan WhatsApp ke Saka bahwa Nadia telah menolak Dimas semalam, dan di Bab 31 baris 63 Saka mengonfirmasi pesan Tari tersebut sudah dibacanya.

**Kesimpulan Hitungan Pengabaian Komunikasi:**
Terdapat **4 titik pengabaian/penahanan komunikasi**, di mana seluruhnya memiliki alasan situasional konkret di halaman dan biaya konflik yang terus meningkat hingga klimaks Bab 27–31. Berdasarkan `rules/01-plot-and-causality.md` §3, pola penahanan komunikasi ini bekerja sebagai bagian dari premis karakter dan **bukan** cacat struktural kerangka cerita (severity pada level kerangka: `ACCEPTABLE` / maksimal `REVIEW`).

---

### 2.4 Audit Pengetahuan Karakter & Konsistensi Motif (`rules/01-plot-and-causality.md` §4 & `rules/05-character-knowledge.md`)

1. **Penanganan Petunjuk yang Bertentangan oleh Tokoh POV (Bab 14 & 18 → Bab 20):**
   - Sesuai `rules/05-character-knowledge.md`, karena Nadia telah melihat tab kos tahunan Cikini + formulir kepegawaian antar-cabang (Bab 14 baris 17) dan mendengar dari Tari bahwa Saka menyerahkan map formulir ke Mbak Sinta HRD (Bab 18 baris 39), Nadia tidak boleh melupakan kedua petunjuk tersebut saat menyimpulkan Saka akan pulang ke Jogja di Bab 20.
   - **Hasil Pemeriksaan:** **LULUS.** Di Bab 20 baris 27, teks secara eksplisit menampilkan proses berpikir Nadia yang mengingat kedua petunjuk tersebut lalu menepisnya secara logis sesuai informasi yang ia miliki saat itu (*"Aku sempat teringat tab kos tahunan Cikini dan formulir kepegawaian antar-cabang di layar laptopnya waktu itu. Namun ingatan itu langsung kutepis karena Saka sendiri sudah bilang bahwa info kos tersebut cuma buat temannya dari Jogja, sedangkan formulir kepegawaian antar-cabang itu kupikir adalah berkas pengembalian masa tugasnya ke cabang asal"*).
2. **Konsistensi Motif Mutasi Saka (Bab 12, 20, 21, 31):**
   - **Hasil Pemeriksaan:** **LULUS.** Motif dan alasan profesional/personal Saka pindah ke Jakarta konsisten: Pak Ramdan menawarinya memegang lini buku ilustrasi baru sejak awal proyek, Saka mengajukan permohonan sejak tiga minggu sebelum Bab 31 (Minggu 2), dan perjalanan Selasa sore ke Yogyakarta murni untuk mengambil tanda tangan pelepasan Pak Bambang serta membereskan kos lama, bukan karena berubah pikiran akibat pesan Tari (Bab 31 baris 57–63).
3. **Cacat Pengetahuan Karakter & Kausalitas di Teks Manuskrip (`F-01` di Bab 19 & `F-02` di Bab 27):**
   - **Pelanggaran 1 (`F-01`, Bab 19 baris 69):** Pada Rabu sore Minggu 4, Dimas mengklaim: *"Aku lihat sendiri kamu sampai bikin sketsa kursi kosong di halaman penutup bukumu."* Ini mustahil secara pengetahuan karakter dan membalik urutan sebab-akibat: sketsa kursi kosong di halaman penutup baru digambar Nadia pada Jumat sore (Bab 21 baris 5) dan dikirim ke percetakan setelah Saka pulang (Bab 24 baris 29). Pada hari Rabu (Bab 19), sketsa itu belum ada; yang digambar Nadia pada hari Senin (Bab 18 baris 49–55) hanyalah siluet botol minum penyok berukuran 2 cm di sudut halaman ucapan terima kasih.
   - **Pelanggaran 2 (`F-02`, Bab 27 baris 45):** Pada Selasa malam Minggu 5 di rumah makan Rawamangun, Dimas berkata kepada Nadia: *"Buku esai kecil gitu biar diurus editor Jogja itu sendiri aja di panggung, toh kata anak HRD dia udah resmi pindah tetap ke Jakarta."* Kalimat ini melanggar logika motivasi Dimas (yang sejak Bab 19 sengaja memanfaatkan isu kepulangan Saka ke Jogja agar Nadia kembali padanya) sekaligus melanggar `rules/05-character-knowledge.md`: setelah mendengar langsung dari Dimas bahwa Saka sudah resmi pindah tetap ke Jakarta, Nadia sama sekali tidak menanggapi fakta krusial tersebut, malah pada baris 63 membatin *"karena takut ditinggal Saka pulang ke Yogyakarta"*, lalu sepanjang Bab 29–31 tetap bertindak seolah belum pernah mendengar kabar mutasi tetap Saka ke Jakarta.

---

## 3. Audit Daftar Rujukan Mundur dan Waktu Relatif (`--refs` / `rules/06-setup-payoff.md` & `rules/02-timeline.md`)

### 3.1 Peta Kalender Cerita (Minggu 0 s.d. Minggu 6)

- **Minggu 0 (Pra-Bab 1):**
  - **Jumat malam:** Dimas memutuskan Nadia di parkiran basement kantor (dirujuk di Bab 1 baris 15, Bab 6 baris 45, Bab 7 baris 11, Bab 10 baris 17).
  - **Sabtu:** Saka pindah ke Jakarta dan menempati kos di Tebet (dirujuk sebagai *"kemarin lusa"* pada Senin malam di Bab 2 baris 33).
- **Minggu 1:**
  - **Senin malam (19.00–19.45):** Bab 1 & Bab 2 (Tangga darurat; lembur poster Dimas & revisi Mbak Dinda).
  - **Selasa (09.00–17.05):** Bab 3 & Bab 4 (Rapat perkenalan proyek 5 minggu *Sela Waktu*; penolakan *flash disk* Mbak Dinda pukul 17.01; penempelan *post-it* kuning pertama di sampul buku sketsa).
  - **Rabu (Pagi & 12.00 siang):** Bab 5 (*Post-it* dipindah ke monitor; makan siang ayam bakar, tolak talangan Riko Rp30.000, es jeruk Saka + 2x *klik* tutup botol; pembuatan karikatur di buku sketsa).
  - **Kamis:** Nadia menolak memotong 200 kupon diskon manual dari staf administrasi (dirujuk di Bab 6 baris 7).
  - **Jumat sore (16.20–17.00):** Bab 6 & Bab 7 (Menolak pembuatan *backdrop* Dimas & Vanya; cokelat susu Saka + 2x *klik* tutup botol).
  - **Sabtu siang (10.55–14.00):** Bab 8 & Bab 9 (Berburu buku referensi di Kwitang; makan soto ayam dekat Halte Senen, karikatur Saka terbuka).
  - **Minggu siang (12.00) – petang:** Bab 10 (Makan siang di rumah Ibu di Rawamangun; Mbak Raras minta pinjam Rp4 juta untuk liburan Daffa ke Bali).
- **Minggu 2:**
  - **Senin (Pagi – 20.30 malam):** Bab 11, Bab 12, & Bab 13 (Salah warna gerobak bakso ungu terong, beringin biru dongker, kucing hijau stabilo; berteduh di kedai kopi Cikini saat hujan deras, cerita masa lalu Saka di Jogja; pukul 20.30 Nadia menelepon Ibu menolak pinjaman Rp4 juta dan memberi Rp500.000 untuk Daffa). *(Pada minggu ke-2 ini pula Saka mengajukan permohonan resmi mutasi tetap ke Jakarta, dirujuk *"tiga minggu yang lalu"* pada Jumat Minggu 5 di Bab 31 baris 51).*
- **Minggu 3:**
  - **Kamis (Siang – 18.15 malam):** Bab 14, Bab 15, Bab 16, & Bab 17 (*"Hampir tiga minggu duduk satu meja"*; tablet gambar baru; Nadia memergoki tab kos tahunan Cikini & formulir antar-cabang di laptop Saka; Dimas menyindir sampul; pukul 15.30 rapat evaluasi sampul; pukul 17.30 satu payung sepanjang Cikini; pukul 18.15 martabak manis di teras kos & terbongkarnya rahasia 2x *klik* tutup botol).
  - **Jumat:** Saka menyerahkan map formulir ke Mbak Sinta HRD (dilihat Tari, dirujuk pada Senin Minggu 4 di Bab 18 baris 39).
- **Minggu 4:**
  - **Senin (08.50 – siang):** Bab 18 (*"Memasuki minggu keempat"*; biskuit asin & es kopi susu; Nadia menggambar siluet botol minum penyok 2 cm di halaman ucapan terima kasih).
  - **Rabu sore (15.50):** Bab 19 (Dimas meminta maaf di dapur kantor setelah putus dari Vanya dan membisikkan bahwa penugasan Saka hanya 5 minggu).
  - **Jumat (13.15 siang – 17.05 sore):** Bab 20 & Bab 21 (Nadia mendengar telepon Pak Ramdan dengan Pak Bambang dan melihat amplop Cabang Yogyakarta; sore hari Saka mengirim file akhir kecuali halaman penutup ke percetakan; Nadia menyelipkan sketsa kursi kosong di halaman penutup dan menolak pulang bareng Saka dengan bahasa baku).
  - **Sabtu (09.00 pagi – malam):** Bab 22 & Bab 23 (Vertigo Ibu kambuh di Rawamangun; Dimas mengantar ke Klinik Pratama Rawamangun dan menunggu 3 jam; sore hari Dimas mengaku salah pada Ibu dan Ibu membujuk Nadia; malam hari Nadia setuju bertemu Dimas di lobi kantor hari Senin).
- **Minggu 5:**
  - **Senin sore (16.00–17.15):** Bab 24 & Bab 25 (Pemeriksaan *dummy* cetak percobaan *Sela Waktu*; Saka melihat sketsa kursi kosong; pesan WA Dimas masuk pukul 16.58; pertengkaran tanpa suara tinggi di lobi pukul 17.10; Nadia menyetujui makan malam keluarga bersama Dimas untuk Selasa malam).
  - **Selasa (09.00 pagi – 20.30 malam):** Bab 26, Bab 27, & Bab 28 (Pagi–siang meja nomor 4 membeku, pukul 10.00 tanda tangan persetujuan naik cetak terbatas edisi peluncuran, siang hari Nadia mencopot *post-it* dari monitor ke buku sketsa; pukul 17.30 Saka berangkat ke Jogja naik kereta malam; pukul 19.30–20.00 makan malam di RM Sederhana Rasa Rawamangun, topeng Dimas terlepas, Nadia membuka kebenaran di depan Ibu dan menolak Dimas secara permanen).
  - **Rabu pagi (08.15):** Bab 29 (Nadia datang membawa kopi hitam tetapi meja Saka sudah kosong; menemukan catatan pensil merah Saka di halaman penutup *dummy*; Tari sudah mengirim pesan WA ke Saka tentang penolakan Dimas).
  - **Kamis siang:** Pak Bambang menandatangani pelepasan resmi Saka di Yogyakarta (dirujuk di Bab 31 baris 51 & 63).
  - **Jumat sore (16.15–18.00):** Bab 30 & Bab 31 (Peluncuran buku *Sela Waktu* di Aula Toko Buku Cikini; pengakuan Nadia di panggung; Saka tiba dari Stasiun Gambir; penjelasan SK Mutasi Tetap dan 2x *klik* tutup botol di balkon teras samping).
- **Minggu 6:**
  - **Senin sore (16.55–17.05):** Bab 32 (Tiga hari pasca-peluncuran; *post-it* ditempel kembali di monitor; Nadia menolak titipan Mbak Dinda & Riko dalam 10 detik sekaligus menagih utang ayam bakar Rp90.000; menempelkan *post-it* balasan di laptop Saka dan berangkat makan malam ke rumah Ibu di Rawamangun).

---

### 3.2 Evaluasi Lengkap Hasil Eksekusi `audit_core.py --refs` (Beserta Rujukan Kontekstual Tambahan)

Pemindaian mekanis dengan `python3 scripts/audit_core.py --root /tmp/uji-canary` menghasilkan `Mechanical findings: 0` pada 32 file bab, sedangkan `python3 scripts/audit_core.py --root /tmp/uji-canary --refs` menghasilkan **77 entri baris rujukan**. Berikut adalah penilaian editorial untuk **setiap entri** ditambah rujukan mundur kontekstual di luar regex:

| Bab & Baris | Kata Kunci | Kutipan Teks | Penilaian & Verifikasi Silang (`rules/06-setup-payoff.md`) | Status |
|---|---|---|---|---|
| **Bab 1, Baris 7** | `dulu` | `"Kalau gue customer service, telepon lo udah gue matiin dari dulu, Dimas!"` | Mengacu pada masa pacaran 2 tahun dengan Dimas sebelum putus. Konsisten dengan premis dan Bab 1 baris 13. | **LULUS** |
| **Bab 1, Baris 17** | `waktu itu` | `"Aku capek, Nad," katanya waktu itu sambil memegang tali helm.` | Mengacu pada malam saat Dimas memutuskan Nadia di parkiran basement pada *"Jumat malam lalu"* (baris 15, tiga hari sebelum Senin malam Bab 1). Konsisten. | **LULUS** |
| **Bab 2, Baris 33** | `kemarin lusa` | `"Saya baru pindah ke Jakarta kemarin lusa."` | Bab 2 berlangsung Senin malam; *kemarin lusa* adalah hari Sabtu sebelum minggu pertama proyek dimulai. Konsisten dengan Bab 3 baris 35 (Selasa pagi hari pertama Saka masuk kantor Jakarta). | **LULUS** |
| **Bab 3, Baris 17** | `Tadi pagi` | `"Tadi pagi jam tujuh lewat lima belas sudah saya kirim ke email Mbak Dinda"` | Bab 3 berlangsung Selasa pagi menjelang pukul 09.00; mengacu pada revisi sampul titipan Mbak Dinda dari Bab 1 baris 11 yang diselesaikan Nadia sebelum berangkat kerja. Konsisten. | **LULUS** |
| **Bab 3, Baris 21** | `Kemarin` | `"Kemarin gue dengar sendiri di pantry."` | Bab 3 adalah Selasa pagi; *kemarin* adalah hari Senin saat Mbak Dinda menitipkan revisi ke Nadia dengan alasan ambil rapor anak padahal mau nonton bioskop bersama suaminya (cocok dengan Bab 1 baris 33). | **LULUS** |
| **Bab 3, Baris 53** | `tadi malam` | `Duduk semeja dengan pria yang tadi malam mendengarkan seluruh aib makianku di tangga darurat?!` | Bab 3 Selasa pagi merujuk pada kejadian Senin malam di tangga darurat (Bab 1–2). Cocok. | **LULUS** |
| **Bab 4, Baris 39** | `dulu` | `Namun sebelum benda itu menyentuh mejaku, Saka sudah lebih dulu berdiri tegak di samping kursinya.` | Frasa urutan tindakan (*"lebih dulu"*), bukan rujukan peristiwa masa lalu. | **LULUS (Non-Rujukan)** |
| **Bab 5, Baris 3** | `kemarin` | `...sambil melempar lirikan masam karena urusan flash disk kemarin sore...` | Bab 5 berlangsung Rabu siang; *kemarin sore* adalah Selasa sore pukul 17.01 saat Saka menolak *flash disk* putih Mbak Dinda (Bab 4 baris 33–55). Detail benda dan waktu cocok 100%. | **LULUS** |
| **Bab 5, Baris 13** | `dulu` | `"Talangin punya gue dulu dong?"` | Kata keterangan (*"terlebih dahulu"*), bukan rujukan masa lalu. | **LULUS (Non-Rujukan)** |
| **Bab 5, Baris 17** | `Bulan lalu` | `Bulan lalu saja Riko sudah tiga kali memakai alasan dompet tertinggal.` | Latar kebiasaan Riko sebelum Bab 1 dengan total utang Rp90.000 (3 x Rp30.000), yang kemudian dibayar (*callback*) secara presisi di Bab 32 baris 33. | **LULUS** |
| **Bab 6, Baris 7** | `Kemarin` | `Kemarin waktu staf administrasi meminta bantuan memotong dua ratus lembar kupon diskon secara manual...` | Bab 6 berlangsung Jumat sore (2 hari setelah Rabu Bab 5, disebut *"dua hari lalu"* di awal paragraf yang sama); *kemarin* adalah hari Kamis Minggu 1. Kronologi hari cocok. | **LULUS** |
| **Bab 6, Baris 15** | `Waktu itu` | `"Buku Sela Waktu itu kan tentang orang kota yang kecapekan kerja sampai lupa waktu."` | Terjaring regex karena judul buku *Sela Waktu* diikuti kata tunjuk *itu*. Bukan rujukan waktu masa lalu. | **LULUS (Non-Rujukan)** |
| **Bab 6, Baris 35** | `dulu` | `...ujar Dimas dengan intonasi memohon yang dulu selalu berhasil meluluhkan hatiku.` | Mengacu pada kebiasaan selama 2 tahun berpacaran. Konsisten. | **LULUS** |
| **Bab 6, Baris 45** | `minggu lalu` | `...menggunakan sifat sungkanku yang minggu lalu dia jadikan alasan untuk mengakhiri hubungan kami!` | Bab 6 adalah Jumat sore Minggu 1; merujuk pada putusnya hubungan mereka pada Jumat malam Minggu 0 (Bab 1 baris 15–17). Tepat satu minggu sebelumnya. | **LULUS** |
| **Bab 7, Baris 11** | `minggu lalu` | `Ingatan Jumat malam minggu lalu mendadak melintas di kepalaku, saat aku berdiri kaku di parkiran motor...` | Bab 7 masih berlangsung pada Jumat sore Minggu 1; merujuk pada Jumat malam Minggu 0 di parkiran basement (Bab 1 baris 15). Cocok. | **LULUS** |
| **Bab 7, Baris 29** | `kemarin` | `"Loh, kan cuma tinggal tarik ukuran dari file poster yang kemarin, Nad," desak Dimas kesal.` | Bahasa lisan Dimas pada Jumat sore yang merujuk pada file poster awal minggu yang sama (dititipkan Senin di Bab 1 baris 11 & 29, diunggah Nadia ke folder bersama Selasa pagi sesuai Bab 7 baris 31). Penggunaan *"yang kemarin"* untuk beberapa hari lalu dalam minggu yang sama wajar dalam dialog lisan. | **LULUS** |
| **Bab 7, Baris 61** | `Tadi pagi` | `"Tadi pagi kasir minimarket depan stasiun ngasih promo beli kopi botol," jawab Saka santai.` | Alasan bohong Saka pada Jumat sore saat memberikan cokelat susu, yang langsung dibantah pengamatan Nadia di baris 67 bahwa pagi tadi Saka menyeduh kopi hitam bubuk di dapur lantai tiga. | **LULUS** |
| **Bab 8, Baris 25** | `Dulu` | `Dulu waktu masih pacaran sama Dimas, kalau kami jalan di trotoar lalu dia pindah ke sisi luar...` | Latar perbandingan masa pacaran 2 tahun dengan Dimas. Konsisten dengan karakterisasi Dimas yang suka pamer. | **LULUS** |
| **Bab 8, Baris 31** | `dulu` | `"Di naskah kan ada bagian yang bahas bioskop tua sama toko roti zaman dulu."` | Frasa nomina (*"zaman dulu"*), bukan rujukan peristiwa antarbab. | **LULUS (Non-Rujukan)** |
| **Bab 8, Baris 35** | `pernah bilang` | `"Dimas pernah bilang gaya kayak gini kusam dan kurang komersial."` | Latar masa pacaran dengan Dimas yang konsisten dengan komentar Dimas di Bab 14 baris 39–41 (*"Kok warnanya agak redup gini... warna pilihan kamu jauh lebih cerah dan komersial"*). | **LULUS** |
| **Bab 8, Baris 37** | `dulu` | `Tangan Saka yang sedang menarik sebuah buku kumpulan foto Jakarta tempo dulu berhenti bergerak.` | Frasa nomina (*"tempo dulu"*). | **LULUS (Non-Rujukan)** |
| **Bab 8, Baris 43** | `Waktu itu` | `"Berarti yang tahu cocok atau enggaknya gambar itu sama isi naskah Sela Waktu itu saya sama kamu, bukan dia"` | Judul buku *Sela Waktu* diikuti kata *itu*. | **LULUS (Non-Rujukan)** |
| **Bab 9, Baris 11–17** *(kontekstual)* | `Waktu makan ayam bakar`, `lima hari`, `hari Rabu lalu` | `"Waktu makan ayam bakar, kamu nyisihin seledri..."` / `"laki-laki yang baru lima hari duduk di sebelah mejaku"` / `"goresan pensilku hari Rabu lalu"` | Bab 9 adalah Sabtu siang Minggu 1: makan ayam bakar terjadi Rabu (Bab 5); Selasa s.d. Sabtu adalah tepat 5 hari sejak mereka semeja di Bab 3; Rabu lalu adalah hari kedua mereka semeja (baris 51). Sangat presisi. | **LULUS** |
| **Bab 9, Baris 39** | `dulu` | `...mata Saka sudah lebih dulu tertuju ke halaman belakang...` | Urutan gerak (*"lebih dulu"*). | **LULUS (Non-Rujukan)** |
| **Bab 10, Baris 17** | `minggu lalu` | `...hubungan dua tahunku dengan calon menantu kesayangannya itu sudah tamat sejak Jumat minggu lalu.` | Bab 10 berlangsung Minggu siang (akhir Minggu 1); mengacu pada Jumat malam sebelum Minggu 1 (9 hari lalu, dibedakan dari Jumat kemarin/2 hari lalu). Wajar dalam penyebutan mingguan. | **LULUS** |
| **Bab 10, Baris 27** | `kemarin` | `"Iya, makanya Mbak udah pesan tiket pesawat dari kemarin," lanjut Mbak Raras santai.` | Ucapan Mbak Raras pada Minggu siang merujuk pada pemesanan tiket hari Sabtu. Konsisten. | **LULUS** |
| **Bab 10, Baris 31, 45, 53** | `dulu` | `"Mbak pinjam tabungan kamu dulu ya empat juta?"` / `"ngalah dulu sama kakaknya"` / `"Aku cek saldo rekeningku dulu nanti malam di kos"` | Kata keterangan (*"terlebih dahulu"* / sementara). | **LULUS (Non-Rujukan)** |
| **Bab 11, Baris 31** | `dulu` | `"Teduh di situ dulu," ajak Saka...` | Kata keterangan (*"terlebih dahulu"*). | **LULUS (Non-Rujukan)** |
| **Bab 11, Baris 49 & 51** | `kemarin`, `Kemarin` | `Beban yang sejak kemarin sore mengganjal... "Kemarin waktu pulang ke Rawamangun, Mbak Raras minta pinjam uang tabunganku"` | Bab 11 berlangsung Senin sore (Minggu 2); *kemarin* adalah Minggu siang–sore di Rawamangun (Bab 10). Lokasi, pelaku, dan nominal (Rp4 juta, tabungan 10 bulan, tablet gambar) cocok 100%. | **LULUS** |
| **Bab 12, Baris 13, 21, 33** | `Dulu` | `"Dulu waktu baru lulus kuliah di Jogja..."` / `"Dulu saya merintis studio penyuntingan kecil..."` / `Dulu kupikir dia sengaja bergaya membawa botol usang.` | Latar masa lalu Saka di Yogyakarta sebelum pindah ke Jakarta dan asumsi awal Nadia di Bab 1–2. Konsisten dan menjadi fondasi callback di Bab 21, 25, dan 31. | **LULUS** |
| **Bab 13, Baris 25** | `Kemarin`, `dulu` | `"Kemarin siang kan kamu bilangnya mau cek saldo dulu."` | Bab 13 berlangsung Senin malam pukul 20.30 (Minggu 2); ucapan Ibu merujuk tepat pada kalimat Nadia di meja makan pada Minggu siang (Bab 10 baris 53). | **LULUS** |
| **Bab 13, Baris 67** | `ceritanya` | `Makasih banyak ya, Mas, buat ceritanya sama tahu isinya tadi sore.` | Merujuk pada tahu isi hangat di kedai kopi (Bab 11 baris 35) dan cerita masa lalu Saka di Jogja (Bab 12) pada Senin sore/petang tadi. Cocok. | **LULUS** |
| **Bab 14, Baris 5** | `dulu` | `...tumpukan map plastik warna-warni titipan warga kantor yang dulu selalu menghalangi pandanganku kini sudah punah sama sekali.` | Merujuk pada kondisi meja Nadia di Bab 1–4 sebelum berlatih menolak. Cocok. | **LULUS** |
| **Bab 14, Baris 15** | `waktu itu` | `"Asal jangan dikasih warna hijau stabilo lagi kayak waktu itu."` | Merujuk pada kejadian Senin Minggu 2 (Bab 11 baris 45: *"Jadi itu yang dari tadi bikin kucing kampung jadi hijau stabilo?"*). Detail warna dan objek cocok 100%. | **LULUS** |
| **Bab 14, Baris 27** | `kemarin` | `...bahwa Vanya kemarin sempat ngambek dan menolak membantu Dimas menyiapkan laporan bulanan...` | Bab 14 adalah Kamis siang Minggu 3; *kemarin* adalah Rabu Minggu 3. Menyiapkan setup putusnya Dimas dan Vanya di Bab 19. | **LULUS** |
| **Bab 14, Baris 29, 41, 45** | `dulu`, `Dulu` | Merujuk pada kesabaran Nadia dan diskusi warna dengan Dimas semasa pacaran dulu (konsisten dengan Bab 8 baris 35 & 47). | **LULUS** |
| **Bab 15, Baris 21** | `Dulu` | `Dulu waktu kami masih berpacaran, setiap kali ada rapat gabungan dan ide desainku dikritik orang lain, Dimas tidak pernah sekali pun membela karyaku.` | Latar masa pacaran 2 tahun yang kontras dengan pembelaan Saka di Bab 15. Konsisten. | **LULUS** |
| **Bab 15, Baris 23 & 61** | `dulu` | `...Saka lebih dulu menggeser laptop peraknya...` / `...berjalan lebih dulu keluar pintu ruang rapat...` | Urutan tindakan (*"lebih dulu"*). | **LULUS (Non-Rujukan)** |
| **Bab 16, Baris 47** | `Dulu` | `Dulu waktu sama Dimas, baru kena gerimis dua tetes saja dia sudah sibuk menyelamatkan rambutnya sendiri pakai map kertas.` | Latar masa pacaran yang dikontraskan dengan tindakan Saka memiringkan payung demi melindungi Nadia dan buku sketsanya. Konsisten. | **LULUS** |
| **Bab 17, Baris 25** | `katanya` | `...sama sekali tidak ada kotak kedua yang katanya berisi martabak telur itu.` | Merujuk pada klaim bohong Saka enam baris sebelumnya (Bab 17 baris 19: *"Tadi niatnya beli martabak telur buat makan di kereta"*). Cocok. | **LULUS** |
| **Bab 17, Baris 51–53** *(kontekstual)* | `Waktu di warung ayam bakar`, `Waktu ngasih cokelat` | `"Waktu di warung ayam bakar, Mas Saka ngaku abangnya salah hitung es jeruk sambil muter tutup botol... Waktu ngasih cokelat sehabis nolak Dimas, Mas Saka ngaku dapat hadiah beli kopi sambil muter botol."` | Merujuk tepat pada kejadian di Bab 5 baris 63–71 dan Bab 7 baris 61–65. Detail alasan bohong dan gestur cocok 100%. | **LULUS** |
| **Bab 18, Baris 3 & 11** *(kontekstual)* | `malam Jumat lalu`, `Kamis sore` | `Sejak rahasia tutup botol minum hitamnya terbongkar di teras kosku malam Jumat lalu...` / `"Kamis sore Mas Saka bilang nggak suka makanan manis"` | Bab 18 adalah Senin pagi Minggu 4; merujuk pada Kamis petang/malam (malam Jumat) Minggu 3 di Bab 17 baris 23 (*"Saya kan nggak suka makanan manis"*). Cocok. | **LULUS** |
| **Bab 18, Baris 17 & 19** | `dulu` | `...dibandingkan hari pertama dulu. Kalau dulu aku duduk di kursi ini dengan bahu tegang...` | Merujuk pada Bab 3–4 saat pertama kali duduk di meja proyek nomor empat. Cocok. | **LULUS** |
| **Bab 18, Baris 29** *(kontekstual)* | `Kamis sore` | `"Kamis sore gue lihat dari jendela atas, Mas Saka balik dari stasiun buat mayungin lo jalan kaki."` | Merujuk pada kejadian Bab 16 baris 7–15 (Kamis sore Minggu 3). Cocok. | **LULUS** |
| **Bab 18, Baris 39 & 43** | `kemarin`, `waktu itu` | `"Hari Jumat kemarin waktu antar berkas personalia, gue lihat Mas Saka nyerahin map formulir ke Mbak Sinta HRD."` / `...tidak terlalu memikirkan ucapan Tari waktu itu.` | Bab 18 adalah Senin siang Minggu 4; *Hari Jumat kemarin* adalah Jumat Minggu 3 (sehari setelah Kamis Bab 14–17). Menjadi setup penting untuk Bab 20 baris 27 dan Bab 31 baris 53. | **LULUS** |
| **Bab 18, Baris 51** | `ceritanya` | `...tapi siapa pun yang tahu ceritanya pasti langsung mengenali benda apa itu.` | Merujuk pada cerita asal-usul botol minum hitam penyok milik Saka (Bab 12 baris 31–35). Cocok. | **LULUS** |
| **Bab 19, Baris 5** | `kemarin` | `Sejak kemarin, suasana di divisi pemasaran agak tegang.` | Bab 19 berlangsung Rabu sore Minggu 4; *kemarin* adalah Selasa Minggu 4 setelah Dimas dan Vanya ribut soal pembagian tugas pameran akhir pekan lalu. Cocok. | **LULUS** |
| **Bab 19, Baris 13 & 17** | `dulu` | `...seperti waktu dia menyuruhku membuat poster dulu.` / `Persis takaran teh hangat yang dulu selalu dibuatkannya untukku...` | Merujuk pada Bab 1 & Bab 6–7 (menyuruh buat poster/backdrop) dan masa awal pacaran 2 tahun lalu. Cocok. | **LULUS** |
| **Bab 19, Baris 29** *(kontekstual)* | `Waktu di parkiran` | `"Waktu di parkiran, terus waktu aku nyuruh kamu depan Vanya, aku bodoh banget."` | Merujuk pada Jumat malam pra-Bab 1 (parkiran) dan Bab 6–7 (menyuruh di depan Vanya). Cocok. | **LULUS** |
| **Bab 19, Baris 65** | `tadi pagi` | `"Orang HRD tadi pagi baru aja bahas masa tugas Mas Saka."` | Klaim lisan Dimas pada Rabu sore tentang pembicaraan HRD pada Rabu pagi. | **LULUS** |
| **Bab 19, Baris 69** *(kontekstual)* | *(rujukan ke sketsa kursi kosong)* | `"Aku lihat sendiri kamu sampai bikin sketsa kursi kosong di halaman penutup bukumu."` | **KONTRADIKSI / ANAKRONISME (`F-01`):** Pada Rabu sore (Bab 19), Nadia **belum** membuat sketsa kursi kosong di halaman penutup. Sketsa kursi kosong baru dibuat Nadia pada **Jumat sore (Bab 21 baris 5)** setelah mendengar telepon Pak Ramdan di Bab 20 (dan ditegaskan kembali di Bab 24 baris 29 & Bab 29 baris 15 bahwa gambar itu dibuat hari Jumat). Pada hari Senin (Bab 18 baris 49–55), Nadia baru menggambar siluet botol minum penyok ukuran 2 cm di halaman ucapan terima kasih. | **TEMUAN (`ERROR` / `HIGH`)** |
| **Bab 20, Baris 5** | `dulu` | `Waktu Pak Ramdan memperkenalkan Saka di ruang rapat pada hari pertama dulu, Pak Ramdan memang sempat menyebut bahwa kami dipasangkan duduk semeja selama lima minggu...` | Merujuk tepat pada ucapan Pak Ramdan di Bab 3 baris 47 (*"Untuk proyek buku esai dan ilustrasi kota Sela Waktu lima minggu ke depan..."*). Cocok 100%. | **LULUS** |
| **Bab 20, Baris 27** | `waktu itu`, `Senin lalu` | `Aku sempat teringat tab kos tahunan Cikini dan formulir kepegawaian antar-cabang di layar laptopnya waktu itu... Kalimat Tari Senin lalu soal formulir di meja Mbak Sinta HRD...` | Merujuk tepat pada Bab 14 baris 17–21 (Kamis Minggu 3) dan Bab 18 baris 39 (Senin Minggu 4). Detail isi layar dan nama Mbak Sinta HRD cocok 100%. | **LULUS** |
| **Bab 21, Baris 25** | `ceritanya`, `dulu` | `Aku teringat ceritanya di kedai kopi dulu: sejak ditinggal mantannya di Yogyakarta saat studionya bangkrut, Saka paling pantang mengumbar janji...` | Merujuk tepat pada cerita Saka di kedai kopi Cikini pada Bab 12 baris 21–37. Detail lokasi, kejadian, dan prinsip hidup Saka cocok 100%. | **LULUS** |
| **Bab 22, Baris 5** | `kemarin` | `Mbak Raras sedang berada di Bandung bersama keluarganya sejak Jumat sore kemarin.` | Bab 22 berlangsung Sabtu pagi (akhir Minggu 4); *Jumat sore kemarin* adalah sehari sebelumnya. Cocok. | **LULUS** |
| **Bab 22, Baris 21, 33, 57** | `tadi pagi`, `Tadi pagi` | Merujuk pada telepon Ibu pukul 06.30 pagi dan kedatangan Dimas pada Sabtu pagi itu. | Konsisten di dalam Bab 22. | **LULUS** |
| **Bab 22, Baris 45** | `Dulu` | `Dulu waktu kami masih pacaran, kalau diajak mengantar ibuku ke pasar...` | Latar masa pacaran 2 tahun. Konsisten. | **LULUS** |
| **Bab 22, Baris 59** | `kemarin`, `hari Rabu lalu` | `...jawaban dingin Saka kemarin sore soal kepulangannya ke Yogyakarta... penyesalan Dimas di dapur kantor hari Rabu lalu...` | Bab 22 adalah Sabtu siang; *kemarin sore* = Jumat sore (Bab 21); *hari Rabu lalu* = Rabu sore di dapur kantor (Bab 19). Sangat presisi. | **LULUS** |
| **Bab 23, Baris 9** | `dulu` | `Sikap jemawa yang dulu melekat padanya kini lenyap tak berbekas.` | Merujuk pada sikap Dimas di Bab 1–15. Cocok. | **LULUS** |
| **Bab 23, Baris 17** | `waktu itu` | `"Aku bilang kalau waktu itu aku bersikap keliru dan kekanak-kanakan sampai menyakiti hatimu."` | Merujuk pada malam saat Dimas memutuskan Nadia di parkiran. Cocok. | **LULUS** |
| **Bab 23, Baris 41** | `dua minggu lalu` | `Tak ada ketegangan kaku seperti saat kami memperdebatkan permintaan Mbak Raras dua minggu lalu.` | **MELESET RINGAN (`F-07`):** Perdebatan permintaan uang Rp4 juta Mbak Raras terjadi pada Minggu siang akhir Minggu 1 (Bab 10) dan Senin malam awal Minggu 2 (Bab 13). Bab 23 berlangsung pada Sabtu sore akhir Minggu 4 (sekitar 19–20 hari atau hampir **tiga minggu** kemudian, mengingat di Bab 14 sudah disebut *"Hampir tiga minggu"* dan di Bab 18 *"Memasuki minggu keempat"*). | **TEMUAN (`REVIEW`)** |
| **Bab 25, Baris 21** *(kontekstual)* | *(rujukan ke kedai kopi)* | `"Kamu sendiri yang bilang di kedai kopi kalau urusan kalian sudah selesai," kata Saka tajam.` | **SALAH DETAIL LOKASI & TANPA TANAM (`F-03`):** Dalam adegan kedai kopi saat hujan deras (Bab 11 & Bab 12), Nadia **tidak pernah sekali pun** menyebut nama Dimas atau membahas urusannya dengan Dimas (ia hanya menceritakan permintaan Rp4 juta Mbak Raras, bujukan Ibu, dan kabel tablet gambar yang rusak). Saka mengetahui Nadia sudah putus dari Dimas lewat amukan di tangga darurat (Bab 1–2) dan penolakan *backdrop* di meja kerja (Bab 6–7), bukan di kedai kopi. | **TEMUAN (`ERROR`)** |
| **Bab 25, Baris 35** | `dulu` | `Namun aku lupa cerita Saka di kedai kopi dulu.` | Merujuk pada cerita Saka di Bab 12 baris 27 tentang mantan kekasihnya di Jogja yang memilih laki-laki pilihan orang tuanya saat studio Saka bangkrut. Detail cocok 100%. | **LULUS** |
| **Bab 26, Baris 19** | `katanya` | `"Ibu kamu tadi udah telepon aku lagi, katanya nggak sabar mau makan ikan bakar bareng kita malam ini."` | Kalimat lisan Dimas mengutip telepon Ibu pada Selasa siang. Cocok. | **LULUS** |
| **Bab 26, Baris 29** | `kemarin` | `"Waktu Ibu sakit kemarin, dia yang ngurusin semuanya, Tar," belaku pelan.` | Bab 26 adalah Selasa siang, sedangkan Ibu sakit pada hari Sabtu (Bab 22, tiga hari sebelumnya). Dalam percakapan lisan akrab bahasa Indonesia, kata *"kemarin"* lazim digunakan secara longgar untuk menunjuk kejadian beberapa hari yang baru lewat (*"waktu Ibu sakit kemarin"*). | **LULUS (Lisan Wajar)** |
| **Bab 26, Baris 37 & 39** | `kemarin` | `...sejak kemarin sore kusembunyikan... "Mas Saka kemarin bilang kalau balik sama Dimas itu pilihan paling masuk akal"` | Bab 26 berlangsung Selasa siang; *kemarin sore* merujuk tepat pada pertengkaran di lobi gedung pada Senin sore pukul 17.10 (Bab 25 baris 49). Cocok 100%. | **LULUS** |
| **Bab 26, Baris 43** | `dulu` | `"Nad, mantan gue zaman kuliah dulu persis kayak si Dimas," kata Tari pelan.` | Latar masa kuliah Tari. Konsisten. | **LULUS** |
| **Bab 26, Baris 51** *(kontekstual)* | `tempo hari` | `Aku sempat teringat cerita Saka tempo hari soal adik perempuannya yang kuliah di Surabaya.` | **RUJUKAN TANPA TANAM (`F-04`):** Di sepanjang Bab 1 s.d. Bab 25 (maupun di `outline.md`), Saka **tidak pernah** bercerita bahwa ia memiliki adik perempuan yang kuliah di Surabaya. Selain tidak pernah ditanam, kalimat ini terselip secara terputus di tengah adegan Nadia menatap *post-it* kuning di bingkai monitornya. | **TEMUAN (`ERROR`)** |
| **Bab 26, Baris 53** | `empat minggu lalu` | `Kertas post-it kuning bertuliskan Bilang enggak itu nggak bikin langit runtuh yang ditempelkan Saka empat minggu lalu...` | *Post-it* ditempelkan Saka pada Selasa sore Minggu 1 (Bab 4 baris 67–73); Bab 26 berlangsung pada Selasa siang Minggu 5 = tepat 4 minggu lalu. Sangat presisi. | **LULUS** |
| **Bab 27, Baris 13 & 47** | `dulu` | `"Mulai malam ini kita buka lembaran baru lagi kayak dulu ya?"` / `"Lagian Nadia kan dari dulu gugup kalau ngomong depan orang banyak."` | Merujuk pada masa pacaran 2 tahun sebelumnya. Konsisten. | **LULUS** |
| **Bab 28, Baris 17, 23, 41** | `dulu`, `waktu itu` | `"Waktu di parkiran kantor, Mas Dimas yang memutuskan hubungan kami lebih dulu."` / `"Bu, waktu itu saya cuma lagi capek kerjaan..."` / `...yang dulu sempat menangisi laki-laki seperti ini di tangga darurat.` | Merujuk pada kejadian putus di parkiran (Bab 1 baris 15–17) dan menangis di tangga darurat (Bab 1). Cocok 100%. | **LULUS** |
| **Bab 28, Baris 57** | `kemarin` | `"Semua biaya klinik, bubur, dan bensin kemarin biar ditransfer balik sama Nadia malam ini"` | Penggunaan lisan *"kemarin"* oleh Ibu pada Selasa malam untuk menunjuk kejadian hari Sabtu lalu (Bab 22). Wajar dalam dialog lisan. | **LULUS (Lisan Wajar)** |
| **Bab 29, Baris 5** | `Tadi pagi` | `Tadi pagi waktu lewat di depan kedai kopi bawah, aku bahkan sengaja membeli segelas kopi hitam panas tanpa gula kesukaan Saka.` | Bab 29 berlangsung Rabu pagi pukul 08.15; merujuk pada perjalanan Nadia beberapa menit sebelum naik lift ke lantai tiga. Cocok. | **LULUS** |
| **Bab 29, Baris 7** | `kemarin` | `Aku mau meminta maaf karena kemarin sempat goyah, sempat termakan hasutan masa lalu, dan sempat bicara menyakitkan di lobi gedung.` | Merujuk pada rangkaian sikap Nadia pada hari Senin–Selasa kemarin (Bab 25–26). Cocok. | **LULUS** |
| **Bab 29, Baris 23** *(kontekstual)* | `Senin sore` | `"Mas Saka Senin sore udah pamit ke Jogja lebih awal."` | **KONTRADIKSI KRONOLOGI / SALAH HARI (`F-05`):** Bab 29 berlangsung **Rabu pagi**. Sehari sebelumnya (**Selasa pagi s.d. siang**, Bab 26), Saka masih bekerja di meja nomor empat dan menyerahkan lembar persetujuan naik cetak kepada Nadia pukul 10.00! Bahkan empat baris setelah kalimat Riko ini (Bab 29 baris 27, 29, 39), Nadia dan Riko sendiri menyebut Saka berangkat **`kemarin sore`** (*"Kemarin sore jam setengah enam. Itu tepat setelah aku pergi meninggalkan kantor untuk menghadiri makan malam bersama Dimas di Rawamangun"* = Selasa sore), dan di Bab 31 baris 61 Saka juga menyebut *"Perjalanan Selasa sore itu"*. Kata *"Senin sore"* di baris 23 jelas salah dan harusnya *"kemarin sore"* / *"Selasa sore"*. | **TEMUAN (`ERROR`)** |
| **Bab 29, Baris 27, 29, 33, 39** | `kemarin`, `Katanya`, `Kemarin` | `"Berangkat ke Jogja kemarin sore?"` / `"Berkas naik cetak kan udah beres kemarin"` / `"Katanya urusan cetak di sini udah beres..."` / `Kemarin sore jam setengah enam.` | Bab 29 adalah Rabu pagi; *kemarin sore* adalah Selasa sore pukul 17.30 setelah berkas naik cetak selesai Selasa siang (Bab 26 baris 7–9) dan bertepatan dengan keberangkatan Nadia ke Rawamangun (Bab 26 baris 19). Konsisten dengan Bab 26 dan Bab 31 baris 61 (setelah kata *"Senin sore"* di baris 23 diperbaiki). | **LULUS** |
| **Bab 29, Baris 63 & 65** | `Tadi malam`, `dulu` | `Tadi malam, setelah pulang dari Rawamangun, aku sempat mengirim pesan kepada Tari.` / `"Lo tenang dulu, Nad"` | Bab 29 Rabu pagi; *tadi malam* adalah Selasa malam sepulang dari RM Sederhana Rasa Rawamangun (Bab 28). Cocok. | **LULUS** |
| **Bab 30, Baris 9** | `dulu` | `...Pak Ramdan memintaku memulai sesi diskusi lebih dulu sambil menunggu Saka menyusul.` | Urutan kegiatan (*"lebih dulu"*). (Namun kalimat yang sama mengandung kesalahan jadwal kereta api `F-06`). | **LULUS (Kata `dulu`) / TEMUAN (`F-06` Jadwal Kereta)** |
| **Bab 30, Baris 21** | `kemarin`, `Selasa malam lalu` | `Sejak kemarin malam aku sudah berlatih bicara berkali-kali di depan cermin kamar... seperti yang diejekkan Dimas di rumah makan Selasa malam lalu.` | Bab 30 berlangsung Jumat sore; *kemarin malam* = Kamis malam; *Selasa malam lalu* = makan malam di rumah makan Rawamangun (Bab 27 baris 47). Sangat presisi. | **LULUS** |
| **Bab 30, Baris 27** | `Dulu` | `"Dulu saya tipe orang yang punya penyakit nggak enakan kronis."` | Merujuk pada kondisi awal Nadia di Bab 1–4. Cocok. | **LULUS** |
| **Bab 31, Baris 21** | `kemarin` | `"Maaf buat sikapku kemarin, dan maaf buat omonganku di lobi."` | Ungkapan lisan Nadia pada Jumat sore yang merujuk pada sikap dinginnya di awal minggu (Senin–Selasa, Bab 24–26). Cocok. | **LULUS** |
| **Bab 31, Baris 41** | `Waktu itu` | `"Waktu itu saya belum pegang surat keputusan resmi di tangan."` | Merujuk pada Senin sore di lobi (baris 39: *"Hari Senin di lobi itu"*). Cocok. | **LULUS** |
| **Bab 31, Baris 47** | `minggu lalu` | `Itu amplop yang sama persis dengan yang kulihat di bawah buku catatannya hari Jumat minggu lalu.` | Bab 31 berlangsung Jumat sore Minggu 5; *hari Jumat minggu lalu* adalah Jumat siang Minggu 4 (Bab 20 baris 35). Tepat satu minggu sebelumnya. *(Catatan kecil `F-08`: perihal yang terlihat separuh di amplop pada Bab 20 baris 35 adalah "Verifikasi Masa Tugas dan Pelepasan Pegawai", sedangkan kertas SK di dalamnya pada Bab 31 baris 51 berjudul "Surat Keputusan Mutasi Tetap Staf Redaksi Senior dari Cabang Yogyakarta ke Kantor Redaksi Jakarta" yang disertai tanda tangan pelepasan Pak Bambang).* | **LULUS** |
| **Bab 31, Baris 51 & 59** | `tiga minggu yang lalu`, `kemarin`, `tiga minggu lalu` | `...tertera tanggal pengajuan permohonan dari Saka sejak tiga minggu yang lalu, dan tanda tangan pelepasan resmi Kepala Cabang Yogyakarta, Pak Bambang, tertanggal hari Kamis kemarin.` | Bab 31 adalah Jumat Minggu 5: *tiga minggu yang lalu* = Minggu 2 (sebelum Nadia melihat tab kos tahunan & formulir antar-cabang di Minggu 3 Bab 14); *hari Kamis kemarin* = Kamis Minggu 5 (sehari sebelum peluncuran buku hari Jumat). Sangat presisi. | **LULUS** |
| **Bab 31, Baris 53** | `dulu` | `Pantas saja dulu aku pernah memergoki layar laptopnya membuka daftar kos tahunan di Cikini dan Tari sempat melihatnya menyerahkan formulir ke Mbak Sinta HRD!` | Merujuk tepat pada Bab 14 baris 17 (daftar kos tahunan Cikini) dan Bab 18 baris 39 (formulir ke Mbak Sinta HRD). Cocok 100%. | **LULUS** |
| **Bab 31, Baris 63** | `kemarin` | `"Pesan Tari pagi itu nggak mengubah keputusan itu, cuma bikin hati saya tenang waktu mengejar tanda tangan kemarin siang supaya bisa naik kereta pagi ke Gambir."` | *Pesan Tari pagi itu* = Rabu pagi (Bab 29 baris 67); *kemarin siang* = Kamis siang di Yogyakarta (cocok dengan tanggal tanda tangan Pak Bambang di baris 51). | **LULUS** |
| **Bab 31, Baris 71** | `Katanya` | `"Katanya kos tahunan itu buat teman Jogja," kataku sambil menunjuk baris tanggal pengajuan di surat itu.` | Merujuk tepat pada dalih bohong Saka di Bab 14 baris 21 (*"Teman Jogja ada yang mau pindah kerja ke daerah sini bulan depan, titip dicarikan info harga"*). Cocok 100%. | **LULUS** |
| **Bab 32, Baris 59** | `waktu itu` | `"Ibu malah nanyain kapan editor Jogja yang di panggung waktu itu mau mampir ke rumah."` | Bab 32 berlangsung Senin sore (tiga hari setelah Jumat sore Bab 30–31); merujuk pada acara peluncuran buku hari Jumat saat Ibu hadir di barisan depan dan mengikuti sesi foto bersama di panggung (Bab 30 baris 5 & Bab 31 baris 3). Cocok. | **LULUS** |

---

## 4. Verifikasi Prosedur Dunia Nyata (`rules/18-real-world-procedures.md`)

Seluruh klaim prosedur operasional, transportasi, penerbitan/percetakan, medis, dan administrasi kepegawaian yang menopang plot telah diverifikasi menggunakan pencarian web eksternal dengan rincian berikut:

| No. | Domain & Lokasi di Naskah | Klaim Urutan & Durasi di Naskah | Fakta Operasional & Standar Dunia Nyata | Sumber Eksternal (URL Penuh & Tanggal Akses) | Status Verifikasi |
|---|---|---|---|---|---|
| **1** | **Transportasi Kereta Api Antarkota (Yogyakarta – Jakarta)**<br>`chapters/bab-30.md` baris 9 & `chapters/bab-31.md` baris 63 | `[Stasiun Tugu Yogyakarta 14.00 WIB ("kereta pagi ... pukul dua siang") -> Stasiun Gambir Jakarta < 16.00 WIB = durasi < 2 jam di naskah vs 6 jam 5 menit – 6 jam 10 menit di dunia nyata]` | Berdasarkan Grafik Perjalanan Kereta Api (Gapeka) PT KAI, waktu tempuh kereta api eksekutif tercepat relasi Stasiun Tugu Yogyakarta – Stasiun Gambir Jakarta (misalnya KA Taksaka / KA Argo Dwipangga) adalah **±6 jam 5 menit hingga 6 jam 10 menit** (contoh: KA Taksaka Pagi KA 43 berangkat dari Yogyakarta pukul **07.30 WIB** dan tiba di Gambir pukul **13.35 WIB**; KA Taksaka Siang KA 47 berangkat pukul **14.45 WIB** dan tiba di Gambir pukul **20.54 WIB**). Mustahil kereta berangkat dari Yogyakarta pukul 14.00 siang dan tiba di Gambir sebelum pukul 16.00 sore (< 2 jam), serta pukul 14.00 bukan jadwal *"kereta pagi"*. | 1. `https://www.kompas.com/jawa-tengah/read/2026/02/21/203000488/jadwal-ka-taksaka-gambir-yogyakarta-pp-cek-harga-tiket-terbaru-2026` (diakses 2026-11-17)<br>2. `https://keretaapikita.com/jadwal-kereta-api-taksaka/` (diakses 2026-11-17) | **TEMUAN (`DOMAIN_FACTUALITY` / `TIMELINE` — `F-06`, Severity `ERROR` / `HIGH`)** |
| **2** | **Transportasi Dalam Kota Jakarta Pusat (Stasiun Gambir – Cikini)**<br>`chapters/bab-30.md` baris 9 | `[Stasiun Gambir -> Toko Buku Cikini = ±10 menit perjalanan kendaraan di naskah vs 4–10 menit di dunia nyata]` | Jarak jalan raya antara Stasiun Gambir dan kawasan Cikini (Menteng, Jakarta Pusat) adalah sekitar **2,5–3 km**, dengan waktu tempuh kendaraan bermotor/taksi/ojek sekitar **4–10 menit** dalam kondisi normal (atau 10–15 menit saat ramai). | `https://www.rome2rio.com/ms/s/Gambir-Stesen/Cikini-Stesen` (diakses 2026-11-17) | **TERVERIFIKASI LULUS** |
| **3** | **Prosedur Penerbitan & Percetakan Buku (*Dummy Proof*, POD/Cetak Digital Terbatas vs *Offset*)**<br>`chapters/bab-21.md` baris 9, `bab-24.md` baris 3, `bab-26.md` baris 7–9, `bab-30.md` baris 5, `bab-32.md` baris 3 | `[File final masuk Jumat sore -> Cetak percobaan (dummy proof) tiba Senin sore (1 hari kerja) -> Persetujuan naik cetak Selasa pukul 11.00 -> Edisi peluncuran cetak digital terbatas tiba Jumat pagi (3 hari kerja), sedangkan cetak massal offset menyusul]` | Dalam industri percetakan buku, pencetakan sampel fisik (*dummy proof*) menggunakan *digital printing* membutuhkan **1–3 hari kerja**, dan pencetakan edisi terbatas dengan metode *Print on Demand* (POD) / cetak digital cepat memakan waktu **1–5 hari kerja**, sedangkan cetak massal *offset* membutuhkan waktu lebih panjang dan lazim menyusul setelah edisi peluncuran terbatas. Naskah bahkan sudah menjelaskan mekanisme ini secara eksplisit di Bab 21 baris 9 dan Bab 32 baris 3. | 1. `https://penerbitdeepublish.com/panduan-penerbitan-percetakan/cetak-cepat/` (diakses 2026-11-17)<br>2. `https://only-print.com/cetak-buku-print-on-demand-pod/` (diakses 2026-11-17) | **TERVERIFIKASI LULUS** |
| **4** | **Prosedur Medis Penanganan Vertigo Akut di Klinik Pratama**<br>`chapters/bab-22.md` baris 10–57 & `bab-23.md` baris 3 | `[Pasien vertigo akut datang pukul 09.30 dengan kursi roda -> Pendaftaran loket -> Ruang observasi & injeksi obat pereda pusing/mual -> Tebus obat racikan di apotek (total durasi ±3 jam s.d. 13.00) -> Rawat jalan & membaik pukul 17.00 setelah minum obat dan istirahat]` | Standar penanganan vertigo perifer akut derajat sedang-berat di fasilitas kesehatan tingkat pertama (Klinik Pratama) mencakup penapisan tanda bahaya, pemberian terapi injeksi simtomatik (antiemetik/vestibular suppressant), **observasi 1–3 jam** di ruang tindakan/observasi hingga pasien stabil untuk berdiri, lalu pemulangan rawat jalan dengan obat oral (seperti *betahistine*/antivertigo) dan istirahat. Urutan dan durasi 3 jam di naskah sangat akurat secara klinis. | 1. `https://www.alomedika.com/penyakit/neurologi/vertigo/penatalaksanaan` (diakses 2026-11-17)<br>2. `https://www.rspon.go.id/pdf/leaflet/26vertigo2021.pdf` (diakses 2026-11-17) | **TERVERIFIKASI LULUS** |
| **5** | **Prosedur Administrasi Mutasi Karyawan Antar-Cabang (HRD)**<br>`chapters/bab-14.md` baris 17, `bab-18.md` baris 39, `bab-20.md` baris 19–35, `bab-31.md` baris 47–65 | `[Tawaran Kepala Redaksi cabang tujuan di awal proyek -> Pengajuan permohonan mutasi pada Minggu 2 -> Penyerahan formulir ke HRD pada Minggu 3 -> Verifikasi masa tugas perbantuan 5 minggu pada Minggu 4 -> Serah terima/tanda tangan pelepasan Kepala Cabang asal (Yogyakarta) pada Kamis Minggu 5 -> Efektif mulai Senin Minggu 6]` | Prosedur mutasi karyawan antar-cabang melibatkan koordinasi HRD cabang tujuan/pusat dan cabang asal: pengajuan formulir mutasi, penerbitan SK Mutasi, serta kewajiban menyelesaikan serah terima tugas (*handover*) dan mendapatkan tanda tangan pelepasan dari Kepala Cabang asal sebelum efektif bertugas penuh di cabang baru. Durasi pengurusan 3 minggu sangat realistis. *(Catatan: kesalahan yang ada bukan pada prosedur HRD Saka, melainkan pada dialog Dimas di Bab 27 baris 45 yang mengklaim Saka sudah resmi pindah tetap pada Selasa malam sebelum tanda tangan pelepasan Kamis turun).* | 1. `https://greatdayhr.com/id-id/blog/surat-mutasi-karyawan-pengertian-fungsi-dan-contohnya/` (diakses 2026-11-17)<br>2. `https://dibimbing.id/blog/detail/contoh-surat-mutasi-kerja` (diakses 2026-11-17) | **TERVERIFIKASI LULUS** *(Prosedur HRD)* |

---

## 5. Daftar Temuan Editorial, Bukti, Keputusan, dan Saran Perbaikan Spesifik (`rules/00`, `rules/13`, `rules/15`, `rules/17`)

Berikut adalah daftar lengkap seluruh temuan dari hasil audit terhadap `/tmp/uji-canary`, diurutkan berdasarkan bobot severity dan dampak rilis:

---

### `[F-01]` Dimas Mengklaim Telah Melihat Sketsa Kursi Kosong di Halaman Penutup Dua Hari Sebelum Sketsa Itu Dibuat Nadia
- **Severity:** `HIGH` (Sekaligus `ERROR` kontinuitas waktu/objek)
- **Kategori:** `CAUSALITY` / `CHARACTER_KNOWLEDGE` / `TIMELINE`
- **Release Impact:** `FIX BEFORE RELEASE`
- **Confidence:** `HIGH`
- **Klasifikasi Keputusan Editorial:** `MANUSCRIPT ERROR` (Tidak ada di `outline.md` Bab 19; murni kesalahan di manuskrip `chapters/bab-19.md`)
- **Lokasi:** `chapters/bab-19.md` baris 69
- **Bukti Kutipan Asal (`chapters/bab-19.md` baris 69, Rabu sore Minggu 4):**
  > `Dimas menatap mataku lurus. "Memangnya selama ini dia pernah ngajak kamu bahas kelanjutan hubungan kalian? Aku lihat sendiri kamu sampai bikin sketsa kursi kosong di halaman penutup bukumu."`
- **Bukti Pembanding Lintas Bab:**
  1. `chapters/bab-18.md` baris 46–55 (Senin siang Minggu 4): Di halaman terakhir/ucapan terima kasih, Nadia baru menggambar **siluet botol minum penyok berukuran 2 cm** di sudut kanan bawah, belum ada gambar kursi kosong.
  2. `chapters/bab-21.md` baris 5 (Jumat sore Minggu 4):
     > `Namun di tengah kesibukanku merapikan halaman terakhir buku Sela Waktu, tanganku sempat membuat satu gambar kecil tambahan di lembar penutup: sketsa dua meja kerja yang bersebelahan, di mana satu kursinya kosong dan hanya menyisakan bayangan sebuah botol minum hitam.`
  3. `chapters/bab-24.md` baris 29 & 39 (Senin sore Minggu 5):
     > `Aku baru ingat bahwa pada Jumat sore lalu, aku sempat menyelipkan satu sketsa kecil tambahan di bagian tengah halaman penutup buku itu sebelum mengirimkan file terakhir tersebut ke percetakan setelah Saka pulang.`
  4. `chapters/bab-29.md` baris 15 (Rabu pagi Minggu 5):
     > `Meja itu kosong melompong, persis seperti sketsa yang kugambar sendiri di halaman penutup buku Sela Waktu hari Jumat lalu.`
- **Masalah Spesifik & Dampak bagi Pembaca:**
  Urutan sebab-akibat terbalik dan melanggar batas pengetahuan tokoh (`rules/01-plot-and-causality.md` & `rules/05-character-knowledge.md`). Sketsa kursi kosong di halaman penutup justru lahir pada hari Jumat sore (Bab 21) **sebagai akibat** dari bisikan keraguan Dimas di Bab 19 dan telepon Pak Ramdan di Bab 20. Ketika Dimas di Bab 19 (Rabu sore) sudah menyebut sketsa kursi kosong itu, pembaca yang teliti akan bingung bagaimana Dimas bisa melihat gambar yang baru akan digambar Nadia dua hari kemudian, serta mengapa di Bab 21 dan Bab 24 narasi memperlakukan sketsa kursi kosong itu sebagai gambar baru yang dibuat hari Jumat.
- **Saran Perbaikan Minimal (`chapters/bab-19.md` baris 69):**
  Hapus kalimat kedua yang anakronistik pada dialog Dimas di baris 69:
  - **Target:**
    `Dimas menatap mataku lurus. "Memangnya selama ini dia pernah ngajak kamu bahas kelanjutan hubungan kalian? Aku lihat sendiri kamu sampai bikin sketsa kursi kosong di halaman penutup bukumu."`
  - **Replacement:**
    `Dimas menatap mataku lurus. "Memangnya selama ini dia pernah ngajak kamu bahas kelanjutan hubungan kalian setelah buku itu naik cetak?"`
- **Analisis Konsekuensi Lintas Bab (`rules/01-plot-and-causality.md` §5):**
  Perbaikan ini **tidak** membatalkan titik balik mana pun. Justru perbaikan ini memulihkan kausalitas murni Bab 19 → Bab 20 → Bab 21 → Bab 24: bisikan keraguan Dimas di Bab 19 ditambah telepon Pak Ramdan di Bab 20 menjadi penyebab Nadia menggambar sketsa kursi kosong di Bab 21, yang kemudian pertama kali dilihat oleh Saka pada *dummy* buku di Bab 24.

---

### `[F-02]` Dimas Membocorkan Bahwa Saka Sudah Resmi Pindah Tetap ke Jakarta pada Bab 27 (Merusak Konflik & Pengetahuan Karakter Bab 27–31)
- **Severity:** `HIGH` (Sekaligus `ERROR` kontinuitas alur informasi)
- **Kategori:** `CHARACTER_KNOWLEDGE` / `CAUSALITY` / `PLOT_LOGIC`
- **Release Impact:** `FIX BEFORE RELEASE`
- **Confidence:** `HIGH`
- **Klasifikasi Keputusan Editorial:** `MANUSCRIPT ERROR` (Bertentangan dengan `outline.md` Bab 27 dan alur informasi Bab 27–31)
- **Lokasi:** `chapters/bab-27.md` baris 45
- **Bukti Kutipan Asal (`chapters/bab-27.md` baris 45, Selasa malam Minggu 5):**
  > `"Buku esai kecil gitu biar diurus editor Jogja itu sendiri aja di panggung, toh kata anak HRD dia udah resmi pindah tetap ke Jakarta," kata Dimas enteng.`
- **Bukti Pembanding Lintas Bab & Outline:**
  1. `outline.md` Bab 27 baris 199:
     > `...sambil menyeletuk enteng, "Lagian buku kecil gitu biar diurus editor Jogja itu aja, Nad. Kamu kan dari dulu juga lembek kalau ngomong di depan orang, lebih bagus kamu ngikut aku aja kayak dulu."`
  2. `chapters/bab-27.md` baris 63 (dua paragraf setelah baris 45 di bab yang sama!):
     > `Dan aku, karena takut ditinggal Saka pulang ke Yogyakarta, hampir saja menyerahkan kembali harga diriku...`
  3. `chapters/bab-29.md` baris 61 (Rabu pagi):
     > `Aku pun mengurungkan niat bertanya ke ruangan Pak Ramdan karena terlalu takut mendengar jawaban yang memastikan Saka sudah pergi untuk selamanya.`
  4. `chapters/bab-31.md` baris 45–55 (Jumat sore):
     > `Aku menatapnya bingung. "Surat keputusan apa maksudnya, Mas?" ... "Mutasi tetap ke Jakarta? Jadi... Mas Saka ke Jogja bukan mau pindah balik ke sana?" tanyaku hampir tidak percaya.`
- **Masalah Spesifik & Dampak bagi Pembaca:**
  Kalimat Dimas di Bab 27 baris 45 (*"toh kata anak HRD dia udah resmi pindah tetap ke Jakarta"*) menimbulkan kerusakan kausalitas ganda:
  1. **Merusak pengetahuan karakter Nadia (`rules/05-character-knowledge.md`):** Jika Nadia sudah diberi tahu di meja makan pada Selasa malam bahwa menurut HRD Saka resmi pindah tetap ke Jakarta, mustahil Nadia sama sekali tidak bereaksi, masih mengira Saka pergi selamanya ke Yogyakarta pada Rabu pagi (Bab 29), dan masih terkejut luar biasa saat melihat SK Mutasi Tetap Saka pada Jumat sore (Bab 31).
  2. **Merusak motivasi Dimas & kronologi SK (`rules/01-plot-and-causality.md`):** Sejak Bab 19, senjata utama Dimas untuk menggoyahkan Nadia adalah klaim bahwa Saka akan pulang ke Jogja. Selain itu, pada Selasa malam (Bab 27), tanda tangan pelepasan resmi Pak Bambang bahkan belum turun (baru ditandatangani Kamis siang di Yogyakarta sesuai Bab 31 baris 51 & 63).
- **Saran Perbaikan Minimal (`chapters/bab-27.md` baris 45):**
  Hapus klausa anakronistik tentang HRD dan mutasi tetap ke Jakarta sehingga sesuai dengan `outline.md` Bab 27:
  - **Target:**
    `"Buku esai kecil gitu biar diurus editor Jogja itu sendiri aja di panggung, toh kata anak HRD dia udah resmi pindah tetap ke Jakarta," kata Dimas enteng.`
  - **Replacement:**
    `"Buku esai kecil gitu biar diurus editor Jogja itu sendiri aja di panggung," kata Dimas enteng.`
- **Analisis Konsekuensi Lintas Bab (`rules/01-plot-and-causality.md` §5):**
  Perbaikan ini menyinkronkan kembali Bab 27 dengan Bab 27 baris 63, Bab 29, dan Bab 31 tanpa mengubah fungsi adegan (topeng Dimas tetap terlepas karena ia meremehkan buku *Sela Waktu* dan menyuruh Nadia membatalkan kehadiran di panggung peluncuran demi acara bos pemasaran), serta menjaga keutuhan *reveal* SK Mutasi Tetap di Bab 31.

---

### `[F-03]` Rujukan Mundur Salah Lokasi & Tanpa Tanam: Saka Mengklaim Nadia Pernah Membahas Dimas di Kedai Kopi
- **Severity:** `ERROR`
- **Kategori:** `SETUP_PAYOFF` / `CONTINUITY`
- **Release Impact:** `FIX BEFORE RELEASE`
- **Confidence:** `HIGH`
- **Klasifikasi Keputusan Editorial:** `MANUSCRIPT ERROR`
- **Lokasi:** `chapters/bab-25.md` baris 21
- **Bukti Kutipan Asal (`chapters/bab-25.md` baris 21):**
  > `"Kamu sendiri yang bilang di kedai kopi kalau urusan kalian sudah selesai," kata Saka tajam. Keningnya berkerut rapat. "Kenapa sekarang dia balik lagi ngurusin rumah kamu?"`
- **Bukti Pembanding Lintas Bab:**
  - Dalam seluruh adegan di kedai kopi dekat Stasiun Cikini pada `chapters/bab-11.md` (baris 31–65) dan `chapters/bab-12.md` (baris 1–57), Nadia **hanya** menceritakan permintaan pinjaman uang Rp4 juta dari Mbak Raras, sikap ibunya yang menyuruhnya mengalah, dan kabel papan gambarnya yang terlilit lakban. Nama **Dimas** tidak pernah disebut satu kali pun di kedai kopi.
  - Saka mengetahui hubungan Nadia dan Dimas sudah putus dari teriakan Nadia di tangga darurat (`chapters/bab-01.md` baris 15–29 & `bab-02.md` baris 19) serta saat Nadia menolak Dimas di meja proyek nomor empat (`chapters/bab-06.md` & `bab-07.md`).
- **Masalah Spesifik & Dampak bagi Pembaca:**
  Melanggar `rules/06-setup-payoff.md` (Bagian *Rujukan mundur*): mengklaim tokoh pernah mengatakan sesuatu di lokasi/bab terdahulu padahal percakapan tersebut tidak pernah terjadi di sana. Pembaca yang mengikuti adegan kedai kopi di Bab 11–12 akan menyadari bahwa yang dibahas di kedai kopi adalah masalah keluarga Nadia (Mbak Raras) dan masa lalu Saka di Jogja, bukan soal Dimas.
- **Saran Perbaikan Minimal (`chapters/bab-25.md` baris 21):**
  Ubah rujukan lokasi *"di kedai kopi"* agar mengacu pada peristiwa yang memang terjadi di depan Saka:
  - **Target:**
    `"Kamu sendiri yang bilang di kedai kopi kalau urusan kalian sudah selesai," kata Saka tajam. Keningnya berkerut rapat. "Kenapa sekarang dia balik lagi ngurusin rumah kamu?"`
  - **Replacement:**
    `"Bukannya urusan kamu sama dia sudah selesai sejak kamu tolak mentah-mentah di meja kita waktu itu?" kata Saka tajam. Keningnya berkerut rapat. "Kenapa sekarang dia balik lagi ngurusin rumah kamu?"`
- **Analisis Konsekuensi Lintas Bab (`rules/01-plot-and-causality.md` §5):**
  Tidak mengubah jalannya pertengkaran di lobi pada Bab 25 dan tidak mengganggu rujukan yang benar di Bab 25 baris 35 (*"Namun aku lupa cerita Saka di kedai kopi dulu"* — yang memang merujuk pada kisah studio dan mantan pacar Saka di Bab 12).

---

### `[F-04]` Rujukan Mundur Tanpa Tanam: Narasi Mengklaim Saka Pernah Bercerita tentang Adik Perempuannya yang Kuliah di Surabaya
- **Severity:** `ERROR`
- **Kategori:** `SETUP_PAYOFF` / `CONTINUITY`
- **Release Impact:** `FIX BEFORE RELEASE`
- **Confidence:** `HIGH`
- **Klasifikasi Keputusan Editorial:** `MANUSCRIPT ERROR`
- **Lokasi:** `chapters/bab-26.md` baris 51
- **Bukti Kutipan Asal (`chapters/bab-26.md` baris 51–53):**
  > `Aku menatap kursi kerja Saka yang kosong di sebelahku, lalu pandanganku beralih ke pojok kiri bawah bingkai monitorku. Aku sempat teringat cerita Saka tempo hari soal adik perempuannya yang kuliah di Surabaya.`
  >
  > `Kertas post-it kuning bertuliskan Bilang enggak itu nggak bikin langit runtuh yang ditempelkan Saka empat minggu lalu kini bagian sudut lemnya sudah mulai kering dan agak mengelupas terkena angin AC.`
- **Bukti Pembanding Lintas Bab:**
  - Di seluruh `chapters/bab-01.md` s.d. `bab-25.md` maupun `outline.md`, Saka tidak pernah sekalipun menyebut atau menceritakan adik perempuan yang kuliah di Surabaya (satu-satunya tokoh yang memiliki adik kuliah di luar kota adalah Nadia sendiri di `chapters/bab-10.md` baris 7: *"adik bungsu laki-laki yang masih kuliah di Bandung"*).
- **Masalah Spesifik & Dampak bagi Pembaca:**
  Melanggar `rules/06-setup-payoff.md` (rujukan mundur tanpa tanam) sekaligus `rules/17-scene-and-line-editing.md` (aliran paragraf): kalimat tentang adik perempuan Saka di Surabaya muncul tiba-tiba tanpa dasar di bab sebelumnya dan memutus fokus visual Nadia yang sedang beralih dari kursi kosong Saka ke *post-it* kuning di pojok kiri bawah bingkai monitornya.
- **Saran Perbaikan Minimal (`chapters/bab-26.md` baris 51):**
  Hapus kalimat sisipan yang tidak memiliki setup tersebut:
  - **Target:**
    `Aku menatap kursi kerja Saka yang kosong di sebelahku, lalu pandanganku beralih ke pojok kiri bawah bingkai monitorku. Aku sempat teringat cerita Saka tempo hari soal adik perempuannya yang kuliah di Surabaya.`
  - **Replacement:**
    `Aku menatap kursi kerja Saka yang kosong di sebelahku, lalu pandanganku beralih ke pojok kiri bawah bingkai monitorku.`
- **Analisis Konsekuensi Lintas Bab:**
  Menghilangkan rujukan palsu dan membuat jembatan visual dari kalimat di baris 51 ke deskripsi *post-it* kuning di baris 53 kembali mengalir utuh. Tidak ada bab lain yang merujuk pada adik Saka di Surabaya.

---

### `[F-05]` Kontradiksi Hari Keberangkatan Saka ke Yogyakarta di Bab 29 (`Senin sore` vs `Selasa sore` / `kemarin sore`)
- **Severity:** `ERROR`
- **Kategori:** `TIMELINE` / `CONTINUITY`
- **Release Impact:** `FIX BEFORE RELEASE`
- **Confidence:** `HIGH`
- **Klasifikasi Keputusan Editorial:** `MANUSCRIPT ERROR`
- **Lokasi:** `chapters/bab-29.md` baris 23
- **Bukti Kutipan Asal (`chapters/bab-29.md` baris 23–39, berlangsung Rabu pagi pukul 08.15):**
  > Baris 23: `Dia menyeruput kopinya sejenak. "Mas Saka Senin sore udah pamit ke Jogja lebih awal."`
  > Baris 27: `"Berangkat ke Jogja kemarin sore?" ulangku dengan suara tercekat di tenggorokan.`
  > Baris 29: `"Berkas naik cetak kan udah beres kemarin," jelas Riko santai.`
  > Baris 39: `Kemarin sore jam setengah enam. Itu tepat setelah aku pergi meninggalkan kantor untuk menghadiri makan malam bersama Dimas di Rawamangun.`
- **Bukti Pembanding Lintas Bab & Outline:**
  1. `chapters/bab-26.md` baris 3–22: Sepanjang hari **Selasa pagi s.d. siang**, Saka masih hadir di kantor, menyerahkan lembar persetujuan naik cetak kepada Nadia pukul 10.00 (diambil kurir pukul 11.00), dan baru menutup laptop menuju ruang rapat saat Dimas datang menjelang jam makan siang.
  2. `chapters/bab-31.md` baris 61: Saka berkata langsung: `"Perjalanan Selasa sore itu dari awal memang buat tanda tangan Pak Bambang dan beresin kos lama."`
  3. `outline.md` Bab 29 baris 211: `...Riko mengatakan bahwa kemarin sore Saka sudah berpamitan pada Pak Ramdan untuk berangkat ke Yogyakarta lebih awal.`
- **Masalah Spesifik & Dampak bagi Pembaca:**
  Kontradiksi kronologi langsung di dalam bab yang sama dan lintas bab (`rules/02-timeline.md`). Karena Bab 29 berlangsung pada **Rabu pagi**, keberangkatan Saka setelah berkas naik cetak beres dan setelah Nadia berangkat makan malam bersama Dimas terjadi pada **Selasa sore** (*"kemarin sore"*), bukan *"Senin sore"*.
- **Saran Perbaikan Minimal (`chapters/bab-29.md` baris 23):**
  Ubah *"Senin sore"* menjadi *"kemarin sore"*:
  - **Target:**
    `Dia menyeruput kopinya sejenak. "Mas Saka Senin sore udah pamit ke Jogja lebih awal."`
  - **Replacement:**
    `Dia menyeruput kopinya sejenak. "Mas Saka kemarin sore udah pamit ke Jogja lebih awal."`
- **Analisis Konsekuensi Lintas Bab:**
  Menyelaraskan baris 23 secara langsung dengan respons Nadia di baris 27 (*"Berangkat ke Jogja kemarin sore?"*), baris 29, baris 39, `chapters/bab-26.md`, `chapters/bab-31.md` baris 61, dan `outline.md` Bab 29.

---

### `[F-06]` Jadwal dan Durasi Perjalanan Kereta Api Yogyakarta–Gambir Mustahil Secara Operasional (`Pukul Dua Siang` Tiba `Sebelum Pukul Empat Sore`)
- **Severity:** `ERROR` (Sekaligus `HIGH` pada verifikasi prosedur dunia nyata `rules/18-real-world-procedures.md`)
- **Kategori:** `DOMAIN_FACTUALITY` / `TIMELINE`
- **Release Impact:** `FIX BEFORE RELEASE`
- **Confidence:** `HIGH`
- **Klasifikasi Keputusan Editorial:** `MANUSCRIPT ERROR`
- **Lokasi:** `chapters/bab-30.md` baris 9
- **Bukti Kutipan Asal (`chapters/bab-30.md` baris 9):**
  > `Kata Pak Ramdan sebelum naik ke panggung tadi, Saka sebenarnya sudah naik kereta pagi yang berangkat dari Stasiun Tugu Yogyakarta pukul dua siang dan dijadwalkan tiba di Stasiun Gambir sebelum pukul empat sore, namun keretanya sempat tertahan antrean sinyal dua puluh menit sebelum masuk Jatinegara. Karena jarak dari Stasiun Gambir ke Cikini hanya sepuluh menit perjalanan, Pak Ramdan memintaku memulai sesi diskusi lebih dulu sambil menunggu Saka menyusul.`
- **Bukti Pembanding Dunia Nyata & Lintas Bab:**
  - Di kalimat yang sama tertulis **"kereta pagi"** (dan di `chapters/bab-31.md` baris 63 Saka juga menyebut *"supaya bisa naik kereta pagi ke Gambir"*), tetapi jam keberangkatannya ditulis **"pukul dua siang"** (14.00 WIB).
  - Berdasarkan jadwal resmi PT KAI (lihat Bagian 4 tabel verifikasi prosedur dunia nyata), waktu tempuh kereta api eksekutif Stasiun Tugu Yogyakarta – Stasiun Gambir Jakarta adalah **±6 jam 5 menit s.d. 6 jam 10 menit**. Kereta yang berangkat pukul 14.00 siang dari Yogyakarta baru akan tiba di Gambir sekitar pukul 20.15–20.54 malam, mustahil dijadwalkan tiba di Gambir sebelum pukul 16.00 sore (durasi < 2 jam). Agar dijadwalkan tiba di Stasiun Gambir sekitar pukul 15.00–15.30 sore (sebelum pukul empat sore), kereta pagi/menjelang siang dari Yogyakarta harus berangkat sekitar **pukul sembilan pagi** (atau pukul delapan lewat tiga puluh/sembilan pagi, waktu tempuh ±6 jam).
- **Masalah Spesifik & Dampak bagi Pembaca:**
  Pembaca Indonesia yang mengenal geografi Jawa dan kereta api Yogyakarta–Jakarta akan langsung terganggu oleh klaim waktu tempuh Yogyakarta–Gambir kurang dari 2 jam serta kontradiksi frasa *"kereta pagi yang berangkat ... pukul dua siang"*.
- **Saran Perbaikan Minimal (`chapters/bab-30.md` baris 9):**
  Ubah jam keberangkatan dari *"pukul dua siang"* menjadi *"pukul sembilan pagi"* (sehingga tetap merupakan kereta pagi dan dengan waktu tempuh nyata ~6,5 jam dijadwalkan tiba di Gambir sebelum pukul empat sore, lalu tertahan sinyal 20 menit di Jatinegara hingga Saka tiba di Cikini pukul 16.30):
  - **Target:**
    `Kata Pak Ramdan sebelum naik ke panggung tadi, Saka sebenarnya sudah naik kereta pagi yang berangkat dari Stasiun Tugu Yogyakarta pukul dua siang dan dijadwalkan tiba di Stasiun Gambir sebelum pukul empat sore, namun keretanya sempat tertahan antrean sinyal dua puluh menit sebelum masuk Jatinegara.`
  - **Replacement:**
    `Kata Pak Ramdan sebelum naik ke panggung tadi, Saka sebenarnya sudah naik kereta pagi yang berangkat dari Stasiun Tugu Yogyakarta pukul sembilan pagi dan dijadwalkan tiba di Stasiun Gambir sebelum pukul empat sore, namun keretanya sempat tertahan antrean sinyal dua puluh menit sebelum masuk Jatinegara.`
- **Analisis Konsekuensi Lintas Bab:**
  Sepenuhnya sinkron dengan `chapters/bab-31.md` baris 63 (*"mengejar tanda tangan kemarin siang supaya bisa naik kereta pagi ke Gambir"*) dan menjaga ketepatan waktu kedatangan Saka di ruang peluncuran buku Cikini pada Bab 30 akhir.

---

### `[F-07]` Ketidaktepatan Kecil Rujukan Waktu Relatif `dua minggu lalu` pada Bab 23
- **Severity:** `REVIEW`
- **Kategori:** `TIMELINE` / `SETUP_PAYOFF`
- **Release Impact:** `OPTIONAL POLISH`
- **Confidence:** `HIGH`
- **Klasifikasi Keputusan Editorial:** `MANUSCRIPT ERROR` (Ringan)
- **Lokasi:** `chapters/bab-23.md` baris 41
- **Bukti Kutipan Asal (`chapters/bab-23.md` baris 41, Sabtu sore akhir Minggu 4):**
  > `Ibu membelai punggung tanganku perlahan. Tak ada ketegangan kaku seperti saat kami memperdebatkan permintaan Mbak Raras dua minggu lalu.`
- **Bukti Pembanding:**
  Perdebatan mengenai permintaan pinjaman Rp4 juta Mbak Raras terjadi pada Minggu siang akhir Minggu 1 (`chapters/bab-10.md`) dan Senin malam awal Minggu 2 (`chapters/bab-13.md`). Karena `chapters/bab-18.md` sudah memasuki Minggu 4 dan `chapters/bab-23.md` berlangsung pada Sabtu akhir Minggu 4, jarak waktunya adalah hampir **tiga minggu** (19–20 hari), bukan dua minggu.
- **Saran Perbaikan Minimal (`chapters/bab-23.md` baris 41):**
  - **Target:**
    `Tak ada ketegangan kaku seperti saat kami memperdebatkan permintaan Mbak Raras dua minggu lalu.`
  - **Replacement:**
    `Tak ada ketegangan kaku seperti saat kami memperdebatkan permintaan Mbak Raras hampir tiga minggu lalu.`

---

### `[F-08]` Perbedaan Kecil Penyebutan Perihal Surat di Amplop Cabang Yogyakarta antara Bab 20 dan Bab 31
- **Severity:** `INFO`
- **Kategori:** `CONTINUITY`
- **Release Impact:** `OPTIONAL POLISH`
- **Confidence:** `MEDIUM`
- **Klasifikasi Keputusan Editorial:** `ACCEPTABLE / AUTHOR CHOICE` (Dapat dipertahankan atau dipoles ringan)
- **Lokasi:** `chapters/bab-20.md` baris 35 vs `chapters/bab-31.md` baris 47–51
- **Bukti Kutipan:**
  - `chapters/bab-20.md` baris 35: `Di sudut kiri atas amplop itu, tercetak jelas logo Penerbit Aksara Senja Cabang Yogyakarta, dengan perihal surat yang separuh tertutup buku: Verifikasi Masa Tugas dan Pelepasan Pegawai.`
  - `chapters/bab-31.md` baris 47–51: `Itu amplop yang sama persis dengan yang kulihat di bawah buku catatannya hari Jumat minggu lalu. Dia menyerahkan lembar kertas resmi di dalam amplop itu ke tanganku. Aku menunduk membacanya. Di bagian kepala surat, tertulis jelas: Surat Keputusan Mutasi Tetap Staf Redaksi Senior dari Cabang Yogyakarta ke Kantor Redaksi Jakarta.`
- **Catatan Analisis:**
  Secara logika dokumen, perihal pada bagian luar amplop pengantar (*Verifikasi Masa Tugas dan Pelepasan Pegawai* untuk dibawa menghadap Pak Bambang di Yogyakarta) memang dapat memuat lembar *Surat Keputusan Mutasi Tetap* yang kolom bawahnya membutuhkan tanda tangan pelepasan resmi Pak Bambang (Bab 31 baris 51). Karena itu hal ini masih masuk akal tanpa wajib diubah, namun telah dicatat untuk kelengkapan audit kontinuitas benda.

---

## 6. Evaluasi Pengalaman Pembaca, Prosa, dan Kualitas Teknis (`rules/10`, `rules/12`, `rules/15`, `rules/17`)

1. **Orientasi Pembaca & Transisi (`rules/15-narrative-and-reader-experience.md`):**
   - Setiap pembukaan bab dari Bab 1 s.d. Bab 32 memiliki orientasi waktu, lokasi, situasi, dan fokus POV orang pertama (*"aku"* / Nadia) yang jernih dan alami tanpa terasa seperti tempelan catatan kronologi mentah (`rules/12-outline-leakage.md`).
   - Satu-satunya rujukan waktu internal yang agak kabur berada di `chapters/bab-25.md` baris 17 (*"bara sakit hati yang sudah kupendam sejak sore itu"* pada adegan Senin sore yang merujuk pada Jumat sore Bab 21), yang dapat diperjelas menjadi *"sejak Jumat sore itu"* sebagai *optional polish*.
2. **Arsitektur Adegan, Blocking Fisik, dan Dialog (`rules/17-scene-and-line-editing.md`):**
   - Posisi tokoh, arah gerak, dan interaksi objek (tangga darurat lantai 3, meja proyek nomor empat, perpindahan sisi luar trotoar Kwitang dan Cikini, pertukaran bangku menghindari asap rokok dan arah kipas di warung soto, hingga gestur ibu jari kanan Saka pada tutup botol minum hitam penyok) mudah dibayangkan oleh pembaca.
   - Suara karakter konsisten dan kontras: kalimat Saka ringkas, lugas, dan datar; monolog batin Nadia ekspresif dengan kecemasan khas *people-pleaser* yang bertumbuh menjadi tenang dan tegas; Dimas manipulatif-manis.
3. **Kualitas Teknis & Format Markdown (`rules/10-manuscript-technical-quality.md`):**
   - Pemindaian mekanis `audit_core.py` mengonfirmasi 0 kesalahan format Markdown, 0 *code fence* tidak tertutup, dan struktur 32 file bab rapi serta konsisten.

---

## 7. Penilaian Delapan Gerbang Kelayakan & Vonis Kesiapan Publikasi (`rules/09-publication-readiness.md`)

### 7.1 Evaluasi Delapan Gerbang Kelayakan

| Gerbang Kelayakan | Status | Catatan Bukti |
|---|---|---|
| **1. Fondasi dan janji cerita** | **LULUS** | Premis, fokus perubahan diri Nadia, dan romansa rekan satu meja di kantor penerbitan terbangun kuat sejak Bab 1–4. |
| **2. Struktur dan perkembangan** | **LULUS** | Progresi 32 bab bergerak maju tanpa bab stagnan; setiap latihan menolak memiliki peningkatan taruhan hingga klimaks Bab 27–31. |
| **3. Kausalitas, karakter, dan konflik** | **PERLU PERBAIKAN LOKAL (`F-01`, `F-02`)** | Kerangka kausalitas utama bekerja dengan baik, namun terganggu oleh dua kalimat anakronistik di manuskrip: klaim Dimas melihat sketsa kursi kosong sebelum dibuat (`bab-19.md:69`) dan ucapan Dimas bahwa Saka sudah resmi pindah tetap ke Jakarta pada Selasa malam (`bab-27.md:45`). |
| **4. Narasi dan orientasi pembaca** | **LULUS** | Orientasi waktu, tempat, POV terbatas Nadia, dan aliran informasi per bab sangat jelas dan mudah diikuti. |
| **5. Adegan dan keterbacaan** | **LULUS** | Blocking fisik, atribusi dialog, reaksi emosional, dan fungsi dramatik tiap adegan bekerja efektif. |
| **6. Continuity, timeline, dan dunia cerita** | **PERLU PERBAIKAN LOKAL (`F-03`, `F-04`, `F-05`, `F-06`)** | Terdapat rujukan mundur tanpa tanam/salah lokasi (`bab-25.md:21` kedai kopi; `bab-26.md:51` adik di Surabaya), salah sebut hari keberangkatan Saka (`bab-29.md:23` Senin sore vs Selasa sore), dan jadwal/durasi kereta Yogyakarta–Gambir yang mustahil (`bab-30.md:9`). |
| **7. Prosa dan teknis naskah** | **LULUS** | Kalimat mengalir lancar, ejaan dan tipografi bersih, 0 temuan mekanis pada struktur Markdown. |
| **8. Ketuntasan dan payoff** | **LULUS** | Seluruh setup utama (*post-it* kuning, *klik* dua kali tutup botol minum hitam penyok, *operator customer service*, utang ayam bakar Riko Rp90.000, SK Mutasi Tetap Saka) terbayar tuntas di Bab 28–32. |

---

### 7.2 Vonis Kesiapan Akhir

- **VONIS:** **`READY WITH MINOR FIXES` ("Perlu Perbaikan Lokal")**
- **Alasan Penetapan Vonis sesuai `rules/09-publication-readiness.md` Bagian D:**
  1. **Mengapa belum `READY TO PUBLISH`:** Sesuai syarat keras `rules/09-publication-readiness.md` baris 69–73, status `READY TO PUBLISH` hanya boleh diberikan apabila tabel sebab-akibat bebas dari temuan `HIGH`, seluruh proses dunia nyata terverifikasi tanpa jadwal mustahil, dan daftar rujukan mundur bebas dari rujukan tanpa tanam/salah detail/salah waktu relatif. Pada naskah ini masih terdapat 6 temuan objektif berstatus `FIX BEFORE RELEASE` (`F-01` s.d. `F-06`).
  2. **Mengapa bukan `NOT READY` ("Kerangka Perlu Dibongkar"):** Sesuai ambang batas skala vonis di `rules/09-publication-readiness.md` baris 78–82, vonis *"kerangka perlu dibongkar"* hanya boleh diberikan jika perbaikan membutuhkan perubahan `outline.md` lintas ≥ 5 bab atau pembatalan titik balik utama. Dalam audit ini, **kerangka cerita dan `outline.md` terbukti 100% sehat dan tidak perlu dibongkar sama sekali**. Seluruh temuan (`F-01` s.d. `F-06`) adalah kesalahan lokal tingkat kalimat/frasa di dalam manuskrip yang dapat diselesaikan tuntas hanya dengan mengedit/menghapus masing-masing **satu kalimat atau satu frasa** pada lokasi terkait tanpa mengubah struktur bab maupun titik balik cerita.

### 7.3 Ringkasan Tindakan Perbaikan Sebelum Rilis (`FIX BEFORE RELEASE`)
1. **`chapters/bab-19.md` (Baris 69 — `F-01`):** Hapus kalimat *"Aku lihat sendiri kamu sampai bikin sketsa kursi kosong di halaman penutup bukumu"* dari dialog Dimas.
2. **`chapters/bab-25.md` (Baris 21 — `F-03`):** Ganti rujukan lokasi *"di kedai kopi"* pada dialog Saka menjadi rujukan ke penolakan Dimas di meja kerja.
3. **`chapters/bab-26.md` (Baris 51 — `F-04`):** Hapus kalimat tanpa setup *"Aku sempat teringat cerita Saka tempo hari soal adik perempuannya yang kuliah di Surabaya."*
4. **`chapters/bab-27.md` (Baris 45 — `F-02`):** Hapus klausa prematur *", toh kata anak HRD dia udah resmi pindah tetap ke Jakarta"* dari dialog Dimas.
5. **`chapters/bab-29.md` (Baris 23 — `F-05`):** Ubah *"Senin sore"* pada dialog Riko menjadi *"kemarin sore"* (Selasa sore).
6. **`chapters/bab-30.md` (Baris 9 — `F-06`):** Ubah jam keberangkatan kereta pagi Saka dari Stasiun Tugu Yogyakarta dari *"pukul dua siang"* menjadi *"pukul sembilan pagi"*.
