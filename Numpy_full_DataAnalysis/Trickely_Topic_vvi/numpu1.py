import numpy as np 
a = np.random.randint(1,100,15) #generate the number of 15
# # sort all data
print(a)
B = np.sort(a)
print(B)
# print(B)[::-1]
# ////////////////////////////////////
b = np.random.randint(1,100,24).reshape(6,4)
print(b)
c = np.sort(b,axis=0)
print('column by change\n',c)
# ///////////////////////////////////////
a = np.random.randint(1,100,15)
b = np.append(a,2000)
print(b)
# ////////////////////////////////////
b = np.random.randint(1,100,24).reshape(6,4)
print(b)
a1 = np.append(b,np.ones((b.shape[0],1)),axis=1)
print(a1)

# ////////////////////////////////////////////////
c = np.array([1,2,3,4,3,2,1,5,6,7,5,6,8])
print(np.unique(c))

# ////////////////////////////////////////////
c = np.array([1,2,3,4,3,2,1,5,6,7,5,6,8])
print(np.where(c >5)) #where function show the index method number of array
d = np.where(c % 2 == 0,0,True)
print('all even number\n',d)

# //////////////////////////////////////
# np.argmax (show the max number index show)
c = np.array([1,2,3,4,3,2,1,5,6,7,5,6,8])
a = np.argmax(c)
print(a)
print(np.argmin(c))

# /////////////////////////////
# np.comsuml
c = np.array([1,2,3,4,3,2,1,5,6,7,5,6,8])
print(np.cumsum(c))
# //////////////////////////////////
a = np.array([10,20,30,44,23,61,48,59,99,66,44,22,11])
b = np.percentile(a,70)
print(np.median(a))
print(b)

# ////////////////////////////////////
a = np.array([10,20,30,44,23,61,48,59,99,66,44,22,11])
b =np.histogram(a,bins=[0,10,20,30,40,50,60,70,80,90,100])
print(b)

# ////////////////////////////////////////////
# np.isin(search the multiple array in work )
c = np.array([1,2,3,4,3,2,1,5,6,7,5,6,8])
item1 = [4,6,2,1,66]
b = c[np.isin(c,item1)]
print(b)
# ////////////////////////////////////////
# np.flip() array ko revers karega
c = np.array([1,2,3,4,3,2,1,5,6,7,5,6,8])
print(np.flip(c))
# //////////////////////////////////
# np.put() change the value in array
c = np.array([1,2,3,4,3,2,1,0,5,6,7,5,6,8])
b = np.put(c,[0,33],[6,555])
print(b)
# //////////////////////////////////////
# np.delete(c,index number) delet the sub array 
c = np.array([1,2,3,4,390,2,1,5,6,7,5,6,8])
A = np.delete(c,4)
print(A)
#  //////////////////////////////////////// Function
m = np.array([1,2,3,4,5,6])
n = np.array([7,6,5,4,3,2])
total = np.union1d(m,n)
print(total)
print(np.intersect1d(m,n))
print(np.setdiff1d(m,n))  #m me ho but n me nahi ho
print(np.setxor1d(m,n))

# /////////////////////////////////////



