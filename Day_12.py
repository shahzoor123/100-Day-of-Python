import mod.word_guessing_art as art
import random
print(art.logo)
print("Welcome to the Number Guessing Game!")



print("I'm thinking of a number between 1 and 100")

number = random.randint(1,101)
print(number)
level = input("Choose a difficulty. Type 'easy' or 'hard':\n")
if level == "easy":
    chance = 6
    for _ in range(5):
        chance -= 1
        print(f"You have {chance} guess remaining to guess the number")   
        guess = int(input("Make a guess: "))
        if guess == number:
            print("You guessed the number")
            break
        elif guess < number:
            print("Too low")
        elif guess > number:
            print("Too High") 
        else:
            print("You lose to guess the number")  
elif level == "hard":
    for _ in range(10):
        chance = 11
        chance -= 1
        print(f"You have {chance} guess remaining to guess the number")   
        guess = int(input("Make a guess: "))
        if guess == number:
            print("You guessed the number")
            break
        elif guess < number:
            print("Too low")
        elif guess > number:
            print("Too High")     
        else:
            print("You lose to guess the number") 
        