bmi = float(input("Masukkan BMI: "))
tb = float(input("Berapa tinggi badanmu: "))

bb = round((bmi * ((tb/100)**2)))

print(f"Jadi berat badan kamu cari adalah {bb}")