import numpy as np 
def compute_length_vector(vector):
    return np.sqrt(np.sum(vector*vector))

def compute_dot_vector(vector1, vector2):
    return np.sum(vector1* vector2)

def compute_multi_vector(matrix_a, vector):
    return np.dot(matrix_a,vector)


if __name__ =="__main__":

    print(f'Cau 1: {compute_length_vector(np.array([-2,4,9,21]))}')

    print(f'Cau 2: {compute_dot_vector(np.array([0,1,-1,2]), np.array([2,5,1,0 ]))}')

    print(f'Cau 3: {(np.array([[1,2],[3,4]])).dot(np.array([1,2]))}') #.dot that mean calculate dot product

    print(f'Cau 4: {(np.array([[-1,2],[3,-4]]))@(np.array([1,2]))}') # @ that mean calculate dot product

    print(f'Cau 5: {(np.array([[-1,1,1],[0,-4,9]]))@(np.array([0,2,1]))}') 

    print(f'Cau 6: {(np.array([[0,1,2],[2,-3,1]]))@(np.array([[1,-3],[6,1],[0,-1]]))}') 

    print(f'Cau 7: {(np.eye(3))@(np.array([[1,1,1],[2,2,2],[3,3,3]]))}') 
    
    print(f'Cau 9: {(np.reshape(np.array([[1,2],[3,4]]),(-1,4),"F")[0])@(np.array([[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]]))}') 
