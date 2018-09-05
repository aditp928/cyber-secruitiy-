problems = []
problems.extend([
    "Too much swag", 
    "Lambos don't fit in the garage", 
    "Not enough room in first class"
])

# Same as using `range` and indexing, but better
for index, problem in enumerate(problems):
    print("My #" + str(index) + " problem is: " + problem + ".")

# Printing a separator, so it's easier to read output
print("------------")

# Adjusting the start number for human readability
for index, problem in enumerate(problems, start=1):
    print("My #" + str(index) + " problem is: " + problem + ".")
    