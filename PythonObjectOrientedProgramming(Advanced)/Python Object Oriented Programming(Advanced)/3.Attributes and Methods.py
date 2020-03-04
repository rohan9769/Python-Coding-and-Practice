# Adding Attributes and Methods

#Making a  game

class PlayerCharacter:
    membership = True #Class Object Attribute,its static
    def __init__(self,name,age): #Constructor Method,automatically called when instantiated that is when object is created
        if(PlayerCharacter.membership):
            self.name = name
            self.age = age

    def run(self):
        print("Running")

    def shout(self):
        print(f'My name is {self.name}')

player1 = PlayerCharacter('Roger',23)
player2 = PlayerCharacter('Cindy',33)
#Player 1 and Player 2 are Objects of the class PlayerCharacter

#Player 1
print(player1.name)
print(player1.age)
print(player1.membership)
print(player1.shout())
player1.run()

#Player 2
print(player2.name)
print(player2.age)
print(player2.membership)
print(player2.shout())
player2.run()
