# Dictionary is an unordered key value pair
dictionary = {
        'a':[1,2,3],
        'b':'Hey',
        'c':True
}

mylist = [
    {
        'a':[1,2,3],
        'b':'Hey',
        'x': True
    },
    {
        'a':[4,5,6],
        'b':'HEELO',
        'x': False
    }
]
print(dictionary['b'])
print(dictionary['a'][0]) #returns 1 from list
print(mylist[0]['a'][2])
