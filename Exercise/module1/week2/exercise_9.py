def max_value(data):
    '''
        # Find list maximimum
            1.max = list[0] 
            2.if new_max > max -> new_max = max
            3. return new_maax
    
    '''
    max = data[0]
    for i in data:
        if i > max:
            max = i
    return max

if __name__ =="__main__":

    assert max_value([1,2,-3,4,5]) == 5
    print(max_value([-1002,13,10431,-94]))