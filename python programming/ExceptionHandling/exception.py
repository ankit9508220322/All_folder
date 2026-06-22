# while True:
#     try:
#       a = int(input("enter the number "))
#       b = int(input("enter the number "))
#       print(f"total number {a / b}")
#     except ValueError:
#         print("invalid input please enter a  bad ")
#     except ZeroDivisionError:
#        print(("hey dont divide by 0  "))
#     except Exception as e:
#         print("something went worng", e)
   

try:
    x = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    print("Cannot divide by zero!")
    
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input! Please enter a number.")

# Alternative using a tuple:
try:
  num = int(input("Enter a number: "))
  result = 10 / num
except (ZeroDivisionError, ValueError) as e:
  print(f"An error occurred: {e}")
try:
    num = int(input("enter the number "));
except ValueError:
    print("thanque ");
except IndexError:
    print("hfhfhfhfhfh");
    