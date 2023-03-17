# contoh generic
nama = "Danuartha"
format_str = f"hello {nama}"

print(format_str)

# angka
angka = 2004.53342522
format_str = f"angka = {angka:.3f}"

print(format_str)

# boolean
boolean = True
format_str = f"boolean = {boolean}"

print(format_str)

# format angka
angka = 20000
format_str = f"angka = {angka:,}"

print(format_str)

# menampilkan leading zero
angka = 2004.4543434
format_str = f"angka = {angka:010.3f}"

print(format_str)

# menampilkan tanda + atau -
minus = -10
plus = 10
format_minus = f"minus = {minus:+d}"
format_plus = f"plus = {plus:+d}"

print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# format angka lain (binary, octal, hexadecimal)

angka = 255
format_binary = f"binary {bin(angka)}"
format_octal = f"octal {oct(angka)}"
format_hex = f"hex {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)