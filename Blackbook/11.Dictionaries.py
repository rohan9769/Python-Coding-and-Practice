# #Dictionary
# #1)Program to create a simple dictionary and print it
# dict1 = {'name':'Lewis',
#          'age':25,
#          'pole positions':44
#          }
# print(dict1)
#
# #2)Program to create a dictionary with employee details and retrieve values upon giving keys
# dict1 = {'name':'Lewis',
#          'age':25,
#          'pole positions':44
#          }
# print(dict1['name'])
# print(dict1['age'])
# print(dict1['pole positions'])
#

# #Operation on dictionaries
# dict1 = {'name':'Lewis',
#          'age':25,
#          'pole positions':44
#          }
# dict2 = {'name':'Alex',
#          'age':19,
#          'pole positions':23
#          }
# print(dict1['name']) #Returns the value of key 'name'
#
# dict2['age'] = 20 #modifies value of  age key in dict2 to 20
# print(dict2)
#
# print(len(dict1)) #returns the no of keys in dict1
#
# del dict1['age'] #del is used to delete a key-value pair,here it deletes age:25 key value pair
# print(dict1)
#
# #To check if a key is available in the dictionary or not(use 'in' and 'not in')
# print('name' in dict2) #returns true
# print('name' not in dict2) #returns false


# #Dictionary Methods:-
# dict1 = {'name':'Lewis',
#           'age':25,
#           'pole positions':44
#           }
# dict2 = {'name':'Alex',
#           'age':19,
#           'pole positions':23
#         }
#
# dict3 = dict1.copy() #Creates a new dictionary(a copy)
# print(dict3)
#
# print(dict1.get('name')) #returns value of the key specified
#
# print(dict1.items()) #returns the entire dicitionary object
#
# print(dict2.keys()) #returns all the keys
#
# print(dict2.values()) #returns all the values
#
# dict3.update(dict1) #Adds all the values of dict3 to dict1
# print(dict1)
#
# dict3.pop('name') #pops k-v pair name from dict3
# print(dict3)

# #3)Program to retrieve keys,values and key-value pairs from a dictionary
# dict = {'name':'Roger',
#         'id':44,
#         'salary':10000
#         }
#
# print(f'Keys are {dict.keys()}')
# print(f'Values are {dict.values()}')
# print(f'k-v pairs are {dict.items()}')

# #4)Program to create a dictionary and find the sum of values
# dict = eval(input('Enter the dictionary : '))
# print(dict)
# result = sum(dict.values())
# print(f'Sum is : {result}')

# #5)Program to create a dictionary from keyboard and display it[Taking dictionary from user][IMP]
# dict={}
# n = int(input('How many items you want'))
# for i in range(n):
#     k=input()
#     v=int(input())
#     dict.update({k:v})
# print(dict)

# #6)Program to create a dictionary and find the sum of values
# dict = {}
# n =int(input('Enter no of items : '))
# for i in range(n):
#     k = input()
#     v = int(input())
#     dict.update({k:v})
#
# print(dict)
# s = sum(dict.values())
# print(f'Sum is {s}')
#
# #7)Program to create a user inputted dictionary and display it
# dict = {}
# n =int(input('Enter no of items : '))
# for i in range(n):
#     k = input()
#     v = int(input())
#     dict.update({k:v})
#
# print(dict)

# #8)Program to create a dictionary with cricket players names and scores in a match and retrieve runs by entering players name
# dict = {}
# n =int(input('Enter no of items : '))
# for i in range(n):
#     k = input()
#     v = int(input())
#     dict.update({k:v})
# print(dict)
#
# p = input('Enter players name :')
# runs = dict.get(p)
# print(runs)


# #Using for loops for dictionaries:-
# #9)Program to show the usage of for loop to retrieve elements of dictionary
# dict= {'Red':'Apple','Green':'Mango','Yellow':'Pineapple'}
# #To print only keys
# for k in dict:
#     print(f'Keys are {k}')
# #To print only values
# for k in dict:
#     print(f'Values are {dict[k]}')
# #To print keys and values both
# for k,v in dict.items():
#     print(f'Key is {k} , Value is {v}')

# #10)Program to find the no of occurences of each letter in a string using dictionary
# dict = {}
# str = 'Book'
# for i in str:
#     dict[i] = dict.get(i,0)+1
#
# print(dict)
# for k,v in dict.items():
#     print(k,v)
#

# #Sorting Dictionary elements using lambdas:-sorted(dict_name.items(),key=lambda x:x[n])[n=0,sort by keys|n=1,sort by values]
# #11)Program to sort elements in a dictionary based on either keys/values
# colors = {10:'Red',11:'Green',12:'Yellow',13:'Blue'}
# sort_by_keys = sorted(colors.items(),key=lambda x:x[0])
# print(sort_by_keys)
# sort_by_values = sorted(colors.items(),key=lambda x:x[1])
# print(sort_by_values)

# #Converting list to dicitonary:-(Use zip() function)
# #12)Program to convert elements of two lists into a key value pair of dictionary
# countries = ['USA','India','China','Germany','France']
# capitals =['Washington DC','New Delhi','Beijing','Munich','Paris']
# z = zip(countries,capitals)
# print(dict(z))

# #Converting String to dictionary:-
# #13)Program to convert string into a key value pair of dictionary
# str='Vijay=23,Roger=66,Nigel=99,Rocky=67'
# lst = []
# for i in str.split(','):
#     j=i.split('=')
#     print(j)
#     lst.append(j)
# print(lst)
# print(dict(lst))

# #Passing Dictionaries to Functions:-
# #14)Function to accept a dictionary and display it
# def fun(dict):
#     for i,j in dict.items():
#         print(i,'--',j)
#
# d={'a':'Apple','b':'Ball'}
# fun(d)

# Ordered Dictionaries
# from collections import OrderedDict
# d = OrderedDict()
# d[11]='A'
# d[12]='B'
# d[13]='C'
# for k,v in d.items():
#     print(k,v)