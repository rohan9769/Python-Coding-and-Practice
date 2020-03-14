from functools import *
# #1)Program to find sum of two numbers
# def add(a,b):
#     return a+b
# c = add(5,4)
# print(f'Sum is {c} ')
#
# #2)Program to test wether no is odd or even
# def odd_eve(a):
#     if a%2==0:
#         print(f'{a} is Even')
#     else:
#         print(f'{a} is Odd')
#
# odd_eve(4)
# odd_eve(3)

# #3)Program to calculate factorial of a number
# def fact(i):
#     prod =1
#     while i>=1:
#         prod = prod*i
#         i=i-1
#     return prod
#
# c = fact(5)
# print(f'Factorial is {c}')

# #4)Program to check if given no is prime or not
# def prime(n):
#     for i in range(2, n):
#         if (n % i) == 0:
#             print(n, "is not a prime number")
#             print(i, "times", n // i, "is", n)
#             break
#     else:
#         print(n, "is a prime number")
#
# prime(5)
# prime(4)

# #5)Program to return the sum and difference of 2 nos
# def sum_diff(a,b):
#     c = a+b
#     d = a-b
#     return c,d
#
# x,y = sum_diff(10,5)
# print(f'Sum is {x} and Difference is {y}')

# #6)Program to return the sum,difference,product and division of 2 nos
# def calc(a,b):
#     c = a+b
#     d = a-b
#     e = a*b
#     f = a/b
#     return c,d,e,f
#
# g,h,i,j = calc(8,4)
# print(f'sum is {g},subtraction is {h},product is {i},division is {j}')

# #7)Program to define a function within another function
# def display(str):
#     def msg():
#         return 'How are you?'
#     result = msg()+str
#     return result
#
# print(display('Krish'))

# #8)Program to demonstrate how to pass function as a parameter
# def display(fun):
#     return 'Very'+fun
#
# def msg():
#     return 'How are you?'
# print(display(msg()))

# #9)Program to demonstrate how a function can return another function
# def display():
#     def msg():
#         return 'How are you'
#     return msg
#
# c = display()
# print(c())

# #10)Program to demonstrate positional arguments
# def attach(s1,s2):
#     s3 = s1+s2
#     print(s3)
#
# attach('New','York')

# #Keyword Arguements:-
# #11)Program to demonstrate keyword arguments
# def shopping(f,d):
#     print(f'Food is {f} and Drink is {d}')
#
# shopping(f='Vegetables',d='Red Bull')

# #Default Arguments
# #12)Program demonstrating default arguments
# def shop(f,d='Cocacola'):
#     print(f'Food is {f} and Drink is {d}')
#
# shop(f='Mashed Potatoes')
# shop(f='Garlic',d='pepsi')

# #Variable Length Arguments(*args,**kwargs):-
# #13)Program to demonstrate *kwargs
# def dinner(f,d,**desserts):
#     print(f'food is {f} , drink is {d} and desserts are {desserts}')
#
# dinner(f='Burger',d='Wine',cake='blackforest,pineapple')

# #14)Program to demonstrate *args
# def summ(*args):
#     sum=0
#     for i in args:
#         sum = sum+i
#     return sum
#
# print(summ(5,10,20))
# print(summ(30,40))

# #Passsing groups of elements to a function
# #15)Function to accept a group of numbers and calc their avg
# def calc(lst):
#     summ = 0
#     n = len(lst)
#     for i in lst:
#         summ = summ + i
#     avg = summ/n
#     return avg
#
# lst = [int(x) for x in input('Enter a number').split()]
# print(calc(lst))

# #16)Function to display group of strings
# def display(lst):
#     return lst
#
# lst = [x for x in input('Enter String').split()]
# print(lst)

# #Recursive Function
# #17)Factorial using recursion
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
#
# print(fact(5))

# #Lambda Functions:- lambda argument:expression
# #18)Simple Lambda Function
# f = lambda x:x*x
# val = f(5)
# print(val)
#
# #19)Lambda function that returns the square of number
# f = lambda x:x*x
# val = f(5)
# print(val)

# #20)Lambda Function that calculates the sum of two nos
# f = lambda a,b:a+b
# val = f(2,3)
# print(val)

# #21)Lambda Function to find biggest of 2 nos
# f = lambda a,b:a if a>b else b
# val = f(3,4)
# print(f'Max is {val}')

# #Map Function(map())[268]:-[Using Lambda function with map()] #map(function,sequence)
# #22)Program to find the squares of elements in a list using map()
# def sq(n):
#     return n*n
# lst = [1,2,3,4,5]
# lst1 = list(map(sq,lst))
# print(lst1)

# #23)Program to find the squares of elements in a list using Lambda function and map()
# lst = [1,2,3,4,5,6]
# lst1 = list(map(lambda x : x*x,lst))
# print(lst1)

# #23)Program to find the product of 2 different lists using lambda function and map()
# lst1=[1,2,3,4,5]
# lst2=[6,7,8,9,10]
# lst_mul = list(map(lambda x,y:x*y,lst1,lst2))
# print(lst_mul)

# #Filter function(filter()):-[Using Lambdas with filter()] #filter(func,seq)
# #24)Program to filter out even nos
# lst=[1,2,3,4,5,6,7,8]
# lst1 = list(filter(lambda x :x%2==0,lst))
# print(lst1)

# #Reduce function(reduce());:-[Using lambdas with reduce()] #reduce(func,seq)
# #25)Lambda function to calculate the product of elements of a list
# lst=[1,2,3,4,5]
# res = reduce(lambda x,y:x*y,lst)
# print(res)

# #Function Decorators[270]:- def decor(fun),fun is a function parameter
# #26)Decorator to increase the value of function by 2
# def decor(fun):
#     def inner():
#         value = fun()
#         return value+2
#     return inner
#
# def num():
#     return 10
# print(decor(num))

# #27)Decorator to increase the value of function by 2 using @
# def decor(fun):
#     def inner():
#         val = fun()
#         return val+2
#     return inner
#
# @decor
# def num():
#     return 10
#
# print(num())

# #28)Program to apply two decorators to the same function
# def decor(fun):
#     def inner():
#         val = fun()
#         return val+2
#     return inner
#
# def decor1(fun):
#     def inner():
#         val = fun()
#         return val*2
#     return inner
#
# @decor
# @decor1
# def num():
#     return 10
#
# print(num())

# #Generators[275]:
# #next() is used to retrieve element by element from generator object
# #29)Program to create a generator that returns a sequence of numbers from x to y
# def mygen(x,y):
#     while x<=y:
#         yield x
#         x+=1
#
# g = mygen(5,10)
# for i in g:
#     print(g)

# #30)Program to create a generator that returns characters from A to C
# def mygen():
#     yield 'A'
#     yield 'B'
#     yield 'C'
#
# g = mygen()
# print(next(g))
# print(next(g))
# print(next(g))

#31)Program to calculate gross salary and net salary of employee
def da(basic):
    da = 0.8*basic
    return da

def hra(basic):
    hra = 0.15*basic
    return hra

def pf(basic):
    pf = 0.12*basic
    return pf

def itax(gross):
    itax = 0.1*gross
    return itax

basic = int(input('Enter Basic Salary : '))

gross = da(basic)+hra(basic)+pf(basic)
print(f'Gross Salary is : {gross}')

net = gross - itax(gross)
print(f'Net Salary is {net}')
