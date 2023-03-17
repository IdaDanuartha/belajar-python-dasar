# Operasi dan manipulasi string

# 1. Menggabungkan string (concatenate)
nama_pertama = 'Sucita'
nama_tengah = 'Danu'
nama_akhir = 'Artha'

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang string (len)
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

# 3. Operator untuk string
# mengecek apakah ada komponen char atau string di string

d = "d"
status = d in nama_lengkap
print("string " + d + " ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk" * 10)
print(10 * "hi")

# indexing
print("Index ke-0 : " + nama_lengkap[0])
print("Index ke-(-2) : " + nama_lengkap[-2])
print("Index ke-[0:5] : " + nama_lengkap[0:6])
print("Index ke-[0, 2, 4, 6] : " + nama_lengkap[0:7:2])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))

# item paling besar
print("paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("Char untuk ASCII 117 adalah " + chr(data))

# operator dalam bentuk method
data = "Novelita putri wahdana"
jumlah = data.count("a")
print("jumlah a pada " + data + " = " + str(jumlah))