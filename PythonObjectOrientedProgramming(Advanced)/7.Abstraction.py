class PlayerCharacter():

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def run(self):
        print('Run')

    def speak(self):
        print(f'Hi my name is {self.name} and I am {self.age} years old')


player1 = PlayerCharacter('Ryan Garcia',23)
player1.speak() #Abstraction
