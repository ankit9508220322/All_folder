# acces the tuple 
# tuple is not changble inmuitable 
t1 = ('ankit','mohit',True,22,11)
print(t1)
print(t1[1])
print(t1[-2])
print(t1[1:2])
print(t1[::-1])
# single iter tuple declear
print('ankit',)
# how to add item this tuple not Aloow
# deleting the item tuple
t2 = ('ankit','mohit',True,22,11)
print(t2)
del t2
print(t2)
# //////////////////////////////////////////////
# operation in tuple
t1 = (1,2,3,4,5,6,7,8)
t2 = (6,5,4,3,2,1)
# Addition 
print(t1 + t2)
# multiplication
print(t1*3)
# membership operation
11 in t1
# looping in tuple
for i in t1:
    print(i)
# //////////////////////////////////////
# function in tuple

t1 = (9,4,22,0,2,3,4,5,6,7,)
print(len(t1))
print(sum(t1))
print(min(t1))
print(max(t1))
print(sorted(t1))
print(t1.count(6))
print(t1.index(3))
# ////////////////////////
a,b,*other = (11,2,3,245,5,6,7,8)
print(a,b)
print(other)
# /////////////////////////
# ziping tuple
t1 = (1,2,3,4,5,6,7,8)
t2 = (6,5,4,3,2,1)
z = list(zip(t1, t2))
print(z)
t = tuple(zip(t1, t2))
# print(t)
