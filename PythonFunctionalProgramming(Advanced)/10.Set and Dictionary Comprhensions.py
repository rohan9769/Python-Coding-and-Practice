#Set comprehnsion

my_list = {char for char in 'Hello'}
print(my_list)

my_list2 = {i for i in range(100)}
print(my_list2)

my_list3 = {i**2 for i in range(100)}
print(my_list3)

#Dictionary Comprehension
simple_dict = {'a':1,'b':2}
my_dict = {key:value**2 for key,value in simple_dict.items() if value%2==0}
print(my_dict)

my_dict2 = {i:i*2 for i in [1,2,3]}
print(my_dict2)