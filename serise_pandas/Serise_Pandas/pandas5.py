import pandas as pd
import numpy as np

# serise indexing
a = pd.Series([12,32,13,14,15,65,33,23,78,0,44])
# integer indexing
print(a[2])
print(a[0])
# ///////////////////////////////////
A = pd.Series(np.arange(30))
print(A)
print(A[4])
# ///////////////////////////////////
data = pd.read_csv('Book3.csv')
print(data)
A = data.city[-5:]
print('last se count karega \n',A)
print('ulter nate number by \n',data.city[::2])
print("you can provide your choice index number \n")
print(data.city[[11,12,13,14,15]])
# ////////////////////////////////