import pandas as pd
import numpy as np
data =pd.read_csv('pandas_practice.csv')
print(data)
#edit the value using  index
A=data.age[2] = 100
print(A)
print(data)
# using label index 
