
class User:
    def sign_in(self):
        print('Logged in')


class Wizard(User): #Wizard class inherits from User class
    def __init__(self,name,power):
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
