#Lambda Expression - one time anonymous functions

# lambda parameter : action to take on the pararmeter

from functools import reduce
my_list = [1,2,3]

# def multi_by2(i):
#     return i*2

def check_odd(i):
    return i%2 != 0

def accumulator(acc,i):
    print(acc,i)
    return acc + i


print(list(map(lambda i: i*2,my_list)))

print(list(filter(lambda i:i%2!=0,my_list)))

