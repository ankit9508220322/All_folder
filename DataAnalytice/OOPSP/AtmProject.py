class Atm:
    def __init__(self):
        self.pin = ""
        self.balance = 10
        self.menu()
        
    def menu(self):
        user_input = input("""
        hii can i help you:
        1. press one create pin:
        2. press 2 change pin:
        3. press 3 check balance:
        4. press 4 withdraw money:
        5. anything else exit 
        """)
        
        if user_input == "1":
            self.create_pin()
        elif user_input == '2':
            self.chande_pin()
        elif user_input == '3':
            self.check_balance()
        elif user_input == '4':
            self.withdrow()
        else:
            return   # exit
        
    # create pin
    def create_pin(self):
        user_input_pin = input("enter your pin: ")
        self.pin = user_input_pin
        
        user_balance = int(input("enter balance: "))
        self.balance = user_balance
        print("success full")
        self.menu()

    # change pin
    def chande_pin(self):#All function name 
        old_pin = input("enter old pin: ")   #int hata diya
        if old_pin == self.pin:
            new_pin = input("enter new pin: ")
            self.pin = new_pin
            print("your pin is changed")
        else:
            print("please enter the correct pin")
        self.menu()

    # check balance
    def check_balance(self):     #All function name 
        user_pin = input("enter the pin: ")            
        if user_pin == self.pin:
            print("your balance is:", self.balance)
        else:
            print("incorrect pin")
        self.menu()

    # withdraw money
    def withdrow(self):   #Alla function name     
        wid_mony = input("enter the pin: ")
        if wid_mony == self.pin:
            amount = int(input("enter the amount: "))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print("success full transfer:", self.balance)
            else:
                print("incorrect balance: ")
        else:
            print("correct enter the pin:")
        self.menu()

obj = Atm()   #Aobj is object i me created
obj.balance="vvvvvv"
# /////////////////////////////////////////////////////////

# a=obj.create_pin()
print(obj.create_pin())
while True:
    user_input = input("""
hii can i help you:
1. press 1 create pin
2. press 2 change pin
3. press 3 check balance
4. press 4 withdraw money
5. anything else exit
""")
    balance = 100011
# CREATE PIN 
    if user_input == "1":
        a = int(input("Enter new pin: "))
        b = int(input("Confirm pin: "))

        if a == b:
            pin = a
            print(" PIN created successfully")
        else:
            print(" PIN not matched")

#  CHANGE PIN 
    elif user_input == "2":
        old_pin = int(input("Enter old pin: "))

        if old_pin == pin:
            new_pin = int(input("Enter new pin: "))
            pin = new_pin
            print(" PIN changed successfully")
        else:
            print(" Wrong PIN")

#  CHECK BALANCE 
    elif user_input == "3":
        check_pin = int(input("Enter pin: "))

        if check_pin == pin:
            print(" Your balance is:", balance)
        else:
            print(" Incorrect PIN")

# WITHDRAW MONEY -
    elif user_input == "4":
        check_pin = int(input("Enter pin: "))

        if check_pin == pin:
            amount = int(input("Enter withdraw amount: "))

            if amount <= balance:
                balance -= amount
                print(" Withdraw successful")
                print("Remaining balance:", balance)
            else:
                print(" Insufficient balance")
        else:
            print(" Wrong PIN")

#  EXIT 
    else:
       print(" Thank you, Exit")