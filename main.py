import sys
import random

# Set the max for number range
max = 10
if len(sys.argv) == 2:
    if sys.argv[1].isdigit():
        tmp_max = int(sys.argv[1])
        max = tmp_max
    else:
        print("Incorrect usage.")
        quit()
score = max

# Choose random number
rand_num = random.randint(0, max)

# Loop until correct guess
while True:
    # Ask user for guess and take input
    while True:
        guess = input("Make a guess: ")

        if guess.isdigit():
            guess_int = int(guess)
            break

    # Check if guess is correct
    if guess_int == rand_num:
        print("You are correct!! Your score is " + str(score) + " !")
        break
    else:
        score -= 1
        if guess_int > rand_num:
            print("Number is lower.")
        else:
            print("Number is higher.")