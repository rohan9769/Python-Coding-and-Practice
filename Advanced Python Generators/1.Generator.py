# Special type of thing in pyhton that allows to use a special keyowrd yield and it can pause and resume functions
# ex range function

range(100) #creates 100 spaces at once in memory
list(range(100)) #creates 100 spaces one by one in memory

def make_list(num):
    result = []
    for i in range(num):
        result.append(i*2)
    return result

my_list = make_list(100)
print(my_list)
print(list(range(20)))