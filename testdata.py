# Print a table of values from 0 to 255 with bits in 
# reverse order (lsb ... msb) => 0x01 = 0x80

lookup = [ 0x00, 0x08, 0x04, 0x0c, 0x02, 0x0a, 0x06, 0x0e,
           0x01, 0x09, 0x05, 0x0d, 0x03, 0x0b, 0x07, 0x0f ]

def reverse_bits(x):
    return (lookup[x % 16] << 4) | lookup[x // 16]

for i in range(16):
    for x in range(16):
        print("0x%02x, " % reverse_bits((i*16)+x), end='')
    print()
