# exception akan terjadi saat program mengalami error saat runtime

from math import nan
# contoh sederhana untuk menangkap exception
data_input = int(input("masukkan angka : "))
hasil = nan

try:
    hasil = 10/data_input
except:
    print("input tidak valid")

print(f"hasil = {hasil}")

# contoh membuat exception
from numbers import Number

def tambah(a, b):
    if not isinstance(a, Number) or not isinstance(b, Number):
        raise "input pertama harus angka"
    return a + b

print(tambah(5, 34))

angka = 0

try:
    hasil = 10/angka
except ZeroDivisionError as err_msg:
    print(err_msg)