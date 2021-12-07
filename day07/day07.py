from pyterator import iterate

f = open("day07.txt", "r")
nums = [int(x) for x in f.readline().strip().split(",")]
f.close()

def f(steps):
    # sum of arithmetic progression
    return (steps/2)*(2+(steps-1))

def part1():

    table = {}
    total, size = sum(nums), len(nums)
    acc = 0

    for i, num in enumerate(sorted(nums)):
        if num in table:
            acc += num
            continue
        a = num*i - acc
        b = total - acc - num*(size-i)

        table[num] = a+b
        acc += num

    _, fuel = sorted(table.items(), key=lambda x: x[1])[0]
    return fuel

def part2():
    return (
        iterate(range(len(nums)))
        .map(lambda pos: (
            iterate(nums).map(lambda x: x-pos).map(abs).map(f).sum()
        ))
        .min()
    )

print(part1())
print(part2())
