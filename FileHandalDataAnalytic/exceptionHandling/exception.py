# Exception
# TypeError
# ValueError
# NameError
# IndexError
# KeyError
# AttributeError
# FileNotFoundError
# ImportError
# ModuleNotFoundError
# ZeroDivisionError
# SyntaxError
# IndentationError
# RuntimeError
# RecursionError
# with open('semple.txt','w')as f:
#     f.write('helo my class')
# # ---- First try block (file handling) ----
# try:
#     with open('semple1.txt', 'r') as a:
#         print(a.read())

# except FileNotFoundError:
#     print("file does not found")

# except NameError:
#     a = 9
#     b = 3
#     c = a + b
#     print(c)

# print("not value find")


# # ---- Second try block (syntax checking) ----
# try:
#     eval("x === 5")

# except SyntaxError:
#     print("Syntax mistake")

# except FileNotFoundError:
#     print('file not met me')

# except ZeroDivisionError:
#     print("cant divided by number")

# except NameError:
#     print('name not found')

# except Exception:
    
#     print('not mina')
# else:
#     print("else condition")
# //////////////////////////////////////////
# try:
#     f = open('semple.txt','r')
# except FileExistsError:
#     print('fine name frror: ')
# except Exception:
#     print('check code: ')
# else:
#     print(f.read())
# /////////////////////////////////////////////
# try:
#     f = open('semple.txt','r')
# except FileExistsError:
#     print('fine name frror: ')
# except Exception:
#     print('check code: ')
# else:
#     print(f.read())
# finally:
#     print('congrachulation ')
# /////////////////////////////////////
# raise error
# class Bank:
#     def __init__(self,balance):
#         self.balance = balance
    
#     def withrow(self,amount):
#         if amount < 0:
#             raise Exception("not negative balance")
#         if self.balance < amount:
#             raise Exception("money not found ")
#         self.balance  = self.balance - amount
# obj = Bank(100000)
# try:
#   obj.withrow(920000)
# except Exception as e:
#     print(e)
# else:
#     print(obj.balance)
# ///////////////////////////////////
class SecurityError(Exception):
    def __init__(self,message):
        print(message)
    def logout(self):
        print('log out all device: ')
    
class Google:
    def __init__(self,name,email,pasword,device):
        self.name = name
        self.email = email
        self.pasword = pasword
        self.device = device
        
    def logine(self,name,email,pasword,device):
        if device != self.device:
            raise SecurityError
        if email == self.email and pasword == self.pasword:
            print('welcome')
        
        
obj1 = Google('ankit','ankit@1234','1234','android')
try:
  obj1.logine('ankit','ankit@1234','1234','android1')
except SecurityError as e:
    e.logout()
else:
    print(obj1.name)
finally:
    print("data is sucess full ")
        