from pydoc import describe
from typing import final
import mod.higher_lower_art as art
import random
import os
import mod.game_data_of_higher_lower as list_dict
print(art.logo)

game_loop = True
while game_loop:
    """one for to compare reveal data one to be guessed by the user not reveal the data"""

    def compare(compare_a,against_b):
        print(f'Compare A: {compare_a["name"]} , {compare_a["description"]} , {compare_a["country"]} , {compare_a["follower_count"]}')
        print(art.vs)
        print(f'Against B: {against_b["name"]} , {against_b["description"]} , {against_b["country"]}, {against_b["follower_count"]}')
        score = 0
        a = compare_a['follower_count']
        b = against_b['follower_count']
        user_guess = input("Who has more followers? Type 'A' or 'B':") 
        g = user_guess
        """Guess again loop"""
        
            
        if g == "a" and a > b:
                
            """"Generate a two random keys from the list"""
            print(f'Compare A: {compare_a["name"]} , {compare_a["description"]} , {compare_a["country"]}')
            print(art.vs)
            print(f'Against B: {against_b["name"]} , {against_b["description"]} , {against_b["country"]}')

            score += 1
            """if user guess is == right than the user guessed value became a and b == new value """
            new_guess = compare_a
            compare_a = against_b
            against_b = random.choice(data)
            """show the score of the user of how many guesses"""
            return print(f"You're right! Current score: {score}.") 
        else:
            global game_loop 
            game_loop = False
            """if not guess right game is over"""
            os.system('cls')
                
            return print(f"Sorry, that's wrong. Final score: {score}") 




    data = list_dict.data
    compare_a = random.choice(data)
    against_b = random.choice(data)

                
    compare(compare_a,against_b)            