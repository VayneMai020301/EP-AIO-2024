import numpy as np 

def create_train_dataset():
    data = [['Sunny', 'Hot', 'High', 'Weak', 'no'],
            ['Sunny', 'Hot', 'High', 'Strong', 'no'],
            ['Overcast', 'Hot', 'High', 'Weak', 'yes'],
            ['Rain', 'Mild', 'High', 'Weak', 'yes'],
            ['Rain', 'Cool', 'Normal', 'Weak', 'yes'],
            ['Rain', 'Cool', 'Normal', 'Strong', 'no'],
            ['Overcast', 'Cool', 'Normal', 'Strong', 'yes'],
            ['Overcast', 'Mild', 'High', 'Weak', 'no'],
            ['Sunny', 'Cool', 'Normal', 'Weak', 'yes'],
            ['Rain', 'Mild', 'Normal', 'Weak', 'yes']]
    
    return  np.array(data)

def compute_prior_probability(data : np.array) -> tuple: 

    """
        This function compute prior probability (Tính xác suất tiên nghiệm)
    """
    categorical = data[: , -1]

    num_yes = np.sum(categorical=='yes')
    num_no  = np.sum(categorical=='no')

    prior_probablity_yes = num_yes / (num_yes  +num_no )
    prior_probablity_no = num_no / (num_yes  +num_no )

    return (prior_probablity_no, prior_probablity_yes)


def statistic (train_data, column = 0, feature = 'Sunny', conditional = 'yes'):
    num_conditional = np.sum(train_data[:, 4] == conditional)
    num_feature_given_conditional = np.sum(train_data[train_data[:,4]==conditional][:, column] == feature)

    return num_feature_given_conditional / num_conditional


def compute_conditional_probability(train_data) -> tuple:
    """
        Return 
    """

    conditional_probability = np.zeros((4,), dtype=object)
    list_x_name = []
    for i in range(0, train_data.shape[1]-1):
        x_unique = np.unique(train_data[:, i])
        list_x_name.append(x_unique)

    outlook_index = 0
    temperature_index = 1
    humidity_index = 2
    wind_index = 3

    p_outlook = np.zeros((2, len(list_x_name[outlook_index])), dtype=float)
    p_temperature = np.zeros((2, len(list_x_name[temperature_index])), dtype=float)
    p_humidity = np.zeros((2, len(list_x_name[humidity_index])), dtype=float)
    p_wind = np.zeros((2, len(list_x_name[wind_index])), dtype=float)

    for i in range(len(list_x_name[outlook_index])):
        p_outlook[1, i] = statistic(dataset, outlook_index, list_x_name[outlook_index][i],conditional='yes')
        p_outlook[0, i] = statistic(dataset, outlook_index, list_x_name[outlook_index][i],conditional='no')

    for i in range(len(list_x_name[temperature_index])):
        p_temperature[1, i] = statistic(dataset, temperature_index, list_x_name[temperature_index][i],conditional='yes')
        p_temperature[0, i] = statistic(dataset, temperature_index, list_x_name[temperature_index][i],conditional='no')

    for i in range(len(list_x_name[humidity_index])):
        p_humidity[1, i] = statistic(dataset, humidity_index, list_x_name[humidity_index][i],conditional='yes')
        p_humidity[0, i] = statistic(dataset, humidity_index, list_x_name[humidity_index][i],conditional='no')
    

    for i in range(len(list_x_name[wind_index])):
        p_wind[1, i] = statistic(dataset, wind_index, list_x_name[wind_index][i],conditional='yes')
        p_wind[0, i] = statistic(dataset, wind_index, list_x_name[wind_index][i],conditional='no')

    conditional_probability[0]= p_outlook
    conditional_probability[1]= p_temperature
    conditional_probability[2]= p_humidity
    conditional_probability[3]= p_wind

    return np.array(conditional_probability), list_x_name

def add_padding_text_to_array(list_list : list[list]):

    max_length = max(len(sublist) for sublist in list_list)
    padded_list = [sublist + [' '] * (max_length - len(sublist)) for sublist in list_list]

    numpy_array = np.array(padded_list, dtype='<U8')
    return numpy_array


def get_index_from_value (list_features : list[np.array], 
                          feature_name :str ) :
    
    return np.nonzero(list_features == feature_name)[0][0] if len(np.nonzero(list_features == feature_name)[0]) >=1 else -1


def prediction_play_tennis (list_x_name , prior_probability , conditional_probability ,x = ["Sunny","Cool","High","Strong"]):

    x1 = get_index_from_value (x [0] , list_x_name [0])
    x2 = get_index_from_value (x [1] , list_x_name [1])
    x3 = get_index_from_value (x [2] , list_x_name [2])
    x4 = get_index_from_value (x [3] , list_x_name [3])

    p0 = prior_probability[0]* conditional_probability[0][0,x1] * conditional_probability[1][0,x2]* conditional_probability[2][0,x3] * conditional_probability[3][0,x4]
    print(f'Probability play tennis = no  when event X hapened: {p0}')

    p1= prior_probability[1]* conditional_probability[0][1,x1] * conditional_probability[1][1,x2]* conditional_probability[2][1,x3] * conditional_probability[3][1,x4]
    print(f'Probability play tennis = yes when event X hapened: {p1}')

    if p0 > p1 :
        y_pred =0
    else :
        y_pred =1

    return y_pred

if __name__ == "__main__":
    print('---------------------------------- CREATE TRAIN DATASET ----------------------------------')
    print(create_train_dataset())
    dataset = create_train_dataset()
    print('\n---------------------------------- COMPUTE PRIOR PROBABILITY ----------------------------------')

    prior_probability = compute_prior_probability(dataset)
    print ("P(play tennis = No") , prior_probability [0]
    print ("P(play tennis = Yes") , prior_probability [1]
    
    print('\n---------------------------------- COMPUTE CONDITIONAL PROBABILITY ----------------------------------')
    conditional_probability, list_features = compute_conditional_probability(dataset)
    print(conditional_probability)
    print(list_features)

    print('\n---------------------------------- GET INDEX FROM VALUE ----------------------------------')
    print(f'Index of Sunny is: {get_index_from_value(list_features[0],"S")}')
    print(statistic(dataset, 0, "Sunny",conditional='no'))

    print('\n---------------------------------- PREDICTION PLAY TENNIS ----------------------------------')
    print(f'Class:0( Play Tennis = No) | 1(Play tennis  = Yes): {prediction_play_tennis(list_features, prior_probability=prior_probability, conditional_probability= conditional_probability)}')    