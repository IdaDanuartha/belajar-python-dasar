# Fungsi dengan return (kembalian)

# fungsi kuadrat
def kuadrat(angka):
    output = angka ** 2
    return output

a = kuadrat(5)
print(a)

# fungsi dengan return banyak
def calculator(num1, num2):
    plus = num1 + num2
    minus = num1 - num2
    times = num1 * num2
    divided = num1 / num2

    return plus, minus, times, divided

p,m,t,d = calculator(10, 5)

print(f"Hasil pertambahan = {p}")
print(f"Hasil pengurangan = {m}")
print(f"Hasil perkalian = {t}")
print(f"Hasil pembagian = {d}")