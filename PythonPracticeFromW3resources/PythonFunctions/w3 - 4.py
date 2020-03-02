#Write a Python program to reverse a string
str = input('Enter a string')

def reverseString(str):
    rstr = ''
    i = len(str)
    while i>0:
        rstr += str[i-1]
        i = i-1

    print(rstr)

reverseString(str)

