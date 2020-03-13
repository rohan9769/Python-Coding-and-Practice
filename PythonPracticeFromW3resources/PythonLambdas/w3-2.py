import random
n = list(int(x) for x in input('Enter a number :').split())
res = list(map(lambda x:x*5,n))
print(res)
