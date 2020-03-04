even = []
def highest_even(list):
    for i in list:
        if i%2 == 0:
            even.append(i)

    print(max(even))

highest_even([10,2,3,4,8,11])