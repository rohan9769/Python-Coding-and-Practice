# Write a Python program to multiply all the items in a dictionary.
dict1={}

# n = int(input('Enter no of items you want'))
# d={}
# for i in range(n):
#     keys = int(input())
#     values = input().split()
#     d[i] = values
#
# print(d)
dict1 = {
    'Vegetables':55,
    'Toys':33,
    'Games':44
}

product=1
for i in dict1.values():
    product = product*i

print(f'Product is: {product}')
