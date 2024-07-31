import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


if __name__ == "__main__":
    data = pd.read_csv ("advertising.csv")
    plt.figure ( figsize =(10 ,8))
    sns.heatmap(data.corr(), annot=False, fmt=".2f", linewidth=.5)
    plt.show ()