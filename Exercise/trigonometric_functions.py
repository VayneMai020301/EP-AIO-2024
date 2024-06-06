import math
def factorial(x):
    assert x >=0 , print("Please typing unsigned integer")
    if x == 0:
        return 1
    else :
        return x* factorial (x-1)

def cal_sin(x,n):
    
    assert n >=0 , print("[ERROR]: Please typing n is unsigned integer")
    sin  = 0
    for i in range(n):
        sin += math.pow(-1,i) * math.pow(x, (2*i+1)) / factorial (2*i+1)
    return sin

def cal_cos(x,n):
    assert n >=0 , print("[ERROR]: Please typing n is unsigned integer")
    cos = 0 
    for i in range(n):
        cos += math.pow(-1,i) * math.pow(x, (2*i)) / factorial (2*i)
    return cos

def cal_sinh(x,n):
    assert n >=0 , print("[ERROR]: Please typing n is unsigned integer")
    sinh = 0
    for i in range(n):
        sinh += math.pow(x, (2*i+1)) / factorial (2*i+1)
    return sinh

def cal_cosh(x,n):
    assert n >=0 , print("[ERROR]: Please typing n is unsigned integer")
    cosh = 0 
    for i in range(n):
        cosh += math.pow(x, (2*i)) / factorial (2*i)
    return cosh