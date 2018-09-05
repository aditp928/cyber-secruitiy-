hobbies = ["Rock Climbing", "Bug Collecting", "Cooking", "Knitting", "Writing"]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Looping through the values in a list
for hobby in hobbies:
    print(hobby)

print("-------------")

# It is possible to loop through the length of a list numerically too
for x in range(len(hobbies)):
    print(x)
    # You can also use this to loop through the index of a list
    print(hobbies[x])
    # This also means that you can loop through two or more lists at once
    print(weekdays[x])

print("-------------")

# It is possible to loop through a range of numbers as well
# The first number in range() is the starting value while the second is the number to loop up to
for x in range(2, 5):
    print(x)

print("-------------")

# Nested for loops can also be used to loop through lists of differing lengths
users_info = [
    ["Jacob", "Password123"],
    ["Ronessa", "AGreatPasscode"],
    ["Eric", "PassPassPass"]
]

for user in users_info:
    for info in user:
        print(info)
