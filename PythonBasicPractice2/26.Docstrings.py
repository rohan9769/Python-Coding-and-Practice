#Docstrings allows us to do is to actually comment inside of our functions

def test(a):
    '''
    Info : This function tests and prints parameter 'a'
    :param a:
    :return:
    '''
    print(a)

test(33)
help(test) #help() = This will print the doctring

print(test.__doc__) #Another way of displaying docstring in the console
