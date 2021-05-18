### TRAVIS Authentication app will get the user information
### Checks the user availability in its List elements
### Ask user to get registered if they are not present in the List
### Travis completely uses List Data Type

List_users = ["Bob","Mike","Aron"]

while True: 
    users_cap = input("Enter your username: ").strip()
    users = users_cap.capitalize()

#### Checking if the user is present in the list
    if users in List_users:
        print("User name exists.. Welcome to Travis")
    else:
        print("User does not exist..")
        response = input("You wanna get added up ? Press Y/y to add and N/n to not add ").lower()
        if response == "y":
            List_users.append(users)    ### Appending the users to the list
            print(List_users)
            print("User {} successfully added".format(users_cap))
        else:
            print("Thank you for using Travis..")


        


