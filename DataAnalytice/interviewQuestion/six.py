# find the in max in array
A = [11,23,1,4,54,22,10]
max_val = A[0]
for i in A:
    if i > max_val:
        max_val = i
print(max_val)
# /////////////////////////// min_value
max_val = A[0]
for i in A:
    if i < max_val:
        max_val = i
print(max_val)
# ///////////////////////// sort method
print(min(A))
print(max(A))