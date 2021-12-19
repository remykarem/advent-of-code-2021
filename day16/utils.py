from day16types import Binary, Stream
from pyterator import iterate



def hexchar2bin(ch: str) -> str:
    return f"{int(ch,16):0>4b}"

def binary2decimal(binary: Binary) -> int:
    return int("".join(binary), 2)

def hex2stream(hex_str: str) -> Stream:
    return iterate(hex_str).flat_map(hexchar2bin)
