#Set,unordered collection of unique objects

my_set = {1,2,4,4,4}
print(my_set)
my_set.add(10)
my_set.add(11)
print(my_set)
print(1 in my_set)
print(len(my_set))

my_set_list = list(my_set)
print(my_set_list)

my_new_set = my_set.copy()
print(my_new_set)
print(my_set)


# my_list = [1,2,3,4,5,5]
# unique_list = set(my_list)
# print(unique_list)