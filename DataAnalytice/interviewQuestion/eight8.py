# check if arrayis sorted
A = [21,2,54,7,8,9,4,10,31]
flag = False
for i in range(0,len(A)-1):
    if A[i] > A[i+1]:
        flag = False
if flag:
    print("sorted")
else:
    print("not sorted: ")
