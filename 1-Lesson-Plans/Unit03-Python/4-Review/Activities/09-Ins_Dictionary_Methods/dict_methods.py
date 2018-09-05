# Dictionary of highly sensitive personal information
my_nemesis = {
    "Weakness": "Kryptonite",
    "Greatest Fear": "Spiders",
    "Secret Lair": "300 Nemesis Drive #665"
}

# Use `keys` to get a list of all the juicy information you have
juicy_information = my_nemesis.keys()
print("I have dirt about my nemesis's " + str(my_nemesis) + ".")

# Use `values to get a list of all the secret information
secret_weapons = my_nemesis.values()
print("To ruin my rival's life, you need to know about: " + str(secret_weapons) + ".")

# Use `items` to get each key/value pair in a loop
for item, juicy_tidbit in my_nemesis.items():
    print("My nemesis's " + item + " is " + juicy_tidbit + ".")
