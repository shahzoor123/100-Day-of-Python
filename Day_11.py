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




def black_jack():
    flag1 = 0
    empty_list = []
    while flag1 < 3:
        flag1 += 1
        data = int(input("enter the number "))
        def add_to_list(num):
                empty_list.append(num)
                full_list = []
                full_list += empty_list
                print(full_list)
                return full_list
        def sum_of_list():
            sum_of_list = 0
            list1 = add_to_list(data)
            for nums in list1:
                sum_of_list += nums
            return sum_of_list
        
        print(sum_of_list()) 
black_jack()













cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
want_to_play = input('want to play game type "y" if not type "n"\n')
if want_to_play == "y":
    print(art.logo)
    u1 = random.choice(cards)
    u2 = random.choice(cards)
    c1 = random.choice(cards)
    c2 = random.choice(cards)
    print(u1,u2,c1,c2)
    
    
else:
    os.system('cls')
    







        

# card_limit = 21



# c1 = random.choice(cards)


# user_cards_list = []
# if want_to_play == "y":
    
#     user_cards = random.choice(cards)
#     user_cards_list += user_cards
#     print(f"Your cards: {user_cards_list}, current score: 11")


# want_to_stand_or_hit = input("want to play game type 'y' if not type 'n'")
