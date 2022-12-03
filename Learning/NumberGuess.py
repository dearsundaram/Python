import random
import time

print("Welcome to number guessing game ")
time.sleep(3)
print("Guess a number between 1 to 10")
print("Picking a number now. Please wait !!")
time.sleep(2)
correct_number = random.randint(1,10)
user_input = int(input("Enter the number you guess?: "))

count = 0

while user_input != correct_number:
    count += 1
    if user_input < correct_number:
        user_input=int(input("Wrong.. You need to guess higher. What is your guess now ??: "))
    elif user_input > correct_number:
        user_input=int(input("Wrong.. You need to guess lower. What is your guess now ??: "))

time.sleep(2)

print(f"You guessed it right.. The correct answer is {correct_number}. It took {count} times for you to find out the right answer")
