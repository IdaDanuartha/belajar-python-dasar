''' Global dan Local Scope '''

# variabel global
nama_global = "danuartha" # <-- ini variabel global
def fungsi():
    print(nama_global)

# variabel local
def fungsi2():
    nama_local = "Artha" # <-- ini variabel local
    print(nama_local)

fungsi2()
# print(nama_local) # <-- tidak bisa mengakses variabel lokal

# merubah variabel global

angka = 0

def ubah_angka(nilai_baru):
    global angka # fungsi ini mendapat akses merubah angka
    angka = nilai_baru

print(f"Sebelum {angka}")
ubah_angka(10)
print(f"Sesudah {angka}")