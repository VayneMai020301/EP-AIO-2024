

def extend_list(list1, list2):
    '''
    # Using extend medthod to extend list
        1. syntax: list.extend(iterable)
        2. Iterabel don't need differencite data type 
        3. Example a = [1,2], a.extend(["1",2], {})

    '''
    list1.extend(list2)
    return list1

list_1 = [1,2]
list_2 = [3,4]
list_3 = [0,0]

if __name__ =="__main__":
    assert extend_list([1,2],extend_list([3,4],[5,6])) == [1,2,3,4,5,6]
    print(extend_list(list_1, extend_list(list_2, list_3)))