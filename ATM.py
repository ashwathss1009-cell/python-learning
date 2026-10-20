class Atm:
    def __init__(self,balance,pin):
        self.__balance = balance
        self.pin = pin
        
    def deposit(self,amount):
        if amount >=0:
            self.__balance +=amount
            return f"deposited successfully \nnew balance is {self.__balance}"
        else:
            return ("Enter the amount correctly")
            
    def withdrawal(self,amount):
        if amount <= self.__balance:
            self.__balance -=amount
            return f"withdrawal successfully \nnew balance is {self.__balance}"
        else:
            return "Enter the amount correctly"
            
    def check_balance(self,pin):
        if self.pin == pin:
            return f"the balance is {self.__balance}"
        else :
            return ("Enter the pin correctly")
            
atm = Atm(100,1234)
while True:
    print("##== Banking simulation ==##\n"
          "1. Deposit\n"
          "2. Withdrawal\n"
          "3. Check balance\n"
          "4. Exit \n")
    
    choice = int(input("Enter your choice :"))
    if choice in [1,2,3]:
        if choice == 1:
            amount = int(input("Enter the amount :"))
            print(atm.deposit(amount))
        
        elif choice == 2:
            amount = int(input("Enter the amount :"))
            print(atm.withdrawal(amount))
        
        elif choice == 3:
            pin = int(input("Enter your pin :"))
            print(atm.check_balance(pin))
    
    if choice == 4:
        print("Thanks for banking !")
        break