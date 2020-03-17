from array import *
arr1 = array('i',[])
n = int(input('Enter no of elements you want : '))
print('Enter the elements: -')
for i in range(n):
    x = int(input())
    arr1.append(x)
print(arr1)


for i in range(len(arr1)):
    lowest = i
    for j in range(i+1,len(arr1)):
        if arr1[j]<arr1[i]:
            lowest=j
            arr1[i],arr1[j] = arr1[j],arr1[i]

print(arr1)



