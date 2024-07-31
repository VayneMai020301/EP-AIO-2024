import numpy as np 

def compute_std_0(x):
    """
        Compute median in numpy
    """
    x = np.array(x)
    mean = np.mean(x)
    variance = 1/len(x) * np.sum((x-mean)**2)
    std = np.sqrt(variance)

    return std

def compute_std(x):
    """
        Compute median in numpy
    """
    x = np.array(x)
    return np.std(x)

if __name__ == "__main__" :
    X = [171, 176, 155, 167, 169, 182]
    print(f'median of X: {compute_std_0(X)}')