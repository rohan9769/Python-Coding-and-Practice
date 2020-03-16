# #Exception Handling in Python
# '''
# try:
#     statements
# except:
#     exception name
#  else:
#       statements
# finally:
#     statements
# '''
#
# #Program to handle ZeroDivisionError exception
# try:
#     c = 5/0
# except ZeroDivisionError:
#     print('Division by Zero Happened')
# finally:
#     print('Handling done')
#     pass

# #Program to handle syntax error given by eval() function
# try:
#     date = eval(input('Enter Date'))
# except SyntaxError:
#     print('Invalid date entered')
# else:
#     print('Date entered is ',date)

# #Program to handle IOError
# try:
#     name = input('Enter name :')
# except IOError:
#     print('IOError occured enter correct input')
# else:
#     print(f'Data entered correctly : {name}')

# #Program to handle multiple execptions
# try:
#     n = int(input('Enter a no :'))
#     c = 5/n
# except ZeroDivisionError:
#     print('Divide by zero error occured')
# except ValueError:
#     print('Wrong input')
# finally:
#     print('Done')

# #assert statement: assert condition,message
# #Program using assert statement and catching AssertionError
# try:
#     x = int(input('Enter number :'))
#     assert x>=5 and x<=10
#     print('No entered : ',x)
# except AssertionError:
#     print('OOPS!')

# #User defined exception
# class MyException(Exception):
#     def __init__(self,msg):
#         self.msg = msg
#
# try:
#     pass
# except MyException as me:
#     raise MyException('message')