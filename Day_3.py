print('''  
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure island\nYour misson is to find the Treasure")
s1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right"\n')
if s1 == "left" or s1 == "Left":
    s2 = input('You come to a lake . There is an island in the middle of the lake. Type "wait" to wait for boat. Type "swim" to swim across\n')
    if s2  == "wait" or s2 == "Wait":
        s3 = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.Which colour do you choose?\n')
        if s3 == "yellow":
            print("You win Treasure has been found wow now i am rich")
        else: 
            print("Game over you were burned by the fire")   
    else:
        print("Game over your were eaten by crocodiles")
else:
    print("Game over you were hit by a car")


