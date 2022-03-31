# pow(10, 3) pow(10, 2) pow(10, 1) pow(10, 0)  #  desjatichnaja sistema ischislenija

x = 127
print(1 * pow(10, 2) + 2 * pow(10, 1) + 7 * pow(10, 0))
# 127

y = 1035
print(1 * pow(10, 3) + 0 * pow(10, 2) + 3 * pow(10, 1) + 5 * pow(10, 0))
# 1035

# pow(2, 3) pow(2, 2) pow(2, 1) pow(2, 0)  #  dvoicnnaja sistema

x = 0b101  #  ob - oznachaet dvoichnaja sistema
print(x)
print(1 * pow(2, 2) + 0 * pow(2, 1) + 1 * pow(2, 0))
#  5
#  5

y = 0b0110
print(y)
print(0 * pow(2, 3) + 1 * pow(2, 2) + 1 * pow(2, 1) + 0 * pow(2, 0))
#  6
#  6

z = 0xffff  #  16-tizerichnaja sistema
print(z)
#  65535
print(format(z, '0>42b'))
#  000000000000000000000000001111111111111111
print(15 * pow(16, 3) + 15 * pow(16, 2) + 15 * pow(16, 1) + 15 * pow(16, 0))
#  65535
print(0b000000000000000000000000001111111111111111)
#  65535

with open('test_binary', 'bw') as test_file:
    for number in range(21):                  #  ili - test_file.write(bytes(range(21))
        test_file.write(bytes([number]))



with open('test_binary', 'br') as test_file:
    for number in test_file:
        print(number)
#  b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n'
# b'\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14'