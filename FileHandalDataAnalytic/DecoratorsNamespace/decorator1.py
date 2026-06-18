# namespace
 #local and global
 
# a = 3 #global variable
# def temp():
#     b = 9 #local variable
#     print(b)
# temp()
# print(a)
# /////////////////////////////
#  #local and global edit  the value not chande you can read and write but not change
try:
    a = 13   # global variable
    def temp():
        a += 1
        print(a)
    temp()
except UnboundLocalError:
    print('global value not change')
else:
    print(a)
    
# ////////////////////////////////////////
# change the value use gloable keyword
a = 3 #global variable
def temp():
    global a
    a+=1 #local variable
    print(a)
temp()
print(a)
# ///////////////////////////////
# local and gloable->function paraneter is local
def Temp(z): # Z is a local variable
    print(z)
a = 7
Temp(5)
print(a)