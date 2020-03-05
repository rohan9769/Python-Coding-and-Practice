# Introspection - means ability to determine type of object in runtime
class User:

    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):  # Wizard class inherits from User class

    def __init__(self, name, power, email):
        super(Wizard, self).__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows, email):
        super(Archer, self).__init__(email)
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with {self.num_arrows} arrows ')


wizard1 = Wizard('Merlin', 55, 'roger@xyz')
print(wizard1.email)
wizard1.sign_in()


print(dir(wizard1)) #Introspection
