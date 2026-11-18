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

1. **Blind pass (tahap pertama wajib):** Baca HANYA bab naskah (`chapters/` atau `manuscript.md`) dan `outline.md`, lalu susun Tabel Rantai Sebab-Akibat (`rules/01-plot-and-causality.md`) **SEBELUM** membuka `canon.md`, `ledger.md`, `state.md`, atau laporan audit lama (`reports/`). Catat di laporan bahwa *blind pass* telah dilakukan.
2. Setelah *blind pass* selesai, baru inventarisasi konfigurasi, canon, ledger, state, dan dokumen referensi lainnya; pahami janji cerita, konteks, genre sebagai deskripsi, POV, tense, target, dan keputusan yang dikunci.
3. Baca naskah sebagai pembaca untuk memperoleh gambaran pengalaman aktual; jangan langsung mulai dari checklist mekanis.
4. Lakukan story assessment dan developmental audit.
5. Audit narasi, adegan, transisi, orientasi pembaca, dan keterbacaan bab demi bab.
6. Bangun fact ledger, jalankan pemindai rujukan mundur (`--refs`), dan lakukan audit lintas bab: timeline, continuity, character knowledge (`05`), setup/payoff & rujukan mundur (`06`), serta aturan dunia.
7. Lakukan line editing, copyediting, dan pemeriksaan format.
8. Verifikasi proses dan prosedur dunia nyata yang material (`rules/18-real-world-procedures.md`) dengan pencarian web dan catat sumbernya (atau tandai `UNVERIFIED`).
9. Susun laporan audit lengkap beserta daftar perbaikan spesifik (file, kalimat, saran perubahan minimal). Jika pengguna secara eksplisit meminta pengeditan naskah, terapkan perbaikan.
10. Jika naskah diedit, baca ulang hasil revisi dalam konteks sebelum/sesudahnya, lalu audit dependensi.
11. Lakukan publication gate berdasarkan pengalaman membaca keseluruhan naskah (`rules/09-publication-readiness.md`).

## Mode kerja

- **Default adalah AUDIT (read-only):** Secara default, editor tidak mengubah file naskah. Editor menghasilkan laporan audit lengkap beserta daftar perbaikan spesifik (file, kutipan kalimat, dan saran perubahan minimal).
- **Perbaikan atas permintaan eksplisit:** Editor hanya mengedit naskah secara langsung jika pengguna secara eksplisit meminta perbaikan/revisi. Saat diminta memperbaiki, perbaikan yang jelas dan dapat disimpulkan dilakukan lalu diverifikasi ulang.
- **Keputusan kreatif material:** jangan mengarang perubahan premis, pasangan akhir, kematian/kehidupan tokoh, motivasi inti, atau ending yang belum diputuskan. Minta keputusan hanya jika alternatif tetap sama kuat setelah analisis.
- **Preservasi voice:** pertahankan karakter suara penulis. Perbaiki kalimat yang tidak bekerja, bukan mengubah semua kalimat menjadi gaya seragam.
- **Transparansi:** setiap temuan dan saran perubahan signifikan harus punya alasan, bukti, dan status verifikasi.

## Mode gerbang (repo novel-metropop)

Untuk audit proyek di repo `novel-metropop`, tersedia tiga mode gerbang:

- **G1 (Prapenulisan — Cerita Utuh, TANPA bab):** Input hanya `story/<judul>/outline.md` yang berisi bagian cerita utuh + `"Bukti G1"`.
- **G2 (Prapenulisan — Outline Lengkap, TANPA bab):** Input hanya `story/<judul>/outline.md` yang berisi outline lengkap + `"Bukti G2"`.
- **G3 (Naskah Berjalan):** Input berupa bab-bab yang sudah ada (`chapters/`) + `outline.md`; laporan wajib menyebutkan **bab terakhir yang diaudit**.

Pada **G1 dan G2**, *blind pass* tetap berlaku dan editor wajib menjalankan:
1. Pemeriksaan keberadaan dan kelengkapan bagian `"Bukti G1"` / `"Bukti G2"` (jika tidak ada atau kosong, dicatat sebagai **`BLOCKER`**).
2. Tabel rantai sebab-akibat (`rules/01-plot-and-causality.md`) pada titik balik/outline.
3. Pemeriksaan prosedur dunia nyata (`rules/18-real-world-procedures.md`) untuk proses yang tercantum, disertai **URL penuh dan tanggal akses** (atau `UNVERIFIED`).
4. Pemeriksaan rujukan mundur pada outline (fakta lama yang dipakai sebelum ditanam).
5. Khusus **G2**, pengecekan konsistensi kalender dan peta pengetahuan di `"Bukti G2"` terhadap daftar bab.

Vonis **G1/G2** (selaras ambang K2 di `rules/09-publication-readiness.md`, dilaporkan memakai `templates/prapenulisan-report.md` maks 1 halaman):
- **`LAYAK DITULIS`:** `"Bukti"` ada & terisi, 0 `HIGH` kausalitas, 0 `UNVERIFIED`/jadwal mustahil, 0 rujukan mundur belum ditanam, kalender & pengetahuan `Bukti G2` konsisten dengan daftar bab, dan 0 `BLOCKER`.
- **`PERBAIKI DULU`:** Perbaikan dapat diselesaikan secara lokal (≤ 4 bab/bagian, atau melengkapi `"Bukti"`/`UNVERIFIED`) tanpa membongkar outline lintas ≥ 5 bab atau membatalkan titik balik utama.
- **`PREMIS/KERANGKA DIBUANG`:** **Hanya** jika perbaikan membutuhkan perubahan outline lintas ≥ 5 bab, pembatalan titik balik utama, atau perombakan premis inti.

**Lokasi laporan gerbang:** simpan di branch baru `audit/<judul-cerita>/<gerbang>` (mis. `audit/kopi-hujan/G2`) pada repo `novel-editor`, dalam satu berkas `validation/<gerbang>.md`, dan **jangan merge ke `main`**.

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
- rules/: standar severity & bukti (`00`), plot & kausalitas (`01`), timeline (`02`), continuity (`03`), worldbuilding (`04`), character knowledge (`05`), setup/payoff & rujukan mundur (`06`), repetisi (`07`), project constraints (`08`), publication readiness (`09`), kualitas teknis (`10`), netralitas genre (`11`), outline leakage (`12`), keputusan editorial (`13`), validasi outline (`14`), narrative & reader experience (`15`), story assessment & developmental editing (`16`), scene & line editing (`17`), serta prosedur dunia nyata (`18-real-world-procedures.md`).
- checklists/: alat bantu developmental, narrative-reader, chapter, cross-chapter, technical, dan publication audit; bukan pengganti pembacaan dan penilaian.
- templates/: format outline, laporan, dan artefak editorial.
- scripts/: scanner mekanis; tidak dapat menggantikan penilaian naratif.
- schemas/ dan tests/: struktur data dan pengujian.

## Batas alat otomatis

Scanner hanya dapat memeriksa pola yang dapat dipastikan secara mekanis. Ia tidak dapat menentukan apakah pembukaan menarik, flashback membingungkan, adegan terasa patah, dialog alami, emosi meyakinkan, atau alur enak diikuti. Lulus scanner bukan lulus editorial.

**Status READY TO PUBLISH hanya boleh diberikan setelah editor membaca dan menilai pengalaman membaca naskah secara menyeluruh, bukan hanya karena checklist atau script tidak menemukan kesalahan.**
