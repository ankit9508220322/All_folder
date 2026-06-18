import numpy as np 
A = np.arange(1,11).reshape(2,5)
print(A)

# ////////////////////////////////////////
# np.ones and np.zero method
B = np.ones((4,8))
print('one method\n',B)

# //////////////////////////////////////
# zero
C = np.zeros((2,4))
print('zero method\n',C)

# /////////////////////////////////////
# random number
D = np.random.random((3,10))
print('generate random number\n',D)

# ////////////////////////////////////
# Liniear space(np.linspace)
A = np.linspace(-10,10,10)
print("\nline space: ",A)

A1 = np.linspace(-10,10,10,dtype=int)
print(A1)

# # ///////////////////////////////////
# # identity method
B = np.identity(3)
print(B)