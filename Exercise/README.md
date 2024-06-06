# How to run activation function in the module
```
cd .\Exercise\
python -c "from activation_functions import *; print(activation('sigmoid', 3.0, 0.0))"
python -c "from activation_functions import *; print(activation('relu', 10.0, 0.0))"
python -c "from activation_functions import *; print(activation('elu', 10.0, 0.0))"
```

# How to run loss function in the module
```
cd .\Exercise\
python -c "from loss_functions import *; print(calculate_loss('MAE',100))"
python -c "from loss_functions import *; print(calculate_loss('MSE',100))"
python -c "from loss_functions import *; print(calculate_loss('RMSE',100))"
```

# How to run classification metrics
```
cd .\Exercise\
python -c "from classification_metrics import *; print(evaluation(2,4,5))" 
```
# How to run MD_nRE metrics
```
cd .\Exercise\
python -c "from MD_nRE import *; print(cal_mdnRE(100.0, 99.5))" 
```

# How to run trigonometric functions
```
cd .\Exercise\
python -c "from trigonometric_functions import *; print(cal_sin(3.14, 10))" 
python -c "from trigonometric_functions import *; print(cal_cos(3.14, 10))"  
python -c "from trigonometric_functions import *; print(cal_sinh(3.14, 10))" 
python -c "from trigonometric_functions import *; print(cal_cosh(3.14, 10))" 
```