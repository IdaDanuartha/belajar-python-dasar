siswa1 = {
    "nama": "Danuartha",
    "kelas": "XII RPL 1",
    "absen": 21
}

siswa2 = {
    "nama": "Novelita",
    "kelas": "XII RPL 1",
    "absen": 37
}

siswa3 = {
    "nama": "Ardellian",
    "kelas": "XII RPL 2",
    "absen": 36
}

data_siswa = {
    "1": siswa1,
    "2": siswa2,
    "3": siswa3,
}

print(f"{'KEY':<6} {'NAMA':<15} {'KELAS':<15} {'ABSEN':<3}")
print(50*"-")

for siswa in data_siswa:
    KEY = siswa

    NAMA = data_siswa[KEY]['nama']
    KELAS = data_siswa[KEY]['kelas']
    ABSEN = data_siswa[KEY]['absen']

    print(f"{KEY:<6} {NAMA:<15} {KELAS:<15} {ABSEN:<3}")

