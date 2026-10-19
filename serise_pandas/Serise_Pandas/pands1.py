import numpy as np
import pandas as pd

# # serise part
# student = ['english','math','english','physics']
# serise1 = pd.Series(student)
# print(serise1)

# ///////////////////////////////
# integer type serise
# total = [11,3,55,87,12,56,34]
# print(pd.Series(total))

# # //////////////////////////////////////////
#  #you can the change index number
# student = ['english','math','english','physics']
# score = [22,32,45,76]
# serise1 = pd.Series(student,index=score) #index number show score 
# print(serise1)

# # //////////////////////////////////////////
# use of disctnory
student={
    'ankit':24,
    'bikash':66,
    'ajit':58,
    'mohit':40,
    'mohit1':40
}
marks_serise = pd.Series(student,name='ankit')
print(marks_serise)
# print(marks_serise)
# print(marks_serise.dtype)
# # chexk all is unick is not unick  show the true and false
# # unick = marks_serise.is_unique
# # print(unick)
# insex = marks_serise.index  #all show in index value in serise
# print(insex)
# value = marks_serise.values  #(all show the value marks)
# print(value)

# # /////////////////////////////////////////////////////////////
