# operators in python
'''+ (Addition),
- (Subtraction),
* (Multiplication),
/ (Division),
% (Modulus),
** (Exponentiation),
// (Floor Division).
'''
a = 20 
b = 20
print("a + b =",a +b)
print("a - b: ",a -b)
print("a * b: ",a * b)
print("a / b: ", a / b)
print("a % b: ", a % b)

a = int(input("enter the 1 number"))
b = int(input("enter the 2 number: "))
print("total number: ", a +b)
 
a = 20
b = 24
print("tottal: ",a +b)

print(10 ** 2)  # Output: 100
a =int(input("enter the length1: "))
b =int(input("enter the length2: "))
c =int(input("enter the length3: "))
d =int(input("enter the length4: "))
total = a + b + c + d / 2
print(total)


# start the comparison operators

# Comparison Operators
# == (Equal)
# != (Not Equal)
# > (Greater Than)
# < (Less Than)
# >= (Greater Than or Equal)
# or Equal),
# <= (Less Than
# or Equal).

print(10 > 5)   # Output: True
print(10 == 5) # Output: False
print(20 != 10)
print(100 != 50 & 40== 40)
print("next line:")
print(True and False)  # Output: False
print(True or False)   # Output: True
print(not True)        # Output: False

# Assignment Operators
'''=, +=, -=, *=, /=, %=, **=, //=.'''
x = 10
x += 5  # Equivalent to x = x + 5
print(x)  # Output: 15
# Membership Operators:
'''in, not in'''

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits) # Output: True
# Identity Operators:

'''is, is not'''
x = 10
y = 10
print(x is y)  # Output: True

a = int(input("enter the number : "));
b = int(input("enter second number: "));

print("a   +   b: ", a + b);
print("a   /   b: ", a / b);
print("a   -   b: ", a - b);
print("a   *   b: ", a * b);
print("a   %   b: ", a % b);
print("a   //   b:", a // b);
print("a   **   b:", a ** b);
print("a   ==   b:", a == b);
print("a   !=   b:", a != b);
print("a   >   b:", a > b);
print("a   <   b:", a < b);
print("a   >=   b:", a >= b);
print("a   <=   b:", a <= b);

# write a program input user and square number
num = int(input("enter the number: "));
# num2 = num ** 2;
# num2 = num * num;
print("square of the number: ",num **2)