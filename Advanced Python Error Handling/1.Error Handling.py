#Error Handling

while True:
    try:
        age = int(input('Whats your age'))
        print(age)

    except ValueError:
        print('Enter a number not a string')

    except ZeroDivisionError:
        print('Enter age more than zero')

    else:
        print('Thank you')
        break