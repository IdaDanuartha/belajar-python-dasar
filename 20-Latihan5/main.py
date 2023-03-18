# Latihan 5 (membuat kalkulator sederhana)

print("\n" + 10*"=" + " Kalkulator Sederhana " + "="*10)

angka1 = float(input("Masukkan angka 1 = "))
operator = input("operator (+, -, x, /) = ")
angka2 = float(input("Masukkan angka 2 = "))

# percabangannya
if operator == "+":
    hasil = angka1 + angka2
    print(f"Hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka1 - angka2
    print(f"Hasilnya adalah {hasil}")
elif operator == "*" or operator == "x":
    hasil = angka1 * angka2
    print(f"Hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka1 / angka2
    print(f"Hasilnya adalah {hasil}")
else:
    print('Operator tidak valid')
