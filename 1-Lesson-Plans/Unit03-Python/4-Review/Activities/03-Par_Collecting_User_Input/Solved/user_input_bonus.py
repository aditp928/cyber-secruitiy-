# TODO: Use `input` to collect the user's name.
username = input("What's your name? ")
# TODO: Use `input` to collect your neighbor's name.
neighbors_name = input("What's your neighbor's name? ")
# TODO: Print the message: "My name is `<YOUR NAME>`, and my neighbor's name is `<NEIGHBOR'S NAME>`."
print("My name is " + username + ", and my neighbor's name is " + neighbors_name + ".")

# TODO: Create a list, called `ages`.
ages = []
# TODO: Prompt the user for their age, and add it to the list.
user_age = input("How old are you? ")
ages.append(user_age)
# TODO: Prompt the user for their neighbor's age, and add it to the list.
neighbors_age = input("How old is " + neighbors_name + "?")
ages.append(neighbors_age)

# TODO: Print: "I am <YOUR AGE> years old."
print("I am " + ages[0] + " years old.")
# TODO: Print: "<NEIGHBOR'S NAME> is <NEIGHBOR'S AGE> years old."
print(neighbors_name + " is " + ages[1] + " years old.")
# NOTE: Do you need to use type conversion? Why or why not?
# No, because `input` stores data as a string by default!

# TODO: Create a list, called `hometowns`.
hometowns = []
# TODO: Prompt the user for their hometown.
user_hometown = input("What's your hometown? ")
# TODO: Prompt the user for their neighbor's hometown.
neighbors_hometown = input("What's " + neighbors_name + "'s hometown? ")
# TODO: Add both responses to the `hometowns` list at the same time.
hometowns.extend([user_hometown, neighbors_hometown])
# NOTE: Which function can you use to add many things to a list at once?

# TODO: Print: "Our hometowns are <YOUR HOMETOWN> and <NEIGHBOR'S HOMETOWN>."
print("Our hometowns are " + hometowns[0] + " and " + hometowns[1] + ".")
