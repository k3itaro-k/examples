"""
guess_the_number

This function generates a random integer number between 0 and 100 .
The user have to guess the random number in a finite number of 
attempts, attempts is passed as an argument, in each attempt the 
function prints a hint about the random number.
"""
import random


def guess_the_number(attempts):
    number = random.randint(0,100)

    while attempts > 0:
        given_number = int(input('Please, give a number: '))
        
        if given_number > number:
            print(f'{given_number} is greater than my number. Try again!')
            attempts -= 1
            print(f'You have {attempts} attempts left')
        elif given_number < number:
            print(f'{given_number} is less than my number. Try again!')
            attempts -= 1
            print(f'You have {attempts} attempts left.')
        else:
            print('*'*50)
            print('Congratulations!')
            print(f'You guessed the number, {number}.')
            print('*'*50)
            break

    if attempts == 0:
        print('*'*50)
        print(f'You lose. The number is {number}')
        print('*'*50)


if __name__=="__main__":
    print('*'*50)
    print('Guess the number between 0 and 100.')
    print('You only have 5 attempts.')
    print('*'*50)
    guess_the_number(5)