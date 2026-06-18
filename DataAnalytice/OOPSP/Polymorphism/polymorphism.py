# method overriding
# method overloading
# ek name ke 2 method hai but dono ka behaviour alag alag hai
# method overloading is concept where inside your class you have ->
# multiple function  width the same name but output is diffrence based on  the input
class shape:
    def area(self,radious):
        return 3.14*radious*radious
    
    def area(self,l,b):
        return l*b
    
s = shape()
# s.area(3)
A=s.area(6,7)
print(A)
    
# operators overloading