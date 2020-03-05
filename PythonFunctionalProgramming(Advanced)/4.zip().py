
# zip() - zips two lists together
# also works with tuples
my_list = [1,2,3,4]
your_list = [5,6,7,8]
their_list = (10,20,30)
def multi_by2(i):
    return i*2

def check_odd(i):
    return i%2 != 0

print(list(zip(my_list,your_list,their_list)))


