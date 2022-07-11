############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################
from sys import flags
from tkinter import E
import mod.blackjack_art as art
import os
import random

def deal():
    for i in range(2):
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card
        
   
def black_jack():
    card_limit = 21
    flag1 = 0
    empty_list = []
    while flag1 < 3:
        flag1 += 1
        data = deal() 
        def add_to_list(num):
            empty_list.append(num)
            full_list = []
            full_list += empty_list
            
            return full_list
        def sum_of_list():
            sum_of_list = 0
            list1 = add_to_list(data)
            for nums in list1:
                sum_of_list += nums
            return sum_of_list
        score = sum_of_list()
        lists = add_to_list(data)
        print(f"Your cards: {lists}, current score: {score}")
        # want_to_play = input(f"Do you want to play a game of Blackjack? Type 'y' or 'n': ")
        # if want_to_play == "y":
        #     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        #     first_round = random.choice(cards)
            
        # else:
        #     os.system("cls")


black_jack()


# want_to_stand_or_hit = input(f"Type 'y' to get another card, type 'n' to pass: y ")

# print(f"Your cards: {}, current score: {}")
# print(f"Computer's first card: {}")
# print(f"Your final hand: {}, final score: {}")
# print(f"Computer's final hand: {}, final score: {}")

# print(f"Computer went over. You win 😃")
# print(f"You went over. You lose 😭")