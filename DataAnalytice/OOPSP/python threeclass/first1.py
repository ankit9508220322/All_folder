class User:
    def __init__(self):
        self.name = "ankit"
    
    def Login(self):
        print("login")
# inheritane class 
# childe class 
class Student(User):
    def enroll(self):
        print("enroll into the cource: ")

u = User()
s = Student()

print(s.name)
s.Login()
s.enroll()
