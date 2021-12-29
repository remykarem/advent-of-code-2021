import numpy as np

def parse_line(line: str) -> list:
    if line=="":
        return None
    else:
        return [int(x) for x in line.split(",")]
    
def all_same(arr1d) -> bool:
    return (arr1d[0] == arr1d).all() 

def get_stuff(X, Y, col):
    diffs = X[:,col][:,None] - Y
    first_row = diffs[0]
    
    idx, = np.where(np.all(first_row==diffs, axis=0))
    
    if len(idx)>0:
        return idx[0], diffs[0,idx][0]
