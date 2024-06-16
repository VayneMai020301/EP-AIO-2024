

def min_value(data):
    '''
        # Find out list minimum
            1. min = list[0]
            2. if new_min < min -> new_min = min 
            3. return new_min
    
    '''
    min = data[0]
    for i in data:
        if i < min:
            min = i
    return min

if __name__ =="__main__":

    assert min_value([1,2,-3,4,5]) == -3
    print(min_value([-1002,13,10431,-94]))