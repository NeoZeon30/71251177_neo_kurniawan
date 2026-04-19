def menghitungPanjangPendek():
    
    kalimat = input("Masukan Kalimat: ")
    memisahkan = kalimat.split()
    pendek = memisahkan[0]
    panjang = memisahkan[0]
    
    for i in memisahkan[1:]:
        if len(i) < len(pendek):
            pendek = i
        if len(i) > len(panjang):
            panjang = i
    print(f'Terpendek adalah: {pendek}')
    print(f'Terpanjang adalah: {panjang}')

menghitungPanjangPendek()