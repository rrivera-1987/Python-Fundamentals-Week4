# class Player: # the first letter for the class name is capitalized.
#     max_hp = 40000 # Inside the code block, describe the class's attributes.
#     # The purpose of a class is to make objects. Which is called instantiation. 
#     # You're creating an instance of a class.
# player1 = Player() # To instantiate an object, declare a name of a variable to store the object.
# print(player1.max_hp) # Then assign as its value the class name followed by an argument.
# player2 = Player() # You can think of a class as a function that creates an object and returns it.
# print(player2.max_hp)

# Player.max_hp = 5000 # we can change the class attribute, even after it has been declared. Outside the code block.
# print(player1.max_hp)
# print(player2.max_hp)

class Player:
    def __init__(self, name, hp): # We can initialize instance attributes inside a class, by defining
       self.name = name # a special method called __init__. This is called a constructor method.
       self.hp = hp     # One thing to know is that we do not need to parametize every single attribute.
       self.score = 0 # Only those attributes where we want to set the initial value dynamically.
       # we can also set up attribute with a default initial value, by declaring them in the constructor, as in self.score
player1 = Player("Aaron", 1200)
player2 = Player("Irene", 1300)     

print("P1: ", player1.name, "   HP:", player1.hp, "  SCORE: ", player1.score)
print("P2: ", player2.name, "   HP:", player2.hp, "  SCORE: ", player2.score)

player1.hp += 500
player1.score += 10
print("P1: ", player1.name, "   HP:", player1.hp, "  SCORE: ", player1.score)
print("P2: ", player2.name, "   HP:", player2.hp, "  SCORE: ", player2.score)
