#iterable can be a list,dictionary,set,tuple,list,string
user = {
    'name' : 'Mark',
    'age' : 500,
    'can_swim' : False
}

for i in user.items(): #returns the items from dictionary
    print(i)

for i in user.values(): #Gives values of the items
    print(i)

for i in user.keys(): #Returns keys of the items
    print(i)


for key,value in user.items():
    print(key,value)

