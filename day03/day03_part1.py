import numpy as np
from collections import Counter

f = open("day03.txt", "r")
arr = []
for line in f:
    arr.append([int(x) for x in line.strip()])

X = np.array(arr)

nums = []
for col in X.T:
    c = Counter(col)
    nums.append(c.most_common(n=1)[0][0])
bin_str = "".join([str(num) for num in nums])

gamma = int(bin_str, 2)
epsilon = gamma ^ int("".join(['1']*len(bin_str)),2)

print(gamma * epsilon)

f.close()
