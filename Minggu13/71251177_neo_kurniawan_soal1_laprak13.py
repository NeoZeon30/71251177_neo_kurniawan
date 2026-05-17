tA = (90,90,90,90)

samaSemua = True
mulai = tA[0]
for angka in tA:
    if angka != mulai:
        samaSemua = False
        break
    
print(samaSemua)