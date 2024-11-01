"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""
# Importing the random module
import random

# start_game function. This is where the logic of the game is 
def start_game():

    # This prints out the welcome message
    print("_____________________________________________\n\n","\u27E3 ","- WELCOME TO THE NUMBER GUESSING GAME -","\u27E2","\n_____________________________________________\n")

    # list that keeps track of how many guesses the player makes in each round. The lowest value in this list is the "Best Score"
    guesses_per_round = []

    # function that handles the logic and exception handling for the player guesses. 
    # It creates a variable for the users input, and makes sure that it is an integer and is within range.
    def guess():
        while True:
            try:
                number_picked = int(input("Pick a number between 1 and 10: "))
                if number_picked <= 0 or number_picked >= 11:
                    raise Exception("That number is out of range. Try again.")
            except ValueError:
                print("Please enter a number.")
            except Exception as e:
                print(e)
            else:
                return number_picked
                break
    
    # function that handles the replay functionality and exceptions for the input.
    # list of accepted values for the exception to check against, anything else throws an error.
    # If the player wants to play again it calls the "loop" function, and lets the player know what the "best score" for this session is, 
    # if not it exits the game, providing a game ending message for the player
    def replay():
        answer_list = ['y','yes','n','no']
        while True:
            try:
                play_again = input("Would you like to play again? [Y]es/[N]o: ")
                if play_again.lower() not in answer_list:
                    raise Exception("Please enter [Y]es/[N]o")                  
            except ValueError:
                print('Please enter a [Y]es or [N]o.')
            except Exception as e:
                print(e)    
            if play_again.lower() == 'y' or play_again.lower() == 'yes':
                best_score = min(guesses_per_round)
                print("\n\nThe best score so far is {}".format(best_score))
                loop()            
            elif play_again.lower() == 'n' or play_again.lower() == 'no':
                print("\nThe game is ending, see you next time!")
                exit()

    # This is the main loop for the game. I wanted to keep this separate so each new round doesn't display the welcome message.
    # generates a winning number (solution), and calls the "guess" function to continuously prompt the player. It checks the player's input against the solution.
    # guess_count holds the amount of guesses it takes the player to guess correctly.
    # provides the player correct feedback and increments the guess_count.
    # When the player's guess is correct, it shows the number of attempts it took, and adds that number to the "guess_per_round" list to get the "best score"
    # Then it calls the "replay" function to ask if the player wants to start a new round of guessing or not
    def loop():
        solution = random.randrange(1,11)
        guess_count = 0
        while True:
            number_picked = guess()
            if number_picked > solution:
                guess_count += 1
                print("It is lower!")
            elif number_picked < solution:
                guess_count += 1
                print("It is higher!")
            elif number_picked == solution:
                guess_count += 1
                guesses_per_round.append(guess_count)
                print("\nYou got it! It took you {} guesses!".format(guess_count))
                replay()
    
    # calls the "loop" function to start a round of guessing.
    loop()

# calls the start_game function to run all of the code
start_game()
