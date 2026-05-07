import re
try:
    masukan = input("Masukkan Nama file: ")
    with open(masukan,'r') as file:
        file = file.read()
        simpan = {}
        jumlahpesan = re.findall(r'^From \S+@(\S+)',file,re.MULTILINE)
        for i in jumlahpesan:
            simpan[i] = simpan.get(i,0) + 1
        print(simpan)
except FileNotFoundError:
    print("File tidak ditemukan ")