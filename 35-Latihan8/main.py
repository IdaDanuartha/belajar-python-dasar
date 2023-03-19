# latihan dictionary
import datetime
import os
import string
import random

siswa_template = {
    'nama': 'Ida Putu Sucita Danuartha',
    'nis': '28853',
    'lahir': datetime.datetime(2004,12,14)
}

data_siswa = {}

while True:
    os.system("cls") # untuk windows
    # os.system("clear") # untuk macos

    siswa = dict.fromkeys(siswa_template.keys())
    print(siswa)
    siswa['nama'] = input("Masukkan nama siswa : ")
    siswa['nis'] = input("Masukkan nis siswa : ")
    TAHUN_LAHIR = int(input("Masukkan tahun lahir (YYYY) : "))
    BULAN_LAHIR = int(input("Masukkan bulan lahir (1-12) : "))
    TANGGAL_LAHIR = int(input("Masukkan tanggal lahir (1-31) : "))

    siswa['lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)
    
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_siswa.update({KEY: siswa})

    print(f"{'KEY':<8} {'NAMA':<15} {'NIS':<8} {'LAHIR':<5}")
    print(50*"-")

    for siswa in data_siswa:
        KEY = siswa

        NAMA = data_siswa[KEY]['nama']
        NIS = data_siswa[KEY]['nis']
        LAHIR = data_siswa[KEY]['lahir'].strftime("%x")

        print(f"{KEY:<8} {NAMA:<15} {NIS:<8} {LAHIR:^5}")

    print("\n")
    is_done = input("Tambah data lagi (y/n)? ")

    if is_done == 'n':
        break 

print("Program selesai")