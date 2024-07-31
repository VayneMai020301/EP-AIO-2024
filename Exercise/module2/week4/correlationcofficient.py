import numpy as np 

def compute_correlation_cofficient_0(v1, v2):
    """
        Compute median in numpy
    """
    v1= np.array(v1)
    v2= np.array(v2)
    
    mean1 = np.mean(v1)
    std1  = np.sqrt(np.var(v1))
    
    mean2 = np.mean(v1)
    std2  = np.sqrt(np.var(v2))

    N = len(v1)
    return 1 / N * (np.sum((v1-mean1)*(v2-mean2)))/ (std1 * std2)


def compute_correlation_cofficient(v1, v2):
    """
        Compute median in numpy
    """
    v1= np.array(v1)
    v2= np.array(v2)

    return np.corrcoef(v1, v2)

if __name__ == "__main__" :
    v1 = [ -2, -5, -11, 6, 4, 15, 9]
    v2 = [ 4, 25, 121, 36, 16, 225, 81]
    print(f'correlation cofficient v1 and v2 : {compute_correlation_cofficient_0(v1, v2)}')