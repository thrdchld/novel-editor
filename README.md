# Novel Editor
Genre-agnostic technical story auditor. Fokus: plot hole, logika sebab-akibat, timeline, worldbuilding, konsistensi, continuity, character knowledge, setup/payoff, repetition, AI-slop indicators, dan aturan teknis khusus proyek.

## Batasan
Tidak menilai tone, gaya penceritaan, voice, diksi, keindahan prosa, atau selera artistik. Tidak memaksakan aturan MetroPop atau genre tertentu. Tidak menganggap fantasi sebagai kesalahan hanya karena berbeda dari dunia nyata. Read-only: tidak mengubah naskah.

## Struktur
- `AGENTS.md`: instruksi agent.
- `EDITOR-PROTOCOL.md`: protokol dan tingkat keparahan.
- `project.yaml`: konfigurasi proyek; semua hard constraints bersifat opsional.
- `rules/`: aturan audit teknis.
- `checklists/`: daftar pemeriksaan.
- `templates/`: format laporan.
- `scripts/`: pemeriksaan mekanis sederhana.
- `schemas/`: skema temuan.

## Penggunaan
1. Letakkan folder ini di repo novel atau jadikan repo auditor terpisah.
2. Sesuaikan `project.yaml`.
3. Isi daftar referensi dengan file yang benar-benar ada (world bible, outline, character bible, timeline, dll.).
4. Jalankan `python scripts/run-audit.py --root PATH_PROYEK`.
5. Minta agent membaca `AGENTS.md` dan `EDITOR-PROTOCOL.md`, lalu audit naskah secara kontekstual.

Script hanya memeriksa hal mekanis sederhana. Plot hole, worldbuilding, dan continuity semantik harus diaudit dengan membaca konteks naskah.

## Severity
- ERROR: kontradiksi eksplisit atau pelanggaran aturan keras yang terbukti.
- HIGH: kegagalan logika/continuity kuat yang kemungkinan membingungkan pembaca.
- REVIEW: indikasi yang memerlukan pertimbangan manusia/penulis.
- INFO: catatan opsional.
