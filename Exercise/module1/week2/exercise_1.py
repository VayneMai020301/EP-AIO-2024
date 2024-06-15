
__doc__= """
    Doc string of exercise_1\n
    max_kernel function help us find new list consis maximum value with each other slising window with kernel_size
"""

def max_kernel(num_list:list, 
               kernel_size:int , stride:int = 1) -> list:

    """
    num_list: input list 
    kernel_size: number positison will be slising
    stride: step of slising

    # Ouput:  
        A list consist max value with each other slising
    
    """
    result = []
    if kernel_size > len(num_list) :
        print("kernel_size must be greater than or equal list's capacity")
        return result
    
    start_idx = 0 
    stop_idx  = 0

    for i in range(len(num_list)):
        start_idx = i ; stop_idx = start_idx + kernel_size 
        
        if stop_idx > len(num_list):break
        result.append(max(num_list[start_idx: stop_idx]))

    return result


if __name__ == "__main__":

    '''
        Test case 1: max_kernel([1,2,3,4,5,6], 6) == [6] 
        Test case 2: max_kernel([1,2,3,4,5,6], 7) == []
        Test case 3: max_kernel([1,2,3,4,5,6], 3) == [3,4,5,6]
    '''
    assert max_kernel([1,2,3,4,5,6], 6) == [6] 
    assert max_kernel([1,2,3,4,5,6], 7) == []
    assert max_kernel([1,2,3,4,5,6], 3) == [3,4,5,6]

    print(max_kernel([3 , 4 , 5 , 1 , -44 , 5 ,10 , 12 ,33 , 1], 3) )