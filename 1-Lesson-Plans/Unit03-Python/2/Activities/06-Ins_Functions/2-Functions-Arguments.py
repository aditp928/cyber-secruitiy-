# Creating a function called "printUserInfo" with three parameters
def printUserInfo(name, age, profession):

    # Parameters are temporary variables for usage within the function
    print("User: " + name)
    print("Age: " + str(age))
    print("Profession: " + profession)

# Calling the "printUserInfo" function, passing two strings and an integer as arguments
# "Jacob" will be the value for name
# 26 will be the value for age
# "Engagement Engineer" will be the value for profession
printUserInfo("Jacob", 26, "Engagement Engineer")
print("--------")


# parameters are not limited to basic variables; lists and dictionaries can also be passed into functions
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


# even other functions can be passed into functions
def printUserDict2(userDict, printFunction):
    printFunction(userDict["name"], userDict["age"], userDict["profession"])

printUserDict2(user, printUserInfo)
