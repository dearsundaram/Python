str =  input(' Enter a string you like ')

choice = input('Type YES if you want to print the string you typed in CAPS or type NO to print the string in lower case: ')

if choice == "YES":
    print(str.upper())
elif choice == "NO":
    print(str)
else:
    print("Invalid option")
