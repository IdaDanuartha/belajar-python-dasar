# dia akan membuat file baru jika tidak ada,
# lalu akan menimpa atau overwrite isinya

# 1. mode write
with open("data1.txt", "w", encoding="utf-8") as file :
    file.write("Ida Putu Sucita Danuartha")
    
# 2. mode append
with open("data2.txt", "a", encoding="utf-8") as file :
    file.write("Ida Putu Sucita Danuartha\n")
    
with open("data2.txt", "a", encoding="utf-8") as file :
    file.write("Novelita Putri Wahdana")

# 3. mode r+
with open("data3.txt", "w", encoding="utf-8") as file :
    file.write("")

with open("data3.txt", "r+", encoding="utf-8") as file :
    file.write("baris ke-1\n")
    file.write("baris ke-2\n")

with open("data3.txt", "r+", encoding="utf-8") as file :
    data = file.read()
    print(data)

with open("data3.txt", "r+", encoding="utf-8") as file :
    file.write("baris ke-3\n")