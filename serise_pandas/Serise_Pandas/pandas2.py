import pandas as pd
import numpy as np
# read the csv file in 
read1 = pd.read_csv('data-export (1).csv')
print(read1)
# ///////////////////////////////
read1 = pd.read_csv('aaa.csv', index_col='sr')
read1 = read1.squeeze()
print(read1)

# //////////////////////////////////////////////////
df = pd.read_csv('aaa.csv', sep='\t', index_col='sr')
print(df)

# ///////////////////////////////
data = pd.read_csv('Book3.csv',index_col='city')
print(data)

# ///////////////////////////////////
# data2 = pd.read_csv('pandas_practice.csv')
# print(data2)

# //////////////////////////////
data2 = pd.read_csv('pandas_practice.csv')
print("print top 4 sailary\n",data2.head())
print("chose the choice \n",data2.age.head(3))
# /////////////////// tell button 5  valu show
# data2 = pd.read_csv('pandas_practice.csv')
# print(data2.tail())
# print(data2.tail(3))

# ////////////////////// use sample randome find one value 
data2 = pd.read_csv('pandas_practice.csv')
print(data2.sample())
print(data2.sample(4))
c = data2.age.sample(5)
print('value c\n',c)
# /////////////////////////////////
# data2 = pd.read_csv('pandas_practice.csv')
# c = data2[['name', 'age']].sample(5).set_index('name')
# print(c)
