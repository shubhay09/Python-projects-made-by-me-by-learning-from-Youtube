pp3 - computer guesses the number 
import random
def compute_guess(x):
    low = 0
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low 
        feedback = input(f" is the {guess} correct ?\nH,L,C to let the computer know if its higher,lower,correct respectively :").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    else:
        print(f"correct the computer guessed the number {guess}")

compute_guess(10)
        
