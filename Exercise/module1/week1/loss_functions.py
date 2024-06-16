import math 
import random

def calculate_loss(_name = None, _num_sample = None) -> float: 
    """
    ##Parameter
        * Loss function name
        * Number sample
    ##Return
        Return loss depend upon function name and number sample
    """
    
    assert _name in ["MAE","MSE","RMSE"], print ("[ERROR]: You wrong loss name, Please typing again")
    assert str (_num_sample).isnumeric(), print ("[ERROR]: You wrong number sample, Please typing again")    

    loss = 0; loss_mse = 0 ;targets = [] ; predicts = []
    for _ in range(_num_sample):
        targets.append(random.uniform(0,10))
        predicts.append(random.uniform(0,10))

    for t, p in zip(targets, predicts):
        if  _name == "MAE":
            loss += abs(t-p)
        elif _name == "MSE":
            loss_mse += (t-p)* (t-p)
        
    if  _name == "MAE":
        return loss / _num_sample
    elif _name == "MSE":
        return loss_mse / _num_sample

    elif _name == "RMSE":
        math.sqrt(loss_mse / _num_sample)
    
    return 0