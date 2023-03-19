# operator dictionary
data_dict = {
    'nama': 'Danuartha',
    'kelas': 'XII RPL 1',
    'absen': 21
}

# panjang dictionary
LENDICT = len(data_dict)
print(f"Panjang dictionary = {LENDICT}")

# mengecek key ada atau tidak
KEY = "nama"
CHECKKEY = KEY in data_dict
print(f"apakah {KEY} ada di data dict: {CHECKKEY}")

# mengakses value (read) dengan get
print(data_dict.get('nama'))
print(data_dict.get('umur', 'key tidak ditemukan'))

# mengubah data dictionary
data_dict['nama'] = "Ida Putu Sucita Danuartha"
data_dict['umur'] = 18
print(data_dict)

data_dict.update({"nama":"Danuartha"}) # kalau key tidak ada maka akan ditambahkan
print(data_dict)

# menghapus data dictionary
del data_dict['umur']
print(data_dict)

