hobbies = ["Rock Climbing", "Bug Collecting", "Cooking", "Knitting", "Writing"]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# range start defaults to 0 - this loops from x=0 to x=4
for x in range(len(hobbies)):
    print(x)
    # can loop through two lists at the same time
    print(hobbies[x])
    print(weekdays[x])

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
