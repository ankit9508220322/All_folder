# empty
print([])
# 1D
print([1,2,3,4,5,5])
# 2D  this is hetrogenous 
print([2,3,4,[2,3,4,5]]) 
#3D
print([1,2,3,[3,4,5,[4,5,6]]])
# hetrogenous
print([1,'ankit',2,3,4+3j,"mohit"])

# ///////////////////////////////////////////////
L = [2,3,4,5,6,7,9]
print(L)
A = [1,2,3,[2,3]]
print(A[3][1])
# ///////////////////////////////////////////////
# adding item in list
# append
# extend
# insert
# ///////////////////////
# adding a one value use the append in last index 
A = [1,2,3,4,4]
A.append('ankiy')
print(A)
# Extend add multiple value 
B = [2,3,4,5]
B.extend([0,9,8,7])
print(B)
# one by one show charecter
B.extend('ankit kumar')
print(B)
# insert
B1 = [2,3,4,5]
B1.insert(2,3000)
print(B1)


# /////////////////////////////////////////
# deleting the list method
# del , remove , pop , clear
C = [2,3,4,5]
del C[2]
del C[1:3]
print(C)
# //////////////////////// Remove
A = [1,2,3,7,8,4,6,9,00,2]
A.remove(00)
print(A)
# ///////////////////////// Pop
# pop in last number delet you can pass the index number pop value pop(0)
A1= [1,2,3,7,8,4,6,9,00,2]
A1.pop()
print(A1)
# /////////////////////////
A2 = [1,2,3,7,8,4,6,9,00,2]
A2.clear()
print(A2)
# //////////////////////////opreations apply 
num1 = [2,3,4,5]
num2 = [7,8,9,0]
print(num1+ num2)
print(num1 * 3)
print(5 in num1)
# /////////////////////////// Loop printing
num = [1,2,3,4,5,6,7]
for i in num:
    print(i)

mom = [2,3,4,5,6,[44,55,66]]
for i in mom:
    print(i)
# ////////////////////////////////////////
# len min max sorted
number = [22,3,44,5,11,61,18,28,2,3]
print(min(number))
print(max(number))
print(len(number))
print(sorted(number))
print(number.count(3))
print(number.index(22))
# ////////////////////////////////////
L = [22,3,44,5,11,61,18,28,2,3]
L.reverse()
print(L)
L.sort()
print(L)
# ////////////////////////////////////
M = [11,22,33,44,2,3,4,5,6,7]
print(sorted(M))
print(id(M))
m = M.copy()
print(m)
# ////////////////////////////////////
S = []
for i in range(1,20):
    S.append(i)
print(S)

# /////////////////////////////
v =[i for i in range(1,12)]
print(v)

# /////////////////////////
x = [1,2,3,4,5]
sq = [i**2 for i in x]
print(sq)

    # 