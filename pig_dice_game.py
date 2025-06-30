import random

def roll_dice(score):
    dice = random.randint(1, 6)
    if dice == 1:
        print('You rolled a 1! You lose your turn.')
        return 0
    else:
        score += dice
        print(f'You rolled a {dice}.')
        print(f'Now your score is: {score}')

    behavior = input('Press "r" to roll the dice or "h" to hold: ')
    if behavior == 'r':
        return roll_dice(score)
    elif behavior == 'h':
        return score
    else:
        print('Invalid input. Please try again.')
        return roll_dice(score)


def play_game():
    global count
    global A_score, B_score
    global status

    score = 0
    if count % 2 == 0:
        print('Player A\'s turn')
        A_score += roll_dice(score)
    else:
        print('Player B\'s turn')
        B_score += roll_dice(score)
    count += 1

    if A_score >= 100:
        print('Player A wins!')
    elif B_score >= 100:
        print('Player B wins!')

if __name__ == '__main__':
    print(' ### Welcome to the Pig Dice Game! ### ')
    print('Let\'s play this!\n')

    A_score = 0; B_score = 0; count = 0
    while True:
        play_game()
        if A_score > 100 or B_score >= 100:
            break
        print(f'Current scores: Player A: {A_score}, Player B: {B_score}\n')
    print('Game over! Thanks for playing.')
