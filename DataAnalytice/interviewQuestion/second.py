# find the element witch left side small/right side larg in array
# L = [3,1,2,5,8,7,9]
# for i in range(1,len(L)-1):
#     flag = True
#     for j in range(0,i):
#         if L[j] > L[i]:
#             flag = False
    
#     for k in range(i + 1,len(L)):
#         if L[k] < L[i]:
#             flag = False
#     if flag:
#         print(L[i])
# //////////////////////////////////
# method number 2
L = [3,1,2,5,8,7,9]
max_arr = []
max_val = L[0]

min_arr = []
min_value = L[-1]

# left max
for i in L:
    if i > max_val:
        max_val = i
    max_arr.append(max_val)

# right min
for i in range(len(L)-1,-1,-1):
    if L[i] < min_value:
        min_value = L[i]
    min_arr.insert(0, min_value)

# final check
for i in range(1, len(L)-1):
    if max_arr[i-1] < L[i] < min_arr[i+1]:
        print(L[i])


# L = [3,1,2,5,8,7,9]
# for i in range(1,len(L)-1):
#     if max(L[:i]) < L[i] < min(L[i+1:]):
#         print(L[i])
        
# L = [3,1,2,5,8,7,9]
# print(L[1])
# print(L[-1])