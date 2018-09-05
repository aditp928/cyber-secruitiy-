hobbies = ["Rock Climbing", "Bug Collecting", "Cooking", "Knitting", "Writing"]

# Looping through the values in a list
for hobby in hobbies:
    print(hobby)

print("-------------")


# range(start, stop) allows you to loop through a range of numbers
# start is the starting value (inclusive), stop is the end value (not inclusive)
for x in range(2, 5):
    print(x)
    # can reference element in list at index x
    print(hobbies[x])

print("-------------")
