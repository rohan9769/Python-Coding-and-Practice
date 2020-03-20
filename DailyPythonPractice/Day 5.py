# Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.
# Suppose the following input is supplied to the program:
# 1,2,3,4,5,6,7,8,9
# Then, the output should be:
# 1,9,25,49,81

# a = [str(int(x)**2) for x in input().split(',') if int(x)%2 ]
# print(','.join(a))

# val=[]
# while True:
#     x = input().split(',')
#     if not x[0]:
#         break
#     val.append(tuple(x))
# print(val)
# val.sort(key=lambda x:(x[0],x[1],x[2]))
# print(val)


# Write a program to compute the frequency of the words from the input.
# The output should output after sorting the key alphanumerically.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

# Then, the output should be:
#
# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

# ss = input().split()
# word = sorted(set(ss))     # split words are stored and sorted as a set
#
# for i in word:
#     print("{0}:{1}".format(i,ss.count(i)))
#


# #Write a method which can calculate square value of number
# def square(n):
#     return n**2
#
# ans = square(4)
# print(ans)
#
# #Define a function which can compute the sum of two numbers.
# def add(a,b):
#     return a+b
# res = add(5,4)
# print(res)
#OR
# c = lambda a,b : a+b
# pritnt(c)


