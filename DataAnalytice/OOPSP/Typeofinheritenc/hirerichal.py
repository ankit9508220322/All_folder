# hirarchical  inheritance
class Phone: #this is parent class
    def __init__(self,price,brande,camera):
        print("inside the phone coustomer: ")
        self.price = price
        self.brande = brande
        self.camera = camera
        
    def Buy(self):
        print("buying a phone: ")
# this is child class
class Smartphne(Phone):
    pass
class Feauterphone(Phone):
    pass
Smartphne(1000,"os","12px").Buy()
Feauterphone(1044,"osv","132px").Buy()
