# # With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.
# lst = [1,2,3,4,5,6,7,8,9,10]
# tup = tuple(lst)
# tp1=tup[:5]
# tp2=tup[5:]
# print(tp1)
# print(tp2)

# Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
# tup = (1,2,3,4,5,6,7,8,9,10)
# lst = []
# for i in tup:
#     if i%2==0:
#         lst.append(i)
#
# tuple_eve = tuple(lst)
# print(tuple_eve)

#Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".
# s = input()
# if s=='yes' or s=='Yes' or s=='YES':
#     print('Yes')
# else:
#     print('No')

#Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
# lst = [1,2,3,4,5,6,7,8,9,10]
# print(list(map(lambda x:x**2,lst)))

#Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].
# lst = [1,2,3,4,5,6,7,8,9,10]
# print(list(map(lambda x:x**2,filter(lambda x:x%2==0,lst))))

# #Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).
# x = []
# for i in range(20):
#     x.append(i)
#
# print(list(filter(lambda x:x%2==0,x)))
