import random

print("""Welcome to Mastermind. The codemaker has generated a random sequence of four colored pegs.
You are the codebreaker. Your goal is to correctly guess the colors and order of these pegs in 10 guesses or less.
For each peg in your guess whose color appears in the codemaker's sequence, the codemaker will respond with a white peg.
For each peg in your guess whose color and position are the same in the codemaker's sequence,
he will respond with a black peg. Good luck.""")

guess_count = -1

while guess_count == -1:
    peg_colors = ["red", "blue", "green", "purple", "pink", "orange"]
    codemaker_sequence = random.choices(peg_colors, k = 4)
    codemaker_position_0 = codemaker_sequence[0]
    codemaker_position_1 = codemaker_sequence[1]
    codemaker_position_2 = codemaker_sequence[2]
    codemaker_position_3 = codemaker_sequence[3]
    guess_count = guess_count + 1

while guess_count in range(0,11):
    print("The possible peg colors are: red, blue, green, purple, pink, orange.")
    print("Please type your guess for position one's peg color")
    guess_position_0 = input("")
    print("Please type your guess for position two's peg color")
    guess_position_1 = input("")
    print("Please type your guess for position three's peg color")
    guess_position_2 = input("")
    print("Please type your guess for position four's peg color")
    guess_position_3 = input("")

    if codemaker_position_0 == guess_position_0:
        print("black")
        wrong_0 = False
    elif codemaker_position_0 == guess_position_1 or codemaker_position_0 == guess_position_2 or \
            codemaker_position_0 == guess_position_3:
        print("white")
        wrong_0 = False
    else:
        print()
        wrong_0 = True

    if codemaker_position_1 == guess_position_1:
        print("black")
        wrong_1 = False
    elif codemaker_position_1 == guess_position_0 or  codemaker_position_1 == guess_position_2 \
            or codemaker_position_1 == guess_position_3:
        print("white")
        wrong_1 = False
    else:
        print()
        wrong_1 = True

    if codemaker_position_2 == guess_position_2:
        print("black")
        wrong_2 = False
    elif codemaker_position_2 == guess_position_0 or codemaker_position_2 == guess_position_1 \
            or codemaker_position_2 == guess_position_3:
        print("white")
        wrong_2 = False
    else:
        print()
        wrong_2 = True

    if codemaker_position_3 == guess_position_3:
        print("black")
        wrong_3 = False
    elif codemaker_position_3 == guess_position_0 or codemaker_position_3 == guess_position_1 or \
            codemaker_position_3 == guess_position_2:
        print("white")
        wrong_3 = False
    else:
        print()
        wrong_3 = True

    if wrong_0 and wrong_1 and wrong_2 and wrong_3 == True:
        print ("Sorry, none of your guesses were right at all. Try again,")
        guess_count = guess_count + 1
    elif codemaker_position_0 == guess_position_0 and codemaker_position_1 == guess_position_1 and \
            codemaker_position_2 == guess_position_2 and codemaker_position_3 == guess_position_3:
        print("Congratulations! You cracked the code.")
        guess_count = 11
    else:
        print("Getting there! Keep guessing.")
        guess_count = guess_count + 1

    while guess_count == 11:
        print("The game has finished. Play again? (yes/no)")
        play_again = input()
        if play_again == "no":
            print("Ok, thanks for playing. -Evan")
            break
        else:
            guess_count = -1








