import numpy as np
# indexing and silicing
B1 = np.arange(12)
B2 = np.arange(12).reshape(4,3)
B3 = np.arange(8).reshape(2,2,2)
print('value is B3\n',B3)
print(B1)
print("value is b -1 \n",B1[-1])


# /////////////////////////////
B2 = np.arange(12).reshape(4,3)
print(B2)
 # index start 0-row, 1-row , 2-row
print(B2[1,2]) # 1=row index and 2=colum index

# # //////////////////////////////////
B3 = np.arange(8).reshape(2,2,2)
print(B3)
print("lopeing case \n",B3[1,0,1])

# # ////////////////////////////////////////////
# #  silicing
B1 = np.arange(12)
B3 = np.arange(8).reshape(2,2,2)
print('slicing\n',B1)
print('slicing2\n',B1[2:5])

# ///////////////////////////////
B2 = np.arange(12).reshape(4,3)
print("original array\n",B2)
print('this is first row \n',B2[0])
print('this is second row \n',B2[1])
print('this is third row \n',B2[2])
print('this is column \n',B2[:,1]) 

B3 = np.arange(27).reshape(3,3,3)
print(B3)
print(B3[1])
print('dusra hai\n',B3[::2])
print('second row \n',B3[0,1,:])
print('second ka bich vala column \n',B3[1,:,1])
print(B3[2,1:,1:])
print("last\n",B3[::2,0,::2])