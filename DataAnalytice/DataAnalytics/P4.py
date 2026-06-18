# check the string palindrome 
A = input("enter the character: ")
flag = True
for i in range(0, len(A)//2):
    if A[i]!=A[len(A)-i-1]:
        flag = False
        print("not a palindrome: ")
        break
if flag:
    print("palindrome: ")