
__doc__ ='''
    Step-by-step find out Levenshtein Distance 

    1. Create maxtrix based on source and target
    1. source represent for delete_cost 
    2. target represent for insert_cost
    3. Diagonal line represion subtraction cost


    D[i,j] = min {
    
        delete_cost     = D[i-1,j] + 1,
        insert_cost     = D[i,j-1] + 1,
        subtract_cost   = D[i-1,j -1] + 1 if source[i] != target[j] else 0
    }

    -> Levenshtein Distance = D[num_rows - 1, num_columns - 1]
'''


def __source_split(source) -> list:
    source_list  = ["#"]
    for character in source : # Set first columns = 0,1,2
        source_list.append(character)
    return source_list

def __create_maxtrix(source, target ) ->list[list]:

    num_columns = len(target) +1  ; num_rows = len(source) + 1

    matrix = [[None] *num_columns for _ in range(num_rows)]
    for i in range(num_rows) : # Set first columns = 0,1,2
        matrix[i][0] = i
       
    for j in range(num_columns) : # Set first columns = 0,1,2
        matrix[0][j] = j

    return matrix, num_rows, num_columns

def levenshtein_distance(source = None, target = None) -> int:
    
   
       
    source_list  =__source_split (source)
    target_list  =__source_split (target)

    matrix, num_rows, num_columns = __create_maxtrix(source,target)

    lenvashtein_dis = []
    for i in range(1, num_rows):
        for j in range(1, num_columns):

            delete_cost = matrix[i-1][j] + 1
            insert_cost = matrix[i][j-1] + 1 
            if source_list[i] == target_list[j]:
                sub_cost =  matrix[i-1][j-1] 
            else:
                sub_cost =  matrix[i-1][j-1] + 1

            matrix[i][j] = min(delete_cost,insert_cost,sub_cost  )
            lenvashtein_dis.append(min(delete_cost,insert_cost, sub_cost ))

    return float(matrix[num_rows-1][num_columns-1])

if __name__ == "__main__":

    assert (levenshtein_distance("yu","you")) == 1.0 
    print (levenshtein_distance("hola","hello"))