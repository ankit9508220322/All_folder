# find the continous subarray with the give sum(give non negative)number 
# L = [1,22,13,7,9,11,10]
# S = 16
# for i in range(0 ,len(L)):
#     subarray = []
#     for j in range(i , len(L)):
#         subarray.append(L[j])
#         if sum(subarray) == S:
#             print(subarray)
# //////////////////////////////////////////////
L = [1,22,13,7,9,11,10]
S = 20
d = {}
curr_sum = 0
for i in range(len(L)):
    curr_sum  = curr_sum +L[i]
    if (curr_sum - S) in d:
        print(d[curr_sum - S]+1,i)
        break
    d[curr_sum] = i
# /////////////////////////////////////////////////
# different method

# L = [1,22,13,7,9,11,10]
# S = 16

# start = 0
# current_sum = 0

# for end in range(len(L)):
#     current_sum += L[end]

#     while current_sum > S and start <= end:
#         current_sum -= L[start]
#         start += 1

#     if current_sum == S:
#         print(L[start:end+1])
# //////////////////////////////////////////////////
# L = [1,22,13,7,9,11,10]
# S = 16
# start = 0
# current_sum = 0
# for end in range(len(L)):
#     current_sum += L[end]
#     # shrink window only one step at a time
#     if current_sum > S:
#         current_sum -= L[start]
#         start += 1

#     if current_sum == S:
#         print(L[start:end+1])
