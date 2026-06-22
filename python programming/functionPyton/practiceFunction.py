'''# Write a function greet() that prints "Hello, Python Learner!" when called.
def greed():
    print("hello ankit kumar");
greed();   

# Write a function square(num) that returns the square of a given number. Test it with different numbers.
def square(x):
    return x*x;

print(square(4));
print(square(6));
    

def full_name(first , last):
    return f"{first} {last}"

print(full_name("choubey ","jii"));

# Write a function calculate_area(length, width=10) that returns the area of a rectangle. Test it by calling the function with:
# Both length and width
# Only length (use default width)

def calculateArea(length , width = 10):
    return length * width

print(calculateArea(8 , 4));
print(calculateArea(4 , 2));
print(calculateArea(13, 20))

# Write a lambda function that adds two numbers and test it
add = lambda a,b: a+b
print(add(3 , 3))
print(add(13 , 3))

square = lambda x: x*x
list1 = [1,2,3,4,5,6,7,8]

print(list((map(square,list1))))'''

 
# factorial number find thesoluction
'''def factorial(n):
    if n == 0 or n == 1:
        return 1
    return factorial(n - 1) *n
print(factorial(5))

# create a program ang all sum of digit
def sum_of_digit(n):
    if n == 0:
        return 0
    return n %10 + sum_of_digit((n / 10))

print(sum_of_digit(12345))'''

# Import the math module and use it to:

# Find the square root of 144
# Calculate sin(90°) (hint: use math.radians())
'''import math
a = math.sqrt((1444))
b = math.radians(90)
print(a , b)'''

'''import requests
a = requests.get("http://api.instagram.com")
print(a.text)'''

# multiply two number
def multiply(a , b):
    return a * b

print(multiply(4 , 6))
print(multiply(4 ,4))

# fibonachi number


    