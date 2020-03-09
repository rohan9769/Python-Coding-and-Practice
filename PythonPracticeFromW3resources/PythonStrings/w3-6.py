# Write a Python program to get the number of occurrences of a specified element in an array

from array import *

nums = array('i',[])
n = int(input('Enter no of elements you want : '))
print('Enter the elements :-')
for i in range(n):
    x = int(input())
    nums.append(x)

ele = int(input('Enter the no whose occurences you want to search : '))
print(f'Element {ele} occurs {nums.count(ele)} times')