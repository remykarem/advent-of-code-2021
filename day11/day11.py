import copy
from typing import Iterator
from pyterator import iterate
from itertools import product

HEIGHT, WIDTH = 10, 10
flashes = 0

initial_state = [
    [8,8,2,6,8,7,6,7,1,4],
    [3,1,2,7,7,8,7,2,3,8],
    [8,1,8,2,8,5,2,8,6,1],
    [4,6,5,5,3,7,1,4,8,3],
    [3,8,6,4,5,5,1,3,6,5],
    [1,8,7,8,2,5,3,5,8,1],
    [8,3,1,7,4,2,2,4,3,7],
    [1,5,1,7,2,5,4,2,6,6],
    [2,6,2,1,1,2,4,7,6,1],
    [3,4,7,3,3,3,1,5,1,4],
]

def neighbours(x: int, y: int) -> Iterator:
    return (
        iterate([(x,y-1),(x-1,y-1),(x-1,y),(x-1,y+1),
                 (x,y+1),(x+1,y+1),(x+1,y),(x+1,y-1)])
        .starfilter(lambda a,b: 0<=a<HEIGHT and 0<=b<WIDTH)
    )

def update_one_energy(state: list, x: int, y: int):
    global flashes
    if state[x][y] == 0:
        return  # it has flashed in this step
    elif state[x][y] + 1 <= 9:
        state[x][y] += 1
    else:
        state[x][y] = 0
        flashes += 1
        for neighbour in neighbours(x,y):
            update_one_energy(state,*neighbour)

def add_one(state: list):
    for i, j in product(range(HEIGHT), range(WIDTH)):
        state[i][j] += 1

def update_state(state: list):
    for i, j in product(range(HEIGHT), range(WIDTH)):
        if state[i][j] > 9:
            update_one_energy(state,i,j)

def step(state: list):
    add_one(state)
    update_state(state)

def part1():
    state = copy.deepcopy(initial_state)
    for _ in range(100):
        step(state)
    print(flashes)

def part2():
    state = copy.deepcopy(initial_state)
    time = 0
    while iterate(state).flatten().any():
        time += 1
        step(state)
    print(time)

part1()
part2()
