# find the duplicates value in array
a = [1,2,3,4,5,3,6,1,7,6]
d = {}
for i in a:
    if i in d:
        d[i] = d[i]+1
    else:
        d[i] = 1
for i in d:
    if d[i] > 1:
        print(i)