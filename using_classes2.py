# class User: # CLASS INSTANCE METHODS:
#     def __init__(self, name, email, password):
#         self.name = name
#         self.email = email
#         self.password = password

#     def change_password(self, password): # How to define an instande method inside a class.
#         self.password = password # Make a method to change the password. Write a normal function, but inside the class
#         print("Your password has been change to", self.password)

# user1 = User("Jane", "jane@nucamp.co", "janespassword")
# print(user1.password) # To print an attribute
# user1.change_password("bestpassword") # This is an instance method, meaing we can call it on the instance, rather than the class.

class Human:
    def __init__(self, name, age):
        self.name =  name
        self.age = age
    
    def walk(self, direction):
        print(self.name, "walks to the", direction)

    def talk(self, speech):
        print(self.name, "says:", speech)

class Wizard(Human): # Class name wizard is inhereting from human class all the attributes, plus more are being added.
    def __init__(self, name, age, spell_points): # This init method overrides the parent class
        super().__init__(name, age) # So we initialize the parent class, so that attributes come along with the new attributes.
        self.spell_points = spell_points
    def cast_spell(self, spell):
        print(self.name, "casts", spell)