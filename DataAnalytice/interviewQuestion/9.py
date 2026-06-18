
A = [21,2,54,7,8,9,4,10,31]
k = 21
A.sort(reverse=True)
print(A[k-1])

# ///////////////////////////////////
a = [5, 2, 9, 1, 5, 6]

n = len(a)

for i in range(n):
    for j in range(0, n - i - 1):
        if a[j] > a[j + 1]:
            # Swap
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp

print("Sorted list:", a)
# /////////////////////////////////////////////
# sorting array
a = [5, 2, 9, 1, 5, 6]

n = len(a)

for i in range(n):
    for j in range(0, n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

print("Sorted list:", a)
# /////////////////////////////////////////////////////
# linear search
a = [5, 2, 9, 1, 5, 6]
key = 9

found = False

for i in range(len(a)):
    if a[i] == key:
        print("Element found at index:", i)
        found = True
        break

if not found:
    print("Element not found")
# //////////////////////////////////////////////binary search
a = [1, 2, 5, 5, 6, 9]  
key = 5

low = 0
high = len(a) - 1

while low <= high:
    mid = (low + high) // 2
    
    if a[mid] == key:
        print("Element found at index:", mid)
        break
    elif a[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Element not found")
