# Outline Leakage Audit

## Tujuan
Memastikan outline, beat sheet, timeline, character bible, world bible, scene list, prompt, dan catatan kerja tetap menjadi alat internal. Naskah hanya menyampaikan informasi yang dibutuhkan pembaca. Outline is guidance, not narration.

## Prinsip
- Pertahankan fakta, canon, dan fungsi cerita; jangan otomatis menyalin bentuk kalimat, label, bullet, tanggal, atau penjelasan dari outline ke prosa.
- Informasi perencanaan boleh muncul jika relevan bagi pembaca, punya alasan dramatik, dan disampaikan alami melalui adegan, tindakan, dialog, atau narasi.
- Jangan menghapus informasi penting hanya karena mirip outline. Uji fungsi dan kebutuhan pembaca.
- Jangan mengubah tone, voice, gaya, humor, atau diksi artistik.
- AI-slop adalah deskripsi gejala tekstual mekanis, bukan bukti bahwa teks dibuat AI.

## Kategori kebocoran wajib
1. **Timeline/tanggal mentah:** tanggal, hari, jam, dan rentang waktu dari timeline disebut berulang tanpa fungsi; pembuka bab memakai tanggal lengkap seperti catatan kronologi; tanggal diulang padahal konteks sudah cukup.
2. **Label struktur/beat:** awal konflik, titik balik, midpoint, klimaks, resolusi, fase, babak, arc, beat, turning point, subplot. Istilah ini tidak otomatis salah; periksa kewajaran dan kebutuhan pembaca.
3. **Profil/ringkasan karakter:** tokoh atau narator mengulang profil, sifat, latar, trauma, motivasi, kelemahan, atau tujuan seperti membaca character bible.
4. **Tujuan/fungsi adegan:** prosa menyebut maksud bab, tujuan adegan, fungsi pertemuan, atau pelajaran yang harus dipetik; adegan dibuka dengan ringkasan outline lalu memperagakan hal yang sama.
5. **State emosi/arc:** narasi berulang menyatakan tokoh memasuki fase pemulihan, belajar menerima, menemukan jati diri, menutup bab lama, atau mencapai perkembangan tertentu; label abstrak menggantikan tindakan dan konsekuensi.
6. **Worldbuilding dump:** semua butir world bible ditumpahkan sekaligus; aturan, sejarah, organisasi, atau sistem dijelaskan secara ensiklopedis tanpa pemicu adegan; informasi yang sama diulang setiap kali aturan digunakan.
7. **Foreshadowing/reveal instruction:** narasi mengumumkan detail akan penting nanti, rahasia akan terbongkar, atau petunjuk dijelaskan terlalu terang karena outline menyatakan fungsinya.
8. **Repetisi fakta/exposition:** fakta, relasi, konflik, atau kejadian masa lalu dijelaskan lagi tanpa konteks baru; dialog menjadi alat menyampaikan informasi yang kedua tokoh sudah ketahui hanya untuk pembaca.
9. **Artefak perencanaan/produksi:** catatan penulis/editor, prompt, instruksi AI, TODO/FIXME, placeholder, ringkasan bab, bullet outline, label POV/scene nonfinal, atau metadata produksi tertinggal.
10. **Pola generatif mekanis:** pembuka bab berulang dengan formula waktu/cuaca/lokasi; tiap bab mengulang recap waktu dan emosi; struktur transisi/penutup identik; frasa abstrak yang sama dipakai dengan fungsi sama; tiap bab menutup dengan kesimpulan moral eksplisit.

Pola generatif adalah sinyal pemeriksaan kontekstual, bukan bukti otomatis kesalahan atau penggunaan AI.

## Metode
1. Inventarisasi outline, timeline, scene list, beat sheet, character bible, world bible, prompt, dan catatan yang tersedia; catat yang tidak tersedia.
2. Pisahkan fakta internal yang harus tetap benar dari cara penyampaiannya. Usia, motivasi, tanggal, dan urutan kejadian dapat menjadi canon tanpa selalu disebut dalam prosa.
3. Periksa tiap bab dan lintas bab dengan sepuluh kategori.
4. Untuk setiap kandidat, tanyakan: apakah pembaca perlu tahu sekarang; apakah tokoh/narator punya alasan alami menyebutnya; apakah sudah dijelaskan; apakah terasa seperti label/ringkasan/instruksi; apakah penghapusan merusak logika, orientasi, setup/payoff, atau pemahaman; bisakah fungsinya dipertahankan lebih organik atau tanpa disebut?
5. Klasifikasikan:
   - **CONFIRMED LEAKAGE:** jelas berupa catatan/instruksi/label internal atau pengulangan tanpa fungsi pembaca.
   - **LIKELY LEAKAGE:** pola kuat menunjukkan outline dipindahkan ke prosa, tetapi perlu konteks/keputusan penulis.
   - **ACCEPTABLE CONTEXT:** informasi diperlukan, punya fungsi dramatik, atau pilihan naratif sah.
   - **NOT A LEAK:** kebetulan mirip outline, tetapi tetap wajar dan relevan.
6. Berikan bukti dan alasan. Jangan tandai hanya karena tanggal, istilah abstrak, refleksi, atau pengulangan muncul satu kali.
7. Jika outline tidak tersedia, lakukan **surface scan** saja. Nyatakan perbandingan langsung outline-ke-naskah belum dapat dilakukan; jangan klaim semua kebocoran telah ditemukan.
8. Jika edit diizinkan, ubah minimal kebocoran terkonfirmasi. Pertahankan canon, fungsi cerita, dan gaya penulis.
9. Setelah edit, periksa continuity, timeline, setup/payoff, pemahaman pembaca, dan konteks bab sebelum/sesudahnya.

## Severity dan release impact
- Catatan/instruksi internal yang jelas tertinggal: ERROR, umumnya FIX BEFORE RELEASE.
- Kebocoran yang membingungkan pembaca, merusak reveal, atau membocorkan informasi terlalu dini: HIGH/BLOCKER sesuai dampak.
- Repetisi/eksposisi mekanis tanpa gangguan pemahaman: REVIEW atau OPTIONAL POLISH.
- Pilihan gaya/naratif yang sah: bukan temuan.

## Laporan
Cantumkan dokumen perencanaan tersedia/tidak tersedia; bab/lokasi dan kutipan; kategori; klasifikasi; alasan dan dampak pembaca; tindakan minimum (hapus, ringkas, ubah menjadi konteks alami, atau pertahankan); serta status verifikasi.

## Prinsip akhir
Outline menjaga konsistensi di belakang layar. Naskah hanya menyampaikan apa yang perlu dialami atau diketahui pembaca. Jangan biarkan pembaca melihat scaffolding yang dipakai penulis untuk membangun cerita.
