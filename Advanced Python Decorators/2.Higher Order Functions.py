#Higher Order Function - function that accpets another function as a parameter OR a function that returns another function

def greet(func):
    func()

def greet2():
    def func():
        return 5
    return func

greet(func=5)