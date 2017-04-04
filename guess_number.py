"""This is the module level Docstring..."""

def guess_number():
    import random

    computer_choice = random.randint(1, 50)
    correct = False

    while correct == False:

        human_guess = int(input('What is your guess?  '))

        if human_guess < computer_choice - 5:
            print("Way too low.  Try again.")
        elif human_guess <= computer_choice - 1:
            print('Too low, but closer.  Try again.')
        elif human_guess > computer_choice + 5:
            print("Whoa, way too high.  Try again")
        elif human_guess >= computer_choice + 1:
            print('Too high, but closer.  Try again.')
        elif human_guess == computer_choice:
            print("Correct Guess!")
            correct = True

    correct_guess = True

    computer_choice = random.randint(1, 50)

    while correct_guess == True:

        correct_guess = input('Would you like to play again?  Y/N  ')
        answer_yes = int(input('What is your guess?  '))

        if correct_guess == 'Y'.lower():
            print(answer_yes)

guess_number()
