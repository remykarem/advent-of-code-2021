# O(n), O(n)
# Sliding window

def part1(f):
    total = 0
    prev = int(next(f).strip())

    for num in f:
        curr = int(num.strip())
        total += curr > prev
        prev = curr

    print(total)


def part2(f):
    total = 0
    a = int(next(f).strip())
    b = int(next(f).strip())
    c = int(next(f).strip())
    prev_sum = a+b+c

    for x in f:
        d = int(x.strip())
        new_sum = prev_sum - a + d
        if prev_sum < new_sum:
            total += 1
        a, b, c = b, c, d
        prev_sum = new_sum

    print(total)

f = open("day01.txt", "r")
f.seek(0)
part1(f)

f.seek(0)
part2(f)

f.close()
