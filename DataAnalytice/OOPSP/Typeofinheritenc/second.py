# multilevel  hierarchical 
class Prodect:
    def review(self):
        print("prodect customer review: ")
class Phone(Prodect):
    def __init__(self,price,brande,camera):
        print("inside the phone coustomer: ")
        self.__price = price
        self.brande = brande
        self.camera = camera
        
    def Buy(self):
        print("buying a phone: ")

class Smartphne(Phone):
        pass
obj1=Smartphne(1000,"os","12px")
obj1.Buy()
obj1.review()

