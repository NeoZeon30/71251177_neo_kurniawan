import re
masukkan = input("Masukan nama file: ")
try:
    with open(masukkan, 'r') as file:
        file = file.read()


    cari = re.findall(r'^From .* ([0-9]{2}):[0-9]{2}:[0-9]{2}', file, re.MULTILINE)

    frekuensi = {}
    for jam in cari:
        frekuensi[jam] = frekuensi.get(jam, 0) + 1

    for jam in sorted(frekuensi):
        print(jam,frekuensi[jam])
except FileNotFoundError:
    print("File tidak ditemukan")