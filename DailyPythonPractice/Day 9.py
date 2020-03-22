# Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).
# x = list(map(lambda x : x**2,range(1,21)))
# print(x)

# #Define a class named American which has a static method called printNationality.
# class American:
#     @staticmethod
#     def printNationality():
#         print('Hi I am a proud American !')
# a=American()
# American.printNationality()

# #Define a class named American and its subclass NewYorker.
# class American:
#     pass
# class NewYorker(American):
#     pass
#
# a = American()
# n = NewYorker()

# Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.
# class Circle:
#
#     def __init__(self,r):
#         self.r = r
#
#     def calcArea(self):
#         return 3.14*self.r*self.r
#
# c = Circle(10)
# print(c.calcArea())

#Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.
# class Rectangle:
#     def __init__(self,l,w):
#         self.l = l
#         self.w = w
#
#     def calcArea(self):
#         return 2*(self.l+self.w)
#
# r = Rectangle(5,5)
# print(r.calcArea())


#Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument.
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
# class Shape:
#     def __init__(self):
#         pass
#     def area(self):
#         pass
#
# class Square(Shape):
#
#     def __init__(self,s=0):
#         Shape.__init__(self)
#         self.s = s
#
#     def area(self):
#         return self.s*self.s
#
# a = Square(5)
# print(a.area())
