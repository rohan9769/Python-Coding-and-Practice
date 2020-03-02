user = {
    'box' : [1,2,3,4],
    'greet':'Hey',
    'age':20
}

print('box' in user)

print('greet' in user.keys()) #will check if user dictionary has key greet,iterates over keys of the dictionary
print(20 in user.values()) #will check if user dictionary has value 20,iterates over the values of the dictionary

print(user.items()) #grabs the entire key value pair

#print(user.clear()) #clears the entire dictionary,creates an empty dictionary

user_2 = user.copy() #copies dictionary
print(user_2)

print(user.pop('age')) #returns the value of the popped key age

print(user.popitem()) #randomly pops any key value pair
print(user)

print(user.update({'box' : [1,2,3,4,5,6]})) #updates a key value
print(user)