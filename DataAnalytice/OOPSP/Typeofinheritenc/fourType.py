# Multiple inheritance
class Phone: #this is pairent class
    def __init__(self,price,brande,camera):
        print("inside the phone coustomer: ")
        self.price = price
        self.brande = brande
        self.camera = camera
        
    def Buy(self):
        print("buying a phone: ")
class prodect:
    def review(self):
        print("coustomer review: ")
class Smartphone(Phone,prodect):
    pass
s = Smartphone(20000,"apple",12)
s.Buy()
s.review()