import numpy as np
# # 1️⃣ Null vector of size 10 but 5th value = 1
a = np.zeros(10)
print(a)

# Random array (a,b) and average
a = int(input("Enter rows: "))
b = int(input("Enter cols: "))
arr = np.random.rand(a,b)
print(arr)
print("Average:", np.mean(arr))
# method two
a1 = np.random.random(10).reshape(5,2)
print(a1)
print('avreage\n',np.mean(a1))

# //////////////////////////
# Q-3`Write a function to create a 2d array with 1 on the border and 0 inside. Take 2-D array 
# shape as (a,b) as parameter to function.
def border_arr(a,b):
    arr = np.zeros((a,b))
    arr[0,:] = 1
    arr[-1,:] = 1
    arr[:,0] = 1
    arr[:,-1] = 1
    return arr
print(border_arr(4,4))

# //////////////////////////////q4
# Q-4` Create a vector of size 10 with values ranging from 0 to 1, both excluded.
a = np.linspace(0,1,12)[1:-1]
print(a)
# //////////////////////////////
# `Q-5` Can you create a identity mattrix of shape (3,4). If yes write code for it.
a = np.ones(12).reshape((3,4))
print(a)

b = np.eye(3,4)
print(b)
# //////////////////////////
a = np.arange(5)
matrix = np.tile(a,(5,1))
print(matrix)
# /////////////////////
index = np.unravel_index(99,(6,7,8))
print(index)
# //////////Reverse numpy float array
arr = input().split()
arr = np.array(arr,float)
print(arr[::-1])
# /////////////////////////////////
def count_elements(arr):
    print("elements_count :",arr.size)

count_elements(np.array([1,2]))