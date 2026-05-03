simpan = []
while True:
    jumlahngka = input("Masukan angka (Ketikkan 'done' jika selesai): ")
    if jumlahngka.lower() == 'done':
        break 
    angka = float(jumlahngka)
    simpan.append(angka)
if simpan:
    ratarata = sum(simpan) / len(simpan)
    print(f'Nilai rata - rata adalah: {ratarata}')
else:
    print("Tidak ada bilangan yang dimasukkan")