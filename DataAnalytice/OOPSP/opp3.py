class Bank:
    def __init__(self,name,account_no,balance):
        self._name = name
        self._account = account_no
        self._balance = balance
        
    def display(self):
        print("Account Number:",self._account)
        print("Account Name:",self._name)
        print("Account balance:", self._balance,'r')
        
    def deposit(self,amount):
        self._balance = self._balance + amount
        
    def withdrawl(self,amount):
        if amount > self._balance:
            print("insufficient funds")
        else:
            self._balance = self._balance - amount
            reduction = self._bank_fee()   # ✅ Call the method
            self._balance = self._balance - reduction
            
    def _bank_fee(self):
        return 0.05 * self._balance   # 5% fee


cust = Bank("ankit",200000303,30000)
cust.deposit(500)
cust.withdrawl(1000)
cust.display()
