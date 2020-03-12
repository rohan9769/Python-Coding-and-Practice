#temp = a
#a = b
#b = temp
from array import *
arr1 = array('i',[])
n = int(input('Enter no of elements you want : '))
print('Enter the elements: -')
for i in range(n):
    x = int(input())
    arr1.append(x)

print(arr1)
flag = True
for i in range(n-1):
    for j in range(n-1-i):
        if arr1[j]>arr1[j+1]:
            temp = arr1[j]
            arr1[j] = arr1[j+1]
            arr1[j+1] = temp
            flag = True
    if flag==False:
            break
    else:
        flag=False

print(arr1)


