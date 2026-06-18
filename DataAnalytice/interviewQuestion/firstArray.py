# # maximum sum of number
# M =[-2,-5,-13,-14,-22,-9]
# D = {}
# for i in range(0,len(M)):
#     subrarry = []
#     for j in range(i,len(M)):
#         subrarry.append(M[j])
#         A=D[sum(subrarry)] = subrarry
        
# maxValue = max(D.keys())

# for i in D:
#  if i == maxValue:
#     print(D[i])
        
# Maximum sum subarray

L = [-2, 4, 7, -1, 6, -11, 14, 3, -1, -6]
d = {}

for i in range(len(L)):
    subarray = []
    for j in range(i, len(L)):
        subarray.append(L[j])
        d[sum(subarray)] = subarray

max_val = max(d.keys())

for i in d:
    if i == max_val:
         
        print("Maximum Subarray:", d[i],i)

# method number two

    