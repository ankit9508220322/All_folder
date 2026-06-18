class ABC:
    def __init__(self):
        self.pin = ''
        self.balance = 200
        self.menu()
    
    def menu(self):
        user_input = input("""
                           1. press 1 create pin
                           2. press 2 change pin
                           3. press 3 check balance
                           4. press 4 withdrow balance
                           """)
        if user_input == '1':
            self.createPin()
        if user_input == '2':
            self.changePin()
        if user_input == '3':
            pass
        if user_input == '4':
            pass
    def createPin(self):
        enter_pin = input("enter the pin: ")
        self.pin = enter_pin
        print(f"your pin is",enter_pin)
        print('sucessfull ')
        
        user_balance = int(input("enter th balance: "))
        self.balance = user_balance
        print("sucessfull Balnce ")
        self.menu()
    
    def changePin(self):
        chance_pin = int(input("enter the old pin: "))
        if self.pin == chance_pin:
            new_pin = int(input("enter the new pin: "))
            self.pin = new_pin
        else:
            print("pour pin is incorect: ")
            self.menu()
            
                
obj = ABC()