# create a sets
# empty set write cerate conversion
# accessing method not allow
# editing set not Allow
S = {}
print(S)
print(type(S))
# ////////////////// 1D-sets
s1 = {1,2,3,4}
print(s1)
# ///////////////////// 2D-sets
s2 = {13,4,5,6,(2,3,4,5)}
print(s2)
# /////////hetrogeneous & homogeneous
a1 = {1,'ankit',2,3,4,'vikash'}
print(a1)

# using type conversion
a2 =set([1,2,3,4,5,6])
print(a2)
# duplicate not allow
a3 = {1,2,3,2,1,4}
print(a3) 
# ///////////////////
m1 ={1,2,3}
m2 ={1,3,2}
print(m1==m2)  #output is TRUE
# /////////////////////////////////
# Adding Methods
S = {1,2,3,4,5}
A=S.add(3)
print(A)

# Add multiple item one time
B = S.update([2,3,88,99])
print(B)

# all sets is  delet
# del
a4 = {1,2,3,4,5}
print(a4)
del a4
print(a4)
# ////////////////////// CHANGEING LINE
d = {"a": 1, "b": 2, "c": 3}
del d["b"]
print(d)
# ///////////////////////////////
# you tell who too do delet item in sets
# discart
# ese btana hota hai ki kon sa number delet karna hai
s = {1, 2, 3}
s.discard(2)

# remove
lst = [1, 2, 3, 4]
lst.remove(2)
print(lst)
# delet the random number of sets using pop function
# pop
a5 = {1,2,3,4,5}
aa=a5.pop()
print(aa)

# ////////////////////////
d = {"a": 1, "b": 2}
x = d.pop("a")
print(x)
print(d)
# ///////////////
d = {"a": 1, "b": 2, "c": 3}
d.popitem()
print(d)
# clear
d = {"a": 1, "b": 2}
d.clear()
print(d)

# //////////////////////////////////////////
# operation apply
# union me both item ka one one items will be print
A1={1,2,3,4}
B1 ={2,4,6,7,8}
C = A1.union(B1)
C1 = A1 | B1
print(C1)
# intersection  that is print the common items
C2 = A1 & B1
print(C2)
# difference  A1 ka vo item jo A2 me not prsent 
C3 = A1 - B1 
print(C3)
C4 = B1 - A1
print(C4)
# symmetric difference(^)
C5 = A1^B1
print(C5)
# membership
a6 = {1,5,8,3,5}
8 in a6
print(a6)
# itera tion & looping 
for i in A1:
    print(i)
# //////////////////////////////////
# set function
# sum/ min/ max /len /sorted
num = {1,3,6,8,4}
print(max(num))
print(min(num))
print(len(num))
print(sorted(num))
# /////////////////////////////////
# frozenset is just an immutable version of a 
A1 = frozenset([2,5,6,8,9])
print(A1)
# set comprehension
A1={i for i in range(1,11)}
print(A1)
A1={i*2 for i in range(1,11)}
print(A1)
A2={i for i in range(1,11) if i > 5}
print(A2)
A3 = {i for i in range(1, 11) if i % 2 == 0}
print(A3)

# nested disctnory
student = {
    "final":{
    'name': 'ankit kumar',
    'age': 88,
    'school': 'maharishi',
    },
    'marks': {
        'math': 95,
        'science': 88,
        'english': 92
    }
}
for i in student:
    print(f"{i}: {student[i]}")
    print(student.keys())

for keys,value in student.items():
    print(keys,value)