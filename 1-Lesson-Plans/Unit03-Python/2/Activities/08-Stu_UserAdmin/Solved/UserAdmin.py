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


# Create a function named getCreds with no parameters that will prompt the user for their username and password
# returns a dictionary that looks like the above dictionaries
def login():
    username = input("USERNAME: ")
    password = input("PASSWORD: ")
    return {"username": username, "password": password}


# Create a function named checkLogin with two parameters: the userInfo and the adminList
# The function should check the credentials to see if they are contained within the admins list
# returns True if the credentials are found, False otherwise
def checkLogin(userInfo, adminList):

    # Loop through the list of admin accounts
    for admin in adminList:

        # If statement to check that the current admin in the admin list matches the user info
        if(admin["username"] == userInfo["username"] and admin["password"] == userInfo["password"]):

            # Return True so that the while loop will stop
            return True

    # If we got here none of the admins in the list match the info inputted, so return False so that the while loop continues
    return False


# Variable used to store whether the inputted info matched an admin in the list
loggedIn = False

# while loop that runs while the user is not loggedIn
while(loggedIn == False):

    # Call the login function and store the info returned in the user variable
    user = login()

    # Call the checkLogin function and store the info returned in the loggedIn variable
    loggedIn = checkLogin(user, admins)

    print("---------")

# Statement which prints when the user successfully logs in
print("YOU HAVE LOGGED IN!")



