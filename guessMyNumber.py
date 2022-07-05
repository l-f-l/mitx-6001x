low = 0
high = 100
guess = int((high + low) / 2)
highOrLowGuess = ""

print("Please think of a number between 0 and 100!")
while highOrLowGuess != "c":
    print("Is your secret number " + str(guess) + "?")
    highOrLowGuess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. "
                           "Enter 'c' to indicate I guessed correctly. ")
    if highOrLowGuess == "h":
        high = guess
        guess = int((high + low) / 2)
    elif highOrLowGuess == "l":
        low = guess
        guess = int((high + low) / 2)
    elif highOrLowGuess == "c":
        print("Game over. Your secret number was: " + str(guess))
        highOrLowGuess = "c"
    else:
        print("Sorry, I did not understand your input.")
