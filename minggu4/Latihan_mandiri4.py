try:
  a = int(input("Masukan sisi pertama: "))
  b = int(input("Masukan sisi kedua: "))
  c = int(input("Masukan sisi ketiga: "))

  if a == b and a == c:
    print ("3 sisi sama")
  elif a == b or a == c or b == c:
    print ("2 sisi sama")
  else:
    print("Tidak ada yang sama")

except:
  print ("Error")