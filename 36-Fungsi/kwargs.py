''' **kwargs (keyword arguments) '''

def fungsi(**kwargs):
    nama = kwargs['nama']
    tinggi = kwargs['tinggi']
    berat = kwargs['berat']

    print(f"{nama} punya tinggi = {tinggi}cm dan berat = {berat}kg")

fungsi(nama="Danu", tinggi=179, berat=83)

# studi kasus
def math(*args, **kwargs):
    hasil = 0

    if kwargs['option'] == 'tambah':
        for a in args:
            hasil += a
    elif kwargs['option'] == 'kurang':
        for a in args:
            hasil -= a
    elif kwargs['option'] == 'kali':
        for a in args:
            hasil *= a
    elif kwargs['option'] == 'bagi':
        for a in args:
            hasil /= a

    return hasil
hasil = math(5,3,6,2,option="kurang")
print(hasil)