# Menduplikat list dengan copy
a = [1,2,3,4,5]
b = a.copy()

print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

print(f"a = {a}")
print(f"b = {b}")

b[1] = 9

print(f"a = {a}")
print(f"b = {b}")
