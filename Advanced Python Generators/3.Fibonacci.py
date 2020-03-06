def fibo(number):
    a=0
    b=1
    for i in range(number):
        yield a
        temp = a
        a= b
        b = temp+b

g = fibo(5)
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print('___________')
for i in fibo(5):
    print(i)



#If we want list of fibonacci numbers

def fibo_list(number):
    a=0
    b=1
    lst = []
    for i in range(number):
        lst.append(a)
        temp = a
        a= b
        b = temp+b
    return lst

print('--------------')
print(fibo_list(5))