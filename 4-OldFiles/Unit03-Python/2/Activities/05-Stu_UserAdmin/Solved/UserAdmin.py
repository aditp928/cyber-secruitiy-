# Administrator accounts list
admins = [
    {
        "username": "DaBigBoss",
        "password": "DaBest"
    },
    {
        "username": "root",
        "password": "toor"
    }
]


# Create a function that will take in the user's information and saves it
def login():
    username = input("USERNAME: ")
    password = input("PASSWORD: ")
    return {"username": username, "password": password}


# Create a function that checks if the username and password entered matches one of those contained within the admins list
def checkLogin(userInfo, adminList):

    # Loop through the list of admin accounts
    for admin in adminList:

        # If the current admin in the admin list matches the user info
        if(admin["username"] == userInfo["username"] and admin["password"] == userInfo["password"]):

            # Return True so that the while loop will stop
            return True

    # If none of the admins in the list match the info inputted, return False so that the loop continues
    return False


# Variable used to store whether the inputted info matched an admin in the list
loggedIn = False

# Loop for as long as the variable loggedIn is False
while(loggedIn == False):

    # Call the login function and store the info returned in the user variable
    user = login()

    # Call the checkLogin function and store the info returned in the loggedIn variable
    loggedIn = checkLogin(user, admins)

    print("---------")

# Statement which prints when the user successfully logs in
print("YOU HAVE LOGGED IN!")
