class bankAccount:
    def __init__(self,acc_holder,balance):
        self.acc_holder = acc_holder
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited ${amount}, Balance now ${self.balance}")
        
    def withdraw(self,amount):
        if (amount > self.balance):
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}, Balance now ${self.balance}")
        
    def check_balance(self):
        print(f"Balance as of now ${self.balance}")
        
total = bankAccount("neha", 2000)
total.deposit(500)
total.withdraw(3000)
total.check_balance()