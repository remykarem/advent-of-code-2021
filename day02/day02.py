from typing import Callable, Tuple
from dataclasses import dataclass
from pyterator import iterate

def parse(instruction: str) -> Tuple[str, int]:
    cmd, value = instruction.strip().split()
    value = int(value)
    return cmd, value

def convert_to_tuple(cmd: str, value: int) -> tuple:
    if cmd == "forward":
        return (value, 0)
    elif cmd == "down":
        return (0, value)
    else:
        return (0, -value)

def add_tuples(a: tuple, b: tuple) -> tuple:
    x = a[0] + b[0]
    y = a[1] + b[1]
    return x, y

@dataclass
class BearingRelative:
    pos: int
    depth: Callable
    aim: int

@dataclass
class Bearing:
    pos: int
    depth: int
    aim: int

def accumulate(prev: Bearing, curr: BearingRelative) -> tuple:
    pos = prev.pos + curr.pos
    depth = prev.depth + curr.depth(prev.aim)
    aim = prev.aim + curr.aim
    return Bearing(pos, depth, aim)

def convert_to_relative(cmd: str, value: int) -> BearingRelative:
    if cmd == "forward":
        return BearingRelative(value, lambda aim: aim*value, 0)
    elif cmd == "down":
        return BearingRelative(0, lambda x: 0, value)
    else:
        return BearingRelative(0, lambda x: 0, -value)


def main():
    f = open("day02.txt")

    # Part 1
    f.seek(0)
    m, n = (
        iterate(f)
        .map(parse)
        .starmap(convert_to_tuple)
        .reduce(add_tuples)
    )
    print(m*n)

    # Part 2
    f.seek(0)
    bearing = (
        iterate(f)
        .map(parse)
        .starmap(convert_to_relative)
        .reduce(accumulate, Bearing(0,0,0))
    )
    print(bearing.pos*bearing.depth)

    f.close()


if __name__ == "__main__":
    main()
