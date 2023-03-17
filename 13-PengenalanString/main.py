# Cara membuat string

# 1. Dengan menggunakan single quote '...'
data = 'ini adalah string'
print(data)

# 2. Dengan menggunakan double quote "..."
data = "ini adalah string"
print(data)

# 3. Menggunakan tanda \
# membuat tanda ' menjadi string
print('hari ini adalah hari jum\'at')

# backslash
print('C:\\user\\Danu')

# tab
print('Danu\tArtha')

# backspace
print('Danu \bArtha')

# baris baru
print("baris pertama.\nbaris kedua") # LF -> line feed -> unix, macos, linux
print("baris pertama.\rbaris kedua") # CR -> carriage return -> commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua") # CRLF -> line feed carriage return -> dipakai oleh windows

# String literal
# menggunakan raw string
print(r'C:\new folder')

# multiline literal string
print("""
Nama : Danuartha
Kelas : XII RPL 1
""")

# multiline literal string dan raw
print(r"""
Nama : Danuartha
Kelas : XII RPL 1
Website : www.danuartha.com\newid
""")