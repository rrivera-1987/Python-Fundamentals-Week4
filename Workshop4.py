class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, new_name):
        self.name = new_name
    
    def change_pin(self, new_pin):
        self.pin = new_pin
    
    def change_password(self, new_password):
        self.password = new_password

class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):
        print(f"{self.name} has an account balance of: ${self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient funds")
    
    def deposit(self, amount):
            self.balance += amount

    def transfer_money(self, recipient, amount):
        print("\nYou are transferring $500 to Bob")
        print("Authentication required")
        pin = int(input("Enter your PIN: "))
        if pin == self.pin:
            if amount > 0 and amount <= self.balance:
                recipient_pin = int(input("Enter recipient's PIN: "))
                if recipient_pin == recipient.pin:
                    recipient.deposit(amount)
                    self.balance -= amount
                    print(f"Transferred: ${amount}")
                    print(f"{recipient.name} has an account balance of: ${recipient.balance}")
                    return True
            else:
                print("Invalid transfer amount.")
        else:
            print("Invalid PIN.")
            return False
     
    def request_money(self, recipient, amount):
        print("\nYou are requesting $250 from Bob")
        print("User authentication required")
        recipient_pin = int(input("Enter recipient's PIN: "))
        if recipient_pin == recipient.pin:
            password = input("Enter your password: ")
            if password == self.password:
                if amount > 0 and amount <= recipient.balance:
                    recipient.withdraw(amount)
                    self.balance += amount
                    print(f"Received: ${amount}")
                    print(f"{self.name} has an account balance of: ${self.balance}")
                    return True
                else:
                    print("Invalid request amount.")
            else:
                print("Invalid password.")
                return False

# """ Driver Code for Task 1 """
# user1 = User("Tony", 2323, "Goat23")
# print(f"{user1.name}, {user1.pin}, {user1.password}")

# """ Driver Code for Task2 """
# user1 = User("Tony", 2323, "Goat23")
# print(f"{user1.name}, {user1.pin}, {user1.password}")

# user1.change_name("Antonio")
# user1.change_pin(4545)
# user1.change_password("Goat4545")
# print(f"{user1.name}, {user1.pin}, {user1.password}")

# """ Driver Code for Task 3 """
# bank_user = BankUser("Alice", 5678, "password")
# print(bank_user.name, bank_user.pin, bank_user.password, bank_user.balance)

# """ Driver Code for Task 4 """
# bank_user = BankUser("Alice", 5678, "password")
# bank_user.show_balance()
# bank_user.deposit(1000)
# bank_user.show_balance()
# bank_user.withdraw(500)
# bank_user.show_balance()

""" Driver Code for Task 5 """
user1 = BankUser("Bob", 1234, "password123")
user2 = BankUser("Alice", 5678, "password567")
user2.deposit(5000)
user2.show_balance()
user1.show_balance()

transfer_sucessful = user2.transfer_money(user1, 500)
if transfer_sucessful:
    print("\nTransfer was sucessful!")
else:
    print("Transfer failed")
user2.show_balance()
user1.show_balance()

request_sucessful = user2.request_money(user1, 250)
if request_sucessful:
    print("Request was sucessful!")
else:
    print("Request failed")
user2.show_balance()
user1.show_balance()
