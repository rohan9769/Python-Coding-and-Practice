#Write a Python program to append items from a specified list.
from array import *

items = [1,2,4,5,6]

arr = array('i',[])
n = int(input('Enter no of elements'))
for i in range(n):
    x = int(input('Enter the element'))
    arr.append(x)

arr.fromlist(items) #To append list items to an array
print(arr)