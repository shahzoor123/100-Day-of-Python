from sys import flags
from tkinter import E
import mod.blackjack_art as art
import os
import random

def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    for i in range(1):
        card = random.choice(cards)
        return card
        

def black_jack():
    card_limit = 21
    flag1 = 0
    empty_list = []
    while flag1 < 1:
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