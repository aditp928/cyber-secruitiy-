# A list of dictionaries
petList = [
    {
        "name": "Misty",
        "breed": "Mutt",
        "age": 12
    },
    {
        "name": "Pixel",
        "breed": "Beagle",
        "age": 2
    },
    {
        "name": "Rockington",
        "breed": "Igneous",
        "age": 200000
    }
]

# Looping through the list to then print out the values in the dictionary
for pet in petList:
    print(pet["name"] + " is a " + pet["breed"] +
          " that is " + str(pet["age"]) + " years old")
