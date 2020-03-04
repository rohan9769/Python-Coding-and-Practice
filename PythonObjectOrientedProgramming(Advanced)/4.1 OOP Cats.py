#Make a class called cat

#1 Instantiate the Cat object with 3 cats
#2 Create a function that finds the oldest cat
#3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

class Cat:
    species = 'mammal'
    def __init__(self,name,age):
        self.name = name
        self.age = age


cat1 = Cat('Roxanne',33)
cat2 = Cat('Anna',43)
cat3 = Cat('Lily',32)


def find_oldest():
    a = max(cat1.age,cat2.age,cat3.age)
    print(f'Oldest cat is {a} years old')

find_oldest()
