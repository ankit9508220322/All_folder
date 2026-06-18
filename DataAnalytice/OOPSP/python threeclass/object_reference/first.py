# class Person:
#     def __init__(self):
#         self.Name = "ankit"
#         self.gender = "male"

# p=Person()
# p.Name
# print(p)
# //////////////////////////////////////////
# pass by reference
# class Person:
#     def __init__(self,name , gender):
#         self.name = name
#         self.gender = gender
        
# # out side the class create function
# def greet(Person):
#     print("jai ram ",Person.name,'and i am a',Person.gender)
# p = Person('ankit','male')
# greet(p)
# ////////////////////////////////////////////////////////////
# collection of object
# list of object
class person:
    def __init__(self,name, gender):
        self.name = name
        self.gender =gender
p1 = person('ankit','male')
p2 = person('neha','mefal')
p3 = person('bikash','male')
la = [p1,p2,p3]

for i in la:
    print(i.name,i.gender)

# ////////////////////////////////////////////////////
# static variable and instance variable
# instance (of object  variables) variables is every object variable diffrent 
# instance variable of object
# variable ke aage (self hoga to instance hoga)

# static variable of class of variable
# static variable har object ke liye sem hota hai and static variable of class 
# agar name ke aage class ka name hoga to static goga

