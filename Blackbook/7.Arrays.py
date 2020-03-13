from array import *
from numpy import *
# #arrayname = array('typecode',[elements])
# #typecode = i-unsigned integer,
#             I- signed integer,
#             f - float,
#             d - double,
#             u - unicode character,
#             b - signed integer,
#             B - unsigned integer

# #1)Program to create integer array
# arr1 = array('i',[1,2,3,4,5])
# print(arr1)
#
# #2)Program to create an array of characters
# arr1 = array('u',['a','b','c'])
# print(arr1)

# #3)Program to create one array from another array
# arr1 = array('i',[1,2,3,4,5,6])
# arr2 = array(arr1.typecode,(a for a in arr1))
# for i in arr2:
#     print(i)

# #Indexing and Slicing :-
# #4)Program to retrieve elements of an array using index
# arr1 = array('i',[1,2,3,4,4,5,6,7])
# for i in range(len(arr1)):
#     print(arr1[i])

# #5)Program to retrieve elements of an array using index and while loop
# arr1 = array('i',[1,2,3,4,4,5,6,7])
# i=0
# while i<len(arr1):
#     print(arr1[i])
#     i=i+1

# #6)Program demonstrating effects of slicing operation(arrayname[start:stop:stride]
# #Create array y with elements from 1st to 3rd from x
# x = array('i',[10,20,30,40,50,60,70,80])
# y = x[1:4]
# print(y)
# #Create array y with elements from 0th till last element from x
# y=x[0:]
# print(y)
# #Create array y with elements from 0th to 3rd from x
# y=x[0:4]
# print(y)
# #Create array y with last 4 elements from x
# y=x[-4:]
# print(y)
# #Create y with 0th to 7th element from x with stride 2
# y=x[0:7:2]
# print(y)

# #7)Program to retrieve and display only a range of elements using slicing
# arr1 = array('i',[1,4,5,6,7,8,9])
# for i in arr1[2:4]:
#     print(i)

# #Array Methods :-

# #8)Program demonstrating various array methods
# arr1 = ['i',[1,2,3,4,5]]
# arr2 = ['i',[5,6,7,8,9]]
# #appending 30 to arr1
# arr1.append(30)
# print(arr1)
# #inserting 99 at position 1 in arr1
# arr1.insert(99,1)
# print(arr1)
# #removing an element from array
# arr1.remove(1)
# print(arr1)
# #removing last element[pop() method]
# arr2.pop()
# print(arr2)
# #finding position of an element using index() method
# print(arr2.index(7))
# #Converting array to a list using tolist method
# lst = arr1.tolist()
# print(lst)

# #9)Program to store students marks in an array,finding total marks and percentage scored
# subjects = int(input('Enter no of subjects'))
# marks = []
# total_marks = 100*subjects
# summ=0
# for i in range(subjects):
#     x = int(input())
#     marks.append(x)
#
# for i in range(len(marks)):
#     summ = summ+marks[i]
#
# percentage = (summ/total_marks)*100
# print(f'Total marks scored are {summ} and percentage is {percentage}')

# #10)Bubble Sort
# #temp=a
# #a=b
# #b=temp
# arr1 = array('i',[])
# print('How many elements you want')
# n = int(input())
# for i in range(n):
#     x = int(input())
#     arr1.append(x)
# print(arr1)
# flag = False
# for i in range(n-1):
#     for j in range(n-1-i):
#         if arr1[j]>arr1[j+1]:
#             t = arr1[j]
#             arr1[j] = arr1[j+1]
#             arr1[j+1] = t
#             flag = True
#     if flag==False:
#         break
#     else:
#         flag=False
# print(f'Sorted Array : {arr1}')

# #11)Program to search for the position of an element in an array using sequential search
# arr1 = array('i',[])
# print('How many elements you want')
# n = int(input())
# for i in range(n):
#      x = int(input())
#      arr1.append(x)
# print(arr1)
#
# s = int(input('Enter element to be searched : '))
# for i in range(len(arr1)):
#     if s == arr1[i]:
#         print(f'Element found at position {i+1}')
#         break
#     else:
#         print('Element not Found')


# NumPy
# #Working with arrays using numpy :-
# #12)Program to create an array using numpy
# arr1 = array([1,2,3,4,5])
# print(arr1)
#
# #13)Program to create a character type array
# arr1 = array(['a','b','c','d'])
# print(arr1)
#
# #14)Program to create a string type array using numpy
# arr1 = array(['roger','nadal','williams'])
# print(arr1)
#
# #15)Program to create a new array from another array
# arr1 = array([5,6,7,8,9])
# b = array(arr1)
# print(arr1)
# print(b)

# #Using linspace() to create arrays :- linspace(start,stop,in how many parts to divide)
# #16)Program to create an array with 5 equal parts using linspace()
# a = linspace(0,10,5)
# print(a)
#
# #Using logspace() to create arrays :-
# #17)Program to create an array with logspace()
# a = logspace(1,4,5)
# print(a)

# #Using arange() to create arrays :- arange(start,stop,stepsize)
# #18)Program to create an array of even no
# a = arange(2,11,2)
# print(a)
#
# #Mathematical operations on numpy arrays[pg175]
# #19)Program demonstrating various mathematical functions in numpy arrays
# a = array([10,20,30.5,-40])
# print(a+5)
# print(a-5)
# print(a%5)
# print(a/5)
# print(sin(a))
# print(cos(a))
# print(tan(a))
# print(max(a))
# print(min(a))
# print(sum(a))
# print(mean(a)) #prints average of array

# #Comparing numpy arrays
# #20)Program to compare two arrays and display boolean result
# a = array([1,2,3,0])
# b = array([0,2,3,1])
# c = a==b
# print(c)
# c = a>b
# print(c)
# c = a<b
# print(c)
#
# #21)Program demonstrating any() and all()
# a = array([1,2,3,0])
# b = array([0,2,3,1])
#
# c = a>b
# print(any(c)) #similar to Logical OR
# print(all(c)) #similar to Logical AND

# #22)Program to compare corresponding elements of two arrays and retrieve the biggest array using where()
# #where(condition,expr 1,expr 2)
# a = array([1,2,3,0])
# b = array([0,2,3,1])
#
# c = where(a>b,a,b) #checks if a>b
# print(c)

# #23)Program to retrieve non zero elements from numpy array using nonzer()
# a = array([0.5,0,2,3])
# c = nonzero(a)
# for i in c:
#     print(i)
# print(a[c])

# #Viewing and Copying Array :-
# #24)Program to create view of existing Array #In view both the arrays are mirror images of each other meaning if an element is changed in new array it will also reflect in the original array
# a = array([1,2,3,4,5])
# b = a.view()
# print('Before Modification')
# print(a)
# print(b)
# b[0] = 99
# print('After Modification')
# print(a)
# print(b)
#
# #25)Program to copy an array as another array
# a = array([1,2,3,4,5])
# b = a.copy()
# print('Before Modification')
# print(a)
# print(b)
# b[0] = 99
# print('After Modification')
# print(a)
# print(b)
#
# #Slicing and Indexing in numpy arrays
# #26)Program demonstrating slicing and indexing in numpy array
# a = arange(10,16)
# print(a)
# #retrieve from 1st element to one element prior to 6th element in stepsize 2
# b=a[1:6:2]
# print(b)
# #retrieve all elements from a
# b=a[0:]
# print(b)
#
# #27)Program to retrieve and display elements of numpy array using index
# a = array([3,4,5,6,7])
# for i in range(len(a)):
#     print(a[i])

# #Dimensions of Array[185] :-
# #28)Create a 2D array of 2 rows and 3 columns
# a = array([[1,2,3],[4,5,6]])
# print(a)
#
# #Attributes of numpy arrays[186] :-
# #a = array([[1,2,3],[4,5,6]])
# print(a.ndim)
# print(a.shape)
# print(a.size)
# print(a.itemsize)
# print(a.dtype)
# print(a.nbytes)
# b = a.reshape(3,2)
# print(b)
# c=a.flatten()
# print(c)

# #Multidimensional Arrays[189]:-
# #29)Program to create multidimensional array using array() fn
# a = array([[1,2,3],
#            [4,5,6]])
# print(a)

# #30)Program to create multidimensional array using reshape() fn
# a = array([1,2,3,4,5,6,7,8])
# c = a.reshape(2,4)
# print(c)

# #Indexing in Multidimensional Arrays[192]:-
# #31)Program to retrieve elements from a 2D array
# a = [[1,2,3],[4,5,6],[7,8,9]] #3x3 matrix
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j])
#
# print(a[0][2]) #prints 3

# #Slicing in Multidimensional Array[194]:-
# a = [[1,2,3],[4,5,6],[7,8,9]]
# a = reshape(a,(3,3))
# print(a)
# #Display 0th row
# print(a[0])
# #Retrieve 0th row and 0th column element
# print(a[0:1,0:1]) #retrieves 1
# #Retrieve 1st row and 2nd column element
# print(a[1:2,1:2]) #retrieves 5
# #Retrieve 2nd row and 2nd column element
# print(a[2:3,1:2]) #retrieves 8
# #Retrieve top 2 rows
# print(a[0:2,0:3])

# #Matrices in NumPy[196]:-
# #32)Program to create a 2D Matrix
# a = [[1,2,3],[4,5,6]]
# b = matrix(a)
# print(b)
#
# #33)Program to create a 2D Matrix v2
# a = matrix([[1,2,3],[4,5,6]])
# print(a)

# #34)Program to get diagonal elements of matrix
# a = matrix([[1,2,3],[4,5,6],[7,8,9]])
# print(a)
# d = diagonal(a) #or a.diagonal() also works
# print(f'diagonal elements are : {d}')

# #35)Program to get the Maximum and Minimum elements of Matrix
# a = matrix([[1,2,3],[4,5,6],[7,8,9]])
# print(a)
# max = a.max()
# min = a.min()
# diag = a.diagonal()
# print(f'Maximum is {max} and Minimum is {min}')
# print(diag)

# #36)Program to calculate sum and average of all the elements in the Matrix
# a = matrix([[1,2,3],[4,5,6],[7,8,9]])
# sum_of_elements = a.sum()
# avg = a.mean()
# print(f'Sum is {sum_of_elements} and average is {avg}')

# #37)Program to calculate the product of elements in the matrix(198)
# a = matrix([[1,2,3],[4,5,6],[7,8,9]])
# print(f'Product of elements is {a.prod()}')
# print(f'Matrix of Product of elements columnwise  is {a.prod(0)}')
# print(f'Matrix of Product of elements done rowise is {a.prod(1)}')

# #Sorting Matrix[199]:- #sort(matrixname,axis)[axis=0 means sort columnwise,1 means rowwise]
# #38)Program to demonstrate sorting in Matrix
# a = matrix([[5,4,1],[2,7,0]])
# print(a)
# print(sort(a,axis=0)) #sorts elements columnwise
# print(sort(a,axis=1)) #sorts elements rowwise
# print(sort(a)) #if no axis is given,sorts element rowwise

# # #Transpose of Matrix[200]:-
# # #39)Program to demonstrate transpose in matrix
# # a = matrix([[1,2,3],[4,5,6],[7,8,9]])
# # print(a)
# # print(a.transpose())
#
# #40)Program to accept matrix from user and display its transpose matrix
# r,c = [int(a) for a in input('Enter no of rows and cols').split()]
# str = input('Enter the elements')
# m = reshape(matrix(str),(r,c))
# print(m)
# x = m.transpose()
# print(x)

# # Matrix Addition and Multiplication[201]:-
# #41)Program to accept two matrix and display sum of the matrix
# r1,c1 = [int(a) for a in input('Enter rows and cols').split()]
# str1 = input('Enter the elements : ')
# m1 = reshape(matrix(str1),(r1,c1))
# print(f'Matrix 1 :{m1}')
# r2,c2 = [int(a) for a in input('Enter rows and cols').split()]
# str2 = input('Enter the elements : ')
# m2 = reshape(matrix(str2),(r2,c2))
# print(f'Matrix 2 :{m2}')
# addition = m1+m2
# print(addition)

# #42)Program to accept two matrix and display product of the matrix
# r1,c1 = [int(a) for a in input('Enter rows and cols').split()]
# str1 = input('Enter the elements : ')
# m1 = reshape(matrix(str1),(r1,c1))
# print(f'Matrix 1 :{m1}')
# r2,c2 = [int(a) for a in input('Enter rows and cols').split()]
# str2 = input('Enter the elements : ')
# m2 = reshape(matrix(str2),(r2,c2))
# print(f'Matrix 2 :{m2}')
# multiplication = m1*m2
# print(multiplication)


