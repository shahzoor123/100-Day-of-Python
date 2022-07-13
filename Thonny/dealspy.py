import random
import os
data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 181,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 174,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    ]
game_loop = True
score = 0

while game_loop:
    os.system('cls')
    score = score + 1
    def Higher_lower(compare_a,against_b):
        print(f'Compare A: {compare_a["name"]} , {compare_a["description"]} , {compare_a["country"]} , {compare_a["follower_count"]}')

        print(f'Against B: {against_b["name"]} , {against_b["description"]} , {against_b["country"]}, {against_b["follower_count"]}')
        
        a = compare_a['follower_count']
        b = against_b['follower_count']
        user_guess = input("Who has more followers? Type 'A' or 'B':") 
        g = user_guess
        
        if g == "a" and a >= b:
            """"Generate a two random keys from the list"""
            print(f'Compare A: {compare_a["name"]} , {compare_a["description"]} , {compare_a["country"]}')

            print(f'Against B: {against_b["name"]} , {against_b["description"]} , {against_b["country"]}')
            return print(f"You're right! Current score: {score}.")

        elif g == "b" and b >= a:
            """"Generate a two random keys from the list"""
            print(f'Compare A: {compare_a["name"]} , {compare_a["description"]} , {compare_a["country"]}')

            print(f'Against B: {against_b["name"]} , {against_b["description"]} , {against_b["country"]}')
            return print(f"You're right! Current score: {score}.")

        else:
            os.system('cls')
            global game_loop 
            game_loop = False
            return print(f"Sorry, that's wrong. Final score: {score}") 


    compare_a = random.choice(data)
    against_b = random.choice(data)   
    Higher_lower(compare_a,against_b)        