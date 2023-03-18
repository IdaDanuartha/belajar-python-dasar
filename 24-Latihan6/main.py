# Latihan Perulangan Membuat Segitiga

sisi = 4

# Segitiga siku-siku
print("=" * 50)

count = 1
for i in range(sisi):
    print("*" * count)
    count += 1

print("=" * 50)

# Segitiga sama sisi
print("=" * 50)
count = 1
space = int(sisi/2)

while True:
    if(count % 2):
        # print jika ganjil
        print(" " * space + "*" * count)
        space -= 1
        count += 1
    else:
        # akan kembali ke atas jika ganjil
        count += 1
        continue
    
    # akan break jika count melebihi sisi
    if count > sisi:
        break
print("=" * 50)