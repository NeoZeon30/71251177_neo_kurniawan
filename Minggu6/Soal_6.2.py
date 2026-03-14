#NeoKurniawan 71251177

def ganjil(atas,bawah):
    if bawah < atas:
        for i in range(bawah,atas):
          if i % 2 != 0:
                print(i,end="," if i < atas -1 else ".")
    elif bawah > atas:
        while bawah > atas:
            if bawah % 2 == 1:
                print(bawah, end=","if bawah > atas + 1 else ".")
            bawah -= 1

a = int(input("Masukan Batas Atas: "))
b = int(input("Masukan Batas Bawah: "))
ganjil(a,b)