def remove_ingredients(data):
    '''
        Return new list with each value is unique (Remove Ingredient're the same)
    
    '''
    result = []
    for i in data:
        if i not in result:
            result.append(i)
    return result

if __name__ =="__main__":

    assert remove_ingredients([1,2,2,4,100,100]) ==[1,2,4,100]
    print(remove_ingredients([1,2,2,4,100,100]))