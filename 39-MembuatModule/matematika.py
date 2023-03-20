# module matematika

# fungsi tambah
def tambah(*numbers) -> int:
    result = 0
    for num in numbers:
        result += num
    return result

def kali(*numbers) -> int:
    result = 1 if len(numbers) > 0 else 0
    for num in numbers:
        result *= num
    return result

def pangkat(num: int, pangkat: int) -> int:
    return num ** pangkat