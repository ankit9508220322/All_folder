# # Super keyword
# class phone:
#     def __init__(self,price,brand,camera):
#         self.price = price
#         self.brande = brand
#         self.camera = camera
#     def buy(self):
#         print("buyng the phone")

# class smarphone(phone):
#     def buy(self):
#         print("buying the smart phone: ")
#         # syntex to call parent ka buy method
#         super().buy()       
# s = smarphone(200,'apple',200)
# s.buy()

# //////////////////////////////////////////
# super constructor
class phone1:
    def __init__(self,price,brand,camera):
        print('inside the phone constructor: ')
        self.price = price
        self.brande = brand
        self.camera = camera
    def buy(self):
        print("buyng the phone")

class smarphone(phone1):
    def __init__(self, price, brand, camera,os,ram):
        print("inside the smart phone: ")
        super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram
        print("inside smartphone constructor: ")
  
s1 = smarphone(200,'apple',200,'android',6)
print(s1.os)
print(s1.ram)
