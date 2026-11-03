# src/simulator.py

def hitung_fcfs(proses):
    waktu_sekarang = 0
    hasil = []
    proses.sort(key=lambda x: x['at'])
    
    for p in proses:
        if waktu_sekarang < p['at']:
            waktu_sekarang = p['at']
        waktu_sekarang += p['bt']
        
        ct = waktu_sekarang
        tat = ct - p['at']
        wt = tat - p['bt']
        
        hasil.append({
            'id': p['id'], 'at': p['at'], 'bt': p['bt'], 
            'ct': ct, 'tat': tat, 'wt': wt
        })
    return hasil

def hitung_sjf(proses):
    waktu_sekarang = 0
    hasil = []
    proses_tersedia = []
    proses.sort(key=lambda x: x['at'])
    sisa_proses = proses.copy()
    
    while sisa_proses or proses_tersedia:
        while sisa_proses and sisa_proses[0]['at'] <= waktu_sekarang:
            proses_tersedia.append(sisa_proses.pop(0))
        
        if proses_tersedia:
            # Pilih proses dengan Burst Time terpendek
            proses_tersedia.sort(key=lambda x: x['bt'])
            p = proses_tersedia.pop(0)
            
            waktu_sekarang += p['bt']
            ct = waktu_sekarang
            tat = ct - p['at']
            wt = tat - p['bt']
            
            hasil.append({
                'id': p['id'], 'at': p['at'], 'bt': p['bt'], 
                'ct': ct, 'tat': tat, 'wt': wt
            })
        else:
            waktu_sekarang = sisa_proses[0]['at']
            
    return hasil

def hitung_rr(proses, quantum):
    waktu_sekarang = 0
    hasil = []
    antrean = []
    proses.sort(key=lambda x: x['at'])
    # Tambahkan key sisa_bt untuk melacak sisa waktu eksekusi
    sisa_proses = [{**p, 'sisa_bt': p['bt']} for p in proses]
    
    if sisa_proses:
        waktu_sekarang = sisa_proses[0]['at']
        
    while sisa_proses or antrean:
        while sisa_proses and sisa_proses[0]['at'] <= waktu_sekarang:
            antrean.append(sisa_proses.pop(0))
            
        if antrean:
            p = antrean.pop(0)
            waktu_eksekusi = min(p['sisa_bt'], quantum)
            waktu_sekarang += waktu_eksekusi
            p['sisa_bt'] -= waktu_eksekusi
            
            # Masukkan proses yang baru tiba selama eksekusi barusan
            while sisa_proses and sisa_proses[0]['at'] <= waktu_sekarang:
                antrean.append(sisa_proses.pop(0))
            
            # Jika belum selesai, kembalikan ke antrean
            if p['sisa_bt'] > 0:
                antrean.append(p)
            else:
                ct = waktu_sekarang
                tat = ct - p['at']
                wt = tat - p['bt']
                hasil.append({
                    'id': p['id'], 'at': p['at'], 'bt': p['bt'], 
                    'ct': ct, 'tat': tat, 'wt': wt
                })
        else:
            if sisa_proses:
                waktu_sekarang = sisa_proses[0]['at']

    # Urutkan berdasarkan ID agar output tabel rapi
    hasil.sort(key=lambda x: x['id'])
    return hasil

def cetak_tabel(hasil, nama_algoritma):
    print(f"\n=== Hasil Simulasi {nama_algoritma} ===")
    print(f"{'ID':<5} | {'AT':<5} | {'BT':<5} | {'CT':<5} | {'TAT':<5} | {'WT':<5}")
    print("-" * 45)
    
    total_tat = total_wt = 0
    for p in hasil:
        print(f"{p['id']:<5} | {p['at']:<5} | {p['bt']:<5} | {p['ct']:<5} | {p['tat']:<5} | {p['wt']:<5}")
        total_tat += p['tat']
        total_wt += p['wt']
        
    print("-" * 45)
    print(f"Rata-rata TAT : {total_tat/len(hasil):.2f}")
    print(f"Rata-rata WT  : {total_wt/len(hasil):.2f}\n")

if __name__ == "__main__":
    daftar_proses = []
    print("--- Simulator Penjadwalan CPU ---")
    n = int(input("Masukkan jumlah proses: "))
    quantum = int(input("Masukkan Time Quantum (untuk Round Robin): "))
    
    for i in range(n):
        print(f"\nProses P{i+1}")
        at = int(input("Arrival Time : "))
        bt = int(input("Burst Time   : "))
        daftar_proses.append({'id': f'P{i+1}', 'at': at, 'bt': bt})
        
    # Eksekusi secara berurutan menggunakan salinan data (.copy())
    hasil_fcfs = hitung_fcfs(daftar_proses.copy())
    cetak_tabel(hasil_fcfs, "First-Come First-Served (FCFS)")
    
    hasil_sjf = hitung_sjf(daftar_proses.copy())
    cetak_tabel(hasil_sjf, "Shortest Job First (SJF)")
    
    hasil_rr = hitung_rr(daftar_proses.copy(), quantum)
    cetak_tabel(hasil_rr, f"Round Robin (Quantum = {quantum})")