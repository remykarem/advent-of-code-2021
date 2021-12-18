def identity(x) -> str:
    return x[0]

def gt(iterable) -> bool:
    return int(iterable[0] > iterable[1])

def lt(iterable) -> bool:
    return int(iterable[0] < iterable[1])

def eq(iterable) -> bool:
    return int(iterable[0] == iterable[1])
