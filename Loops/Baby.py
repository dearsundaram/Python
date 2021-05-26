### Baby asks random questions ###

### importing choice function from random module ###
from random import choice
questions = ["why is sky blue ?", "Why is leaf green ?", "why is sun red ?"]
actual_question=choice(questions)
answer=input(actual_question).strip().lower()
while answer != "just because":
    answer=input("Why ??? ")
    
