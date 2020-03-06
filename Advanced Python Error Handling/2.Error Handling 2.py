def sum(n1,n2):
    try:
        return n1/n2
    # except(TypeError,ZeroDivisionError):
    #     print('What even?')
    except(TypeError, ZeroDivisionError) as err:
        print(err)
        # print('What even?')

print(sum(1,0))