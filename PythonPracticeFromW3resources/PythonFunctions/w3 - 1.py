#Write a Python function to find the Max of three numbers
a=int(input('Enter 1st number'))
b=int(input('Enter 2nd number'))
c=int(input('Enter 3rd number'))
def max(a,b,c):
    if a>b and a>c:
        print('Greatest is {}' .format(a))

    elif b>a and b>c:
        print('Greatest is {}' .format(b))

    else:
        print('Greatest is {}' .format(c))


max(a,b,c)
