import random as rd

def roll_dice():
    count = 0
    value = 0
    while True:
        result = rd.randint(1, 6)
        if result == 1:
            print("You rolled a 1! Game over.")
            return value
        print("The number on the dice is:", result)
        count += 1
        choose = input('Press "r"(roll) or "h"(hold).')
        if choose == 'h':
            return value
        elif choose == 'r':
            value += result
            continue
        else:
            print("Invalid input. Please enter 'r' to roll or 'h' to hold.")
            continue