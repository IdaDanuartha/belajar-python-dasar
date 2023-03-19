''' Type hints untuk fungsi '''

# penggunaan type hints
def kuadrat(angka: int) -> int:
    hasil = angka**2
    return hasil

HASIL = kuadrat()
print(HASIL)
