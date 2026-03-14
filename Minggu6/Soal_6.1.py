#NeoKurniawan 71251177

def perkalian(a,b):
    hasil = 0
    for i in range (a) :
        hasil +=  b
        if i < a - 1:
            print(b,end=" + ")
        else:
            print(b, end=" = ")
    print(hasil)

a = int(input("Masukan angka 1: "))
b = int(input("Masukan angka 2: "))
print(f"{a} x {b} =",end=" ")
perkalian(a,b)