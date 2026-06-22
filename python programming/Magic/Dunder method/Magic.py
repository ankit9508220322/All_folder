class Employee:
    company = "hp"
    def __init__(self,name,salary):
        self.firstName = name
        self.income = salary
        
    # magic method to get attribute
    def __str__(self):
        return f"Employee name if {self.firstName}and salary is {self.income}"
        
    def __repr__(self):
         return f"name {self.firstName}and salary is {self.income}"
        
e = Employee("ankit",2000)
print(e.company,e.firstName)
print(str(e))
print(repr(e))