#OOP

#Making a wizard game

class PlayerCharacter:
    def __init__(self,name,age): #Constructor Method,automatically called when instantiated that is when object is created
        self.name = name
        self.age = age

    def run(self):
        print("Running")

player1 = PlayerCharacter('Roger',23)
player2 = PlayerCharacter('Cindy',33)
#Player 1 and Player 2 are Objects of the class PlayerCharacter
print(player1.name)
print(player1.age)
player1.run()
print(player2.name)
print(player2.age)
player2.run()
