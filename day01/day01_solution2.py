# O(n), O(n)
# Sliding window
from collections import deque


def part1(f):
    a = int(next(f).strip())

    total = 0
    for num in f:
        b = int(num.strip())
        total += b > a
        a = b
    print(total)


def part2(f):

    a = int(next(f).strip())
    b = int(next(f).strip())
    c = int(next(f).strip())
    window = deque([a, b, c], maxlen=3)
    prev_sum = sum(window)

    total = 0
    for x in f:
        num = int(x.strip())
        window.append(num)
        new_sum = sum(window)
        if prev_sum < new_sum:
            total += 1
        prev_sum = new_sum

    print(total)

def main():
    f = open("day01.txt", "r")
    f.seek(0)
    part1(f)
    f.seek(0)
    part2(f)
    f.close()

if __name__ == "__main__":
    main()
