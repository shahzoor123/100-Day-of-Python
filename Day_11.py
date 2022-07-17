import mod.blackjack_art as art
import os
import random

print(art.logo)


def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw 🤔 "
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😭"
    elif user_score == 0:
        return "win with a Blackjack 😎"
    elif user_score > 21:
        return "Opponent went over. You win 🤯"
    elif user_score > computer_score:
        return "You win 😎"
    else:
        return "You lose 😭"

    # def play_game():


#     user_cards  = []
#     computer_cards = []
#     is_game_over = False

#     for _ in range(2):
#         user_cards.append(deal())
#         computer_cards.append(deal())

#     while not is_game_over:

#         user_score = calculate_score(user_cards)            
#         computer_score = calculate_score(computer_cards)
#         print(f"Your cards: {user_cards}, current score: {user_score}")
#         print(f"Computer's first card: {computer_cards[0]}")         
#         if user_score == 0 and computer_score == 0 or user_score > 21:
#             is_game_over = True               
#         else:
#             want_to_stand_or_hit = input(f"Type 'y' to get another card, type 'n' to pass: y ")
#             if want_to_stand_or_hit == "y":
#                 user_cards.append(deal())
#             else:
#                 is_game_over = True    
#     while computer_score != 0 and computer_score < 17:
#         computer_cards.append(deal())
#         computer_score = calculate_score(computer_cards)
#     print(f"Your final hand: {user_cards}, final score: {user_score}")
#     print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
#     print(compare(user_score,computer_score))

# while input("Do you want to play a game of Blackjack? Type 'y' to get another card, type 'n' to pass: y ") == "y":
#     os.system("cls")
#     play_game()


def black_jack():
    card_limit = 21
    flag1 = 0
    empty_list = []
    while flag1 < 2:
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


black_jack()
