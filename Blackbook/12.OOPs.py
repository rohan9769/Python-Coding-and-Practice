# #Classes and Objects:-
# class Person:
#     name = 'Anay'
#     age = 32
#     def talk(self):
#         print(f'My name is {self.name}')
#         print(f'Age is {self.age}')
#
# p1 = Person() #Creating object p1 from class Person()
# p1.talk()

# #Encapsulation
# class Person:
#     def __init__(self,name,age): #This is a constructor
#         self.name = name
#         self.age = age
#
#     def talk(self):
#         print(f'My name is {self.name} and age is {self.age}')
#
# p1 = Person('Ryan',22)
# p1.talk()

# #Inheritance
# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
#
#     def calc_area(self):
#         area = 3.14*(self.radius**2)
#         print(area)
#
# class Sphere(Circle):
#     def calc_vol(self):
#         vol = (3.14*4/3)*(self.radius**3)
#         print(vol)
#
# c1 = Circle(10)
# c1.calc_area()
# s1 = Sphere(10)
# s1.calc_vol()

#Polymorphism
def add(a,b):
    print(a+b)

add(3,2)
add('Core','Python')
