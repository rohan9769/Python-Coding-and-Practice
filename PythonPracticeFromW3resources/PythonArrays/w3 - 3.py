#Write a Python program to reverse the order of the items in the array.
from array import *

a = array('i',[])
n = int(input('Enter the no of elements'))
for i in range(n):
    x = int(input('Enter the element'))
    a.append(x)

print(a)
print("Array after reversing : ")
a.reverse()
print(a)
