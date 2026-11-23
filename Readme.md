# Simulator Penjadwalan CPU

Proyek ini adalah simulator penjadwalan CPU berbasis antarmuka teks (CLI) yang dibangun dengan Python untuk memenuhi tugas mata kuliah Sistem Operasi.

## Fitur (MVP)
* Input dinamis: ID Proses, Arrival Time, Burst Time, dan Time Quantum.
* Algoritma: First-Come First-Served (FCFS), Shortest Job First (SJF), dan Round Robin (RR).
* Output: Tabel metrik waktu (CT, TAT, WT, dan rata-rata), serta puncak alokasi memori Python selama simulasi tiap algoritma.

Pengukuran memori menggunakan `tracemalloc`, sehingga menunjukkan puncak alokasi objek Python selama pemanggilan algoritma (byte dan KiB). Nilainya bergantung pada versi Python dan lingkungan; nilai ini bukan total RAM proses atau sistem operasi. Kompleksitas ruang tambahan ketiga algoritma adalah O(n), dengan n sebagai jumlah proses.

## Cara Menjalankan
1. Pastikan Python 3 sudah terinstal.
2. Buka terminal atau command prompt di direktori repositori ini.
3. Jalankan perintah berikut:
   ```bash
   python src/simulator.py