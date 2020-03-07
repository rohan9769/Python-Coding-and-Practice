import random as r


print(r.random())
print(r.randint(1,20))
print(r.choice([1,2,3,4,5])) #makes a choice from iterator list


my_list = [1,2,3,4,5]
print(r.shuffle(my_list))
print(my_list)