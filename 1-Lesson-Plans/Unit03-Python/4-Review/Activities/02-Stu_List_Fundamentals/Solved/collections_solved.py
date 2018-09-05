# NOTE: You'll need to use type conversion to make this work.
# TODO: Create a list, called `favorite_countries`. Store the name of four favorite countries inside it.
favorite_countries = ["Norway", "Spain", "Taiwan", "Morocco"]
# TODO: Print the message: "My favorite countries are: <YOUR LIST HERE>."
print("My favorite countries are: " + str(favorite_countries) + ".")
# TODO: Print the message: "I have <NUMBER OF FAVORITE COUNTRIES> favorite countries."
print("I have " + str(len(favorite_countries)) + " favorite countries.")

# TODO: Print the message: "My first favorite country is <FIRST COUNTRY IN YOUR LIST>.
print("My first favorite country is " + favorite_countries[0] + ".")
# TODO: Print the message: "My second favorite country is <SECOND COUNTRY IN YOUR LIST>.
print("My second favorite country is " + favorite_countries[1] + ".")
# TODO: Print the message: "My third favorite country is <THIRD COUNTRY IN YOUR LIST>.
print("My third favorite country is " + favorite_countries[2] + ".")
# TODO: Print the message: "My fourth favorite country is <FOURTH COUNTRY IN YOUR LIST>.
print("My fourth favorite country is " + favorite_countries[3] + ".")

# TODO: Add two more countries to your list.
favorite_countries.append("Canada")
favorite_countries.append("Mexico")
# TODO: Print: "Now I have <LENGTH OF LIST> favorite countries."
print("Now I have " + str(len(favorite_countries)) + " favorite countries.")
# TODO: Print: "My new favorites are <FIRST COUNTRY YOU ADDED> and <SECOND COUNTRY YOU ADDED>."
print("My new favorites are " + favorite_countries[4] + " and " + favorite_countries[5] + ".")

# TODO: Add two more countries to your list, again. This time, use `extend`.
favorite_countries.extend(["Finland", "Hungary"])
# TODO: Print: "...And NOW, I have <LENGTH OF LIST> favorite countries!"
print("...And now, I have " + str(len(favorite_countries)) + " favorite countries!")
# TODO: Print: "My newest favorites are <FIRST COUNTRY YOU ADDED> and <SECOND COUNTRY YOU ADDED>."
print("My new favorites are " + favorite_countries[6] + " and " + favorite_countries[7] + ".")
