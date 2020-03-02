my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

#Set Methods

print(my_set.difference(your_set)) #returns difference elements between two sets,any duplicates gets ignored

#my_set.discard(5) #discards the element entered
#print(my_set)

#my_set.difference_update(your_set) #removes differences and updates it
#print(my_set)

print(my_set.intersection(your_set)) #returns intersection that is common elements between 2 sets

print(my_set.isdisjoint(your_set))

print(my_set.union(your_set))

print(my_set.issubset(your_set))

print(my_set.issuperset(your_set))