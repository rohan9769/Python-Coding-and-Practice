# @decorator supercharge functions and add extra functionality to it

def hello(func):
    func()

def greet():
    print('Still here')

a= hello(greet)
print(a)