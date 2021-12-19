import enum
from typing import Callable, Iterator, List


LiteralValue = int
Stream = Iterator # a packet is a stream of values
BitLength = int
Version = int
Reducer = Callable
Binary = List[str]


class PacketType(enum.Enum):
    LITERAL = 0
    OPERATOR = 1
