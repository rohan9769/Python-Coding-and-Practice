# #1)Display group of messages if condition is True
# str = 'Yes'
# if str == 'Yes':
#     print('Good')

# #2)Find if no is even or odd
# n = int(input('Enter  a  Number  : '))
# if n%2==0:
#     print('Even')
# else:
#     print('Odd')

#3)Check wether no is between 1 and 10
# n = int(input('Enter  a  Number  : '))
# if n>=1 and n<=10:
#     print('Yes no is between 1 and 10')
# else:
#     print('Uh oh!')
#
# #4)Accept a numeric digit from keyboard and display in words:
# n = int(input('Enter  a  Number  : '))
# if n == 0:
#     print('ZERO')
# elif n==1:
#     print('ONE')
# elif n==2:
#     print('TWO')
# elif n==3:
#     print('THREE')
# elif n==4:
#     print('FOUR')
# elif n==5:
#     print('FIVE')
# elif n==6:
#     print('SIX')
# elif n==7:
#     print('SEVEN')
# elif n==8:
#     print('EIGHT')
# elif n==9:
#     print('NINE')
# else:
#     print('Enter no less than 10')

# #While Loop:-
# #5)Display no from 1 to 10 using while loop
# i=1
# while i<10:
#     print(i)
#     i = i+1

# #6)Display even no between 100 and 200
# i=100
# while i<201:
#     if i%2==0:
#         print(i)
#     i=i+1
#
# #7)Display even no between m and n
# m = int(input('Enter range start : '))
# n = int(input('Enter range end : '))
# while i>=m and i<=n:
#     if i%2==0:
#         print(i)
#     i=i+1

# #For Loop:-
# #7)Display characters of a string using for loop
# name = input('Enter a String :')
# for i in name:
#     print(i)

# #8)Display characters of a string using for loop ver2(accessing using index)
# name = input('Enter a String :')
# for i in range(len(name)):
#     print(name[i])

# #9)Display odd numbers from 1 to 10 using range()
# for i in range(10):
#     if i%2!=0:
#         print(i)

# #10)Display odd numbers from 1 to 10 in descending order
# for i in range(10,0,-1):
#     if i%2!=0:
#         print(i)
#
# #11)Display elements of a list using for loop
# lst = [1,2,3,4,5,6,7,8]
# for i in lst:
#     print(i)

# #12)Display and find sum of a list using for loop
# lst = []
# summ = 0
# n = int(input('Enter no of elements :'))
# for i in range(n):
#     x = int(input())
#     lst.append(x)
#
# print(lst)
# for i in lst:
#     summ = summ+i
# print(summ)
# #print(sum(lst)) Shortcut,remove 2nd for loop

# #13)Search for an element in the list
# lst = []
# n = int(input('Enter no of elements :'))
# for i in range(n):
#     x = int(input())
#     lst.append(x)
#
# print(lst)
# search = int(input('Enter the element to be searched : '))
# for i in range(len(lst)):
#     if search==lst[i]:
#         print(f'Element found at index {i}')
#

# #Break Statement :-
# #14)Program to display no from 10 to 6 and break when display is 5
# x = 10
# while x>=1:
#     print(f'x = {x}')
#     x = x-1
#     if x==5:
#         break
# print('Loop Over')

# #Continue Statement :-
# #15)Display no from 1 to 5 using continue
# x = 0
# while x<10:
#     x = x+1
#     if x>5:
#         continue
#     print(f'x = {x}')
# print('Loop Exits')

# #Assert Statement :- (assert expression,message)
# #16)A program to assert that the user enters a no greater than zero
# n = int(input('Enter a  number :'))
# assert n>0,'Wrong input'
# print(n)

# #Return Statement
# #17)Function that returns the sum of two nos
# def add(a,b):
#     sum = a+b
#     return sum
#
# print(add(5,6))
# #OR
# # def add(a,b):
# #     return a+b
# #
# # res = sum(5,6)
# # print(res)