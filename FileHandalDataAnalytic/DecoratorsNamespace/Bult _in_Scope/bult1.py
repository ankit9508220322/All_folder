# built in function show all buil-in-name
# import builtins
# print(dir(builtins))
# Enclosing scope
# def outer():
#     def inner():
#         print('innrer function: ')
#     inner()
#     print('outer scope : ')
# outer()
# print('main program: ')
# ///////////////////////////////////
def outer():
 a = 8
 def inner():
    print(a)
 inner()
 print('outer scope ')
a = 1
outer()
print('main scope : ')
