def residual_devide_by_3(data):
    ''''
        Find new list with element which residula devide by 3 equal 0 (zero) 
    
    
    '''
    result = []
    for i in data:
        if i % 3 == 0:
            result.append(i)
    return result

if __name__ =="__main__":

  assert residual_devide_by_3([1,2,3,4,5,6]) == [3,6]
  print(residual_devide_by_3([123,12395,1931,41,123,9]))