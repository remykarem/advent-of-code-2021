from pyterator import iterate

f = open("day09.txt", "r")

nums = (
    iterate(f)
    .map(lambda line: line.strip()).map(list)
    .map(lambda nums: iterate(nums).map(int).to_list())
    .to_list()
)

def part1():
    to_add = 0
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            num = nums[i][j]
            if all_greater_than(nums,i,j,num):
                to_add += (num+1)
    
    return to_add

def all_greater_than(nums, i, j, num):
    return (
        iterate([(i,j-1),(i,j+1),(i-1,j),(i+1,j)])
        .starfilter(lambda i,j: 0<=i<len(nums) and 0<=j<len(nums[i]))
        .starmap(lambda i,j: nums[i][j]>num)
        .all()
    )

def part2():
    stack, seen, sizes = [], set(), []
    height, width = len(nums), len(nums[0])

    for i in range(height):
        for j in range(width):
            
            if (i,j) in seen:
                continue
            else:
                stack.append((i,j))
            
            size = 0
            while stack:
                # Update seen
                ctx = stack.pop()
                seen.add(ctx)
                
                x, y = ctx
                
                # Update size
                if nums[x][y]==9:
                    continue
                else:
                    size += 1
                
                # Update stack
                neighbours = [
                    (m,n) for m,n in [(x+1,y), (x,y-1), (x,y+1), (x-1,y)]
                    if (0<=m<height) and (0<=n<width) and ((m,n) not in stack) and ((m,n) not in seen)]
                stack.extend(neighbours)
                
            # Update sizes
            sizes.append(size)

    sizes.sort(reverse=True)

    return iterate(sizes).take(3).prod()



print(part1())
print(part2())
