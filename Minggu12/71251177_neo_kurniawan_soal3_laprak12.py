import re 
masukan = input("Masukkan nama file:")
try:
    with open(masukan,'r') as file:
        file = file.read()
        tampung = {}
        cari = re.findall(r"^Author: (\S+)",file,re.MULTILINE)
        for i in cari:
            tampung[i] = tampung.get(i,0) + 1
        print(tampung)    
except FileNotFoundError:
    print("file tidak ditemukan")