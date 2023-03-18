data = ["Ida", "Putu", "Sucita", "Danuartha"]

# mengambil data dari list diatas
print(f'''
Data pertama = {data[0]}
Data terakhir = {data[-1]}
''')

# mengambil info jumlah data dalam list
panjang_data = len(data)
print(f"Panjang data list = {panjang_data}")

## Manipulasi data list

# menambahkan item pada list sesuai posisi
data.insert(0, "Novelita")
print(data)

# menambahkan di akhir list
data.append("Putri")
print(data)

# menambah list dengan list
data_baru = [1, 45, 23, 12]
data.extend(data_baru)
print(data)

# mengubah data list
data[1] = "Unknown"
print(data)

# menghapus data list
data.remove("Putu")
print(data)

# menghapus data paling akhir
data.pop()
print(data)