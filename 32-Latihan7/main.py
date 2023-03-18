# latihan list (program daftar buku)

data_buku = [
    ["Atomic Habits", "Fredly"],
    ["Make Game From Scratch", "Nicola Deep"],
]

print(5*"-" + " Masukkan Data Buku " + "-"*5)
while True:
    print("\n")
    judul = input("Judul buku : ")
    penulis = input("Penulis buku : ")

    buku_baru = [judul, penulis]
    data_buku.append(buku_baru)

    print("No | Judul | Penulis")
    for index, buku in enumerate(data_buku):
        print(f"{index}  | {buku[0]} | {buku[1]}")

    print(50*"=")

    isContinue = input("Apakah dilanjutkan? (y/n) ")
    
    if isContinue == "n":
        break

print("Program selesai")