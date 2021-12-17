from day13 import Point

assert Point(6,0).folded_vertical(3) == Point(0,0)
assert Point(5,0).folded_vertical(3) == Point(1,0)
assert Point(4,0).folded_vertical(3) == Point(2,0)
assert Point(2,0).folded_vertical(3) == Point(2,0)
assert Point(1,0).folded_vertical(3) == Point(1,0)
assert Point(0,0).folded_vertical(3) == Point(0,0)
