A = int(input("enter the nuber: "))
B = int(input("enter the number: "))
for i in range(A ,B+1):
    for j in range(2 , i):
        if i % j == 0:
            break
        else:
            print(i)