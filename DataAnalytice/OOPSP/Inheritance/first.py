# aggregation 
class customer:
    def __init__(self,name,gender,address):
        self.name = name
        self.gender = gender
        self.address = address
    
    def print_address(self):
        print(self.address.city,self.address.pin,self.address.state)
    # edit profile
    def edit_profile(self,new_name,new_city,new_state,new_pin):
        self.name = new_name
        self.address.edit_address(new_city,new_pin,new_state)

class Address:
    def __init__(self,city ,pin ,state):
        self.city = city
        self.pin = pin
        self.state = state

        # edit address
    def edit_address(self,new_city,new_state,new_pin):
        self.city = new_city
        self.state = new_state
        self.pin = new_pin

# this method is aggregation
Add1 = Address('kochas',11223,'sasaram')
cust = customer('ankit','mail',Add1)
cust.name
print(cust.gender,cust.name)
cust.print_address()
cust.edit_profile('mohit',1234567,'city','nalanda')
cust.print_address()
