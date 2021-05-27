### To findout vowels and consonents in the given word ###
vowels = 0
consonents = 0
letter = input("Enter the word in which you want to know volwel and consonent count ")
for i in letter:
    if i.lower() in "aeiou":
        vowels+=1
    elif i == " " or i in "@#$%^&*?!<>/`~":
        pass
    else:
        consonents+=1
print("The total vowel count is {}".format(vowels))
print("The totla consonent count is {}".format(consonents))

