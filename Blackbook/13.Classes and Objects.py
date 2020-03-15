# #Creating a class:-
# class Student:
#     def __init__(self):
#         self.name = 'Alok'
#         self.age = 15
#         self.gender = 'Male'
#
#     def talk(self):
#         print(f'My name is {self.name}. I am {self.age} years old and I am a {self.gender}')
#
# s1 = Student() #Creating an object/instance s1  from class Student [object = classname()]
# s1.talk()
# print(s1.name)
# print(s1.age)
# print(s1.gender)
#
# #1)Program to define Student class and create an object of it.Also call methods and display it
# class Student:
#     def __init__(self):
#         self.name = 'Alok'
#         self.age = 15
#         self.gender = 'Male'
#
#     def talk(self):
#         print(f'My name is {self.name}. I am {self.age} years old and I am a {self.gender}')
#
# s1 = Student() #Creating an object/instance s1  from class Student [object = classname()]
# s1.talk()
#
# #Constructor:-[A constructor is instantiated each time the object of class is instantiated]
# #General way to declare a constructor
# # def __init__(self,name):
# #     self.name = name
# #     self.marks = marks

# #2)Program to create a Student class with a constructor having more than one parameter
# class Student:
#     def __init__(self,name,age,rollno): #here constructor is parameterized
#         self.name = name
#         self.age = age
#         self.rollno = rollno
#
#     def talk(self):
#         print(f'My name is {self.name} and my roll number is {self.rollno}.I am {self.age} years old')
#
# s1 = Student('Roger',44,108765)
# s1.talk()
# print(s1.name)
# print(s1.age)
# print(s1.rollno)

# #3)Program to create a Student class with a default constructor
# class Student:
#     def __init__(self,name=' ',age=5,rollno=100): #here constructor is parameterized
#         self.name = name
#         self.age = age
#         self.rollno = rollno
#
#     def talk(self):
#         print(f'My name is {self.name} and my roll number is {self.rollno}.I am {self.age} years old')
#
# print('When parameter values provided')
# s1 = Student('Roger',44,108765)
# s1.talk()
# print('When no parameters values are provided')
# s2 = Student()
# s2.talk()

#Types of Methods[Instance methods,Class methods and Static methods]:

# #Instance Method
# #4)Program using a student class with instance methods to process data of sevaral students
# class Student:
#     def __init__(self,name,marks):      #Constructor
#         self.name = name
#         self.marks = marks
#     def display(self):                  #Insatance method
#         print(f'Hi {self.name}')
#         print(f'Your marks are {self.marks}')
#     def grade(self):               #Instance method
#         if self.marks>=600:
#             print('You received A grade')
#         elif self.marks>=500 and self.marks<600:
#             print('You recieved B Grade')
#         elif self.marks>=300 and self.marks<500:
#             print('You recieved C grade')
#         else:
#             print('You are failed')
#
# n = int(input('Enter no of students you want : '))
# i=0
# while i<n:
#     name = input('Enter name : ')
#     marks = int(input('Enter the marks obtained : '))
#
#     s = Student(name,marks)
#     s.display()
#     s.grade()
#     i=i+1

# #Class Methods:-
# #5)Program to use class method to handle common feature of all instances of birds class
# class Birds:
#     wings = 2 #class variable
#
#     @classmethod
#     def fly(self,name):
#         print(f'{name} flies with {self.wings} wings')
#
# Birds.fly('Parrot')
# Birds.fly('Pigeon')

# #Static Methods[classname.method]:-
# #6)Program to create a static method that calculates the square root of a given no
# import math
# class squareroot:
#     @staticmethod
#     def calc_root(x):
#         result = math.sqrt(x)
#         return result
#
# no = int(input('Enter a no'))
# res = squareroot.calc_root(no)
# print(res)

#7)Program to create a bank class where deposits and withdrawls can be handled by instance methods
import sys
class Bank:
    def __init__(self,name,balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self,amt):
        self.balance+=amt
        return self.balance

    def withdraw(self,amt):
        if amt < self.balance:
            self.balance-=amt
        else:
            print('Low Balance')
        return self.balance

b = Bank('Rohan')
while True:
    amt = int(input('Enter amount'))
    choice = input('d - deposit , w - withdraw , e-exit')
    if choice=='e':
        sys.exit()
    if choice == 'd':
        print(f'Balance after deposit : {b.deposit(amt)}')
    elif choice == 'w':
        print(f'Balance after withdrawing : {b.withdraw(amt)}')




