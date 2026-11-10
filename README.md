# Novel Editor

**Novel Editor adalah sistem penyuntingan novel berbantuan AI yang menilai dan memperbaiki naskah sebagai karya utuh sekaligus pengalaman membaca.** Sistem ini dirancang untuk menerima naskah AI yang belum matang, menemukan masalah pada fondasi cerita maupun penyajiannya, melakukan perbaikan editorial yang dapat dipertanggungjawabkan, lalu menentukan apakah naskah sudah layak dibaca dan diterbitkan.

Standar ini genre-agnostic. Ia tidak memaksakan formula genre atau selera artistik editor, tetapi tidak membatasi pemeriksaan hanya pada kesalahan teknis mekanis.

## Mandat editorial

Editor wajib menjawab dua pertanyaan yang berbeda:

1. **Apakah cerita bekerja?** Premis, konflik, karakter, sebab-akibat, perkembangan, struktur, adegan, dan penyelesaian membentuk cerita yang koheren.
2. **Apakah cerita tersampaikan dengan baik kepada pembaca?** Pembaca dapat memahami orientasi waktu/tempat, mengikuti perpindahan adegan, mengenali siapa yang bertindak dan mengetahui apa, memahami emosi serta motivasi dari konteks, dan terus mengikuti alur tanpa kebingungan yang tidak disengaja.

Naskah yang logis tetapi membingungkan saat dibaca belum lulus. Naskah yang kalimatnya rapi tetapi konflik dan adegannya tidak bekerja juga belum lulus.

## Cakupan penyuntingan

1. **Story assessment:** premis, janji cerita, konflik utama, daya dorong, fokus, dan kelayakan rancangan.
2. **Developmental editing:** struktur keseluruhan, urutan peristiwa, perkembangan konflik, karakter, subplot, eskalasi, klimaks, dan ending.
3. **Narrative editing:** cara informasi disajikan; orientasi pembaca; pembukaan/penutupan flashback; transisi waktu, tempat, adegan, dan bab; POV; eksposisi; ritme informasi; kejelasan motivasi dan emosi.
4. **Scene editing:** tujuan dan fungsi adegan, kondisi awal/akhir, perubahan yang terjadi, sebab-akibat, blocking, dialog, reaksi, dan hubungan antarscene.
5. **Continuity editing:** timeline, karakter, relasi, benda, lokasi, kondisi fisik, pengetahuan, sumber daya, dan aturan dunia.
6. **Line editing:** kejernihan kalimat, aliran paragraf, repetisi, referen, pilihan kata yang tidak tepat, kalimat janggal, dan keterbacaan—tanpa menyeragamkan voice.
7. **Copyediting:** ejaan, typo, tata bahasa, tanda baca, konsistensi istilah, dan format.
8. **Fact checking:** fakta/prosedur dunia nyata yang material bagi cerita.
9. **Publication assessment:** dampak masalah terhadap pengalaman pembaca dan keputusan reader-ready.

## Prinsip penilaian

- Nilai naskah berdasarkan tujuan cerita, bukti dalam naskah, logika internal, dan pengalaman pembaca yang wajar—bukan selera pribadi editor.
- Gaya, tone, voice, humor, diksi artistik, dan bentuk narasi adalah pilihan kreatif, bukan wilayah terlarang untuk dianalisis. Editor boleh menilai apakah pilihan penyajian berhasil menyampaikan adegan, tetapi tidak boleh menggantinya hanya karena lebih menyukai gaya lain.
- Flashback tidak wajib memakai tense tertentu. Yang wajib ialah pembaca mendapat orientasi temporal yang cukup dan dapat mengenali kapan adegan masa lalu dimulai serta kapan cerita kembali.
- Pacing bukan angka kecepatan universal. Periksa apakah informasi, aksi, reaksi, dan jeda ditempatkan sehingga perkembangan cerita dapat diikuti dan efek adegan tercapai.
- Outline adalah dokumen kerja, bukan hukum yang mengalahkan manuskrip. Perbedaan harus dianalisis; tentukan apakah manuskrip, outline, atau canon yang perlu diperbaiki.
- Tidak semua ambiguitas adalah kesalahan. Misteri dan penahanan informasi boleh disengaja selama pembaca tetap memahami hal yang perlu dipahami pada saat itu.
- Perbaiki masalah dengan perubahan terkecil yang memulihkan fungsi cerita. Jangan melakukan rewrite total jika revisi lokal atau struktural terbatas sudah cukup.
- Jangan menahan publikasi untuk optional polish. Standarnya reader-ready, not perfect.

## Alur kerja

1. Inventarisasi naskah, outline, canon, konfigurasi, dan dokumen referensi.
2. Pahami janji cerita, konteks, genre sebagai deskripsi, POV, tense, target, dan keputusan yang dikunci.
3. Baca naskah sebagai pembaca untuk memperoleh gambaran pengalaman aktual; jangan langsung mulai dari checklist mekanis.
4. Lakukan story assessment dan developmental audit.
5. Audit narasi, adegan, transisi, orientasi pembaca, dan keterbacaan bab demi bab.
6. Bangun fact ledger dan lakukan audit lintas bab: timeline, continuity, knowledge, setup/payoff, serta aturan dunia.
7. Lakukan line editing, copyediting, dan pemeriksaan format.
8. Verifikasi fakta eksternal yang material bila diperlukan.
9. Putuskan dan terapkan perbaikan; jangan berhenti pada daftar temuan.
10. Baca ulang hasil revisi dalam konteks sebelum/sesudahnya, lalu audit dependensi.
11. Lakukan publication gate berdasarkan pengalaman membaca keseluruhan naskah.

## Mode kerja

- **Audit read-only:** tidak mengubah file jika pengguna hanya meminta penilaian.
- **Workflow produksi:** jika pengguna meminta editor menjalankan atau memperbaiki naskah, audit dan perbaikan editorial adalah default. Perbaikan yang jelas dan dapat disimpulkan dilakukan tanpa meminta persetujuan satu per satu.
- **Keputusan kreatif material:** jangan mengarang perubahan premis, pasangan akhir, kematian/kehidupan tokoh, motivasi inti, atau ending yang belum diputuskan. Minta keputusan hanya jika alternatif tetap sama kuat setelah analisis.
- **Preservasi voice:** pertahankan karakter suara penulis. Perbaiki kalimat yang tidak bekerja, bukan mengubah semua kalimat menjadi gaya seragam.
- **Transparansi:** setiap perubahan signifikan harus punya alasan, bukti, dan status verifikasi.

## Severity dan dampak rilis

Severity: ERROR, HIGH, REVIEW, INFO.

Dampak rilis:
- BLOCKER: mengganggu pemahaman atau merusak cerita secara material.
- FIX BEFORE RELEASE: masalah nyata yang harus dibereskan tetapi terbatas.
- ACCEPTABLE / AUTHOR CHOICE: pilihan kreatif atau ambiguitas yang bekerja.
- OPTIONAL POLISH: penyempurnaan yang tidak perlu menunda rilis.

Kategori dan format laporan lengkap berada di EDITOR-PROTOCOL.md dan rules/.

## Struktur repository

- AGENTS.md: mandat dan instruksi utama agent.
- SKILL.md: entrypoint reusable.
- EDITOR-PROTOCOL.md: prosedur kerja, diagnosis, bukti, severity, dan kebijakan edit.
- rules/: standar story assessment, developmental, narrative, scene, continuity, line/copy editing, outline, dan publication.
- checklists/: alat bantu audit; bukan pengganti pembacaan dan penilaian.
- templates/: format outline, laporan, dan artefak editorial.
- scripts/: scanner mekanis; tidak dapat menggantikan penilaian naratif.
- schemas/ dan tests/: struktur data dan pengujian.

## Batas alat otomatis

Scanner hanya dapat memeriksa pola yang dapat dipastikan secara mekanis. Ia tidak dapat menentukan apakah pembukaan menarik, flashback membingungkan, adegan terasa patah, dialog alami, emosi meyakinkan, atau alur enak diikuti. Lulus scanner bukan lulus editorial.

**Status READY TO PUBLISH hanya boleh diberikan setelah editor membaca dan menilai pengalaman membaca naskah secara menyeluruh, bukan hanya karena checklist atau script tidak menemukan kesalahan.**
