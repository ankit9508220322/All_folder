import qrcode

class Atm:
    def __init__(self):
        self.pin = ''
        self.balance = 0
        self.menu()
        
    def menu(self):
        user_input = input("""           
1. press 1 create the pin
2. press 2 change the pin
3. press 3 check balance
4. press 4 withdraw balance
""")

        if user_input == '1':
            self.create_pin()
 
        if user_input == '2':
            self.chenge()

        if user_input == '3':
            self.scanner()

        if user_input == '4':
            pass

    def create_pin(self):
        enter_pin = int(input("enter the new pin: "))
        enter_pin2 = int(input("enter the confirm pin: "))

        if enter_pin == enter_pin2:
            self.pin = enter_pin2
            print("your pin is successful")
        else:
            print("not match your pin", enter_pin2)

        self.menu()

    # change pin atm
    def chenge(self):
        new_pin = int(input('enter the old pin: '))
        if self.pin == new_pin:
            conform = int(input("enter new pin: "))
            self.pin = conform
            print("sucess full change pin ")
        else:
            print("old pin is rong ")

        self.menu()
        
    def scanner(self):
        number = input("Enter your pin: ")

        # Convert number → UPI ID
        upi_id = f"{number}@upi"

        # UPI URL
        upi_url = f"upi://pay?pa={upi_id}&pn=Recipient&cu=INR"

        # Generate QR Code
        qr = qrcode.make(upi_url)

        # Save & Show
        qr.save("upi_number_qr.png")
        qr.show()
        self.menu()


atm = Atm()