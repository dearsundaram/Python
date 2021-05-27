### Get the sentance from user ###
orignal = input("Enter the sentance ").strip().lower()
### Split that sentance in to words ###
words = orignal.split()    ## this will convert string of words to list
#print(words)

### Loop through words and convert into Pig Latin ###
new_words=[]

for word in words:   ## this will iterate the words (list)
    ### If the word starts with vowel, add "yay" at the last of word
    ### Else move the first consonent cluster and move it to the end followed by "ay"
    if word[0] in "aeiou":
        temp_word = word+"yay"
        new_words.append(temp_word)
        #print(new_words)
    else:
        vowel_count = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_count = vowel_count+1
            else:
                break
        cons = word[:vowel_count]
        the_rest = word[vowel_count:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)

### Stick words back together ###
new_words = " ".join(new_words)

### Output the final string ###
print(new_words)