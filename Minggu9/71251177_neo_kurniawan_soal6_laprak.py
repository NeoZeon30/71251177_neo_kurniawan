import re
import random

def randompassword(text):
    dariEmail = re.findall(r'\S+@\S+', text)
    
    simpan = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    for email in dariEmail:
        username = re.sub(r'@.*', '', email)
        
        password = ''
        for i in range(8):
            password += random.choice(simpan)
        print(f'{email} username: {username} , password: {password}')

text = """
Berikut adalah daftar email dan nama pengguna dari mailing list: anton@mail.com dimiliki oleh antonius budi@gmail.co.id dimiliki oleh budi anwari slamet@getnada.com dimiliki oleh slamet slumut matahari@tokopedia.com dimiliki oleh toko matahari """

randompassword(text)