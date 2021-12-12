from pyterator import iterate

f = open("day12.txt", "r")
node2children = {}
cave_map = iterate(f).map(str.strip).map(lambda line: set(line.split("-"))).to_list()

def find_children(node: str):
    if node in node2children:
        return node2children[node]
    else:
        children = iterate(cave_map).filter(lambda path: node in path).flat_map(lambda path: path-{node}).to_set()
        node2children[node] = children
        return children

def get_num_paths_part1(node: str, visited: list, initial = False):
    if node == "end":
        return 1
    elif node == "start" and not initial:
        return 0
    elif is_small_cave(node) and node in visited:
        return 0
    else:
        visited.append(node)
        children = find_children(node)
        return sum([
            get_num_paths_part1(child, list(visited))
            for child in children
        ])

def is_small_cave(node: str):
    return node.islower() and node not in ["start","end"]

def get_num_paths_part2(node: str, visited: list, chosen=None, initial=False):
    if node == "end":
        return 1
    elif node == "start" and not initial:
        return 0
    elif is_small_cave(node) and node in visited:
        if chosen is None:
            chosen = node
        else:
            return 0
    
    visited.append(node)
    children = find_children(node)
    return sum([
        get_num_paths_part2(child, list(visited), chosen)
        for child in children
    ])

print(get_num_paths_part1("start", [], initial=True))
print(get_num_paths_part2("start", [], initial=True))
f.close()
