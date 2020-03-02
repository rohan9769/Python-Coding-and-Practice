user = {
    'box' : [1,2,3,4],
    'greet':'Hey',
    'age':20
}

print(user.get('box')) #get() is used to retrieve values
print(user.get('age',55)) #this means grab the age from the dictionary but if it does not exist use the age as 55

#Another way to create a dictionary
user_2 = dict(name= 'JohnTron')
print(user_2)