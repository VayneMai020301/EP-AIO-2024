import numpy as np

def compute_median_0(x:list) ->float:
    """
        Compute median from scratch
    """
    n = len(x)
    x = sorted(x)
    if n%2 == 0:
        return (x[int(n/2)] + x[int(n/2 - 1)]) / 2
    else:
        return x[int(n+1)/2]

def compute_median(x:list) ->float:
    """
        Compute median in numpy
    """
    x = np.array(x)
    return np.median(x)

if __name__ == "__main__" :
    X = [1, 5, 4, 4, 9, 13]
    print(f'median of X: {compute_median(X)}')