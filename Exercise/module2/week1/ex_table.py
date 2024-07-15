import pandas as pd
import numpy as np
df = pd.read_csv('advertising.csv')

data = df.to_numpy()
print(f'{df.head()}\n')


def question_15(data):
    max_sales_value = np.max(data[:,3], axis=0)
    index = np.argmax(data[:,3])
    print(f'max value: {max_sales_value} Index: {index}\n')

def question_16(data):
    avaerage_tv = np.average(data[:,0], axis=0)
    print(f'Average of TV: {avaerage_tv}\n')

def question_17(data):
    data_sales = data[:,3]
    print(f'Number sample in Sales > 20: {np.sum(data_sales >=20)}\n')

def question_18(data):
    data_sales = data[:,3]
    index = np.nonzero((data_sales >= 15))

    data_radio_condition  =  data[:,1][index]
    print(f'{np.average(data_radio_condition)}\n')


def question_19(data):
    average_newspaper = np.mean(data[:,2])
    index = np.nonzero((data[:,2] > average_newspaper))

    sum_sales_condition = np.sum(data[:,3][index])
    print(f'{sum_sales_condition}\n')


def question_20(data):
    average_sale = np.mean(data[:,3])

    reflection = np.zeros((200,1), dtype='U10')
    reflection[np.nonzero(data[:,3] > average_sale)] = "Good"
    reflection[np.nonzero(data[:,3] == average_sale)] = "Average"
    reflection[np.nonzero(data[:,3] < average_sale)] = "Bad"

    print(f'{reflection[7:10]}\n')


def question_21(data):
    mean_sale_value = np.mean(data[:,3])
    distance_to_sales = np.abs(np.subtract(data[:,3] ,mean_sale_value))
    index_min_distance  = np.argmin(distance_to_sales)

    value_nearest_mean = data[:,3][index_min_distance]
    reflection = np.zeros((200,1), dtype='U10')

    reflection[np.nonzero(data[:,3] > value_nearest_mean)] = "Good"
    reflection[np.nonzero(data[:,3] == value_nearest_mean)] = "Average"
    reflection[np.nonzero(data[:,3] < value_nearest_mean)] = "Bad"

    print(f'{reflection[7:10]}\n')


if __name__ == "__main__":
    question_15(data)
    question_16(data)
    question_17(data)
    question_18(data)
    question_19(data)
    question_20(data)
    question_21(data)
