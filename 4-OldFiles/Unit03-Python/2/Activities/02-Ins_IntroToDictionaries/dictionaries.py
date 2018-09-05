# Creating a dictionary by setting a variable equal to "keys" and "values" contained within curly brackets
pet = {
    # A key is a string while the value can be any data type
    "name": "Misty",
    "breed": "Mutt",
    "age": 12
}
print(pet)

# A single value can be collected by referencing the dictionary and then using the key as the index
print(pet["name"])

# The value of a key can also be changed by setting it equal to a new value
pet["age"] = 13
print(pet["age"])

# The del() function can be used to remove a key/value pair from a dictionary
del(pet["breed"])
print(pet)

# .keys() can be used to collect a list of the keys in a dictionary
print(pet.keys())

# .values() can be used to collect a list of the values in a dictionary
print(pet.values())

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
