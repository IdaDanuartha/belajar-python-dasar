# Membaca file eksternal

print(10*"=", " Membaca File txt ", "="*10)
file = open("data.txt", mode="r")

print(f"Status read : {file.readable()}")
print(f"Status write : {file.writable()}")

## baca seluruh file
# print(file.read())

## baca perbaris
# print(file.readline(), end="") # baca baris pertama
# print(file.readline(), end="") # baca baris kedua

## baca semua baris sebagai list
print(file.readlines())

file.close()

print(f"Apakah file sudah ditutup : {file.closed}")

## salah satu teknik membuka file di python
print(10*"=", " Membaca File txt dengan with ", "="*10)

with open("data.txt", "r") as file:
    content = file.read()
    print(content, end="")
