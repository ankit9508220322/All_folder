# conditional operators in python else if
age  = 22
if(age > 18):
    print("you can eligiable")
# else if
age = 44
if(age > 28):
    print("pass the drive car")
elif(age > 19):
    print("you can drive car")
else:
    print("you are not eligible")
# //////////////////////////////////////////////
ages = int(input("enter the age: "))

if ages > 32:
    print("you can chalavo")
elif ages >= 18 and ages <= 32:
    print("bye bye bye kariye ga")
else:
    print("not allow")

# check number is odd and even
number = int(input("enter the number: "))
if number % 2 == 0:
    print("this number is even")
else:
    print("this number is odd")
    if(number % 3 == 0):
        print("this number is divide by 3")
    
    else:
        print("this number is not  odd and evendivid by  3")
    # find the number  is greater not greator
    
number1 = int(input("input first number:"))
number2 = int(input("enter second second: "))
if(number1 > number2):
    print("first number is grater")
elif(number2 > number1):
    print("second number is grater")
else:
    print("number is equal")
    

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if(a > b):
    print("First number is greater")
else:
    print("Second number is greater")


# check number is grater on not and equal
a = int(input("enter number: "))
if(a > 0):
    print("number is positive")
elif(a < 0):
    print("number is negative")
else:
    print("number is equal")

a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

if a > b and a > c:
    print("A is largest")
elif b > c:
    print("B is largest")
else:
    print("C is largest")

n = int(input("enter the number: "));
for i in range(1, 11):
    print("table of", n * i);
    
# Factorial of a Number
n = int(input("Enter a number: "))
fact = 1
for i in range(1, n+1):
    fact = fact * i

print("Factorial of is", fact)
