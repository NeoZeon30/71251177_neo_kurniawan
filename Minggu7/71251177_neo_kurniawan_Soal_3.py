a= int(input("Tinggi: "))
b= int(input("Lebar: "))

panjang = a * b
for i in range(1, panjang + 1):
    print(i, end=" ")
    if i % b == 0:
        print()