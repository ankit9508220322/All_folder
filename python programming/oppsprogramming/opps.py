'''studentrecord = ["ankit",10]
student2 = ["ajit",20]
print(f"{student2[0]} is in class{student2}")'''

# using oops creating student records........................................
# class Student:
#     name = "ankit"
#     greed = 10
#     roolno = 234323
#     age = 33
# # object - instance of class 
# A1 = Student()
# print("my name is",A1.name,"and age is ",A1.age,"my grade ", A1.greed,"rool number", A1.roolno)

# # new question start this line............................................
# class Record:
#     def __init__(self, fullname,  fullgreed ,parcentage):
#         self.name = fullname
#         self.greed = fullgreed
#         self.parcentage = parcentage

# # object - instance of class 
# gatedata = Record('ankit kumar chaubey',11,89)
# gatedata2 = Record('ajit kumar chaubey',41,89)
# print(gatedata.name, gatedata.greed ,gatedata.parcentage)

# print(gatedata.name ,gatedata.greed)
# print(gatedata2.__dict__)
# ///////////////////////////////////////////////////////////////////
# # modifi object property

# gatedata.name = 'vikash'
# print(gatedata.name)
# # delet object data
# del gatedata.parcentage
# print(gatedata.__dict__)

# inherent in class

class Animal:
    location = "sasatam australia"
    def __init__(self,name):
        self.NAME = name
    def speak(self):
        print("generick animal speack sound")
        
class Dog(Animal):
    def speak(self):
        print("woof!")


d = Dog("droun")
d .speak()
print(d.location)

# # copy this all line  in nots
# class Animal:  # Pairent class (superclass)
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print("Generic animal sound")

# class Dog(Animal):  # Dog inherits from Animal (Dog is a subclass of Animal)
#     def speak(self):  # We *override* the speak method (more on this later)
#         print("Woof!")

# class Cat(Animal):  # Cat also inherits from Animal
#     def speak(self):
#         print("Meow!")
# class ele(Animal):
#     def speak(self):
#         print("bho bho bho bho")
# # Create objects:
# A = Dog("Rover")
# B = Cat("Fluffy")
# C = ele ("jai ram ji ki")

# # They both have a 'name' attribute (inherited from Animal):
# print(A.name)  # Output: Rover
# print(B.name)  # Output: Fluffy
# print(C.name)

# # They both have a 'speak' method, but it behaves differently:
# A.speak()  # Output: Woof!
# B.speak()  # Output: Meow!
# C.speak()
