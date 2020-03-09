# Write a Python program to reverse the order of the items in the array

from array import *

nums = array('i',[])
n = int(input('Enter no of elements you want : '))
print('Enter the elements :-')
for i in range(n):
    x = int(input())
    nums.append(x)

print(nums)
nums.reverse()
print(str(nums))