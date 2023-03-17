# Operator bitwise, operasi biner, binary

a = 9
b = 5

# Bitwise OR (|)
c = a | b
print('\n========== OR ==========')
print('nilai :', a, ', binary :', format(a, '08b'))
print('nilai :', b, ', binary :', format(b, '08b'))
print('---------------------------------- (|)')
print('nilai :', c, ', binary :', format(c, '08b'))

# Bitwise AND (&)
c = a & b
print('\n========== AND ==========')
print('nilai :', a, ', binary :', format(a, '08b'))
print('nilai :', b, ', binary :', format(b, '08b'))
print('---------------------------------- (&)')
print('nilai :', c, ', binary :', format(c, '08b'))

# Bitwise XOR (^)
c = a ^ b
print('\n========== XOR ==========')
print('nilai :', a, ', binary :', format(a, '08b'))
print('nilai :', b, ', binary :', format(b, '08b'))
print('---------------------------------- (~)')
print('nilai :', c, ', binary :', format(c, '08b'))

# Bitwise NOT (~)
c = ~a
print('\n========== NOT ==========')
print('nilai :', a, ', binary :', format(a, '08b'))
print('----------------------------------')
print('nilai :', c, ', binary :', format(c, '08b'))

# Shifting

# shifting right (>>)
c = a >> 2
print('\n========== Shift Right ==========')
print('nilai :', a, ', binary :', format(a, '08b'))
print('----------------------------------')
print('nilai :', c, ', binary :', format(c, '08b'))

# shifting left (<<)
c = a << 2
print('\n========== Shift Left ==========')
print('nilai :', a, ', binary :', format(a, '08b'))
print('----------------------------------')
print('nilai :', c, ', binary :', format(c, '08b'))