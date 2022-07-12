import random

print("Welcome to the Number Guessing Game!")



print("I'm thinking of a number between 1 and 100")

number = random.randint(1,101)

level = input("Choose a difficulty. Type 'easy' or 'hard':\n")
if level == "easy":
    chance = 5
    while chance == 0:
        guess = int(input("Enter a number"))
        if guess == number:
            print("You guessed the number")
        else:
            continue    
else:
    chance = 10
    while chance == 0:
        guess = int(input("Enter a number"))
        if guess == number:
            print("You guessed the number")
        else:
            continue  