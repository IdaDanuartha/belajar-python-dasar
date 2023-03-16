# Operasi Aritmatika

a = 10
b = 3

# Pertambahan
hasil = a + b
print("hasil dari", a, "+", b, "= ", hasil)

# Pengurangan
hasil = a - b
print("hasil dari", a, "-", b, "= ", hasil)

# Perkalian
hasil = a * b
print("hasil dari", a, "*", b, "= ", hasil)

# Peembagian
hasil = a / b
print("hasil dari", a, "/", b, "= ", hasil)

# Modulus
hasil = a % b
print("hasil dari", a, "%", b, "= ", hasil)

# Eksponen (perpangkatan)
hasil = a ** b
print("hasil dari", a, "**", b, "= ", hasil)

# Floor division (pembagian kebawah)
hasil = a // b
print("hasil dari", a, "//", b, "= ", hasil)

# Prioritas operasi, operational precedence
'''
    1. Tanda kurung ()
    2. Exponen **
    3. Perkalian dan teman-teman * / ** % //
    pertambahan dan pengurangan + -
'''

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z //x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)
