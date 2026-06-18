# create a sets
# empty set write cerate conversion
S = {}
print(S)
print(type(S))
s1 = {1,2,3,4}
print(s1)
# /////////////////////
s2 = {13,4,5,6,(2,3,4,5)}
print(s2)
# ///////////////////
m1 ={1,2,3}
m2 ={1,3,2}
print(m1==m2)
# /////////////////////////////////
S = {1,2,3,4,5}
A=S.add(3)
print(A)
B = S.update([2,3,88,99])
print(B)
# all set delet
# del
d = {"a": 1, "b": 2, "c": 3}
del d["b"]
print(d)
# ///////////////////////////////

# discart
s = {1, 2, 3}
s.discard(2)

# remove
lst = [1, 2, 3, 4]
lst.remove(2)
print(lst)

# pop
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
A1={1,2,3,4}
B1 ={2,4,6,7,8}
C = A1.union(B1)
C1 = A1 | B1
print(C1)
C2 = A1 & B1
print(C2)
C3 = A1 - B1 
print(C3)
C4 = B1 - A1
print(C4)
C5 = A1^B1
print(C5)
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
# set comorehension
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