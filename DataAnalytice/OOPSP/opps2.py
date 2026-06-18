class Fraction:
    def __init__(self,x,y):
        self.num = x
        self.num2 = y
    
    def __str__(self):
        return '{}/{}'.format(self.num,self.num2)
    
    def __add__(self, other):
       new_num = self.num*other.num2+other.num*self.num2
       new_num2 =self.num2*other.num2
       return '{}/{}'.format(new_num,new_num2)
    
    def __sub__(self, other):
       new_num = self.num*other.num2-other.num*self.num2
       new_num2 =self.num2*other.num2
       return '{}/{}'.format(new_num,new_num2)
    
frc1 = Fraction(3,4)
frc2 = Fraction(1,2)
print(frc1 + frc2)
print(frc1 - frc2)