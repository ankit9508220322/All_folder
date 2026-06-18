# f  = open('fires_file','w')
# f.write("jai ram ji ki \nhar har mahadev")
# f.close()
# ////////////////////////////////////////
# write the multiple file in 
# f = open('second_file','w')
# f.write('i am ankit kumar chaubey')
# f.write('\nvikash kumar chaubey')
# f.close()
# //////////////////////////////
# if the file first is alreday in prsent
# f = open('second_file','w')
# f.write('Ajit kumar chaubey')
# f.close()
# /////////////////////////////////////////
# Add the anothe r word in python 
# f = open("second_file",'a')
# f.write('\nmy god is bajarang bali')
# f.close()
# ///////////////////////////////////////
# write the user long text in file multiple word
# L = ['Positive points include personal\n strengths like empathy,\n reliability, and adaptability, alongside cognitive seggrowth mindset']
# f = open('fiest_file','w')
# f.writelines(L)
# f.close()
# /////////////////////////////////////
# f = open('second_file','r')
# A=f.read()
# print(A)
# f.close()
# /////////////////////////////////
# how read number of chareacter
# f = open('second_file','r')
# A=f.read(10)
# print(A)
# f.close()
# /////////////////////////////////////
# f = open('second_file','r')
# print(f.readable(),end='')
# A=f.readline(1)
# print(A)
# f.close()
# /////////////////////////////////////// with method in write
# with open('third_file','w') as f:
#     f.write('jai ram ji ki')
# //////////////////////////////////////////////
# with open('third_file','r') as data:
#     print(data.read())
# ////////////////////////////////////////////////
# # moveing withine a file 10 charcter
# with open('second_file','r')as data2:
    # print(data2.read(15))
# ////////////////////////////
# long = ['jai ram ji' for i in range(100)]
# with open('third_file','w') as pd:
#     print(pd.writelines(long))
# with open('third_file','r')as pd:
#     line = 10
#     while len(pd.read(line))> 0:
#         print(pd.read(line),end = ' *** ')
#         pd.read(line)
# # /////////////////////////////////////////////
# with open('fiest_file','r')as f:
#     print(f.read(5))
#     print(f.tell())#current position  before current print 10 line
#     print(f.seek(0))#this again starting point 0 again  start  0 index line
# //////////////////////////////////////////////////////////////
# d = {
#     'name':'ankit',
#     'age':22,
#     'village':'andour',
#     'policstation':'kochas'
# }
# with open('pick.jpg','w')as f:
#     f.write(str(d))
# with open('pick.jpg','r')as f:
#     print(f.read())
# ////////////////////////////////////////////////////
# serilazation cheapter
# import json
# L = [2,3,4,5,6,7,8]
# with open('demo.json','w')as f:
#     json.dump(L, f)
# ///////////////////////////////////////////////////
# import json
# d = {
#     'name':'ankit',
#     'age':22,
#     'village':'andour',
#     'policstation':'kochas'
# }
# with open('demo.json','w')as f:
#     json.dump(d,f,indent=4)
# with open('demo.json','r')as f:
#     print(json.load(f))
# /////////////////////////////////////////////////
import pickle
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print('my name is',self.name,'and age is',self.age,'your old')
p = Person('ankit',22)

with open('pickel.pic','wb')as f:
    pickle.dump(p,f)
    # ////////////////////////////////
with open('pickel.pic','rb')as f:
    p = pickle.load(f)
    p.display()