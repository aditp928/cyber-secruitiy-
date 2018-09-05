# Creating a dictionary by setting a variable equal to "keys" and "values" contained within curly brackets
pet = {
    # A key is a string while the value can be any data type
    "name": "Misty",
    "breed": "Mutt",
    "age": 12
}

# .keys() returns a list of the keys in a dictionary
print(pet.keys())

# .values() returns a list of the values in a dictionary
print(pet.values())

# .items() returns a list of key, value pairs in a dictionary
print(pet.items())

# use .items() to loop through all of the information about the pet
for key, value in pet.items():
    print("The pet's " + key + " is " + str(value))
