# looping dictionary
data_dict = {
    'nama': 'Danuartha',
    'kelas': 'XII RPL 1',
    'absen': 21
}

for dict in data_dict.keys():
    print(data_dict.get(dict))

print(50*"=")

for dict in data_dict.values():
    print(dict)

print(50*"=")

for key,value in data_dict.items():
    print(f"Key = {key}, Value = {value}")
