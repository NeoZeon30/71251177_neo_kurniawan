pajak = 0.14
belanja = 0.1
alat_tulis = 0.01
sedekah = 0.25
sedekah_yatim = 0.30
gaji = int(input("Gaji Yang Anda Inginkan:"))
jam_kerja = int(input("Jumlah Jam Kerja Selama Seminggu:"))

total_gaji = (gaji * jam_kerja) * 5
total_pajak = total_gaji * pajak
gaji_bersih = total_gaji - total_pajak
total_belanja = gaji_bersih * belanja
beli_alat_tulis = gaji_bersih * alat_tulis
sisa = gaji_bersih - (total_belanja + beli_alat_tulis)
untuk_sedekah = sisa * sedekah
untuk_anak_yatim = untuk_sedekah * sedekah_yatim
untuk_anak_dhuafa = untuk_sedekah - untuk_anak_yatim

print('Gaji bersih Untuk Budi:', round(total_gaji))
print('Setelah bayar pajak:', round(total_pajak))
print('Beli pakaian:', round(total_belanja))
print('Beli Alat tulis:', round(beli_alat_tulis))
print('Sedekah:', round(untuk_sedekah))
print('Untuk anak yatim:', round(untuk_anak_yatim))
print('Untuk anak dhuafa:', round(untuk_anak_dhuafa))