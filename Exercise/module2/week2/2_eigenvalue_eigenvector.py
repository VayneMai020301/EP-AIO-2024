import numpy as np

def compute_eigenvalue_eigenvector(matrix):

    a, b = matrix[0, 0], matrix[0, 1]
    c, d = matrix[1, 0], matrix[1, 1]

    trace = a + d
    det = a * d - b * c

    coefficients = [1, -trace, det]
    eigenvalues = np.roots(coefficients) # Solve quadratic equation to find solution of quadratic equation

    print("Matrix A:\n", matrix)
    print("Eigenvalues of A:", eigenvalues)

    lambda1, lambda2 = eigenvalues

    # Solve (A - lambda1*I)v = 0
    I = np.identity(2)
    a_lambda1_i = matrix - lambda1 * I

    # Eigenvector corresponding to lambda1
    if a_lambda1_i[0, 0] != 0:
        v1_1 = 1
        v1_0 = -a_lambda1_i[0, 1] / a_lambda1_i[0, 0]
    else:
        v1_0 = 1
        v1_1 = -a_lambda1_i[1, 0] / a_lambda1_i[1, 1]

    eigenvector1 = np.array([v1_0, v1_1])
    eigenvector1 = eigenvector1 / np.linalg.norm(eigenvector1)

    # Solve (A - lambda2*I)v = 0
    a_lambda2_i = matrix - lambda2 * I

    if a_lambda2_i[0, 0] != 0:
        v2_1 = 1
        v2_0 = -a_lambda2_i[0, 1] / a_lambda2_i[0, 0]
    else:
        v2_0 = 1
        v2_1 = -a_lambda2_i[1, 0] / a_lambda2_i[1, 1]

    eigenvector2 = np.array([v2_0, v2_1])
    eigenvector2 = eigenvector2 / np.linalg.norm(eigenvector2)

    eigenvectors = np.column_stack((eigenvector1, eigenvector2))

    return (eigenvalues,eigenvectors)

if __name__ == "__main__":

    matrix_a =np.array([[0.9,0.2],[0.1,0.8]])

    eigenvalues, eigenvector  = np.linalg.eig(matrix_a)
    print(f'Eigenvalue: \n{eigenvalues}')
    print()
    print(f'Eigenvector: \n{eigenvector}')
    print('-'*20)
    print(compute_eigenvalue_eigenvector(matrix_a))