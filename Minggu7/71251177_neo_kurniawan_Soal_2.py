n = int(input("Masukan angka: "))

for i in range(n, 0, -1):
    hasil = 1
    for j in range(i, 0, -1):
        hasil *= j
    print(hasil,end=" ")
    for j in range(i, 0, -1):
        print(j,end=" ")
    print()