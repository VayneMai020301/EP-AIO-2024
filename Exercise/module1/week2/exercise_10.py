def find_element_list(data, element):
    '''
        Return True if value already exits in list else return False
    
    '''
    result = []
    for i in data:
        if i == element:
            result.append(True)
        else:
            result.append(False)

    return any(result)

if __name__ =="__main__":

    assert find_element_list([1,2,3,4,5], 3) == True
    assert find_element_list([1,2,3,4,5], -3) == False

    print(find_element_list([1,2,3,4] ,2))