num = int(input("enter the number: "))
if(num  > 0):
    print("this number is positive")
elif(num < 0):
  print("number is negative  : ")
else:
    print("number is zero : ")


age = 18
age = int(input("enter the age: "))
if(age >20):
    print("you can vote")
else:
    print("you can no voate: ")
    
a = int(input("enter the number between(1-7): "))
match a:
     case 1:
         print("sunday")
     case 2:
         print("monday")
     case 3:
        print("tuesday")
     case 4:
         print("wednesday")
     case 5:
         print("thursday")
     case 6:
         print("friday")
     case 7:
         print("saturday")
     case _:
         print("not valid number")
         
num1 = int(input("enter the number: "))
num2 = int(input("enter the number: "))
operation = input("cho0se the operation(+,-,*,/): ")

match operation:
    case'+':
        print(num1 + num2)
    case'-':
        print(num1 - num2)
    case'*':
        print(num1 * num2)
    case '/':
        print(num1 / num2)
    case _:
        print("not involve operation: "+ operation)
        
        
sum = 0
for i in range(1 ,100):
     sum = sum + i
print(sum)

sum = 0
i = 1
while i <= 100:

    sum += i
    i += 1
    print(sum)

# check the correct password 
password = "123qwe"
enter_password = input("enter  password: ")
while (enter_password != password):
    enter_password = input("again enter password  ")
else:
 print("successful")
 
 
# reverse number
num = 12345678
reverse_num = 0
while num != 0:
    reverse_num = reverse_num * 10 + num % 10
    num //= 10
print("reverse number is: ", reverse_num)

# # factorial of number
num = int(input("enter the number: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print("factorial is: ", factorial)

# reverse number
number = 87654321
print(str(number)[::-1]);