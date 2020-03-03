#Keyword Arguments
def say_hello(name,greeting):
    print(f'{greeting} {name}')

say_hello(name = 'Ron',greeting = 'Hello') #Keyword Arguments

#Default Parameters
def say_hello1(name = 'Ron',greeting = 'namamste'):
    print(f'{greeting} {name}')

say_hello1() #keyword arguments override default parameters
