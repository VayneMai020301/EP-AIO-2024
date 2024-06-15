def function_helper(x):
    '''
        Using list comprehension to find out value greater than 0 (Zero)
    
    '''
    if x> 0: return "T"
    else: return "F"

def my_function(data)->list :
    result  = [function_helper(x) for x in data]
    return result

if __name__ =="__main__":

    assert my_function([20,-3,-3,-3]) == ["T","F","F","F"]
    print(my_function([20,-23,-3,-3]))