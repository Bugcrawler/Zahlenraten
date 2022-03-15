import random

# Variables
round = 0
Played = True
guessed_number = random.randint(0, 100)

# Starts round
while Played:
    round = round + 1
    print()  # just a whitespace (looks better)
    print(round)

    # Gets guess
    user_input = int(input("Please give me a number.: "))

    # Tests winning
    if user_input == guessed_number:
        print("Win!")
        Played = False
        break

    # Case 1 number was too big
    elif user_input > guessed_number:
        print("that's too much.")

   # Case 2 number was too small
    else:
        print("your number was too small.")

    #Tests loosing
    if  round == 7:
        print("How Bad! Try it again.")
        print("That's the number " + str(guessed_number))
        Played = False
        print("End")
