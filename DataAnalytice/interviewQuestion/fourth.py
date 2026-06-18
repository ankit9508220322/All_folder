# find the intersection 2 array
A = [1,2,3,4,5,8]
B = [43,6,7,8,1]
for i in A:
    if i in B:
        print(i)
# //////////////////////////////////////////
a = [1,2,3,4,5,8]
b = [43,6,7,8,1]
print(list(set(a) & set(b)))
# //////////////////////////////////////
a = [1,2,3,4,5,8]
b = [43,6,7,8,1]

result = set(a).intersection(set(b))

print(list(result))

