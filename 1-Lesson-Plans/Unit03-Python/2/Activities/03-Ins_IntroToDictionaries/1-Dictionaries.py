# Creating a dictionary by setting a variable equal to "keys" and "values" contained within curly brackets
pet = {
    # A key is a string while the value can be any data type
    "name": "Misty",
    "breed": "Mutt",
    "age": 12
}
print(pet)

# values are obtained by referencing the dictionary and using the key as the index
print(pet["name"])

# adding to or modifying the dictionary is done by setting the key equal to a new value
pet["age"] = 13
pet["color"] = "gold"
print(pet)

# The del() function can be used to remove a key/value pair from a dictionary
del(pet["breed"])
print(pet)
