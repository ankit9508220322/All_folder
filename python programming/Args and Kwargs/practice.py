# # Write a decorator timer that calculates how long a function takes to execute. Test it with a function that sums numbers from 1 to 1,000,000.
from time import time
def timer(func):
    def waraper(n):
        t1 = time()
        result = func(n)
        t2 = time()
        print(t2- t1)
        return result
    return waraper

# @timer
# def sum(n):
#     sum = 0
#     for i in range(1, n+1):
#         sum+= i
#     return sum           
        
# a = sum(1000000)
# print(a);

# # getters and setters
class Employee:
    def __init__(self,salary):
        self._salary = salary
    @property
    def salary(self):
       return self._salary
   
    @salary.setter
    def salary(self, value):
        if(value < 0):
            print("please dont send a negative value");
        else:
            self._salary = value
            
e = Employee(10000)
e.salary = -2000
print(e.salary)


# # static class method
# class Result:
#     def __init__(self):
        
#      @classmethod
#      def add( a, b):
#         return a + b
#     @classmethod
#     def description(cls):
#         print("thisis a result class : ");
        
# a = Result
# print(a.add(20 , 10))
# a.description()

# Result.description()
# print(Result.add(10 , 10))

# class Book:
#     def __init__(self, title ,author):
#         self.title = title
#         self.author = author
#     def __str__(self):
#         return f"title : {self.title},as author : {self.author}"
        
#     def __len__(self):
#         return len((self.title))

# b = Book("most spoken class book", "Unknown Author")
# print(len(b));
# print(b);

# b2 = Book("java: ","jjjjj")
# print(b2);
# print(len(b2));


# problem number 4 question handeling method
# class NegativeNumberError(Exception):
#     pass

# try:
#     num = int(input("enter the two  number:"))
#     if num < 0:
#         raise NegativeNumberError("Negative number entered")
#     result = 45/num
#     print(f"result is {result}");
    
# except ValueError:
#     print("inviled the value error")
    
# except ZeroDivisionError:
#     print("zero division by 0");
# except NegativeNumberError as e:
#     print(f"error the number cannot  be negative",e)
    
# Use map() to convert [1, 2, 3, 4, 5] into their cubes.
# number = [1,2,3,4,5]
# cube = lambda x: x**3
# number1 = list(map(cube, number))
# print(number1)

# # Use filter() to get only even numbers from [10, 11, 12, 13, 14].
# a = [10,22,12,14,41]
# f = lambda x: x % 2 ==0
# a1 = filter(f )
# print(list(a1));

# //////////////////////////////////////////////////////
# while(text := input("enter the character ")) != "ankit":
#     print(f"your enterd the text {text}")
# else:
#     print("thnkyou your currect  text")
    # ////////////////////////////////////////////////
# from operator import index


# def sum_all(*arge):
#     total = 0
#     for num in arge:
#         total +=num;
#     return total

# print(sum_all(2,11,33,44));
