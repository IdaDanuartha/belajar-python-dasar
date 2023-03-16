# tipe data: Angka satuan (integer)
data_integer = 1
print("data : ", data_integer, ", bertipe : ", type(data_integer))

# tipe data: Angka dengan koma (float)
data_float = 1.5
print("data : ", data_float, ", bertipe : ", type(data_float))

# tipe data: Kumpulan karakter (string)
data_string = "Danuartha"
print("data : ", data_string, ", bertipe : ", type(data_string))

# tipe data: biner true / false (boolean)
data_bool = True
print("data : ", data_bool, ", bertipe : ", type(data_bool))

## --- Tipe data khusus ---

# Bilangan Kompleks
data_complex = complex(5,10)
print("data : ", data_complex, ", bertipe : ", type(data_complex))

# Tipe data dari bahasa C
from ctypes import c_double

data_c_double = c_double(10.5)
print("data : ", data_c_double, ", bertipe : ", type(data_c_double))