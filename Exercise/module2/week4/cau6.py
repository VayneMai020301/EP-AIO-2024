import numpy as np 
import pandas as pd

features = ["TV", "Radio", "Newspaper"]


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

    for feature_1 in features :
        for feature_2 in features :
            print()
            print(f'{feature_1} and {feature_2}: {np.round(compute_correlation_cofficient(data[feature_1], data[feature_2]),2)}')
