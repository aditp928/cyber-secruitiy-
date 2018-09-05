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
<YOUR CODE HERE>

# Create a function named checkLogin with two parameters: the userInfo and the adminList
# The function should check the credentials to see if they are contained within the admins list
# returns True if the credentials are found, False otherwise
<YOUR CODE HERE>

    # for loop through the list of admin accounts
    <YOUR CODE HERE>

        # If statement to check that the current admin in the admin list matches the user info
        <YOUR CODE HERE>

            # Return True so that the while loop will stop
            <YOUR CODE HERE>

    # If we got here none of the admins in the list match the info inputted, so return False so that the while loop continues
    <YOUR CODE HERE>


# Variable used to store whether the inputted info matched an admin in the list
loggedIn = False

# while loop that runs while the user is not loggedIn
<YOUR CODE HERE>

    # Call the login function and store the dictionary returned in a variable
    <YOUR CODE HERE>

    # Call the checkLogin function and store the boolean returned in the loggedIn variable
    <YOUR CODE HERE>

    print("---------")

# If we got here, the while loop has broken! Statement which prints that the user successfully logged in
print("YOU HAVE LOGGED IN!")
