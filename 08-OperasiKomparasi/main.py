# Operasi Komparasi
# Setiap hasil dari operasi komparasi adalah boolean
# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2

# lebih besar dari >
hasil = a > 3
print(a, '>', b, '=', hasil)

# lebih kecil dari <
hasil = a < 3
print(a, '<', b, '=', hasil)

# lebih besar atau sama dengan >=
hasil = a >= 3
print(a, '>=', b, '=', hasil)

# lebih kecil atau sama dengan <=
hasil = a <= 3
print(a, '<=', b, '=', hasil)

# sama dengan ==
hasil = a == 3
print(a, '==', b, '=', hasil)

# tidak sama dengan !=
hasil = a != 3
print(a, '!=', b, '=', hasil)

# 'is' sebagai komparasi object identity
hasil = a is b
print(a, 'is', b, '=', hasil)

# 'is not' sebagai komparasi object identity
hasil = a is not b
print(a, 'is not', b, '=', hasil)