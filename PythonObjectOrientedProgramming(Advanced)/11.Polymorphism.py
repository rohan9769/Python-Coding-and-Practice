#Polymorphism - Different method in classes can share the same method name but function differently
#Like here the class Wizard and Archer have the same method name attack but the method performs differently in both th classes
class User:
    def sign_in(self):
        print('Logged in')

    # def attack(self):
    #     print('do nothing')


class Wizard(User): #Wizard class inherits from User class
    def __init__(self,name,power):
        #User.attack(self)
        self.name = name
        self.power =power

    def attack(self):
        print(f'Attacking with power {self.power}')


class Archer(User):
    def __init__(self,name,num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with {self.num_arrows} arrows ')



user1 = User()
user1.sign_in()

wizard = Wizard('Roger',55)
archer = Archer('Robin',88)
wizard.attack()
print(wizard.name)
print(archer.name)
archer.attack()
wizard.sign_in()
archer.sign_in()



print(isinstance(wizard,User)) #checks if object is instance of class

#Polymorphism demo
def player_attack(char):
    char.attack()
player_attack(wizard)
player_attack(archer)

for char in [wizard,archer]:
    char.attack()
