# TODO: Create a dictionary, called `countries`
# TODO: Choose five countries to use as keys. List their capital cities as values.
country_capitals = {
    "Fiji": "Suva",
    "Guatemala": "Ciudad de Guatemala",
    "Mexico": "El Distrito Federal",
    "Spain": "Madrid",
    "Germany": "Berlin"
}

# TODO: Print: "The capital of <COUNTRY> is <CAPITAL>", for each country in the dict
# NOTE: Don't use a `for` loop--do it manually, in five lines.
print("The capital of Fiji is " + country_capitals["Fiji"] + ".")
print("The capital of Guatemala is " + country_capitals["Guatemala"] + ".")
print("The capital of Mexico is " + country_capitals["Mexico"] + ".")
print("The capital of Spain is " + country_capitals["Spain"] + ".")
print("The capital of Luxembourg is " + country_capitals["Germany"] + ".")


# TODO: Use `keys` to create a list of the countries in your dictionary, and store it in a variable
countries = country_capitals.keys()
# TODO: Use a `for` loop to print: "My list contains the country <COUNTRY>"
for country in countries:
    print("My list contains the country " + country + ".")

# TODO: Use `values` to create a list of the capitals in your dict, and store it in a variable
capitals = country_capitals.values()
# TODO: Use a `for` loop to print: "I've been to <CAPITAL>!"
for capital in capitals:
    print("I've been to " + capital + ".")

# TODO: Use `items` to create a list of the key/value pairs in your dictionary, and store it in a variable
country_capital_pairs = country_capitals.items()
# TODO: Use a `for` loop to print: "The capital of <COUNTRY> is <CAPITAL>."
for country, capital in country_capital_pairs:
    print("The capital of " + country + " is " + capital + ".")
