import numpy as np
# # # attributes in 5 
# number of diminction (ndim)
A1 = np.arange(10)
print("\n value is ndid\n",A1.ndim)
print("\n value is shape\n",A1.shape)
print("\nvale is size \n",A1.size) #array size 
print("\n value is itemsize\n",A1.itemsize) #show memory size
print("\nvalue is datatype \n",A1.dtype)  #check data type

# # ////////////////////////////////////////////
# changeing data type   (astype)
A1 = np.arange(10)
print(A1.dtype)
A =A1.astype(np.int32) #set data type
print(A)
print(A.dtype)

# # ////////////////////////////////////// time 51
# Array opreations
A1 = np.arange(12).reshape(3,4)
A2 = np.arange(12,24).reshape(3,4)
print('main array\n',A1)
print('line one\n',A1*2) # scaler opreations
print('line two\n',A1**2)
print('line three\n',A1+2)
print('line four\n',A1-2)
print('line five\n',A1/2)
print('six method\n',A1==5)
print('seven method\n',A1>2)
print('jai ram \n',A1<=2)
print('eight\n',A1>=2)

# # # /////////////////////////////////////////
A1 = np.arange(12).reshape(3,4)
A2 = np.arange(12,24).reshape(3,4)
print('add the two array\n',A1 + A2) # vector operation

# # ///////////////////////////////////////////
# min /max /sub/prod
# array function
B1 = np.random.random((3,5))
B1 = np.round(B1 * 100)
print(B1)
print(np.max(B1))
print(np.min(B1))
print(np.sum(B1))
print(np.prod(B1))
#  any row maxvalue 0->column and 1->rows
print(np.max(B1,axis=1))
print(np.max(B1,axis=0))
print(np.sum(B1,axis=0))


# //////////////////////////////////////////
B1 = np.random.random((3,5))
B1 = np.round(B1 * 100)
print(np.mean(B1,axis=1))
print(np.median(B1,axis=1))
print(np.median(B1))
print(np.std(B1,axis=1))
print(np.var(B1,axis=1))
print(np.sin(B1))


# # # //////////////////////////////////
# # # Dought product 
B1 = np.arange(12).reshape(3,4)
B2 = np.arange(12,24).reshape(4,3)
print(np.dot(B1,B2))
print(np.log(B1))
print(np.exp(B2))



