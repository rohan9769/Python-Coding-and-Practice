#Write a Python program to remove the first occurrence of a specified element from an array

from array import *

arr = array('i',[])
n = int(input('Enter the length of array'))
for i in range(n):
    x = int(input('Enter the element'))
    arr.append(x)

print(arr)

item = int(input('Enter element whose first occurence is to be deleted'))
print(arr.count(item))

if arr.count(item)>1:
    arr.remove(item)
    print(arr)



