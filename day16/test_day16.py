from day16.day16 import binary2decimal, hex2stream, hexchar2bin


assert hexchar2bin("0") == "0000"
assert hexchar2bin("E") == "1110"

assert hex2stream("D2FE28").join() == "110100101111111000101000"
assert hex2stream("38006F45291200").join() == "00111000000000000110111101000101001010010001001000000000"
assert hex2stream("EE00D40C823060").join() == "11101110000000001101010000001100100000100011000001100000"

assert binary2decimal(['1','1','1']) == 7
assert binary2decimal(['0','1','1']) == 3
