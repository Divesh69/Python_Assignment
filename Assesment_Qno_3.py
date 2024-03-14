# Write a Python program that generates a random number between 1
# and 100 and asks the user to guess the number. The program should
# provide feedback to the user (e.g., "Too high" or "Too low") based on
# their guess and count the number of attempts it takes to guess the
# correct number. Once the user guesses the correct number, the
# program should display the number of attempts.

import random

randnum = random.randint(1, 100)
print(randnum) 
guessCount = 0

while True:
    userGuess = int(input('Guess the number between 1 and 100: '))
    guessCount += 1

    if userGuess < randnum:
        print("Your guess is low")
    elif userGuess > randnum:
        print("Your guess is high")
    else:
        print("Congratulations! Your guess is correct.")
        break

print("You guessed the number in", guessCount, "attempts.")