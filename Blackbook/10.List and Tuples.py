# #1)Program to create list with different types of elements
# lst = ['roger','cristiano',55,66]
# print(lst)

# #2)Program to create a list using range()
# #lst=list(range(9))
# lst1 = range(10)
# for i in lst1:
#     print(i)

# #3)Program to access list elements using loops
# lst = [1,2,3,4,5,6,7,8,9]
# for i in range(len(lst)):
#     print(lst[i])

# #Updating Elements in List:-(Lists are mutable)
# lst = [1,2,3,4,5,6,7,8,9]
# lst.append(10)
# print(lst)
# lst[1]=11
# print(lst)
# lst[2:4]=0,0
# print(lst)
# del lst[1] #deletes element at index 1
# print(lst)
# lst.remove(6) #deletes 6 from list
# print(lst)
# lst.reverse()
# print(lst)
# #Retrieves element starting from 0th to length of list
# i=0
# while i<len(lst):
#     print(i)
#     i=i+1

# #4)Program to access list elements using while loop
# lst = [1,2,3,4,5,6,7]
# i=0
# while i<len(lst):
#     print(lst[i])
#     i=i+1

# #5)Program to diplay elements in list in reverse order without using reverse
# days = list([x for x in input('Enter the days : ').split()])
# for i in range(len(days)):
#     i=i+1
#     print(days[-i])


# #Concatenation in Lists:-
# lst1=[1,2,3,4,5]
# lst2=[6,7,8,9,10]
# lst_tot = lst1+lst2
# print(lst_tot)

# #Repetition of Lists:-
# lst1 = [1,2,3,4,5]
# print(lst1*6)

# #Membership in List:-
# lst1 = [10,20,30,40]
# x = 20
# print(x in lst1)

# #Methods to process List:-
# #6)Progam to understand list processing
# num = [10,20,30,40,50]
# print(sum(num)) #returns sum of list
# print(num.index(20)) #returns index of 20
# num.insert(1,80) #inserts 80 at index 1
# print(num)
# num1 = num.copy() #copies num to new list num1
# print(num1)
# print(num.count(20)) #returns the no of times 20 occurs in the list
# num1.remove(40) #removes 40 from list num1
# print(num1)
# num.pop() #removes last element from the list
# print(num)
# num.sort() #sorts list in ascending order
# print(num)
# num.reverse()
# print(num)

# #7)Program to Find biggest and smallest from the list
# lst = list([int(x) for x in input('Enter the numbers:').split()])
# print(lst)
# print(max(lst))
# print(min(lst))

# #Sorting Lists:-
# #8)Program to sort list of elements using bubble sort
# a = []
# n = int(input('Enter no of elements : '))
# for i in range(n):
#     x = int(input())
#     a.append(x)
# print(a)
# flag = False
# for i in range(len(a)):
#     for j in range(n-1-i):
#         if a[j]>a[j+1]:
#             temp = a[j]
#             a[j] = a[j+1]
#             a[j+1] = temp
#             flag = True
#     if flag==False:
#         break
#     else:
#         flag=False
#
# print(f'Sorted array is {a}')


# #Counting no of occurences of element in the list:-
# #9)Program to know how many times an element occured in a list without using count() method
# lst = []
# n = int(input('Enter no of elements you want : '))
# for i in range(n):
#     x = int(input())
#     lst.append(x)
#
# print(f'List is : {lst}')
# ctr=0
# c = int(input('Enter element to be counted : '))
# for i in range(len(lst)):
#     if lst[i]==c:
#         ctr+=1
#
# print(f'{c} occurs {ctr} times in the list')

# #10)Program to know how many times an element occured in a list using count method
# lst=[2,3,4,4,2,2,3]
# print(lst.count(3))

# #Finding Common elements between two lists
# lst1 = [1,2,3,4]
# lst2 = [3,4,5,6]
# """Converting list to set"""
# s1 = set(lst1)
# s2 = set(lst2)
# print(s1.intersection(s2))


# #Nested List
# #11)Program to create a nested list and display its elements
# lst=[10,20,30,40,[50,60,70]]
# print(lst[4])
# for i in lst[4]:
#     print(i)

# #Nested List as a Matrix:-
# #12)Program to retrieve elements of matrix
# mat = [[1,2,3],[4,5,6],[7,8,9]]
# #to display rows
# for i in range(len(mat)):
#     print(mat[i])
# #to display each column element in row 0
# for i in mat[0]:
#     print(i)
# #to display each column element in row 1
# for i in mat[1]:
#     print(i)
# #to display all elements using for
# for i in mat:
#     for c in i:
#         print(c)

# #List Comprehension:
# #13)Program to create a list of squares of no
# #squares = [x**2 for x in range(10)]

# #14)Program to create a list of squares of no and retrieve only even nos
# lst = [x**2 for x in range(10) if x%2==0]
# print(lst)
#
# #15)Program to add two lists using list comprehension
# x = [10,20,30]
# y = [40,50,60]
# lst = [i+j for i in x for j in x]
# print(lst)
#
# #16)Program to retrieve first letter of each word in a list
# words = ['Apple','Orange','Grapes','Peach']
# lst = [w[0] for w in words]
# print(lst)


# #Tuples(immutable):
# #Creating Tuples:-
# tup = () #empty tuple
# tup1 = (1,2,3)
# tup2 = (1,2,-1,'china','usa')
# tup3 = 12,3,4,5,6
# print(tup3)

# #Accessing tuples
# tup = 1,5,7,3,2
# print(tup[0]) #prints 1
# print(tup[-1]) #prints 2
# print(tup[1:3]) #prints 5,7
# print(tup[:]) #prints all
# print(tup[::2]) #prints the tuple with stepsize 2

# #Operation on Tuples:-(finding length,concatenation,membership,repetition and iteration)
# tup = (10,20,30,40,50,50)
# print(len(tup))
# print(10 in tup)
# print(tup*3)

# #Tuple functions:-
# t = (1,7,4,5,7,8)
# print(len(t))
# print(min(t))
# print(max(t))
# print(t.count(7))
# print(t.index(4)) #returns index of element 4

# #17)Program to accept elements in form of a tuple and display sum and average
# lst = []
# n = int(input('Enter no of elements'))
# for i in range(n):
#     x = int(input())
#     lst.append(x)
# tup = tuple(lst)
# print(tup)
# sum = 0
# for i in range(len(tup)):
#     sum = sum+tup[i]
# avg = sum/n
# print(f'Sum is {sum} and average is {avg}')

# #18)Program to find first occurence of element in tuple
# num = eval(input('Enter the nos'))
# x = int(input('Enter the element to be searched for occurence'))
# for i in range(len(num)):
#     if x==num[i]:
#         print(f'First occurs at {i}')
#         break
#
#
# #Nested Tuples:-
# nst = (1,2,3,4,5,(6,7,8,9))

#Sorting Nested Tuples:-(sorted(tuple,key=lambda x:x[0])
tup = ((10,'Lionel'),(7,'Cristiano'),(44,'Lewis'),(46,'Valentino'))
print(sorted(tup)) #by default sorts by integer
print(sorted(tup,key=lambda x:x[1])) #Sorts by name as x[1]=name

a = [1,2,3,4]
for i in range(len(a)):
    print(a[i])