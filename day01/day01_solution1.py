# # Solution 1: O(n), O(n^3)
# Copying iterators then skipping

from pyterator import iterate, tee

f = open("day01.txt", "r")

m,n = tee(f)

(
    m.zip(n.skip(1))
    .map(lambda x: iterate(x).map(str.strip).map(int).to_list())
    .starmap(lambda a,b: a<b)
    .sum()
)

f.seek(0)
p,q,r = tee(f,3)

c = (
    p.zip(q.skip(1)).zip(r.skip(2))
    .starmap(lambda a,b: (a[0],a[1],b))
    .map(lambda x: iterate(x).map(str.strip).map(int).to_list())
    .map(sum)
)

m,n = tee(c)
(
    m.zip(n.skip(1))
    .starmap(lambda a,b: a<b)
    .sum()
)

f.close()
