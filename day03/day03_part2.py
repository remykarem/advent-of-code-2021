from pyterator import iterate
import numpy as np


def get_o2_rating(X: np.ndarray, col: int) -> list:

    pred = X[:, col].sum() >= X.shape[0]/2
    indices, = np.where(X[:, col] == pred)

    if len(indices) == 1:
        return X[indices][0].tolist()
    else:
        return get_o2_rating(X[indices], col+1)


def get_co2_rating(X: np.ndarray, col: int) -> list:

    pred = X[:, col].sum() < X.shape[0]/2
    indices, = np.where(X[:, col] == pred)

    if len(indices) == 1:
        return X[indices][0].tolist()
    else:
        return get_co2_rating(X[indices], col+1)


def num_arr2decimal(arr: list) -> int:
    bin_str = "".join([str(x) for x in arr])
    return int(bin_str, 2)


def get_ratings(arr: list) -> tuple:
    report_o2 = np.array(arr)
    report_co2 = np.array(arr)

    rating_o2 = get_o2_rating(report_o2, 0)
    rating_co2 = get_co2_rating(report_co2, 0)

    return num_arr2decimal(rating_o2), num_arr2decimal(rating_co2)


def main():

    f = open("day03.txt", "r")
    arr = (
        iterate(f)
        .map(str.strip)
        .map(lambda line: [int(x) for x in line])
        .to_list()
    )

    a, b = get_ratings(arr) # recursion
    print(a*b)
    
    f.close()


if __name__ == "__main__":
    main()
    