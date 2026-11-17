# Status Paket

Versi 3.1 — standar kerja editor novel berbantuan AI yang genre-agnostic.

## Cakupan

- Plot logic, plot hole, causality, dan audit rantai sebab-akibat dari bab mentah (**E1** — `rules/01-plot-and-causality.md`, `templates/manuscript-report.md`): tabel 7 kolom (`peristiwa | keinginan tokoh | hambatan | pilihan | akibat yang tampak di halaman | pertanyaan "kenapa tidak X?" | jawaban di halaman`), penolakan alasan abstrak (*"karena nggak enakan/gengsi"*) tanpa pemicu konkret di halaman, hitungan konflik yang bisa selesai dengan satu pertanyaan/pesan yang diabaikan tokoh, serta kewajiban motif penahanan informasi yang sudah ditanam.
- Timeline, chronology, usia, durasi, deadline, dan konsistensi waktu relatif.
- Continuity karakter, relasi, benda, lokasi, sumber daya, institusi, dokumen, dan informasi.
- Worldbuilding dan aturan internal.
- Character knowledge dan aliran informasi (**E2** — `rules/05-character-knowledge.md`): pencatatan apa yang diketahui tokoh dan dari mana sumbernya pada setiap keputusan, serta kewajiban menanggapi petunjuk yang sudah ditanam dan diketahui POV tetapi bertentangan dengan kesimpulannya di halaman.
- Setup/payoff, janji cerita, misteri, resolusi, dan audit rujukan mundur (**E2** — `rules/06-setup-payoff.md`): setiap rujukan ke masa lalu (*"dulu"*, *"waktu itu"*, *"ceritanya di"*, *"katanya"*, *"kemarin"*, *"minggu lalu"*, dll.) wajib ditemukan pada bab sebelumnya dengan detail yang sama.
- Prosedur dan proses dunia nyata (**E3** — `rules/18-real-world-procedures.md`): identifikasi proses penerbitan/percetakan, hukum, medis, transportasi, birokrasi/HRD, dan keuangan beserta durasi/urutannya, verifikasi pencarian web dengan pencatatan sumber, dan penandaan `UNVERIFIED` (bukan lulus) bila tidak dapat diverifikasi.
- Pemindai rujukan mundur mekanis (**E4** — `scripts/audit_core.py --refs`): flag CLI `--refs` untuk mengekstrak daftar markdown semua kata/frasa relatif-waktu dan rujukan masa lalu per bab beserta nomor baris dan kutipan pendek untuk diperiksa editor AI.
- Keterbacaan naratif, orientasi pembaca, blocking adegan, dan transisi (`rules/15`, `rules/16`, `rules/17`).
- Teknis naskah: ejaan, typo, tata bahasa objektif, tanda baca, konsistensi nama/istilah, Markdown, struktur bab, placeholder, dan catatan internal.
- Repetition, AI-slop indicators, dan hard constraints proyek.

## Batas

Mempertahankan identitas kreatif, tone, voice, dan pilihan artistik penulis (tidak menghakimi selera pribadi), tetapi tetap menilai apakah kalimat, adegan, dan transisi berhasil menyampaikan makna kepada pembaca. Script Python (`scripts/run-audit.py`, termasuk `--refs`) hanya membuat daftar dan pemeriksaan mekanis; penilaian semantik, kausalitas, dan ejaan kontekstual tetap dilakukan melalui pembacaan editor.

## Kebijakan kerja dan Blind Pass

- **Mode kerja default adalah AUDIT (read-only):** Editor menghasilkan laporan audit lengkap beserta daftar perbaikan spesifik (file, kalimat, dan saran perubahan minimal). Pengeditan langsung pada file naskah **hanya** dilakukan jika pengguna secara eksplisit meminta perbaikan. Saat pengeditan diminta, perubahan harus minimal, mempertahankan voice penulis, dan diverifikasi ulang.
- **Aturan Blind Pass wajib:** Pada tahap pertama audit, editor wajib membaca **HANYA** bab naskah (`chapters/` atau `manuscript.md`) dan `outline.md`, lalu menyusun Tabel Rantai Sebab-Akibat (**E1**) **SEBELUM** membuka `canon.md`, `ledger.md`, `state.md`, atau laporan audit lama (`reports/`). Laporan wajib mencatat secara eksplisit bahwa *blind pass* telah dilakukan.

## Publication readiness

Keputusan berbasis dampak pembaca dan gerbang kelayakan (`rules/09-publication-readiness.md`):
- READY TO PUBLISH
- READY WITH MINOR FIXES
- NOT READY
- INSUFFICIENT EVIDENCE

Temuan dibedakan menjadi BLOCKER, FIX BEFORE RELEASE, ACCEPTABLE/AUTHOR CHOICE, dan OPTIONAL POLISH.
