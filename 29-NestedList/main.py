# nested list / list bersarang
data1 = [1,"Ida", 17]
data2 = [2,"Putu", 19]
data3 = [3,"Danuartha", 21]

list_data = [data1, data2, data3]
print(f"Peserta = {list_data}")

for data in list_data:
    print(f'''
    Id = {data[0]}
    Nama = {data[1]}
    Umur = {data[2]}
    ''')