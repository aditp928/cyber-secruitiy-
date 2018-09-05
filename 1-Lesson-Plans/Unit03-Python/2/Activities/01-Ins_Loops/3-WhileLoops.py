# Creating a variable that will be checked in the loop
userInput = "yes"

# While loops run infinitely up until the condition is no longer met
while (userInput == "yes"):

    print("ROUND AND ROUND WE GO!")
    print("----------------------")

    # If the user enters anything other than "yes" then they escape from the loop
    userInput = input("Would you care to loop again? (yes or no) \n")

# This line will not print until the loop is escaped
print("YOU ESCAPED THE LOOP!")
