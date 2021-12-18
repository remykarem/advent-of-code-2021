from typing import List


Binary = List[str]


def hexchar2bin(ch: str) -> str:
    return f"{int(ch,16):0>4b}"

def binary2decimal(binary: Binary) -> int:
    return int("".join(binary), 2)
