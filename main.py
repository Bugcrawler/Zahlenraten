# imported modules
import random

# Variables
Game_round = 0
Played = True
guessed_number = random.randint(0, 100)

# Starts the round.
while Played:
    Game_round = Game_round + 1
    print()  # just a whitespace (looks better)
    print("guess number:", game_round)

    # Gets the guess guess.
    user_input = int(input("Please give me a number.: "))

    # Tests winning condition
    if user_input == guessed_number:
        print("You win!")
        Played = False
        break

    # Case 1: The guessed number is too big.
    elif user_input > guessed_number:
        print("Your number is too much.")

    # Case 2: The guessed number is too small.
    else:
        print("Your number is too small.")

    # Tests loosing condition
    if game_round == 7:
        print("How Bad!")
        print("Try again.")
        print("That's the number:" + str(guessed_number))
        Played = False
        print("End!")
