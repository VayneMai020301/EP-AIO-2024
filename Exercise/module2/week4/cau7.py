import numpy as np 
import pandas as pd

def compute_correlation_cofficient(v1, v2):
    """
        Compute median in numpy
    """
    v1= np.array(v1)
    v2= np.array(v2)

    return np.corrcoef(v1, v2)

if __name__ == "__main__":

    data = pd.read_csv("advertising.csv")
    print(data.head())

    v1 = data["Radio"]
    v2 = data["Newspaper"]
    
    print(f'{"Radio"} and {"Newspaper"}: {np.round(compute_correlation_cofficient(v1, v2),2)}')
