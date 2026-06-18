# # this is main part of decorators in python
# def modify(func,num): #this is decorater
#     return func(num)

# def square(num):# take in input vlue decorators
#     return num **2
# modify(square , 2)
# ///////////////////////////
# simple example
# def my_decorators(func):
#     def wrapper():
#         print('****************************** ')
#         func()
#         print('*************&&&&&&&&&')
#     return wrapper()
# def hello():
#     print('hello ')
# my_decorators(hello)    
# //////////////////////////////////////////
# def my_decorators(func):
#     def wrapper():
#         print('jairam ji ki ')
#         func()
#         print('jai hanuman ji ki jai ho: ')
#     return wrapper()
# @my_decorators
# def hello():
#     print('hello ')
# hello
# ////////////////////// how much excution time decorators 
import time
def timmer(func):
    def wrapper():
        start = time.time()
        func()
        print('time taken by',func.__name__,time.time()-start,'secs')
    return wrapper()
@timmer
def hello():
    print('hello ram ji ')
    time.sleep(4)

@timmer
def display():
    print('ankit kumar chaubey: ')
    time.sleep(4)
hello # hello function call 
display()
