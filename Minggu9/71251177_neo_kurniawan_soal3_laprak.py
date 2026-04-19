import re
def menghapus():
    teks = "  saya   tidak      suka       memancing   ikan     "
    mengganti = re.sub(r'\s+'," ", teks)
    hasil = re.sub(r'^ | $',"", mengganti)
    print(hasil)

menghapus()