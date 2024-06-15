def mean_of_list(data = [0,1,2]):
    '''
        Mean value calculation with list
    
    '''
    sum = 0
    for i in data:
        sum += i
    return sum / len(data)

if __name__ =="__main__":

    assert mean_of_list([4,6,8]) == 6
    print(mean_of_list())