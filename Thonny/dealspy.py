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
while game_loop:
    """one for to compare reveal data one to be guessed by the user not reveal the data"""

    def Higer_lower(compare_a,against_b):
        print(f'Compare A: {compare_a["name"]} , {compare_a["description"]} , {compare_a["country"]} , {compare_a["follower_count"]}')
        print(art.vs)
        print(f'Against B: {against_b["name"]} , {against_b["description"]} , {against_b["country"]}, {against_b["follower_count"]}')
        score = 0
        a = compare_a['follower_count']
        b = against_b['follower_count']
        user_guess = input("Who has more followers? Type 'A' or 'B':") 
        g = user_guess
        """Guess again loop"""
        
            
        if g == "a" and a >= b:
                
            """"Generate a two random keys from the list"""
            print(f'Compare A: {compare_a["name"]} , {compare_a["description"]} , {compare_a["country"]}')
            print(art.vs)
            print(f'Against B: {against_b["name"]} , {against_b["description"]} , {against_b["country"]}')

            score = score + 1
            """if user guess is == right than the user guessed value became a and b == new value """
            # new_guess = compare_a
            compare_a = against_b
            against_b = random.choice(data)
            """show the score of the user of how many guesses"""
            return print(f"You're right! Current score: {score}.")
        elif g == "b" and b >= a:

            """"Generate a two random keys from the list"""
            print(f'Compare A: {compare_a["name"]} , {compare_a["description"]} , {compare_a["country"]}')
            print(art.vs)
            print(f'Against B: {against_b["name"]} , {against_b["description"]} , {against_b["country"]}')

            score += 1
            """if user guess is == right than the user guessed value became a and b == new value """
            new_guess = compare_a
            compare_a = against_b
            against_b = random.choice(data)
            print(new_guess)
            
            """show the score of the user of how many guesses"""
            return print(f"You're right! Current score: {score}.")

        else:
            global game_loop 
            game_loop = False
            """if not guess right game is over"""
            os.system('cls')
                
            return print(f"Sorry, that's wrong. Final score: {score}") 



compare_a = random.choice(data)
against_b = random.choice(data)

            
Higer_lower(compare_a,against_b)            