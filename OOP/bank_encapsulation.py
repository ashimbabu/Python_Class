class BankAccount:
    def __init__(self,name,initial_balance):
        self.name = name
        self.__initial_balance = initial_balance
        
    def deposit(self,amount):
        
        self.__initial_balance = self.__initial_balance + amount
        print(f"{amount} deposited sucessfully.")
        
        
    def withdraw(self,amount):
        
        self.__initial_balance = self.__initial_balance - amount
        print(f"{amount} withdrawn sucessfully.")
        
    def show_balance(self):
        
        print(f"Your total bank balance is {self.__initial_balance}")
        
acc = BankAccount("Ram Sharma",20000)
while True:
    
    print("\nYour available options:")
    print("1. Deposit Amount\n2. Withdraw Amount\n3. Show Total Bank Balance\n4. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        amount = int(input("Enter amount to deposit:"))
        acc.deposit(amount)
        
    elif choice == 2:
        amount = int(input("Enter amount to withdraw:"))
        acc.withdraw(amount)
        
    elif choice == 3:
        acc.show_balance()
        
    elif choice == 4:
        print("Exited")
        break
    
    else:
        print("INvalid Choice")