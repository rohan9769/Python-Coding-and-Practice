# Introspection - means ability to determine type of object in runtime
class User:
    def sign_in(self):
        print('logged in')


class Wizard(User):  # Wizard class inherits from User class

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with {self.num_arrows} arrows ')
    def run(self):
        print('Too fast run')

class HybridBorg(Wizard,Archer):
    def __init__(self,name,power,num_arrows):
        Archer.__init__(self,name,num_arrows)
        Wizard.__init__(self,name,power)

wizard1 = Wizard('Merlin', 55)
wizard1.sign_in()

hybridborg = HybridBorg('bunny',43,1000)
hybridborg.attack()
hybridborg.attack()