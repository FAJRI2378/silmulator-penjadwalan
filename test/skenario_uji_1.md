# Laporan Pengujian MVP Simulator Penjadwalan CPU

**Tanggal Uji:** 2 November 2026
**Status:** LULUS (PASS)

## 1. Data Input Pengujian
Pengujian dilakukan menggunakan 3 proses dengan spesifikasi berikut:
* **P1:** Arrival Time (AT) = 0, Burst Time (BT) = 5
* **P2:** Arrival Time (AT) = 1, Burst Time (BT) = 3
* **P3:** Arrival Time (AT) = 2, Burst Time (BT) = 8
* **Time Quantum (RR):** 2

---

## 2. Validasi FCFS (First-Come First-Served)
**Perhitungan Matematis Manual:**
* **P1** tiba di t=0, dieksekusi 0-5. Completion Time (CT) = 5.
  * Turnaround Time (TAT) = CT - AT = 5 - 0 = 5
  * Waiting Time (WT) = TAT - BT = 5 - 5 = 0
* **P2** tiba di t=1, dieksekusi 5-8. CT = 8.
  * TAT = 8 - 1 = 7
  * WT = 7 - 3 = 4
* **P3** tiba di t=2, dieksekusi 8-16. CT = 16.
  * TAT = 16 - 2 = 14
  * WT = 14 - 8 = 6

* **Rata-rata TAT manual:** (5 + 7 + 14) / 3 = 8.67
* **Rata-rata WT manual:** (0 + 4 + 6) / 3 = 3.33

**Hasil Program:** COCOK. Output terminal program menunjukkan Rata-rata TAT: 8.67 dan Rata-rata WT: 3.33.

---

## 3. Validasi SJF (Shortest Job First - Non Preemptive)
**Perhitungan Matematis Manual:**
* **t=0:** Hanya P1 yang tersedia. Dieksekusi 0-5. CT = 5. (TAT=5, WT=0)
* **t=5:** Antrean tersedia adalah P2 (BT=3) dan P3 (BT=8). P2 dipilih karena BT paling pendek.
* **P2** dieksekusi 5-8. CT = 8. (TAT=7, WT=4)
* **P3** dieksekusi 8-16. CT = 16. (TAT=14, WT=6)

* **Rata-rata TAT manual:** 8.67
* **Rata-rata WT manual:** 3.33

**Hasil Program:** COCOK.

---

## 4. Validasi Round Robin (Quantum = 2)
**Perhitungan Matematis Manual (Gantt Chart Simulasi):**
* **t=0-2:** P1 berjalan (Sisa BT P1=3). Antrean: [P2(t=1), P3(t=2), P1]
* **t=2-4:** P2 berjalan (Sisa BT P2=1). Antrean: [P3, P1, P2]
* **t=4-6:** P3 berjalan (Sisa BT P3=6). Antrean: [P1, P2, P3]
* **t=6-8:** P1 berjalan (Sisa BT P1=1). Antrean: [P2, P3, P1]
* **t=8-9:** P2 berjalan hingga selesai (Sisa BT P2=0). **CT P2 = 9**. Antrean: [P3, P1]
* **t=9-11:** P3 berjalan (Sisa BT P3=4). Antrean: [P1, P3]
* **t=11-12:** P1 berjalan hingga selesai (Sisa BT P1=0). **CT P1 = 12**. Antrean: [P3]
* **t=12-14:** P3 berjalan (Sisa BT P3=2). Antrean: [P3]
* **t=14-16:** P3 berjalan hingga selesai (Sisa BT P3=0). **CT P3 = 16**.

**Kalkulasi Metrik (TAT = CT - AT, WT = TAT - BT):**
* **P1:** CT=12 | TAT = 12-0 = 12 | WT = 12-5 = 7
* **P2:** CT=9  | TAT = 9-1 = 8   | WT = 8-3 = 5
* **P3:** CT=16 | TAT = 16-2 = 14 | WT = 14-8 = 6

* **Rata-rata TAT manual:** (12 + 8 + 14) / 3 = 11.33
* **Rata-rata WT manual:** (7 + 5 + 6) / 3 = 6.00

**Hasil Program:** COCOK. Keluaran tabel hasil Round Robin menunjukkan akurasi 100% terhadap perhitungan manual.

## Kesimpulan
Logika perhitungan waktu pada algoritma FCFS, SJF, dan Round Robin telah tervalidasi dan berfungsi tanpa *bug*.