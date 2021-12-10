from typing import Optional
from pyterator import iterate

POINTS_PART1 = {')':3, ']':57, '}':1197, '>':25137}
POINTS_PART2 = {'(':1, '[':2, '{':3, '<':4}
PAIRS = {'{': '}', '(':')', '<':'>', '[':']'}

def get_wrong_character(string: str) -> Optional[str]:
    stack = []
    for ch in string:
        if ch in PAIRS:
            stack.append(ch)
        else:
            left = stack.pop()
            if PAIRS[left] != ch:
                return ch
    return None

def get_remaining_chars(string: str) -> list:
    stack = []
    for ch in string:
        if ch in PAIRS:
            stack.append(ch)
        else:
            stack.pop()
    return stack

def calculate_score(chars: list) -> int:
    return (iterate(chars)
        .map(POINTS_PART2.__getitem__)
        .reverse()
        .reduce(lambda a,b: a*5+b))
    

f = open("day10.txt", "r")

f.seek(0)
part1 = (
    iterate(f)
    .map(str.strip)
    .filter_map(get_wrong_character)
    .map(POINTS_PART1.__getitem__)
    .sum()
)

f.seek(0)
part1_ = (
    iterate(f)
    .map(str.strip)
    .filterfalse(get_wrong_character)
    .map(get_remaining_chars)
    .map(calculate_score)
    .to_list()
)
part2 = sorted(part1_)[len(part1_)//2]

print(part1)
print(part2)

f.close()
