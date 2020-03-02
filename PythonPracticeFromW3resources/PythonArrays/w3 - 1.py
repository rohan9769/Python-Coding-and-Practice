#Write a Python program to create an array of 5 integers and display the array items. Access individual element through indexes.
from numpy import *

a = array([1,4,6,7,9])
for i in range(len(a)):
    print(a[i])
