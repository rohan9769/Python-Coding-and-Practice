#reduce

from functools import reduce
my_list = [1,2,3]

def multi_by2(i):
    return i*2

def check_odd(i):
    return i%2 != 0

def accumulator(acc,i):
    print(acc,i)
    return acc + i


print((reduce(accumulator,my_list,0)))