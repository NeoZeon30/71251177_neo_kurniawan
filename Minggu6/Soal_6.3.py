#NeoKurniawan 71251177

jumlah_mata_kuliah = int(input("Berapa Jumlah Mata Kuliah: "))
bobot_sks = {'A' : 4, 'B' : 3,'C' : 2, 'D' : 1}
hasil = 0
for i in range(jumlah_mata_kuliah):
    nilai_mk =(input(f"Nilai MK {i + 1}: "))
    hasil += bobot_sks [nilai_mk]
print(f"Nilai IPS anda semester ini {round((hasil/jumlah_mata_kuliah),2)}")