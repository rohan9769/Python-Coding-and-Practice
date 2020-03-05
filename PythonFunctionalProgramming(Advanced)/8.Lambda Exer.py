# Using Lambda expressions return list containing the squares of the list items

my_list = [5,4,3]
print(list(map(lambda i : i**2,my_list)))

#Using lambda expression sort the list
a = [(0,2),(4,3),(9,9),(10,-1)]

a.sort(key=lambda x : x[1])
print(a)