#List Comprehension

#Comprehensions are quick way for us to create list/sets/dictionary

#my_list = [parameter for parameter in iterable]

my_list = [char for char in 'Hello']
print(my_list)

my_list2 = [i for i in range(100)]
print(my_list2)

my_listdouble = [i**2 for i in range(100)]
print(my_listdouble)

mylist3 =[i**2 for i in range(100) if i%2 == 0]
print(mylist3)