# Operasi logika
# not, or, and, xor

# NOT (membalikan nilai boolean, jika true maka false)
print("==== NOT ====")

a = True
c = not a

print('a = ', a)
print('c = ', c)

# OR (jika salah satu true, maka hasilnya adalah true)
print("==== OR ====")

a = True
b = False
c = a or b
print(a, 'OR', b, '=', c)

a = False
b = False
c = a or b

print(a, 'OR', b, '=', c)

# OR (jika dua buah nilai true, maka hasilnya true)
print("==== AND ====")

a = True
b = False
c = a and b
print(a, 'AND', b, '=', c)

a = True
b = True
c = a and b

print(a, 'AND', b, '=', c)

# XOR (akan true jika salah satu true, sisanya false)
print("==== XOR ====")

a = True
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)

a = True
b = True
c = a ^ b

print(a, 'XOR', b, '=', c)