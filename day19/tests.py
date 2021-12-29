import numpy as np
from utils import all_same


assert not all_same(np.array([1,2,3]))
assert all_same(np.array([1,1,1]))
