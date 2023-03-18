data1 = [1,2,3]
data2 = [4,5,6]

data2D = [data1, data2]
data2D_copy = data2D.copy()

print(f"data = {data2D}")
print(f"data copy = {data2D_copy}")

# ambil data dari nested list
data = data2D[0][1]
print(f"data = {data}")

# menggunakan deep copy
from copy import deepcopy
data2D_deepcopy = deepcopy(data2D)

print(f"address asli = {hex(id(data2D))}")
print(f"address deep = {hex(id(data2D_deepcopy))}")

data2D[1][2] = 99
print(f"data = {data2D}")
print(f"data copy = {data2D_copy}")
print(f"data deep = {data2D_deepcopy}")