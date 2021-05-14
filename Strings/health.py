###### Create a random number which defines the health potion of an imaginary player #####

##### In order to randomly generate numbers, we use random module ####
import random

health = 50

difficulty = 1

potion_health = int(random.randint(25,50)/difficulty)

health = health + potion_health

print (health)
