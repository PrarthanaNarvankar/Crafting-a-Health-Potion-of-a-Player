#Crafting a Health Potion Project Using Python

#Assume a game in which a player has 3 level like easy,medium and difficulty.
# 1: Easy    2: Medium   3: Difficult
#In the game a player may had given a specific health and while playing player may loose or gain the health .
#So we will predict the player health at different levels of the game . 

import random

health=50

difficulty=1

potion_health=int(random.randint(25,50)/difficulty)

health=health + potion_health

print("Hey! Player your health  is ")

print(health)
