n = int(input("Masukkan Jumlah kategori: "))
data_aplikasi = {}

for i in range(n):
    nama_kategori = input(f"Masukkan nama Kategori ke-{i+1}: ")
    print(f'Masukkan 5 nama aplikasi di kategori {nama_kategori}')
    aplikasi = []
    for j in range(5):
        nama_aplikasi = input(f'Nama aplikasi-{j+1}: ')
        aplikasi.append(nama_aplikasi)
    data_aplikasi[nama_kategori] = aplikasi

jumlah_muncul = {}

for daftar in data_aplikasi.values():
    aplikasi_unik = set(daftar)
    for apk in aplikasi_unik:
        if apk in jumlah_muncul:
            jumlah_muncul[apk] += 1
        else:
            jumlah_muncul[apk] = 1

print("aplikasi yang muncul di satu kategori")
for apk in jumlah_muncul:
    if jumlah_muncul[apk] == 1:
        print(apk)

if n>2:
    print("aplikasi yang muncul di dua kategori")
    for apk in jumlah_muncul:
        if jumlah_muncul[apk] == 2:
            print(apk)
            
            