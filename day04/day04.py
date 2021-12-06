import numpy as np
from pyterator import iterate

# X = [
#     [
#         [22, 13, 17, 11, 0],
#         [8, 2, 23, 4, 24],
#         [21, 9, 14, 16, 7],
#         [6, 10, 3, 18, 5],
#         [1, 12, 20, 15, 19]
#     ],
#     [
#         [3, 15, 0, 2, 22],
#         [9, 18, 13, 17, 5],
#         [19, 8, 7, 25, 23],
#         [20, 11, 10, 24, 4],
#         [14, 21, 16, 12, 6]
#     ],
#     [
#         [14, 21, 17, 24, 4],
#         [10, 16, 15, 9, 19],
#         [18, 8, 23, 26, 20],
#         [22, 11, 13, 6, 5],
#         [2, 0, 12, 3, 7]
#     ]
# ]


# generator = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10,
#              16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]


def update_state(state, numbers):
    condition = np.isin(state, numbers)
    state = np.ma.masked_where(condition, state)
    return state


def get_winners(state) -> list:

    mask = state.mask

    horizontal_winners = mask.all(axis=2, keepdims=True).any(axis=1).flatten()
    vertical_winners = mask.all(axis=1, keepdims=True).any(axis=2).flatten()

    (winners,) = np.where(horizontal_winners | vertical_winners)

    return winners.tolist()


def parse_table(table: list) -> list:
    return iterate(table).map(parse_table_line).to_list()


def parse_table_line(line: str) -> list:
    return [int(x) for x in line.split()]


def main():

    f = open("day04.txt", "r")

    f.seek(0)

    X = (
        iterate(f)
        .skip(1) # skip the first \n
        .split_at(lambda x: x == "\n")
        .map(parse_table)
        .to_list()
    )
    X = np.array(X)

    generator = [int(x) for x in f.readline().strip().split(",")]
    num_boards = X.shape[0]

    state = np.ma.MaskedArray(X, False)
    k = 0
    while not (winners := get_winners(state)):
        k += 1
        state = update_state(state, generator[:k])

    generator[k-1] * state[winners[0]].sum()

    state = np.ma.MaskedArray(X, False)
    k = 0
    prev, curr = [], []
    while True:
        curr = get_winners(state)
        if len(curr) == num_boards:
            winners = list(set(curr)-set(prev))
            break
        elif len(curr) == num_boards-1:
            prev = curr
        k += 1
        state = update_state(state, generator[:k])

    generator[k-1] * state[winners[0]].sum()
    
    f.close()

if __name__ == "__main__":
    main()
