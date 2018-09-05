user_list = [
    "Laurice",
    "Veola",
    "Giovanna",
    "Muoi",
    "Leandro",
    "Mia",
    "Son",
    "Collin",
    "Hoyt",
    "Oscar",
    "Elida",
    "Kitty",
    "Arden",
    "Adele",
    "Hoa",
    "Doug",
    "Louis",
    "Diann",
    "Luana",
    "Blanch"
]

password_list = [
    "HDWTWXht",
    "nWKz3chG",
    "FnnpGmjz",
    "7QEtS9xv",
    "BDzPM5f4",
    "P3xTtXnM",
    "NannBPbM",
    "ZZrQPstQ",
    "Z7d97Fhb",
    "eZjLLT7Y",
    "eRm2bjPV",
    "2B6fy4Ab",
    "bBvRevr2",
    "EJnT3RnN",
    "pfutL26V",
    "ZdrsxEhd",
    "XMdqwmzY",
    "LQt47eBb",
    "ykCRhuXA",
    "uJbgRkax"
]

# BONUS: Create a variable called "logged_in" and set it to False initially
logged_in = False

# Take in user input for their name
username = input("Please enter your username: ")

# Take in user input for their password
password = input("Please enter your password: ")

# Loop through both the user list and the password list
for x in range(len(user_list)):

    # Check that the username and password matches those in the lists
    if(username == user_list[x] and password == password_list[x]):

        # Print out "Login Successful"
        print("LOGIN SUCCESSFUL")

        # BONUS: Set the "logged_in" variable to True
        logged_in = True

# BONUS: If the for loop completes and "logged_in" is still false...
if(logged_in == False):

    # BONUS: Print out "Login Failed"
    print("LOGIN FAILED")
