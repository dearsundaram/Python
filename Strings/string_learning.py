
## Python program to get the details from user  and print in a concatenated format ##
name = input("Enter your name: ")
age = input("Enter your age: ")
hobby = input("Enter you hobby: ")
location = input("Enter your location: ")

## Sting concatination of above inputs  ##
stringConcat = "Your name is {} and you are {} old. Your hobby is {} and you live in {}"
outputString = stringConcat.format(name, age, hobby, location)

## Print the output string ##
print(outputString)

