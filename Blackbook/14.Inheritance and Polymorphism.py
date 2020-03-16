# #Program to create a Teacher class and store it as Teacher.py
# class Teacher:
#     def setid(self,id):
#         self.id = id
#     def getid(self):
#         return self.id
#     def setname(self,name):
#         self.name = name
#     def getid(self):
#         return self.name
#     def setaddress(self,address):
#         self.address = address
#     def getaddress(self):
#         return self.address
#     def setsalary(self,salary):
#         self.salary = salary
#     def getsalary(self):
#         return self.salary
#Refer student.py,teacher.py,inh.py,inhstud.py

# #Creating Student class from Teacher class
# from teacher import *
# class Student(Teacher):
#     def setmarks(self,marks):
#         self.marks = marks
#     def getmarks(self):
#         return self.marks
#
# s = Student()
# s.setmarks(55)
# s.setid(55)
# s.setname('roger')
# s.setaddress('lane')
# print(f'id is {s.getid()}')
# print(f'Name is {s.getname()}')
# print(f'Address is {s.getaddress()}')
# print(f'Marks is {s.getmarks()}')

# #Constructor in inheritance
# #Program to access base class constructor from sub class
# class Father:
#     def __init__(self):
#         self.property = 800000
#     def display(self):
#         print(f'Fathers property is {self.property}')
#
# class Son(Father):
#     pass
#
# s = Son()
# print(s.property)
# s.display()

#super() method
# class Father:
#     def __init__(self,property=0):
#          self.property = 800000
#     def display(self):
#          print(f'Fathers property is {self.property}')
#
# class Son(Father):
#     def __init__(self,property1=0,property=0):
#         super().__init__(property)
#         self.property1 = property1
#
#     def display(self):
#         print(f'Total property of child is {self.property1+self.property}')
#
# s = Son(20000)
# s.display()

# class Square:
#     def __init__(self,x):
#         self.x = x
#
#     def area(self):
#         print(f'Area of square is {self.x**2}')
#
# class Rectangle(Square):
#     def __init__(self,x,y):
#         super().__init__(x)
#         self.y =y
#
#     def area(self):
#         super().area()
#         print(f'Area of rectangle is {self.x * self.y}')
#
# r = Rectangle(5,4)
# r.area()

# #Inheritance
# #Single Inheritance
# #Program showing single inheritance in which two subclasses are derived from a single base class
# class Bank:
#     cash = 100000
#     def available_cash(self):
#         print(Bank.cash)
#
# class StateBank(Bank):
#     cash=15000
#     def available_cash(self):
#         print(f'Available Cash is {StateBank.cash+Bank.cash}')
#
# class AmericaBank(Bank):
#     cash=20000
#     def available_cash(self):
#         print(f'Available Cash is {AmericaBank.cash+Bank.cash}')
#
# s = StateBank()
# s.available_cash()
# a = AmericaBank()
# a.available_cash()

#Multiple Inheritance
class Father:
    def height(self):
        print('6ft height')

class Mother:
    def eye_color(self):
        print('Eye color is blue')
class Child(Father,Mother):
    pass

c=Child()
c.height()
c.eye_color()




