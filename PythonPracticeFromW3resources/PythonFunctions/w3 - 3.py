#Write a Python function to sum all the numbers in a list.

lst =[]
n = int(input('Enter length of the list'))
def muloflist(lst):
    for i in range(n):
        x = int(input('Enter the element :'))
        lst.append(x)

    print(lst)
    ans=1
    for i in lst:
        ans = ans*i

    print(ans)

muloflist(lst)





