import mod.word_guessing_art as art
import random
print(art.logo)
print("Welcome to the Number Guessing Game!")



print("I'm thinking of a number between 1 and 100")

number = random.randint(1,101)

level = input("Choose a difficulty. Type 'easy' or 'hard':\n")
if level == "easy":
    chance = 5
else:
    chance = 10
    