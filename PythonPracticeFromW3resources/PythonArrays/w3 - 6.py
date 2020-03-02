# Write a Python program to get the number of occurrences of a specified element in an array.
from array import *

a = array('i',[])
n = int(input('Enter the no of elements you want'))
for i in range(n):
    x = int(input('Enter the elements'))
    a.append(x)

print(a)
ch = int(input('Enter the element to be searched for occurences'))
occurences = a.count(ch)
print('The element has occured these no of times',occurences)
