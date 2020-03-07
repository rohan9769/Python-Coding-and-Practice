import random as r
#Generate number 1-10
answer = r.randint(1,10)

#get input from user
print('----WELCOME TO GUESS THE NUMBER GAME----')
#check if input is a no between 1 to 10
while True:
    try:
        n = int(input('Enter a number'))
        if n>=1 and n<=10:
            if n==answer:
                print('Genius,you guessed the right number!')
                break
    #     else:
    #         print('Umm 1 to 10 not more than that')
    # except ValueError:
    #     print('Enter a number')
    #     break
    finally:
        pass

