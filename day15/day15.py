from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Iterator
from functools import cached_property
from heapq import heapify, heappush, heappop
from pyterator import iterate


def full_map_part1(x,y):
    return grid[x][y]

def full_map_part2(x,y):
    x_major, x_minor = divmod(x,len(grid))
    y_major, y_minor = divmod(y,len(grid[0]))
    addend = x_major + y_major
    return (grid[x_minor][y_minor]-1+addend)%9+1

@dataclass
class Node:
    start2node: int
    loc: tuple
        
    @cached_property
    def f(self) -> int:
        return self.start2node + self.node2end

    @cached_property
    def node2end(self) -> int:
        x, y = self.loc
        return abs(x-height) + abs(y-width)
    
    def __lt__(self, other: Node) -> bool:
        return self.f < other.f

def find_min_cost() -> Optional[int]:
    open_set = [Node(0,(0,0))]
    closed_set = {(0,0)}
    heapify(open_set)
    
    while node := heappop(open_set):
        if node.loc == (height-1, width-1):
            return node.start2node
        for neighbour in get_neighbours(node, closed_set):
            heappush(open_set, neighbour)
        closed_set.add(node.loc)

def get_neighbours(node: Node, closed_set: set) -> Iterator[Node]:
    x, y = node.loc
    neighbour_locs = [(x+1,y),(x-1,y),(x,y-1),(x,y+1)]

    return (
        iterate(neighbour_locs)
        .starfilter(lambda a,b: 0<=a<height and 0<=b<width)
        .filter(lambda loc: loc not in closed_set)
        .starmap(lambda a,b: Node(
            start2node=node.start2node + full_map(a,b),
            loc=(a,b),
        ))
    )

f = open("day15.txt","r")
f.seek(0)
grid = iterate(f).map(str.strip).map(lambda line: [int(x) for x in line]).to_list()
height, width = len(grid), len(grid[0])     # part1
full_map = full_map_part1
print(find_min_cost())

height, width = len(grid)*5, len(grid[0])*5 # part2
full_map = full_map_part2
print(find_min_cost())

f.close()
