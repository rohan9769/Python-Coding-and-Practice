# #1)Python program to access each element of string in forward and reverse direction
# str = 'Core Python'
# print('Forward order :-')
# for i in str:
#     print(i)
#
# print('Reverse order :-')
# for i in str[::-1]:
#     print(i)

# #String Slicing:- [start,stop,stepsize]
# str = 'Core Python'
# #Access String from 0th to 8th element in step of 1
# print(str[0:9:1])
# #Access String from 0th to last character
# print(str[0:])
# #Access from str[2] to str[3] in step of 1
# print(str[2:4:1])
# #Access entire string in step of 2
# print(str[::2])
# #Access string from str[2] to the ending
# print(str[2:])
# #Access string from str[0] to str[3] in step of 1
# print(str[0:4:1])
# #Access string from str[-4] to str[-2]
# print(str[-4:-1])
# #Access string from str[-6] till the ending
# print(str[-6:])
#
# #Repeating Strings:-
# str = 'Core Python'
# print(str*2)

# #Concatenate Strings:-
# str = 'Core Python'
# str1 = 'is awesome'
# print(str+' '+str1)

# #2)Program to check wether a substring exists in the string or not
# str = input('Enter String')
# sub = input('Enter substring')
# #print(str.__contains__(sub)) #shortcut
# if sub in str:
#     print('True')
# else:
#     print('False')
#
# #3)Program demonstrating comparison of strings
# str1 = 'Boy'
# str2 = 'Box'
# if str1==str2:
#     print('True')
# else:
#     print('False')

# #4)Program demonstrting removal of spaces from the string
# str = 'Mukesh Deshmukh'
# print(str.strip())  #removes space from both side of the string
# print(str.lstrip()) #removes spaces from left of the string
# print(str.rstrip()) #removes spaces from right of the string

# #5)Program to find the first occurence of substring in a string
# str = input('Enter a String')
# sub = input('Enter substring to find')
# n = str.find(sub,0,len(str))
# if n==-1:
#     print('Substring not found')
# else:
#     print(f'Substring found at index {n}')

# #6)Program to find the first occurence of substring in a string using index()
# str = input('Enter a String')
# sub = input('Enter substring to find')
# n = str.index(sub,0,len(str))
# if n==-1:
#     print('Substring not found')
# else:
#      print(f'Substring found at index {n}')

# #7)Program to find all occurences of substring in a given string
# str = input('Enter a String')
# sub = input('Enter substring to find')
# i=0
# n=len(str)
# flag = False
# while i<n:
#     pos = str.find(sub,i,n)
#     if pos!=-1:
#         print(f'Found at index {i+1}')
#         i = pos+1
#         flag=True
#     else:
#         i=i+1
# if flag==False:
#     print('Not Found')
#
# #8)Program to count substring in a given string,count()
# str = 'This is a book'
# print(str.count('is'))

# #9)Program to replace a string with another string,replace()
# str = 'This is a book'
# str1 = str.replace('book','ball')
# print(str1)

# #10)Program to demonstrate split() and join() in string
# #n = [int(x) for x in input('Enter the numbers').split(',')]
# #print(n)
# str = 'Red,blue,green'
# str1 = str.split(',')
# print(str1)
# str2 = ','.join(str1) #seprator.join(str)
# print(str2)

# #11)Program to demonstrate changing case of strings, upper(),lower()
# str = 'HeY EverYOne'
# print(str.upper())
# print(str.lower())

# #12)Proogram to check starting and ending of the string, startswith(),endswith()
# str = 'This is Python'
# print(str.startswith('This')) #str.startswith(substring)
# print(str.endswith('on')) #str.endswith(substring)

#String Testing Methods:-
# str1='HEYWASSUP'
# print(str1.isupper())
# str2 = '100'
# print(str2.isdigit())
# str2='CR7'
# print(str2.isalnum())
# str3='This Is Title'
# print(str3.istitle()) #returns true if each word in the string starts with capital letter
# str4='hello'
# print(str4.islower())
# str5='AbcD'
# print(str5.isalpha())
# str6='5.6'
# print(str6.isdecimal())
# str7 = '   '
# print(str7.isspace())

#String Formatting[227]:-
# name = 'Roger'
# print(f'Name is {name}')
# print('Name is {}'.format(name))

# #Working with characters[228]:-
# str = 'Hello World'
# ch = str[0]
# print(ch)
# ch1=str[0:1]
# print(ch1)
#                     #String Testing methods can also be applied to characters

# #13)Program to know the type of character entered by the user
# str = input('Enter a character')
# ch = str[0]
# if ch.isalnum():
#     if ch.isalpha():
#         print('Its an alphabet')
#         if ch.isupper():
#             print('The alphabet is capital')
#         else:
#             print('The alphabet is small')
#     else:
#         print('Its a number')
# elif ch.isspace():
#     print('Its a space')
# else:
#     print('It may be a special character')

# #Sorting Strings[229]:- #str.sort(),does not retain OG string #sorted(str),retains the original string
# #14)Program to sort a group of strings in alphabetical order
# str = [x for x in input('Enter strings').split()]
# str_sorted = sorted(str)
# print(str_sorted)

# #Searching in a String[230]:-
# #15)Program to search for the position of a string in a group of strings
# str = [x for x in input('Enter the strings').split()]
# str_search = input('Enter String to be searched : ')
# for i in range(len(str)):
#     if str[i]==str_search:
#         print(f'Found at {i}')

# #Finding number of characters and words[231]:-
# #16)Program to find the length of string without using len()
# str = [x for x in input('Enter the strings').split()]
# i = 0
# for s in str:
#     print(str[i],end='')
#     i = i+1
# print(i)

# #17)Program to find no of words in a string
# str = [x for x in input('Enter the strings').split()]
# i=c=0
# for s in str:
#     if str[i]==' ':
#         c = c+1
#         #i=i+1
#     else:
#         pass
#     i =i+1

# #18)Program to insert a substring into a string
# str = [x for x in input('Enter the strings').split()]
# sub = input('Enter substring to be inserted :')
# str.append(sub)
# print(str)
# print(' '.join(str))


