class PlayerCharacter():

    def __init__(self,name,age):
        self._name = name #._name means its a private variable
        self._age = age

    def run(self):
        print('Run')

    def speak(self):
        print(f'Hi my name is {self._name} and I am {self._age} years old')


player1 = PlayerCharacter('Ryan Garcia',23)
player1.speak()

# ___init___ , is a dunder method
