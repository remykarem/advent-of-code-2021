from __future__ import annotations
from typing import List, Set
import numpy as np

from utils import get_stuff


def find_overlaps(a: Scanner, b: Scanner) -> tuple:
    overlap_positions = []
    
    for i in range(len(a.beacons_relative_scanner)):
        for j in range(len(b.beacons_relative_scanner)):
            
            a.move_to_beacon(i)
            b.move_to_beacon(j)

            if a.len_intersection(b) >= 12:
                overlap_positions.append((i,j))
    
    return overlap_positions


class Scanner:

    def __init__(self, beacons):
        self.beacons_relative_scanner = np.array(beacons) 
        self.beacons_relative_origin = np.array(beacons)
        self.current = None     # current position based on self.original
        self.is_aligned = False # coords
        self.beacons_absolute = None
        self.origin = [0,0,0] # origin of the scanner
        self.directions = np.array([[1,1,1]])
        self.indices = [0,1,2]
        
    @property
    def aligned_beacons_set(self) -> set:
        return set(map(tuple,self.beacons_absolute.tolist()))
    
    @property
    def beacon_hashes(self) -> Set[frozenset]:
        # Strong assumption; might lead to false positives
        return set(map(frozenset,np.abs(self.beacons_relative_scanner)))
        
    def move_to_beacon(self, position):
        self.current = self.beacons_relative_scanner[position]
        self.beacons_relative_scanner -= np.array(self.current)
        
    def len_intersection(self, other: Scanner) -> int:
        """Symmetric"""
        a = self.beacon_hashes - set(tuple(self.current))
        b = other.beacon_hashes - set(tuple(other.current))
        return len(a.intersection(b))
    
    def align_with(self, other: Scanner, this_beacons: List[int], other_beacons: List[int]):
        indices, directions, origin = self._get_alignment(other, this_beacons, other_beacons)
        self.origin = origin
        self._align_beacons(indices, directions, origin)
        self.is_aligned = True
    
    def _get_alignment(
        self, other: Scanner, this_beacons: List[int], other_beacons: List[int]
    ) -> tuple:

        indices, directions, coords = [None]*3, [None]*3, [None]*3,
        
        a = self.beacons_relative_origin[this_beacons]
        b = other.beacons_relative_origin[other_beacons]
        
        for col in range(3):
            
            yo = get_stuff(a,b,col)
            if yo:
                i, val = yo
                direction = 1
            else:
                i, val = get_stuff(-a,b,col)
                direction = -1

            coords[i] = -val
            directions[i] = direction
            indices[i] = col

        return indices, directions, coords
    
    def _align_beacons(self, indices, directions, relative):
        assert not self.is_aligned, "how many times do you want to align"

        self.beacons_relative_origin = self.beacons_relative_origin[:,indices]
        self.beacons_relative_origin *= np.array([list(directions)])
        self.beacons_relative_origin += np.array([list(relative)])
        self.beacons_absolute = np.array(self.beacons_relative_origin)
