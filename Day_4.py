import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_images = [rock,paper,scissors]
user = int(input("What do you choose?Type 0 for Rock,1 for paper or 2 for Scissors\n"))
if user >= 3 or user < 0:
    print("You typed an invalid number you lose!")
else:
    print("You Choose")
    print(game_images[user - 1])
    computer = random.randint(0,2)
    print("Computer Choose")
    print(game_images[computer - 1])

    if user == 1 and computer == 2:
        print("You Lose!")
    elif user == 2 and computer == 0:
        print("You Lose!")
    elif user == 0 and computer == 1:
        print("You Lose!")
    elif user == 0 and computer == 2:
        print("You Win!")
    elif user == 1 and computer == 2:
        print("You Lose!")
    elif user == 2 and computer == 1:
        print("You Lose!")
    elif user == computer:
        print("Its a Draw")         
