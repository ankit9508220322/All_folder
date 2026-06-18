# single  hierarchical 
 
class Phone:
    def __init__(self,price,brande,camera):
        print("inside the phone coustomer: ")
        self.__price = price
        self.brande = brande
        self.camera = camera
        
    def Buy(self):
        print("buying a phone: ")

class Smartphne(Phone):
    
        pass
Smartphne(1000,"os","12px").Buy()

