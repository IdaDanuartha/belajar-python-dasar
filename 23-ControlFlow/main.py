# continue, break and pass

# pass -> berfungsi sebagai dummy, tidak akan dieksekusi

angka = 0

while angka < 10:
    angka += 1

    if angka == 3:
        pass # ini tidak akan dieksekusi
    elif angka == 4:
        continue # akan membuat loop meloncat ke step selanjutnya
    elif angka == 7:
        break # jika angka adalah 7 maka loop akan berhenti disini

    print(f"angka ke-{angka}")