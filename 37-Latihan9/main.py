''' Latihan Fungsi (program menghitung luas dan keliling persegi panjang) '''
import os
os.system('cls')

print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
print(40*"-")

def choices():
    choice = input('''Pilih mau hitung apa? (1/2)
    1. Luas
    2. Keliling
    = ''')

    return choice

def input_user():
    # mengambil input user
    panjang = int(input("masukkan panjang : "))
    lebar = int(input("masukkan lebar : "))
    return panjang, lebar

def hitung_luas(panjang, lebar):
    hasil = panjang * lebar
    return hasil

def hitung_kll(panjang, lebar):
    hasil = 2 * (panjang + lebar)
    return hasil

def display_msg(msg, value):
    print(f"Hasil perhitungan {msg} persegi panjang = {value}")

while True:
    PANJANG, LEBAR = input_user()
    pilihan = choices()
    
    if(pilihan == '1'):
        luas = hitung_luas(PANJANG, LEBAR)
        display_msg("luas", luas)
    elif(pilihan == '2'):
        kll = hitung_kll(PANJANG, LEBAR)
        display_msg("keliling", kll)
    else:
        print("Pilihan tidak ada")
        
    is_continue = input("Mau lanjut atau tidak ? (y/n) ")
    if is_continue != 'y':
        break

print("PROGRAM SELESAI")