# num = [1,2,3,4,5]
# num1 = [3,4,5,6,8,9,0,2]
# total =[] 
# for i in num:
#     if i in num1:
#         if i not in total:
#             total.append(i)

# print(total)
# ////////////////////////////////////
# L = ['ankit is a good ','boy but not very goos','a b c d e f']
# new = ' '
# result = []
# for i in L:
#     result.extend(i.split(new))

# print(result)
# //////////////////////////////////////////////
# L = ['ankitIS a good ', 'boyBUT not veryID goosA', 'a b c d e f']

# for i in L:
#     temp = [[]]
#     for char in i:
#         if char.isupper():
#             temp.append([])
#         temp[-1].append(char)

#     for item in temp:
#         print("".join(item))
#     print("------")
# L1 = [1, 2, 3, 4, 5]
# L2 = [6, 7, 3, 1, 7, 9]

# union = []

# for i in L1:
#     if i not in union:
#         union.append(i)

# for j in L2:
#     if j not in union:
#         union.append(j)

# print(union)
# ///////////////////////////////////
# L1 = [1, 2, 3, 4, 5]
# L2 = [6, 7, 3, 1, 7, 9]
# union = sorted(set(L1) | set(L2))
# print(union)
# /////////////////////////////////
# num = [[1,2,3],[4,5,6],[7,8,9]]
# num2 = []
# for i in num:
#     num2.append(max(i))

# print(num2)
# /////////////////////////////////////////////
# transpode the matrix in list and create new list
# matrix = [
#     [1,2,3,4],
#     [5,6,7,8],
#     [9,4,7,11]
# ]

# transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# print(transpose)
# convert the one day matrix form 
matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,4,7,11]
]
num = []
for i in matrix:
    for item in i:
        num.append(item)

print(num, end=' ')
