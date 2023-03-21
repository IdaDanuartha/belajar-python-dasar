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