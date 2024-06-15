def factorial(n):
    '''
        Factorial Calculation with list
    
    '''
    result = 1
    while n >=1 :
        result =result*n
        n = n-1
    return result

if __name__ =="__main__":

    assert factorial(5) == 120
    print(factorial(8))