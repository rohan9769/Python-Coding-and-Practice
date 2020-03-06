


#creating our own decorator
def my_decorator(func):
    def wrap_func(*args,**kwargs):
        print('*****')
        func(*args,**kwargs)
        print('******')
    return wrap_func

@my_decorator
def hello(greeting,emoji='sadface'):
    print(greeting,emoji)



hello('Hello')


