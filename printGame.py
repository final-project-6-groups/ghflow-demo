from dice import roll_dice

def print_game():
    while True:
        player1_score = roll_dice()
        print("Player 1's score is:", player1_score)

        if player1_score >= 50:
            print("Player 1 wins!")
            return
        
        player2_score = roll_dice()
        print("Player 2's score is:", player2_score)

        if player2_score >= 50:
            print("Player 1 wins!")
            return
        
def main():
    print_game()    

if __name__ == "__main__":
    main()