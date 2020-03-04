# *args , **kwargs

# *args
def super_func(*args):
    return sum(args)

print(super_func(1,2,3,3,4))


# **kwargs
def bday_party(**kwargs):
    for i in kwargs.values():
        print(i)

bday_party(name=['Roger','David','Billy','Novak'])

# Both in one snippet

def big_bash(*args,**kwargs):
    for i in kwargs.values():
        print(f'{args} : {i}')

big_bash(1,2,3,4,5,names = ['Ricky','Melanie','Luna'])


# Rule for ordering : paramaters,*args,default,**kwargs
#Example

def big_bash(user,*args,gender='M',**kwargs):
    for i in kwargs.values():
        print(f'{args} : {i}')

big_bash('Joy',1,2,3,4,5,names = ['Ricky','Melanie','Luna'])
