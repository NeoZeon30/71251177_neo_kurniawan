# 71251177
# Neo Kurniawan

def cek_digit_belakang(angka1, angka2, angka3):
  x = angka1 % 10
  y = angka2 % 10
  z = angka3 % 10
  if x == y or y == z or z == x:
    return True
  else:
    return False

print(cek_digit_belakang(30, 20, 18))
print(cek_digit_belakang(145, 5, 100))
print(cek_digit_belakang(71, 187, 18))
print(cek_digit_belakang(1024, 14, 94))
print(cek_digit_belakang(53, 8900, 658))