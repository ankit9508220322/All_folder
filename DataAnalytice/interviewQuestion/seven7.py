# find the accur thime this value
from collections import Counter

a = [1,2,3,4,5,3,2,1,7,6]
b1 = 2

d = Counter(a)

for key, value in d.items():
    if value == b1:
        print(key)
        break

# ////////////////////////////////////////////
a = [1,2,3,4,5,3,2,1,7,6]
b1 = 2
d = {}
for i in a:
    if i in d:
        d[i] = d[i]+1
    else:
        d[i] = 1
for i in d:
    if d[i] ==b1:
        print(i)
        break