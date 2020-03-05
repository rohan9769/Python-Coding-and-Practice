# Write a Python program to sum all the items in a dictionary.

dict1 = {
    'Vegetables':55,
    'Toys':33,
    'Games':44
}

total=0
for i in dict1.values():
    total = total+i

print(f'Total is: {total}')