# Width and Multiline

data_nama = "Ucup Surucup"
data_umur = 17
data_tinggi = 150.1
data_nomor_sepatu = 44

# string standard
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
print(data_string)

print(20*"=")

# string multiline (dengan menggunakan enter, newline, \n)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_nomor_sepatu}"
print(data_string)

print(20*"=")

# string multiline (kutip triplets)
data_string = f"""
nama    = {data_nama:>10},
umur    = {data_umur:>10},
tinggi  = {data_tinggi:>10},
sepatu  = {data_nomor_sepatu:>10}
"""
print(data_string)