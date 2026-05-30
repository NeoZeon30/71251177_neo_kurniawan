def hitung(angka):
    if angka < 10:
        return angka
    else:
        return  (angka % 10) + hitung(angka // 10)

print(hitung(234))

