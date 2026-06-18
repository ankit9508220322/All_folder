# remove the particular character: 
A = input("enter the character: ")
remov = input("remove the any chracter: ")
result = " "
for i in A:
    if i != remov:
        result = result + i
        
print(result)