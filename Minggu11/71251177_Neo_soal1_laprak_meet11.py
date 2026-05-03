def angka_terbaik(data):
    urutan = sorted(data, reverse=True)
    return urutan[:3]

print(angka_terbaik([2, 4, 30, 80, 39, 67]))