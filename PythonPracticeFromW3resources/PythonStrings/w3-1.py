# Write a Python program to create an array of 5 integers and display the array items.
# Access individual element through indexes

from array import *

nums = array('i',[1,2,3,4,5])
print(nums)

for i in range(len(nums)):
    print(nums[i])