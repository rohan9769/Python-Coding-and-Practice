# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
#Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# lst = list(map(int,input('Enter nos').split()))
# print(lst)
# print(tuple(lst))


# Define a class which has at least two methods:
#
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# class Hello:
#     def __init__(self):
#         self.s = " "
#
#     def getString(self):
#         self.s = input('Enter the string')
#
#     def printString(self):
#         print(self.s.upper())
#
# obj1 = Hello()
# obj1.getString()
# obj1.printString()


# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24

# from math import *
# C, H = 50, 30
# def calc(D):
#     return sqrt((2 * C * D) / H)
# print(",".join([str(int(calc(int(i)))) for i in input().split(',')]))



# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
#
# Suppose the following input is supplied to the program:
#
# without,hello,bag,world
# Then, the output should be:
#
# bag,hello,without,world

# words = [x for x in input().split(',')]
# words.sort()
# print(','.join(words))


# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
#
# Suppose the following input is supplied to the program:
#
# Hello world
# Practice makes perfect
# Then, the output should be:
#
# HELLO WORLD
# PRACTICE MAKES PERFECT

# lst = []
# while True:
#     x = input()
#     if len(x)==0:
#         break
#     lst.append(x.upper())
#
# for i in lst:
#     print(i)

