class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def sum(self, p):
        return Point((self.x + p.x ),(self.y + p.y))
    
    def print_point(self):
        print(f"x is {self.x} and y is {self.y}")
    

p1 = Point(11 , 11)
p2 = Point(2 , 2)

p = p1.sum(p2)
p.print_point()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name
    
    def set_age(self, new_age):
        if 0 >= new_age <= 150:
            self.age = new_age
        else:
            print("Invalid age")

# object 1
person1 = Person("ankit", 22)
print("Name:", person1.get_name(),"age",person1.get_age())
# print("Age:", person1.get_age())

# object 2
person2 = Person("vikash", 55)
print("Name:", person2.get_name())
print("Age:", person2.get_age())

# only age print this method in line


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_age(self):
        return self.age
    
    def set_age(self, new_age):
        if 0 <= new_age <= 150:
            self.age = new_age
        else:
            print("Invalid age")

# object 1
person1 = Person("ankit", 22)
print(person1.get_age())

# object 2
person2 = Person("vikash", 55)
print(person2.get_age())