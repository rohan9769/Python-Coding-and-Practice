#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
str = input("Enter String")


def countUppLow(str):
    upp = 0
    low = 0
    for i in str:
        if i.isupper():
            upp = upp+1

        elif i.islower():
            low = low+1


        else:
            pass
    print(upp)
    print(low)

countUppLow(str)






