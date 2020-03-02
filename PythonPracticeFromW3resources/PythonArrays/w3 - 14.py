#Write a Python program to find whether a given array of integers contains any duplicate element.
# Return true if any value appears at least twice in the said array and
# return false if every element is distinct.

from array import *

arr = array('i',[])
n = int(input('Enter the length of array'))
for i in range(n):
    x = int(input('Enter the element'))
    arr.append(x)

print(arr)
for i in range(len(arr)-1):
    if arr[i] == arr[i+1]:
        print(arr[i])
        print('True')







