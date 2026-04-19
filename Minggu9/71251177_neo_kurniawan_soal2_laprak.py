def menghitungAngka():
    kalimat = input("Masukan Kalimat: ")
    lower = kalimat.lower()
    cekKata = input("Kata Yang ingin di cek: ")
    
    if cekKata in kalimat:
      jumlah =  lower.count(cekKata)
    print(f'Jumlah kata adalah: {jumlah}')

menghitungAngka()