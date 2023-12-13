class User: # CLASS INSTANCE METHODS:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def change_password(self, password): # How to define an instance method inside a class.
        self.password = password # Make a method to change the password. Write a normal function, but inside the class
        print("Your password has been change to", self.password)

class BankUser(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.balance = 0
    def check_balance(self):
        print(self.name, "has an account balance of: ", self.balance)

bankuser1 = BankUser("Jane", "jane@nucamp.co", "bestpassword")


