try:
  bln = int(input("Masukkan bulan: "))

  hari31 = [1,3,5,7,8,10,12]
  hari30 = [4,6,9,11]
  
  if bln in hari31:
    print("Jumlah Hari: 31")
  elif bln in hari30:
    print("Jumlah Hari: 30")
  elif bln == 2:
    print("Jumlah Hari: 29")
  else:
    print("Bulan hanya (1-12)")

except:

    print("Error")
