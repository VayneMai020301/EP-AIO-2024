import numpy as np

def compute_mean_0(x :list) ->float :
    """
        Compute median from scratch
    """
    
    return sum(x) / len(x)

def compute_mean(x :list) ->float :
    """
        Compute median in numpy
    """
    x = np.array(x)
    return np.mean(x)

if __name__ == "__main__" :
    X = [2, 0, 2, 2, 7, 4, -2, 5, -1, -1]
    print(f'mean of X: {compute_mean_0(X)}')