# Creating a function called "printHello" with no parameters
def printHello():

    # Simply prints "Hello!" to the screen
    print("Hello!")


# Functions will not run the code contained until the function is called
# Calling the "printHello" function
printHello()
print("--------")


# Creating a function called "printUserInfo" with three parameters
def printUserInfo(name, age, profession):

    # Parameters are temporary variables for usage within the function
    print("USER: " + name)
    print("AGE: " + str(age))
    print("PROFESSION: " + profession)


# Calling the "printUserInfo" that passes two strings and an integer through
# "Jacob" will be the value for name
# 26 will be the value for age
# "Engagement Engineer" will be the value for profession
printUserInfo("Jacob", 26, "Engagement Engineer")
print("--------")

# Function parameters are not limited to basic variables; lists and dictionaries can be pushed into functions as well
user = {
    "name": "Jacob",
    "age": 26,
    "profession": "Engagement Engineer"
}


def printUserDict(userDict):
    print("USER: " + userDict["name"])
    print("AGE: " + str(userDict["age"]))
    print("PROFESSION: " + userDict["profession"])


printUserDict(user)
print("--------")


# Functions can also be used to pass data into an external variable through the use of return
def collectPetInfo():

    name = input("What is your pet's name? ")
    breed = input("What is your pet's breed? ")
    favoriteMeal = input("What is your pet's favorite meal? ")

    petDict = {
        "name": name,
        "breed": breed,
        "favoriteMeal": favoriteMeal
    }

    return petDict

    # Return will also quit out of the function, so any code placed after a return statement will not run
    print("THIS WILL NOT RUN")


myPet = collectPetInfo()
print(myPet)
