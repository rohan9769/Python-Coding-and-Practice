#WAP to find sum of a list
lst = []
n = int(input("Enter no of elements"))
print("Enter the elements")
ctr = 0
for i in range(n):
    ctr = ctr+1
    x = int(input())
    lst.append(x)

print(lst)
c = sum(lst)
print(f'Sum of list is {c} and no of elemetns are {ctr}')


