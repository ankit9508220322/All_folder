import numpy as np
# Advance indexing
# Fancy indexing
a = np.arange(24).reshape(6,4)
# print(a)
find = a[[0,2,5]]
print('row prit 0,2,5\n',find)
# ///////////////////////////////////////
a = np.arange(24).reshape(6,4)
find2 = a[:,[0,2]]
print('find column\n',find2)

# ///////////////////////////////////////////
# boolean indexing
num = np.random.randint(1,100,24).reshape(6,4)
print(num)

a= num > 50
print(a)
# show number 
b = num[num > 50]
print(b)
# ////////////////
c = num[num % 4 == 0]
print(c)
total = num[(num > 40)and (num % 2 == 0)]
print(total)
# find the number not devide by 7
total1 = num[a % 7 == 0]
print(total1)

# ///////////////////////////////////////////////
# Broadcasting Method   same shap
A = np.arange(6).reshape(2,3)
b = np.arange(6,12).reshape(2,3)
print(A + b)
# /////////////////////////////////
# Diffrent shap
A = np.arange(6).reshape(2,3)
b = np.arange(3).reshape(1,3)
print(A + b)

# //////////////////////////////
A = np.arange(3).reshape(1,3)
b = np.arange(3).reshape(3,1)
print(A + b)

# //////////
A = np.arange(3).reshape(1,3)
b = np.arange(4).reshape(4,1)
print(A + b)
# /////////// not work it will 
A = np.arange(12).reshape(3,4)
b = np.arange(12).reshape(4,3)
print(A + b)

# /////////////////////////////// not work

A = np.arange(16).reshape(4,4)
b = np.arange(4).reshape(2,2)
print(A + b)
