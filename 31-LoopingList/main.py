# looping dari list

# for loop
data_angka = [1,3,6,3,7,8]

for angka in data_angka:
    print(f"angka = {angka}")

data_nama = ['Ida', "Putu", "Sucita", "Danuartha"]

print(50*"=")

for nama in data_nama:
    print(f"nama = {nama}")

print(50*"=")

# for loop dan range
panjang = len(data_nama)

for i in range(panjang):
    print(f"nama = {data_nama[i]}")

print(50*"=")

# while loop
i = 0

while i < panjang:
    print(f"nama = {data_nama[i]}")
    i += 1

# list comprehension
print(50*"=")

[print(f"angka = {i}") for i in data_angka]

# enumerate
print(50*"=")

for index, data in enumerate(data_nama):
    print(f"index = {index}, data = {data}")

