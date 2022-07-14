from pydoc import describe
from typing import final
import mod.higher_lower_art as art
import random
import os
import mod.game_data_of_higher_lower as list_dict
print(art.logo)
data = list_dict.data

game_loop = True
score = 0
against_b = random.choice(data)   
while game_loop:
    
    os.system('cls')
    compare_a = against_b
    against_b = random.choice(data)
    score += 1

    def Higher_lower(compare_a,against_b):
        print(f"You're right! Current score: {score}.")
        print(f'Compare A: {compare_a["name"]} , {compare_a["description"]} , {compare_a["country"]}')
        print(art.vs)
        print(f'Against B: {against_b["name"]} , {against_b["description"]} , {against_b["country"]}')
      
        a = compare_a['follower_count']
        b = against_b['follower_count']
        user_guess = input("Who has more followers? Type 'A' or 'B':") 
        g = user_guess
        
        
        if g == "a" and a >= b:
            """"Generate a two random keys from the list"""
            print(f'Compare A: {compare_a["name"]} , {compare_a["description"]} , {compare_a["country"]}')
            print(art.vs)
            print(f'Against B: {against_b["name"]} , {against_b["description"]} , {against_b["country"]}')
            

        elif g == "b" and b >= a:
            """"Generate a two random keys from the list"""
            print(f'Compare A: {compare_a["name"]} , {compare_a["description"]} , {compare_a["country"]}')
            print(art.vs)
            print(f'Against B: {against_b["name"]} , {against_b["description"]} , {against_b["country"]}')
            

        else:
            os.system('cls')
            global game_loop 
            game_loop = False
            return print(f"Sorry, that's wrong. Final score: {score}") 

    

    
    Higher_lower(compare_a,against_b)            