import numpy as np

def activation(_name =None, _value= None, _alpha = 0.0):
  assert _name in ["sigmoid","relu","elu"], print(f"[ERROR]: {_name} activation function is not supported, Please typing activation function name again")
  assert isinstance(_value,float), print("[ERROR]: Please typing _value in float")
  assert isinstance(_alpha,float), print("[ERROR]: Please typing _alpha in float")

  if _name == "sigmoid":
    return 1/(1+np.exp(-_value))
  elif _name == "relu":
    return max(0,_value)

  elif _name == "elu":
    if _value <= 0:
      return _alpha * (np.exp(_value)-1)
    else:
      return _value