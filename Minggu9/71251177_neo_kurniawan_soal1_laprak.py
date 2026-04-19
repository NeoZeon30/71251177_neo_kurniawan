def anagram():
    kataSatu = input("Masukan Kata Pertama: ")
    kataDua = input("Masukan Kata Kedua: ")
    if sorted(kataSatu) == sorted(kataDua):
        print(f'{kataSatu} adalah anagram dari {kataDua}')
    else:
        print(f'{kataSatu} bukan anagram dari {kataDua}')
anagram()