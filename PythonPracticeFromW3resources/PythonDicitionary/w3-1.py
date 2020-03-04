# Write a Python script to sort (ascending and descending) a dictionary by value.

def func_sortAsc(list):
    return sorted(list)

def func_sortDesc(list):
    return sorted(list,reverse=True)

print(func_sortAsc([2,1,3,4,5]))
print(func_sortDesc([1,2,3,4,5,6]))