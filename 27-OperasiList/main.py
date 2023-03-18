data = [3,5,7,3,6,3,4,5,4,1,4,9,8,0]
print(f"data angka = {data}")

# count data
jumlah_data_3 = data.count(3)
print(f"Jumlah angka 3 = {jumlah_data_3}")

print(50 * "=")

# ambil posisi data
data2 = ["Ida", "Danuartha", "Sucita"]
index_ida = data2.index("Ida")

print(f"Index ida = {index_ida}")

# mengurutkan list secara ascending
print(f"data angka sebelum diurut = {data}")
data.sort()
print(f"data angka setelah diurut (asc) = {data}")

# mengurutkan list secara descending
data.reverse()
print(f"data angka setelah diurut (desc) = {data}")