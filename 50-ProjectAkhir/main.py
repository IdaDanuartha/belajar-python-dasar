# persiapan
import os

if __name__ == "__main__":
    sistem_operasi = os.name

    # match sistem_operasi:
    #     case "posix": os.system("clear")
    #     case "nt": os.system("cls")
    os.system("cls")

    print("SELAMAT DATANG DI PROGRAM")
    print("DATABASE PERPUSTAKAAN")
    print(50*"=")

    while True:
        print(f'''
1. Tampilkan buku (read)
2. Tambah buku (create)
3. Ubah buku (update)
4. Hapus buku (delete)\n''')

        user_option = input("Masukkan opsi: ")

        print(50*"=")

        match user_option:
            case "1": print("Read Data")
            case "2": print("Create Data")
            case "3": print("Update Data")
            case "4": print("Delete Data")

        print(50*"=")
        is_done = input("Apakah selesai (y/n)? ")
        if is_done == 'y' or is_done == 'Y':
            break
        os.system("cls")

    print('\n')
    print(16*"=", " Program Selesai " + "="*16)