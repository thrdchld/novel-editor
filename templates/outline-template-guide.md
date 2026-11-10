# Panduan Pengisian Outline Universal

## Tujuan

Dokumen ini menjelaskan cara menggunakan `templates/outline-template.md` oleh AI pembuat outline dari model/provider mana pun. Hasilnya harus dapat dibaca AI lain, diaudit, diperbaiki, dan dipakai sebagai acuan penulisan puluhan bab.

## Prinsip utama

- Template adalah peta informasi, bukan format kaku atau formula cerita.
- Isi semua aspek yang relevan; bagian yang tidak relevan boleh ditandai "Tidak berlaku".
- AI boleh menambah bagian, kolom, diagram, tabel, lampiran, atau catatan bebas.
- Jangan menghapus atau memadatkan fakta penting demi tampilan ringkas.
- Jangan mengarang keputusan kreatif yang belum diberikan. Tandai OPEN/BELUM DIPUTUSKAN.
- Pisahkan fakta kanonis, rencana yang masih fleksibel, asumsi, dan catatan internal.
- Genre hanya konteks. Tidak ada struktur plot, trope, ending, atau jumlah subplot universal.
- Outline harus cukup rinci untuk memandu penulisan tanpa memaksa gaya bahasa atau prosa bab.

## Cara mengisi setiap lapisan

1. **Metadata:** nyatakan versi dan status. Pastikan jumlah bab, bahasa, POV, tense, dan hard constraints diketahui atau ditandai terbuka.
2. **Identitas cerita:** premis, logline, pertanyaan utama, fokus, dan batas cerita menjelaskan apa yang sedang dirancang.
3. **Ringkasan utuh:** jelaskan cerita dari awal hingga akhir, termasuk spoiler dan ending. Jangan hanya menulis teaser atau sinopsis promosi.
4. **Konflik dan kausalitas:** tunjukkan apa yang mendorong peristiwa. Setiap kejadian besar sebaiknya lahir dari pemicu, keputusan, aturan, atau konsekuensi yang dapat ditelusuri.
5. **Tokoh dan relasi:** catat hanya detail yang memengaruhi cerita. Bedakan motivasi, tujuan, pengetahuan, kemampuan, dan status hubungan.
6. **Dunia dan aturan:** catat aturan yang memengaruhi tindakan atau risiko. Untuk cerita realistis, bagian ini dapat sederhana; untuk speculative fiction dapat lebih luas.
7. **Timeline:** gunakan tanggal pasti jika diketahui; jika tidak, gunakan urutan relatif yang konsisten. Jangan mencampur "tiga hari kemudian" dengan tanggal yang mustahil.
8. **Knowledge map:** tentukan siapa tahu apa, kapan, dan melalui saluran apa. Ini mencegah tokoh mengetahui informasi tanpa pernah mendapatkannya.
9. **Object/resource tracker:** lacak benda, dokumen, uang, kemampuan, akses, luka, atau sumber daya yang memengaruhi plot.
10. **Struktur/arc:** gunakan model yang cocok atau tidak memakai label struktur sama sekali. Model bukan hukum dan tidak boleh menimpa maksud cerita.
11. **Outline bab:** untuk tiap bab, jelaskan kondisi awal, tindakan, alasan, hasil, dan perubahan. Satu bab boleh memiliki beberapa adegan; jangan dipaksakan satu adegan jika rancangan memerlukan lebih.
12. **Setup/payoff:** catat petunjuk dan janji yang benar-benar penting. Tidak semua detail perlu dibayar.
13. **Canon/keputusan:** tandai LOCKED, FLEXIBLE, atau OPEN agar editor tahu apa yang boleh disesuaikan otomatis.
14. **Catatan bebas:** simpan konteks tambahan yang membantu AI lain memahami pilihan pembuat outline.

## Kualitas rincian per bab

Outline bab terlalu tipis jika hanya menyebut "Maya sedih", "mereka bertengkar", "rahasia terbongkar", atau "tokoh berubah". Jelaskan:
- apa yang memicu kejadian;
- siapa melakukan apa;
- mengapa tindakan itu masuk akal bagi tokoh;
- informasi apa yang dimiliki tokoh;
- apa yang berubah setelah kejadian;
- konsekuensi apa yang dibawa ke bab berikutnya.

Jangan mengisi setiap kolom dengan kalimat panjang jika satu kalimat jelas sudah cukup. Ketelitian berarti informasi dapat diuji, bukan jumlah kata.

## Penanganan ketidakpastian

Gunakan label konsisten:
- `LOCKED`: keputusan kanonis yang tidak boleh diubah diam-diam.
- `FLEXIBLE`: detail teknis/rencana yang boleh disesuaikan untuk memperbaiki konsistensi.
- `OPEN`: keputusan belum dibuat.
- `ASSUMPTION`: asumsi kerja yang perlu diuji.
- `NOT APPLICABLE`: aspek tidak relevan bagi cerita.

Jika ketidakpastian memengaruhi logika inti atau ending, jelaskan konsekuensinya. Jangan menyembunyikan kekosongan dengan detail karangan.

## Independensi AI

Outline harus menggunakan heading, label, nama tokoh, nomor bab, tanggal, dan istilah yang konsisten. Hindari referensi samar seperti "seperti yang dijelaskan sebelumnya" tanpa menunjuk bagian/ID. Gunakan ID stabil (T1, C1, S1, P1, dan seterusnya) untuk fakta yang dirujuk berulang. AI lain harus dapat memahami dokumen tanpa akses ke percakapan tempat outline dibuat.

## Serah terima ke Novel Editor

AI pembuat outline menyerahkan:
1. file outline lengkap;
2. daftar file tambahan jika ada;
3. status LOCKED/FLEXIBLE/OPEN;
4. catatan asumsi dan bagian yang belum diputuskan.

Jangan meminta Novel Editor menilai gaya atau potensi pasar. Tugas Novel Editor adalah audit teknis: kelengkapan informasi untuk eksekusi, logika internal, sebab-akibat, kronologi, kontinuitas, character knowledge, aturan dunia, setup/payoff, serta keterpahaman. Outline yang belum lolos harus diperbaiki otomatis sejauh keputusan dapat disimpulkan tanpa mengarang pilihan kreatif.

## Catatan kompatibilitas

Outline lama boleh memakai format berbeda. Editor harus menginventarisasi dan memetakan informasi yang tersedia ke kategori template, bukan menolak dokumen hanya karena heading atau susunannya berbeda. Konversi format hanya diperlukan jika meningkatkan keterbacaan, auditabilitas, atau interoperabilitas.
