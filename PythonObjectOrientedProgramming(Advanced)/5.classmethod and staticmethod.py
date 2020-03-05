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

    @classmethod #A classmethod can be used even without instantiating the class but they are not used often
    def add_things(cls,n1,n2):
        return n1+n2
        #return cls('Ted',n1+n2) #can also instantiate class

    @staticmethod   #used when we don't need access to any class specific data
    def add_things2(n1,n2):
        return n1+n2

#player1 = PlayerCharacter('Roger',23)

print(PlayerCharacter.add_things(5,3))

# player3 = PlayerCharacter.add_things(5,4)
# print(player3)






# player2 = PlayerCharacter('Cindy',33)
# #Player 1 and Player 2 are Objects of the class PlayerCharacter
#
# #Player 1
# print(player1.name)
# print(player1.age)
# print(player1.membership)
# print(player1.shout())
# player1.run()
#
# #Player 2
# print(player2.name)
# print(player2.age)
# print(player2.membership)
# print(player2.shout())
# player2.run()
