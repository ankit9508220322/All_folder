class Employee:
    def __init__(self,name, age, salary):
        self.firstName = name
        self.age = age 
        self.salary =salary
        
e = Employee("ankit",22,10000)
e.project = 4
print(e.firstName,e.age,e.salary)


# ///////////////////////////////
class Person:
    def __init__(self, name):
        self._name = name  # Convention: underscore (_) denotes a private attribute.

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name 

p = Person("Alice")
print(p.get_name())  # Alice
p.set_name("Bob")
print(p.get_name())  # Bob 


# /////////////////////////////////////////////////
class Person:
    def __init__(self,name):
        self.name = name
    @property
    def name(self):  # Getter
        return self.name
    @name.setter
    def name(self , new_name):
        self._name = new_name

p = Person("chaubey jii")
print(p.name)

p.name = "ankit"
print(p.name)

# //////////////////////////////////////////////
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):  # Getter
        return self._name

    @name.setter
    def name(self, new_name):  # Setter
        self._name = new_name 

    @name.deleter
    def name(self):
        del self._name

p = Person("Alice")
print(p.name)  # Alice
del p.name
print(p.name)  # AttributeError: 'Person' object has no attribute '_name'