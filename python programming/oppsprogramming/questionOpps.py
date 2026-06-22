# class Account:
#     def __init__(self, bal, account):
#         self.balance = bal
#         self.account = account

#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs.", amount, "was debited")
#         print("Total balance =", self.get_balance())

#     def credit(self, amount):
#         self.balance += amount
#         print("Rs.", amount, "was credited")
#         print("Total balance =", self.get_balance())

#     def get_balance(self):
#         return self.balance


# # Create an account object
# acc1 = Account(10000, 123456)

# # Perform operations
# acc1.debit(1000)
# acc1.credit(500)

# question Create a class Car with a method drive() that prints "Car is moving"
# Create an object of Car and call drive().

class Car:
    def drive(self):
        print("car is drive");
# create object
car1 = Car()
car1.drive()

class Person:
    def __init__(self,name , age):
        self.name = name
        self.age = age
        pass
p1 = Person("ankit ", 22)
print(p1.name, p1.age)