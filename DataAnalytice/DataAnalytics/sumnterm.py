number = int(input("enter the number: "))
sum = 0

while number > 0:
    last = number % 10
    sum = sum + last
    number = number // 10
print("Sum of digits:", sum)
