# Lambda function
kuadrat = lambda angka,pangkat : angka**pangkat
print(kuadrat(10,3))

cek_ganjil_genap = lambda x: 'genap' if x%2 == 0 else 'ganjil'
print(cek_ganjil_genap(4))

# anonymous function
# currying <- Haskell Curry
def pangkat(n):
    return lambda angka:angka**n

pangkat3 = pangkat(3)
print(pangkat3(10))