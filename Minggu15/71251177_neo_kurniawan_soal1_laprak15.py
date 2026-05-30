def bilanganprima(prima):
    def cekprima(prima, bagi):
        if prima < 2:
            return False
        if bagi * bagi > prima:
            return True
        if prima % bagi == 0:
            return False
        return cekprima(prima, bagi + 1)
    if cekprima(prima, 2):
        return "Itu adalah Bilangan Prima"
    else:
        return "Itu Bukan Bilangan Prima"
print(bilanganprima(20))
print(bilanganprima(7))

