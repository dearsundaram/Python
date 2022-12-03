
#### Fortune Cookie Project ####
import random

print(random.randint(1,10))  ##random integer num from 1 to 10
print(random.random()) ##random float number
##########################
print("######################")
print("Yes No Maybe using rand choice module")
luck=(random.choice(['yes','no','may be']))
print(f"Do I have a luck {luck}")
##########################
print("######################")
print("Yes No Maybe using rand int module")
luck=random.randint(1,3)
if luck == 1:
  print("Do I have a luck: YES")
elif luck == 2:
  print("Do I have a luck: NO")
else:
  print("Do I have a luck: MAYBE")

print("End of program")
print("######################")
print("How your fortune is going to be today and your lucky number....!")
fortune_number = random.randint(1,3)
if fortune_number == 1:
  fortune_str = "Its your lucky day"
  print(f"{fortune_str} and your lucky number is {fortune_number}")
if fortune_number == 2:
  fortune_str = "Its going to be a tough day"
  print(f"{fortune_str} and your lucky number is {fortune_number}")
if fortune_number == 3:
  fortune_str = "You will die today"
  print(f"{fortune_str} and your lucky number is {fortune_number}")