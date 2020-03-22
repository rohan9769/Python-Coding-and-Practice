#Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].
# li = [5,6,77,45,22,12,24]
# li = [x for x in li if x%2!=0]
# print(li)

#By using list comprehension, please write a program to print the list after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
# li = [5,6,77,45,22,12,24]
# li = [x for x in li if x%5!=0 and x%7!=0]
# print(li)

#By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].
# li = [12,24,35,70,88,120,155]
# li = [x for x in li[1:6:2]]
# print(li)
#OR
# li = [12,24,35,70,88,120,155]
# li = [li[i] for i in range(len(li)) if i%2 != 0]
# print(li)

#By using list comprehension, please write a program to print the list after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].
# li = [12,24,35,70,88,120,155]
# li = [li[i] for i in range(len(li)) if i<3 or i>4]
# print(li)


