''' *args '''

def data_siswa(*data):
    nama = data[0]
    nis = data[1]
    umur = data[2]
    print(f"Nama = {nama}, nis = {str(nis)}, umur = {str(umur)} tahun")

data_siswa("Danu", 28853, 18)

# studi kasus
def pertambahan(*angka) -> int:
    hasil = 0
    for a in angka:
        hasil += a
    
    return hasil

print(pertambahan(3,4,6,7,10))
