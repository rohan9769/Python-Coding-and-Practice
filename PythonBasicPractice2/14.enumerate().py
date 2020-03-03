#Enumerate is useful when you need an index counter
# for i,char in enumerate('Hello World'):
#     print(i,char)
#
# for i,int in enumerate([1,2,3]):
#     print(i,int)
#
#
# for i,j in enumerate((1,2,3,4)):
#     print(i,j)

#WAP to print the element at the 50th index
for i,j in enumerate(list(range(100))):
    if i == 50:
        print(i,j)