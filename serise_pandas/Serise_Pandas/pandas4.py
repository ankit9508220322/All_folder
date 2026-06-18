import pandas as pd
# seridse maths count dont messing value
data = pd.read_csv('pandas_practice.csv')
A = data.age.count()
print(A)
print('All age of key value of sum',data.age.sum())
# ///////////////////////////////////////
# min median mode std var
data = pd.read_csv('pandas_practice.csv')
print('mean value \n',data.age.mean())
print("mediam value \n ",data.age.mean())
print("mode value sadbe jada bar jo aaya hai\n ",data.age.mode())
print("sabse jada age \n",data.age.mode())
print("max number \n",data.age.max())
print("min number \n",data.age.min())
print("describe number provide summery mathimatcal  \n",data.age.describe())

# ////////////////////////////////////////////////
data = pd.read_csv('Book3.csv')
A = data.CODE.describe()
print(A)
