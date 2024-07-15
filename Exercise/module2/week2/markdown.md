## Length of vector

$$\text{Vector:} \space v = [v_1,v_2,..., v_n]^T$$
$$\text{Legnth of a vector: }\space ||v|| = \sqrt{v_1^2 + v_1^2 + ... +v_n^2}$$

* Example 
```markdown
>>> v = np.array([1,2,3,4])
>>> v
[1 2 3 4]
>>> np.linalg.norm(v)
5.477225575051661
```
```markdown 
def compute_length_vector(vector):
    return np.sqrt(np.sum(vector*vector))

>>> print(compute_length_vector(v))
5.477225575051661
```

## Dot Product between two vector 

$$\text{Vector: }\space v= \begin{bmatrix} v_1 \\\ v_2 \\\ ... \\\ v_n \end{bmatrix} u = \begin{bmatrix} u_1 \\\ u_2 \\\ ... \\\ u_n \end{bmatrix} $$
$$\text{Dot Product: } v.u = v_1*u_1 + v_1*u_1 + ... + v_n*u_n = \sum_{i=0}^{n}(v_i*v_i)$$

```markdown
>>> a = np.array([2,3,4])
>>> b = np.array([5,6,7])
>>> print(np.dot(a,b))
56 
```

```markdown
def compute_dot_vector(vector1, vector2):
    return np.sum(vector1* vector2)

>>> print(compute_dot_vector(a,b))
56
```

## Multiplyin a vector by a matrix

* $$\text{Matrix A: } = \space \begin{bmatrix} a_{11} \space ... \space a_{1n} \\\ ... \space ... \space ...\\\ a_{m1} \space ... \space a_{mn} \end{bmatrix}, A \epsilon R^{m*n} $$

* $$\text{Vector: }\space v= \begin{bmatrix} v_1 \\\ v_2 \\\ ... \\\ v_n \end{bmatrix},v \epsilon R^{n}$$
* $$c =Av = \space \begin{bmatrix} a_{11}*v_1 + \space ... \space a_{1n}*n_n \\\ ... \space ... \space ...\\\ a_{m1}*v_1 + \space ... \space a_{mn}* v_n \end{bmatrix} $$
## Matrix Inverse

* $$\text{Matrix A: }\bold A \space =  \begin{bmatrix} a \space b \\\ c\space d \end{bmatrix}, \bold A \epsilon R^{2*2}$$
* $$\text{Determinant of } \bold A \epsilon R^{2*2} : det(\bold A) = ad - bc$$
* $$\text{if} \space det(A) != 0 \space \text{ A is invertible}$$
* $$\text{Inverse Matrix A: } A^{-1} \space  = \space \frac{1}{det(A)} \begin{bmatrix} d \space -b \\\ -c \space a \end{bmatrix}$$


## Eigenvalue and Eigenvector 

* $$\bold A \epsilon R^{n*n}, \bold I \text{ (identitty matrix) } \epsilon R^{n*n}, v \epsilon R^{n}$$

* $$Eigenvalue \space (\lambda): det (\bold A - \lambda \bold I) = 0$$

* $$Eigenvector \space (v): \space \bold Av = \lambda v <=> (\bold A- \lambda \bold I)v = 0$$

* $$Normalize \space vector: \space \frac{v}{||v||}, v_i\space = \space \frac{v_{i}}{\sqrt{\sum_{1}^{n}v_{i}^2}}$$

```python 
import numpy as np
matrix_a =np.array([[0.9,0.2],[0.1,0.8]])

eigenvalues, eigenvector  = np.linalg.eig(matrix_a)
print(f'Eigenvalue: \n{eigenvalues}')
print()
print(f'Eigenvector: \n{eigenvector}')
Eigenvalue: 
[1.  0.7]

Eigenvector:
[[ 0.89442719 -0.70710678]
 [ 0.4472136   0.70710678]]
```
