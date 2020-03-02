#Tuple are like list but they are immutable
my_tuple = (1,2,3,4,5)
print(my_tuple.index(1))
print(my_tuple)
print(my_tuple[1])
print(5 in my_tuple)

#Tuple are faster than list

user = {
    (1,2) : [1,2,3,4],
    'greet':'Hey',
    'age':20
}

print(user[(1,2)])