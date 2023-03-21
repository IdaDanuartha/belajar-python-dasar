from . import Operasi

def read_console():
    data_file = Operasi.read()
    
    id = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    # Header
    print("\n" + "="*100)
    print(f"{id:6} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100)

    # Data
    for i,data in enumerate(data_file):
        data_break = data.split(",")
        id = data_break[0]
        judul = data_break[1]
        penulis = data_break[2]
        tahun = data_break[3]
        created_at = data_break[4]
        print(f"{id:6} | {judul:.40} | {penulis:.40} | {tahun:5}\n", end="")

    # Footer
    print(100*"=" + "\n")

def create_console():
    print("\n" + "="*30)
    print("Silahkan tambah data buku\n")
    judul = input("Judul\t: ")
    penulis = input("Penulis\t: ")
    
    while True:
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Panjang tahun harus 4, silahkan masukkan tahun lagi (yyyy)")    
        except:
            print("Tahun harus angka, silahkan masukkan tahun lagi (yyyy)")

    Operasi.create(judul,penulis,tahun)
    print("\nBerikut adalah data baru anda")
    read_console()