import re

def cektanggal(teks):
    
    hariini = 739379
    tekspisah = teks.split(" ")
    
    for i in tekspisah:
        if i[0].isdigit():
            tanggal = re.split(r'\W', i)
            hari = int(tanggal[2])
            bulan = int(tanggal[1])
            tahun = int(tanggal[0])
            jumlahHariSebulan = [31,28,31,30,31,30,31,31,30,31,30,31]
            jumlahHariPertahun = (tahun - 1) * 365
            totalhari = sum(jumlahHariSebulan[:bulan-1])
            totalhari += hari
            total = jumlahHariPertahun + totalhari
            selisih = hariini - total
            print(f'{tahun}-{bulan:02d}-{hari:02d} selisih {selisih} hari')

cektanggal("Pada tanggal 1945-08-17 Indonesia merdeka. Indonesia memiliki beberapa pahlawan nasional, seperti Pangeran Diponegoro (TL: 1785-11-11), Pattimura (TL: 1783-06-08) dan Ki Hajar Dewantara (1889-05-02).")