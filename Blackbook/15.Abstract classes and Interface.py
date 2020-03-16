# #Abstract classes:-
# #Program to create an abstract class and subclass which implements abstract method of abstract class
# from abc import *
# class Myclass(ABC):         #way to declare an abstract class
#     @abstractmethod         #way to declare an abstract method
#     def calc(self,x):
#         pass
#
# class Sub1(Myclass):
#     def calc(self,x):
#         print(f'Square is {x**2}')
#
# class Sub2(Myclass):
#     def calc(self,x):
#         print(f'Cube is {x**3}')
#
# s1 = Sub1()
# s1.calc(2)
# s2 = Sub2()
# s2.calc(5)

#Refer abs.py,maruti.py and santro.py for Abstract classes

# #Interfaces:-
# #All methods in an interface are abstract methods
# #1)Program to develops an interface to connect to any database
#
# from abs import *
# #Abstract class(Myclass) works like an interface
# class Myclass(ABC):
#     @abstractmethod
#     def connect(self):
#         pass
#     def disconnect(self):
#         pass
#
# #Subclass Oracle
# class Oracle(Myclass):
#     def connect(self):
#         print('Connecting to Oracle Database....')
#     def disconnect(self):
#         print('Disconnecting from Oracle Database....')
#
# #Subclass Sybase
# class Sybase(Myclass):
#     def connect(self):
#         print('Connecting to Sybase Database....')
#     def disconnect(self):
#         print('Disconnecting from Sybase Database....')
#
# class Database:
#     str = input('Enter name : ')
#     classname = globals()[str]
#     x = classname()
#     x.connect()
#     x.disconnect()

# #2)Program which contains a Printer Interface and its subclasses send text to any printer
# from abs import *
# class Printer(ABC):
#     @abstractmethod
#     def print(self,text):
#         pass
#     @abstractmethod
#     def disconnect(self):
#         pass
#
# class Ibm(Printer):
#     def print(self,text):
#         print(text)
#         print('Hello this is sent to printer and is printed by Ibm printer')
#     def disconnect(self):
#         print('Disconnected....')
#
# class Epson(Printer):
#     def print(self,text):
#         print(text)
#         print('Hello this is sent to printer and is printed by Epson printer')
#     def disconnect(self):
#         print('Disconnected....')
#
# class Userprinter:
#     with open("config.txt",'r') as f:
#         str = f.readline()
#
#         classname = globals()[str]
#         x = classname()
#         x.printit()
#         x.disconnect()

