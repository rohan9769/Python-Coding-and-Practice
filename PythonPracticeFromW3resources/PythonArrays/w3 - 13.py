#Write a Python program to convert an array to an ordinary list with the same items

from array import *

arr = array('i',[])
n = int(input('Enter the length of array'))
for i in range(n):
    x = int(input('Enter the element'))
    arr.append(x)

lst = arr.tolist()
print(lst)