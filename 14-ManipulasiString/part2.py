# operator dalam bentuk methods

## merubah case dari string

# merubah semua ke upper case
salam = "halo!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lower case
salam = "HaLo NaMA SayA DANU"
print("normal = " + salam)
salam = salam.lower()
print("lower = " + salam)

# pengecekan dengan isX method
salam = "halo"
is_salam_lower = salam.islower()
print(salam + " is lower = " + str(is_salam_lower))
is_salam_upper = salam.isupper()
print(salam + " is upper = " + str(is_salam_upper))

# isalpha() <-- untuk mengecek semuanya huruf
# isalnum() <-- huruf dan angka
# isdecimal() <-- angka saja
# isspace() <-- spasi, tab, newline \n
# istitle() <-- semua kata dimulai dengan huruf besar

## ngecek komponen startswith() dan endswith()
cek_start = "Danu Artha".startswith("Danu")
print("start = " + str(cek_start))

cek_end = "Danu Artha".endswith("Artha")
print("end = " + str(cek_end))

## penggabungan komponen join() split()
pisah = ['aku', 'sayang', 'kamu']
gabungan = ', '.join((pisah))
print(pisah)
print(gabungan)

gabungan = 'aku_sayang_kamu'
print(gabungan.split("_"))

# alokasi karakter rjust(), ljust(), center()
kanan = "kanan".rjust(10, "=")
print("'" + kanan + "'")

kiri = "kiri".ljust(10, "=")
print("'" + kiri + "'")

tengah = "tengah".center(20, "=")
print("'" + tengah + "'")

# kebalikannya -> strip()
tengah = tengah.strip("=")
print("'" + tengah + "'")