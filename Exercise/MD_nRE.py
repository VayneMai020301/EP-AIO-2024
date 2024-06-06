import math

def cal_mdnRE(y = None, y_predict=None,n = None, p = None) -> float:
    
    """
    ## Parameter
        * y: True Positive
        * y_predict: predict value
        * n: nth root
        * p: Exponential

    -----------------------
    ## Return
        * Return mean difference of nth root error
    
    """

    assert str(y).isnumeric and (isinstance(y, float) or isinstance(y, int)) , print("[ERROR]: Please try again y")
    assert str(y_predict).isnumeric and (isinstance(y_predict, float) or isinstance(y_predict, int)), print("[ERROR]: Please try again y_predict")
    assert str(n).isnumeric and (isinstance(n, float) or isinstance(n, int))  , print("[ERROR]: Please try again n")
    assert str(p).isnumeric and (isinstance(p, float) or isinstance(p, int))  , print("[ERROR]: Please try again p")

    return round(math.pow((math.pow(y, 1/n) - math.pow(y_predict, 1/n)) , p),3)