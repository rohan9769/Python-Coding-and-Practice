lst = []
n = int(input("Enter Length of List"))
for i in range(n):
    x = int(input("Enter the number"))
    lst.append(x)

print(lst)
smallest = min(lst)
print(f'Smallest Number is  {smallest}')