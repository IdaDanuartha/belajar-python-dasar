# Date and time (latihan)
import datetime as dt

print("Program mendeteksi hari lahir seseorang\n")
print("Silahkan masukkan tanggal, bulan dan tahun lahir anda :")
tanggal = int(input("Tanggal : "))
bulan = int(input("Bulan : "))
tahun = int(input("Tahun : "))

tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")
print(f"Harinya adalah : {tanggal_lahir:%A}")

today = dt.date.today()
print(f"Haari ini tanggal : {today}")

umur_hari = today - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30

print(f"Umur anda adalah : {umur_tahun} tahun, {umur_bulan_sisa} bulan")