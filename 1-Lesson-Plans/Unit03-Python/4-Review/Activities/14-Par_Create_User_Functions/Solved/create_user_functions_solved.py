# Copy and paste your `validate_password` function here
def validate_password(password):
    # Inside the function, check if the password is longer than 6 characters long
    if len(password) > 6:
        # If it is, return `True`
        return True
    else:
        # Otherwise, return `False`
        return False

def collect_user_information():
    # Prompt the user for their username
    username = input("What's your username? ")
    # Prompt the user for their email
    email = input("What's your email? ")
    # Prompt the user for their password
    password = input("What's your password? ")

    # Return a list with username, email, and password
    return [username, email, password]

def create_user(username, email, password):
    # Use your `validate_password` function to check if the password is secure
    if validate_password(password):
        # If so, create a dictionary, called `user` with the keys "Username", "Email", and "Password"
        # Associate these keys with the values the user entered
        user = {
            "Username": username,
            "Email": email,
            "Password": password
        }
        # When you're done, use `items` to print: `"Your username is <USERNAME>"`; `"Your email is <EMAIL"`; and `"Your password is <PASSWORD>"`
        for key, value in user.items():
            print("Your " + key + " is: " + value + ".") 

        # Return user
        return user

    # If the password is too short, tell the user to try again
    else:
        print("Your password is too short, try again!")

# Get user information
user_data = collect_user_information()
username = user_data[0]
email = user_data[1]
password = user_data[2]

# Create user
user = create_user(username, email, password)

# Now we can update the user!