while True:
    try:
        age = int(input('Enter age'))
        10/age
    except ValueError:
        print('Enter a number')
    except ZeroDivisionError:
        print('Enter number more than 0')
    else:
        print('Thanks')
        break
    finally: #finally block executes regardless at the end of everything
        print('Ok,I am done')