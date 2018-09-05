# TODO: Use a `for` loop and the `range` function to print every number up to 10
for number in range(10):
    print("My number is: " + str(number) + ".")

# TODO: Use the `range` function to print every number between 5 and 10
for number in range(5, 10):
    print("My number is: " + str(number) + ".")

# TODO: Create a list called `problems`
problems = []
# TODO: Add up to 99 problems to this list.
problems.extend([
    "Too much swag", 
    "Lambos don't fit in the garage", 
    "Not enough room in first class"
])
# TODO: Store the length of this list in a variable
length = len(problems)
# TODO: Use the `range` function to print every number up to the length of this list
for number in range(length):
    print("My number is: " + str(number) + ".")

# TODO: Instead of using the range function to print every number up to the length of the list...
# TODO: ...Use it to print every element in the list.
# NOTE: Use the number as an index.
for index in range(length):
    print(problems[index])

# TODO: Use a `for` loop and range` to print: "My #1 Problem is: <FIRST PROBLEM>", etc.
for index in range(length):
    print("My #" + str(index) + " problem is: " + problems[index] + ".")
