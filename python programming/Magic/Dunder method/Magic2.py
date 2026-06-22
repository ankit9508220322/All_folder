class Book:
    def __init__(self, title , pages):
        self.title = title
        self.pages = pages
    
    def __len__(self):
        return self.pages

b = Book("python book",232)
print(len(b))
print(len(b.title))

class Ankit:
    def __init__(self , name,age):
        self.name  = name
        self.age = age
    def __len__(self):
        return self.age
b = Ankit("Ankit", 25)
print(len(b))
print(b.name)
print(b.age)
# print(sum(tupal))'''