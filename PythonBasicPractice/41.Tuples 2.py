my_tuple = (1,2,3,4,5)
new_tuple = my_tuple[1:2]
print(new_tuple)

x,y,z,*other = (6,7,8,9,10,11)
print(other)

#Tuple Methods
print(my_tuple.count(3))
print(my_tuple.index(4))
print(len(my_tuple))