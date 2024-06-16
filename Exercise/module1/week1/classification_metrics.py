
def evaluation(tp= None, fp= None, fn= None):

  """  
  ## Parameter
    * tp: True Positive
    * fp: False Negative
    * fp: False Positive
   
  -----------------------
  ## Return
    * Return Precison, Recall or F1-Score depend upon input from end user
  
  """

  notifications = "[ERROR]: Please typing value in int"
  assert str(tp).isnumeric(), print(notifications)
  assert str(fp).isnumeric(), print(notifications)
  assert str(fn).isnumeric(), print(notifications)

  print("--"*30)
  precison = tp/(tp+fp)
  recall = tp/(tp+fn)
  print(f"Precision : {precison}")
  print(f"Recall : {recall}")
  f1_score = 2* precison* recall  / (precison + recall)
  print(f"F1-score : {f1_score}")
