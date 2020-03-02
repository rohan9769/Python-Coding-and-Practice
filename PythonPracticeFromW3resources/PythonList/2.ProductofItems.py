lst = []
n = int(input("Enter Length of List"))
for i in range(n):
    x = int(input("Enter the number"))
    lst.append(x)

print(lst)
prod = 1
for i in lst:
    prod = prod * i

print(f'The product of elements is {prod}')