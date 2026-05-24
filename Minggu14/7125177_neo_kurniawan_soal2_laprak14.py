list_angka = [1,2,3,4,5,6,7,8,9,10]
print(f'Sebelum List diubah ke Set: {list_angka}')
ubah_set = set(list_angka)
print(f'Setelah List diubah ke Set: {ubah_set}')
print()

set_angka = {10,32,515,32,5}
print(f'Sebelum Set diubah ke List: {set_angka}')
ubah_list = list(set_angka)
print(f'Setelah Set diubah ke List: {ubah_list}')
print()

tuple_angka = (115,162,24,634)
print(f'Sebelum Tuple diubah ke Set: {tuple_angka}')
ubah_tuple = set(tuple_angka)
print(f'Setelah Tuple diubah ke Set: {ubah_tuple}')
print()

simpanset = {15,6132,242,6}
print(f'Sebelum Set diubah ke Tuple: {simpanset}')
mengganti_tuple = tuple(simpanset)
print(f'Setelah Set diubah ke Tuple: {mengganti_tuple}')

