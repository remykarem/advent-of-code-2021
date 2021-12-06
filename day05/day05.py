from collections import Counter, Generator
from typing import Iterator, List
from pyterator import iterate


def parse_line(line: str) -> List[int]:
    list_str = line.strip().replace(" -> ", ",").split(",")
    return [int(x) for x in list_str]

def is_vertical_or_horizontal(x1, y1, x2, y2) -> bool:
    return x1==x2 or y1==y2

def enumerate_points_pt1(x1, y1, x2, y2, x_step, y_step) -> Generator:
    if x1==x2:
        return ((x1,y) for y in range(y1,y2+y_step,y_step))
    else:
        return ((x,y1) for x in range(x1,x2+x_step,x_step))
    
def include_step(x1, y1, x2, y2) -> tuple:
    x_step = -1 if x1 > x2 else 1
    y_step = -1 if y1 > y2 else 1
    return x1, y1, x2, y2, x_step, y_step

def get_num_points_ge_2(points) -> int:
    counter = Counter(points)
    return len([v for v in counter.values() if v>=2])

def enumerate_points_pt2(x1, y1, x2, y2, x_step, y_step) -> Iterator:
    if x1==x2:
        return ((x1,y) for y in range(y1,y2+y_step,y_step))
    elif y1==y2:
        return ((x,y1) for x in range(x1,x2+x_step,x_step))
    else:
        return zip(range(x1,x2+x_step,x_step), range(y1,y2+y_step,y_step))
        
assert list(enumerate_points_pt2(9,7,7,9,-1,1)) == [(9, 7), (8, 8), (7, 9)]

def main():
    f = open("day05.txt", "r")

    # Part 1
    f.seek(0)
    points = (
        iterate(f)
        .map(parse_line)
        .starfilter(is_vertical_or_horizontal)
        .starmap(include_step)
        .starmap(enumerate_points_pt1)
        .flatten()
    )
    print(get_num_points_ge_2(points))

    # Part 2
    f.seek(0)
    points = (
        iterate(f)
        .map(parse_line)
        .starmap(include_step)
        .starmap(enumerate_points_pt2)
        .flatten()
    )
    print(get_num_points_ge_2(points))

    f.close()

if __name__ == "__main__":
    main()
