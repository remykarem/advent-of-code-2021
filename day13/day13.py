from __future__ import annotations
from dataclasses import dataclass
from pyterator import iterate, tee
from typing import Callable, Iterator

@dataclass(frozen=True, eq=True)
class Point:
    x: int
    y: int
        
    def folded_vertical(self, v: int) -> Point:
        if self.x == v:
            raise ValueError
        elif self.x < v:
            return self
        else:
            x = (v-1) - (self.x-(v+1))
            return Point(x, self.y)
        
    def folded_horizontal(self, h: int) -> Point:
        if self.y == h:
            raise ValueError
        elif self.y < h:
            return self
        else:
            y = (h-1) - (self.y-(h+1))
            return Point(self.x, y)

def parse_point(point: str) -> Point:
    coords = [int(x) for x in point.split(",")]
    return Point(*coords)

def parse_instruction(instruction: str) -> Callable:
    axis, value = instruction.strip().split()[-1].split("=")
    value = int(value)
    if axis == 'x':
        return lambda point: point.folded_vertical(value)
    else:
        return lambda point: point.folded_horizontal(value)
    
def print_points(points: Iterator[Point]):
    dots = points.groupby(lambda p: p.y, lambda p: p.x)
    for row in range(6):
        arr = ["#" if x in dots[row] else "." for x in range(39)]
        print("".join(arr))


f = open("day13.txt", "r")

f.seek(0)
raw_points, raw_instructions = iterate(f).split_at(lambda line: line.strip()=="")
points = raw_points.map(parse_point)
instructions = raw_instructions.map(parse_instruction)

# Part 1
points.filter_map(next(instructions))
points_part1, points_part2 = tee(points, 2)
print(len(set(points_part1)))

# Part 2
for instruction in instructions:
    points_part2.filter_map(instruction).unique_everseen()
print_points(points_part2)

f.close()
