from typing import List
import numpy as np
from itertools import combinations
from pyterator import iterate

from utils import parse_line
from scanner import Scanner, find_overlaps


def get_scanners(f):
    f.seek(0)
    gen = (
        iterate(f)
        .filterfalse(lambda line: line.startswith("---"))
        .map(str.strip)
        .map(parse_line)
        .split_at(lambda line: line is None)
    )
    return iterate(gen).map(list).map(Scanner).to_list()

def find_all_beacons(scanners: List[Scanner]):
    scanners[0].is_aligned = True
    all_beacons = set(map(tuple,scanners[0].beacons_relative_origin.tolist()))
    stack = list(combinations(range(len(scanners)),2))
    yo = {}

    for a, b in stack:
        
        if scanners[a].is_aligned and scanners[b].is_aligned:
            continue
            
        if (a,b) in yo:
            overlapping_beacons = yo.pop((a,b))
        else:
            overlapping_beacons = find_overlaps(scanners[a], scanners[b])
        if not overlapping_beacons:
            continue

        a_beacons, b_beacons = map(list,zip(*overlapping_beacons))
        
        if scanners[a].is_aligned:
            scanners[b].align_with(scanners[a], b_beacons, a_beacons, a)
            new_beacons = scanners[b].aligned_beacons_set
        elif scanners[b].is_aligned:
            scanners[a].align_with(scanners[b], a_beacons, b_beacons, b)
            new_beacons = scanners[a].aligned_beacons_set
        else:
            stack.append((a,b))
            yo[(a,b)] = overlapping_beacons # my brain is fried; let's just do this
        
        all_beacons.update(new_beacons)

    return all_beacons


if __name__ == "__main__":
    f = open("day19.txt", "r")
    scanners = get_scanners(f)
    all_beacons = find_all_beacons(scanners)
    print(len(all_beacons))

    X = np.array([scanner.origin for scanner in scanners])
    max_dist = np.abs(X[:,None] - X).sum(-1,keepdims=True).max(0,keepdims=True).max() # i dont care anymore
    print(max_dist)
