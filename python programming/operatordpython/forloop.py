n = int(input("text number:"))
for i in range(1, 22):
    print(i * n)


for i in range(100):
    print(i)
 
fruits = ["apple","banana","cherry","kiwi"]
for i in fruits:
  print(i)
  
  
# print the only even number 
sum = 0
for i in range(2 ,100,2):
    print(i)
    sum = sum +i
print("total sum of even number: ", sum)

# Print each letter in a word array from
name = ("ankit", "kumar", "chaubey")
A = []
for item in name:
    A.append(item)
print(A)


# Print each letter in a word
# name1 = "chaubey jii "
# for total in name1:
#     print(total)
    
#print sum all number

sum = 0
for i in range(1, 11):
    sum =sum+ i
    print(i)
    
print("Sum =", sum)

# Print multiplication table of a number
# num = int(input("print the number: "));
# for i in range(1, 11):
#     print("table",num *i);

# Print squares of numbers from 1 to 10
'''for i in range(1, 11):
    print("Square of", i, " = ", i * i)'''

    # print(i**2)

# 8. Count how many numbers are positive
number=[2, -3, 5, -1, 6, 0, 97,77,0,0]
count = 0
for n in number:
    if n > 0:
        count += 1
        print("total number: ", count)

numbers = [2, -3, 5, -1, 6, 0, 9]
count = 0
for n in numbers:
    if n > 0:
        count += 1

print("Total positive numbers =", count)
for i in range(1, 6):
    print(" * "*(i-1))
    
# 10. Reverse a string using for loop
name = "ankit kumar"
reverse = " "
for char in name:
    reverse = char + reverse
print("reverse string: ", reverse)

string="hello hii"
print(string[::-1])

# # Square Star Pattern
for i in range(5):
    for j in range(5):
        print("*", end=" *")
    print()

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()


for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

