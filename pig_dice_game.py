import random

def roll_dice(score):
    pass

def play_game():
    pass

if __name__ == '__main__':
    print(' ### Welcome to the Pig Dice Game! ### ')
    print('Let\'s play this!\n')

    A_score = 0; B_score = 0; count = 0
    While True:
        play_game()
        if A_score > 100 or B_score >= 100:
            break
        print(f'Current scores: Player A: {A_score}, Player B: {B_score}\n')
    print('Game over! Thanks for playing.')
