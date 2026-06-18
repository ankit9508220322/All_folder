import numpy as np

# iterating
B1 = np.arange(12)
for i in B1:
    if i == 6:
        break
    print(i)
# /////////////////////////
B2 = np.arange(12)
for i in B2:
    if i == 6:
        continue
    print("continue: ",i)
    
# /////////////////////////////////////
B2 = np.arange(12).reshape(4,3)
for i in np.nditer(B2):
    print(i)
num = np.transpose(B2) #transpose method
print(num)
print("method two\n" ,B2.T)
# convert 2D arrayto one Di array (ravel)
print(B2.ravel())

# ////////////////////////////////////
B3 = np.arange(27).reshape(3,3,3)
for i in np.nditer(B3):
    print(i)

# /////////////////////////////////////////
# STACKING  horizental
num1 = np.arange(12).reshape(3,4)
num2 = np.arange(12,24).reshape(3,4)
Add = np.hstack((num1,num2))
print(Add)

# vertical stacking
print("vertical stacking\n")
Add2 = np.vstack((num1,num2))
print(Add2)

# /////////////////////////////////////////
# breack te array any part (splitting)method (1)horizontal splitting and vertial splitting

num1 = np.arange(12).reshape(3,4)
Add3 = np.hsplit(num1,2)
print(Add3)
# vertial splitting
num2 = np.arange(12,24).reshape(3,4)
Add4 = np.vsplit(num2,3)
print(Add4)