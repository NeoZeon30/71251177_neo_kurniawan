file1 = input("Masukkan File Pertama: ")
file2 = input("Masukkan File Kedua: ")

try:
    with open(file1, 'r') as f1:
        isi1 = f1.read()
        isi1 = isi1.lower()
except FileNotFoundError:
    print(f"Error: File {file1} tidak dapat ditemukan")
    exit()

try:
    with open(file2, 'r') as f2:
        isi2 = f2.read()
        isi2 = isi2.lower()
except FileNotFoundError:
    print(f"Error: File {file2} tidak dapat ditemukan")
    exit()

kata1 = set(isi1.split())
kata2 = set(isi2.split())
kata_sama = kata1 & kata2

print("Kata Sama yang ada pada file tersebut adalah:")
if kata_sama:
    for i in sorted(kata_sama):
        print(i)
else:
    print("Tidak ada kata yang sama di kedua file.")
    
    