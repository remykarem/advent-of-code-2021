from math import prod
from typing import List, Tuple
from reducer import eq, gt, identity, lt

from day16types import BitLength, LiteralValue, PacketType
from day16types import Reducer, Stream, Version
from utils import binary2decimal


REDUCERS = [sum, prod, min, max, identity, gt, lt, eq]
PACKETTYPES = [PacketType.LITERAL if i==4 else PacketType.OPERATOR 
               for i in range(8)]
PACKETTYPE_INFOS = list(zip(PACKETTYPES, REDUCERS))

def parse_version(stream: Stream) -> Version:
    binary = stream.islice(3)
    return binary2decimal(binary)


def parse_ptype(stream: Stream) -> Tuple[PacketType, Reducer]:
    type_id = binary2decimal(stream.islice(3))
    return PACKETTYPE_INFOS[type_id]


def parse_packet(stream: Stream) -> Tuple[BitLength, Version, LiteralValue]:
    
    head_version = parse_version(stream)
    ptype, reducer = parse_ptype(stream)
    
    if ptype == PacketType.LITERAL:
        bitlength, version, values = parse_packet_literal(stream)
    else:
        bitlength, version, values = parse_packet_operator(stream)
    
    # 3 for version + 3 for ptype
    return 3+3+bitlength, head_version+version, reducer(values)


def parse_packet_literal(stream: Stream) -> Tuple[BitLength, Version, List[LiteralValue]]:
    """Literal type"""
    
    binary = []
    bitlength = 0
    leading = '1' # sentinel
    
    while leading == '1':
        leading, *part_binary = stream.islice(5)
        binary.extend(part_binary)
        bitlength += 5
        
    return bitlength, 0, [binary2decimal(binary)]  # 0 is sentinel


def parse_packet_operator(stream: Stream) -> Tuple[BitLength, Version, List[LiteralValue]]:
    """Operator type"""
    
    length_type_id = next(stream)
    
    if length_type_id == '0':
        bitlength, version, values = parse_packet_operator_bitlength(stream)
        
    elif length_type_id == '1':
        bitlength, version, values = parse_packet_operator_qty(stream)

    else:
        raise ValueError("Illegal state")
        
    return bitlength+1, version, values
        
        
def parse_packet_operator_bitlength(stream: Stream) -> Tuple[BitLength, Version, List[LiteralValue]]:
    """Operator subtype"""
        
    bitlength, version = 0, 0
    length = binary2decimal(stream.islice(15))
    values = []

    while bitlength < length:
        bitlength_, version_, value = parse_packet(stream)
        bitlength += bitlength_
        version += version_
        values.append(value)
    
    return bitlength+15, version, values
        
        
def parse_packet_operator_qty(stream: Stream) -> Tuple[BitLength, Version, List[LiteralValue]]:
    """Operator subtype"""
    
    bitlength, version = 0, 0
    qty = binary2decimal(stream.islice(11))
    values = []
    
    for _ in range(qty):
        bitlength_, version_, value = parse_packet(stream)
        bitlength += bitlength_
        version += version_
        values.append(value)
        
    return bitlength+11, version, values