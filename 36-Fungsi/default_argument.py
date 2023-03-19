# Default Argument

# def fungsi(argument = default_value):

# contoh 1
def say_hello(nama = 'anonymous'):
    print(f"Hallo {nama}")

say_hello("Danu")
say_hello()

# contoh 2
def hitung_pangkat(angka, pangkat):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(pangkat=3, angka=10))