#Map,filter,zip are very common functions

# filter() helps to filter things for us
# map(action,data on which action should be take)

def multi_by2(i):
    return i*2

def check_odd(i):
    return i%2 != 0


print(list(filter(check_odd,[1,2,3,4,5])))

