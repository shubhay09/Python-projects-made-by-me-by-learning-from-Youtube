import random 

def play():
    user = input("Enter r for rock, p for paper, s for scissors: ")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return "It's a tie"

    if is_win(user, computer):
        return "YOU WON"
    else:
        return "YOU LOST"
def is_win(user, computer):
    return (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r')

a = play()
print(a)
