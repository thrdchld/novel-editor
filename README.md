# Novel Editor

**Novel Editor adalah standar kerja editor teknis novel yang genre-agnostic.** Tujuannya memastikan naskah solid, sinkron, logis, dan dapat diikuti pembaca sebelum dipublikasikan—tanpa menuntut kesempurnaan.

## Apa yang diperiksa

Novel Editor memeriksa seluruh aspek teknis cerita yang dapat diverifikasi dari naskah dan dokumen proyek:

1. Plot hole, integritas plot, dan sebab-akibat.
2. Timeline, kronologi, usia, durasi, deadline, dan urutan kejadian.
3. Continuity karakter, relasi, benda, lokasi, kondisi fisik, sumber daya, dokumen, dan informasi.
4. Character knowledge dan aliran informasi.
5. Worldbuilding, aturan internal, batas, biaya, pengecualian, institusi, geografi, dan sistem.
6. Setup/payoff, janji cerita, petunjuk, misteri, dan penyelesaian konflik.
7. Keterbacaan faktual: siapa melakukan apa, di mana, kapan, dengan informasi apa, dan mengapa.
8. Repetisi informasi/adegan dan indikator AI-slop yang mengganggu fungsi cerita.
9. Teknis naskah: ejaan, typo, tata bahasa objektif, tanda baca, konsistensi nama/istilah, format Markdown, struktur bab, catatan editor, placeholder, dan kesalahan format lain.
10. Hard constraints proyek yang dinyatakan secara eksplisit, misalnya POV, tense, jumlah kata, format bab, atau larangan tanda baca tertentu.

## Yang tidak dinilai

- Tone, gaya penceritaan, voice, diksi, humor, keindahan prosa, atau selera artistik.
- Preferensi editor tentang bagaimana kalimat seharusnya terdengar.
- Konvensi genre sebagai aturan wajib.
- Realisme dunia nyata untuk cerita fantasi/sci-fi yang memiliki aturan internal sendiri.

**Pengecualian penting:** kesalahan teknis bahasa tetap diperiksa. Typo, ejaan baku yang keliru, kalimat yang secara tata bahasa rusak hingga maknanya tidak jelas, tanda baca yang mengubah makna, atau format yang merusak tampilan adalah masalah teknis. Namun, kalimat yang hanya berbeda gaya atau terasa kurang indah bukan kesalahan.

## Mode kerja

- **Audit:** default read-only. Tidak mengubah naskah.
- **Perbaikan atas instruksi eksplisit:** jika pengguna meminta koreksi diterapkan, editor boleh mengubah naskah sesuai temuan yang disetujui/terbukti. Jangan mengubah tone atau gaya.
- **Verifikasi:** setelah perbaikan, audit ulang bagian terdampak dan cek efek lintas bab. Jangan mengulang seluruh audit tanpa alasan.

Mengedit aturan dan konfigurasi Novel Editor tidak sama dengan mengedit naskah novel.

## Struktur

- \`AGENTS.md\`: instruksi utama agent.
- \`EDITOR-PROTOCOL.md\`: protokol audit, bukti, severity, dan kebijakan perbaikan.
- \`project.yaml\`: konfigurasi cakupan, referensi, hard constraints, dan mode kerja.
- \`rules/\`: standar pemeriksaan teknis.
- \`checklists/\`: checklist bab, lintas bab, worldbuilding, teknis naskah, dan publikasi.
- \`templates/\`: format laporan temuan dan keputusan.
- \`scripts/\`: scanner mekanis; bukan pengganti audit kontekstual.
- \`schemas/\`: skema data temuan.
- \`tests/\`: pengujian scanner.

## Cara menggunakan

1. Tempatkan paket ini di repository novel atau gunakan sebagai standar terpisah.
2. Sesuaikan \`project.yaml\` dengan lokasi naskah dan dokumen referensi yang benar-benar ada.
3. Masukkan outline, canon, timeline, character bible, world bible, dan glossary jika tersedia.
4. Jalankan:

   \`\`\`bash
   pip install -r requirements.txt
   python scripts/run-audit.py --root PATH_PROYEK
   \`\`\`

5. Minta agent membaca \`AGENTS.md\`, \`EDITOR-PROTOCOL.md\`, semua rule relevan, konfigurasi, dokumen referensi, dan naskah.
6. Lakukan audit per bab dan audit lintas bab. Untuk naskah panjang, bangun fact ledger dan lanjutkan secara bertahap tanpa menghilangkan konteks.
7. Hasilkan laporan dengan bukti dan keputusan kelayakan publikasi.
8. Jika diminta memperbaiki, terapkan koreksi teknis minimal lalu lakukan verifikasi ulang.

## Batas scanner otomatis

Script hanya memeriksa hal mekanis yang dapat dipastikan dengan aturan sederhana: cakupan file, jumlah kata per bab jika dikonfigurasi, urutan/duplikasi nomor bab, pagar code fence, pola catatan/placeholder, em dash jika dilarang, dan kata berulang berdekatan.

Scanner **tidak** dapat membuktikan plot hole, menilai makna kalimat secara penuh, mendeteksi semua typo, atau menggantikan pemeriksaan ejaan dan continuity oleh editor. Hasil scanner harus dibaca bersama audit kontekstual. Jangan pernah mengklaim seluruh naskah sudah diperiksa hanya karena script selesai berjalan.

## Severity dan dampak rilis

Severity:
- \`ERROR\`: kontradiksi eksplisit atau pelanggaran hard rule yang terbukti.
- \`HIGH\`: kegagalan logika/continuity yang kuat dan mengganggu pemahaman.
- \`REVIEW\`: indikasi yang memerlukan verifikasi atau keputusan penulis.
- \`INFO\`: catatan opsional.

Dampak rilis:
- \`BLOCKER\`: menghalangi publikasi.
- \`FIX BEFORE RELEASE\`: kesalahan teknis nyata yang perlu diperbaiki, tetapi lokal.
- \`ACCEPTABLE / AUTHOR CHOICE\`: pilihan kreatif/ambiguitas yang tidak merusak pemahaman.
- \`OPTIONAL POLISH\`: tidak boleh menahan publikasi.

## Publication readiness

Kemungkinan keputusan:
- \`READY TO PUBLISH\`
- \`READY WITH MINOR FIXES\`
- \`NOT READY\`
- \`INSUFFICIENT EVIDENCE\`

Prinsipnya: **reader-ready, not perfect**. Jika tidak ada blocker material, jangan menahan novel hanya untuk optional polish. Keputusan teknis ini bukan jaminan penerimaan platform, legalitas hak cipta, atau kesuksesan pasar.
