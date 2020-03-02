#Write a Python program to remove a specified item using the index from an array
from array import *

arr = array('i',[])
n = int(input('Enter the length of array'))
for i in range(n):
    x = int(input('Enter the element'))
    arr.append(x)

z = int(input('Enter index from where the element is to be removed'))
arr.pop(z)
print(arr)