# copy dictionary

data_dict = {
    'nama': 'Danuartha',
    'kelas': 'XII RPL 1',
    'absen': 21
}

data_copy = data_dict.copy()

print(f"Data asli = {data_dict}")
print(f"Data copy = {data_copy}")

print(50*"=")

data_dict['nama'] = 'Danu'
print(f"Data asli = {data_dict}")
print(f"Data copy = {data_copy}")

print(50*"=")

# pop dictionary
dataNama = data_dict.pop("nama")
print(f"data nama = {dataNama}")
print(f"data asli = {data_dict}")

print(50*"=")

# pop item dictionary
dataTerakhir = data_dict.popitem()
print(f"data terakhir = {dataTerakhir}")
print(f"data asli = {data_dict}")