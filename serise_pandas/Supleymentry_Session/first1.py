import pandas as pd
import numpy as  np
import sys
data = pd.read_csv('Book3.csv')
print(data)
A=sys.getsizeof(data)
print('size of sys method\n',A)
# Correct way to check memory usage
B = data.memory_usage(deep=True).sum()
print("Memory Usage (bytes):", B)
# ////////////////////////////
data = pd.read_csv('student.csv',index_col='name')
print(data)
print(data.hindi.clip(10,200))
print(data.clip(100,200))
# ///////drop_dublicate
A = pd.Series([1,1,22,3,4,5,6,11,22,1,2,3,1])
print(A)
B = A.drop_duplicates()
print('Drop all dublicate \n',B)
print(A.dropna())
# ///////////////////////////////////
data = pd.read_csv('student.csv')
A = data['name'].apply(lambda x: str(x).split())
print(A)