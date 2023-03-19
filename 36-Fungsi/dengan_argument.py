''' Fungsi dengan argument '''

def print_nama(nama):
    print(f"Haloo {nama}")

nama = input("Masukkan Nama kamu : ")
print_nama(nama)

# fungsi tambah angka
def tambah(angka1, angka2):
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")

tambah(1, 5)

def list_nama(nama):
    data_nama = nama.copy()
    for n in data_nama:
        print(f"Nama = {n}")

nama = ["Danu", "Novel", "Artha"]

list_nama(nama)