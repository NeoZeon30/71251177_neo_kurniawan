n = int(input("Masukan Angka: "))

for i in range(n, 0, -1):
    primadekat = 0
    for j in range (1,i+1):
        if i % j == 0:
            primadekat += 1
    if primadekat == 2:
        print(f"Bilangan prima terdekat <{n} adalah {i}")
        break