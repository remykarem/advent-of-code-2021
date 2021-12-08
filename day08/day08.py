from pyterator import iterate
from functools import reduce
from operator import and_, sub

#
#     1         -
# 2.1   2.2    | |
#     3         -
# 4.1   4.2    | |
#     5         -
#
num2positions = {
    0: [1, 2.1, 2.2,    4.1, 4.2, 5],
    1: [        2.2,         4.2,  ],
    2: [1,      2.2, 3, 4.1,      5],
    3: [1,      2.2, 3, 4.2,      5],
    4: [   2.1, 2.2, 3,      4.2   ],
    5: [1, 2.1,      3, 4.2,      5],
    6: [1, 2.1,      3, 4.1, 4.2, 5],
    7: [1,      2.2,         4.2,  ],
    8: [1, 2.1, 2.2, 3, 4.1, 4.2, 5],
    9: [1, 2.1, 2.2, 3,      4.2, 5],
}

def signal_patterns_to_signal(signal_patterns: str) -> dict:
    return iterate(signal_patterns.split()).groupby(len, set, lambda x: x[0] if len(x)==1 else list(x))

def signal_to_segment(signal: dict) -> dict:
    segment = {}
    segment[1]   = signal[3] - signal[2]
    segment[4.2] = reduce(and_, [signal[2]]+signal[6])
    segment[2.2] = signal[2] - segment[4.2]
    segment[3]   = reduce(and_, [signal[4] - segment[1] - segment[2.2] - segment[4.2]]+signal[5])
    segment[2.1] = signal[4] - signal[2] - segment[3]
    segment[5]   = reduce(sub, [reduce(and_,signal[5])]+list(segment.values()))
    segment[4.1] = reduce(sub, [signal[7]]+list(segment.values()))
    
    return {k:v.pop() for k,v in segment.items()}

def segment_to_num(segment):
    return {
        frozenset({segment[x] for x in num2positions[i]}): i 
        for i in range(10)}

def decode(input_pattern: str, output: str) -> int:
    signal = signal_patterns_to_signal(input_pattern)
    segment = signal_to_segment(signal)
    evaluator = segment_to_num(segment)
    
    return int(
        iterate(output.split())
        .map(frozenset)
        .map(lambda x: evaluator[x])
        .map(str)
        .join()
    )

f = open("day08.txt", "r")

f.seek(0)
part1 = len(
    iterate(f)
    .map(lambda line: line.strip().split(" | ")[1])
    .flat_map(lambda line: [len(x) for x in line.split()])
    .filter(lambda num_segments: num_segments in [2,3,4,7])
    .to_list()
)

f.seek(0)
part2 = (
    iterate(f)
    .map(lambda line: line.strip().split(" | "))
    .starmap(decode)
    .sum()
)

print(part1)
print(part2)
