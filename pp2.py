#pp2 - guessing number game
#random 

import random 

def guess(x):
    random_no = random.randint(1, x)
    user_guess = 0  
    while user_guess != random_no:
            user_guess = int(input(f'Guess the number between 1 and {x}: '))
            if user_guess < 0:
                print("enter a positive number")
            elif user_guess < random_no:
                print("Guess again, a little high.")
            elif user_guess > random_no:
                print("Guess again, a little low.")      
    else:
        print(f'Correct! The number is {random_no}.')

guess(10)
