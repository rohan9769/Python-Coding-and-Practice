#Write a Python program to insert a new item before the second element in an existing array.

from array import *

arr = array('i',[])
n = int(input('Enter the length of array'))
for i in range(n):
    x= int(input('Enter the element :'))
    arr.append(x)
print(arr)
item = int(input('Enter item to be inserted'))
arr.insert(1,item)
print(arr)