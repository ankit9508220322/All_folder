import numpy as np
# working with mathematical formula
a = np.arange(10)
print(np.sum(a))
print(np.sin(a))
# sigmoid

def sigmoid(array):
  return 1/(1 + np.exp(-(array)))

a = np.arange(100 )
print(sigmoid(a))

# /////////////////////////Working with missing value
a = np.array([1,2,3,4,np.nan,6])
print(a)
B = np.isnan(a)
print(B)
C = a[np.isnan(a)] #only show true value
print('only show true value\n',C)
D=a[~np.isnan(a)]
print(D)



