# Creator: Joseph Ervin
# Program description: this program is a word puzzle game.
# the program takes a random word of any length from a list and gives the player one random letter from that word. The player must guess where this letter goes.
# Every time they guess the position of a letter correctly, that letter is locked in. The goal is to lock all the letters in to finish the word in as little tries as possible.
# word bank created using randomwordgenerator.com. Also includes the worlds longest word pneumonoultramicroscopicsilicovolcanoconiosis to show that any word works in this program no matter the length.

word_bank = "pneumonoultramicroscopicsilicovolcanoconiosis", "card", "blaze", "trace", "real", "point", "fruit", "loops"

challenge = False


def run_program(challenge):  # defines the function run_program. The variable inside the parenthesis is the parameter.
    from random import randint  # imports the randint function from the random library
    word_numb = randint(0,
                        len(word_bank) - 1)  # assigns variable word_numb to a random integer between 0 and the number of words in the word bank minus 1 to fit list indexes
    if challenge == True: word_numb = 0  # sets word_numb to 0 if challenge is true so that the word that's chosen is element 0 of the word_bank
    word = word_bank[
        word_numb]  # assigns variable word to be the element with the index of the random integer from word_numb
    word_length = len(word)  # assigns variable word_length to be the length of the string word.

    # establishing lists to track the letters of the word and whether theyve been found yet.
    unknown_letters = []
    known_letters = []
    letters = []

    # establishing varibles to track player guesses(their accepted input)
    answer_tracker = []  # empty brackets create an empty list
    guess_counter = 0

    letter_counter = 0  # counter to count through the letters of the chosen word.
    for letter_counter in word:  # for loop that runs through each character of the word that has been chosen and adds it to lists. for loops are used when the number of iterations is known.
        letters.append(letter_counter)  # append adds the arguement passed to the end of a list
        unknown_letters.append(letter_counter)
        known_letters.append("_")
    letter_numb = randint(0, (
                len(unknown_letters) - 1))  # randint returns a random integer between the first number and the second number.

    print("\nA random word has been chosen. Your word is", str(word_length),
          "letters long. Guess where each letter goes in this word to find the full word.\nIf you think you know the" +
          "word you can enter it to finish the game faster.\nType RESTART to restart the game, EXIT to leave, or CHALLENGE to try the worlds longest word.\n")

    while True:  # while loop runs while the condition is true and only stops when the condition becomes false.
        # Used for when the number of iterations is unknown. In this case it only breaks when a function is called that ends or restarts the program

        print("Guesses used:", guess_counter)

        letter = unknown_letters[
            letter_numb]  # the letter that the player will be given is taken from the letters that the player doesn't know yet.

        for counter in range(1, word_length + 1):  # loops through all integers between 1 and the word_length +1
            print(str(counter),
                  end=" ")  # prints the string of the integer. end= puts whatever is in the parenthesis at the end of the print output. by default a print statement ends by starting a new line.
        print("")
        for counter in range(word_length):
            print(known_letters[counter], end=" " * len(str(counter)))
        print("")

        print("Guess where the letter", letter.upper(),
              "goes in the word.")  # upper gets the uppercase of the string

        guess = input("\nEnter a number between 1 and " + str(word_length) + ": ")

        # checks if the player input a valid number and if not then checks if they input any of the commands
        valid = False  # used for if the answer is valid or not
        if guess.isnumeric():  # isnumeric checks if a string is a number. if statement runs the code indented below it only if the condition is true. #i learned this function from programiz.com
            guess = int(guess) - 1
            for counter in range(word_length):
                if guess == counter and guess not in answer_tracker:  # loops through the word length and checks if the guess is any of those values and if its not an number thats already been answered.
                    valid = True
                    if letters[guess] == (letter):
                        known_letters[
                            guess] = letter  # adds the letter guessed to the known letters list as the element with the index of guess
                        if known_letters == letters:
                            word_found(guess_counter,
                                       word)  # calls the word_found function and passes 2 arguements into it.
                        unknown_letters.remove(letter)  # remove removes all instances of an item from a list
                        answer_tracker.append(guess)
                        letter_numb = randint(0, (len(unknown_letters) - 1))
                        print("\ncorrect")
                    else: #else statement runs the code indented beneath it in any case other than when the if statement is run
                        print("\nincorrect")
            guess += 1
        else:

            if guess.lower() == "restart":
                restart()  # runs the restart function with no arguements
            elif guess.lower() == "challenge": #elif runs the code indented under it if the condition is true and the if statement before it is false.
                run_challenge()
            elif guess.lower == "exit":
                exit()  # function that exits the program. I learned this function from SA Andrew.
            elif guess.lower() == word:
                word_found(guess_counter, word)
            elif guess.lower() == "number":
                number_input = int(input())
                sprint_1_basic_calculations(
                    number_input)  # runs the function with number_input as the only arguement.
                sprint_2_missing_requirements(number_input)
        if valid == False:
            print(guess, "is not a valid answer. Please enter an answer that is valid.")
            guess_counter -= 1

        guess_counter += 1  # += 1 is the same as saying x = x + 1. It just adds a number to the variable's variable


def restart():
    print("\n")
    run_program(False)  # runs the function and passes False as the arguement for the challenge parameter


def run_challenge():
    print("\n")
    run_program(True)  # runs the function and passes True as the arguement for the challenge parameter


def word_found(guesses_parameter, word_parameter):  # defines word_found funcion with two parameters
    print("Congratulations! You have found the full word", word_parameter, "in only", (guesses_parameter + 1),
          "guesses!")
    end = input("Hit enter to exit or type RESTART to play again.")
    if (str(end)).lower() == "restart":
        restart()
    else:
        exit()


def sprint_1_basic_calculations(number):
    double_number = number * 2  # * operator multiplies
    number_squared = number ** 2  # ** operator puts the first number to the power of the second number
    number_half = number / 2  # / operator divides
    number_odd_or_even = number % 2  # % operator takes the modulus or the remainder of dividing the first number by the second number
    number_half_floored = number // 2  # // operator divides the first number by the second number and floors that value aka rounds down.
    number_plus_100 = number + 100  # + operator is basic addition. Adds the second number to the first number
    number_minus_100 = number - 100  # - operator is basic subtraction. Subtracts the second number from the first number.
    print(double_number, number_squared, number_half, number_odd_or_even, number_half_floored, number_plus_100,
          number_minus_100)

def sprint_2_missing_requirements(number):
    if number > 0: print("this number is positve.") # > operator checks if the first number is larger than the second number.
    if number != 10: print("this number is not 10") # the != operator means does not equal so if the values do not equal each other it returns True.


run_program(False)
