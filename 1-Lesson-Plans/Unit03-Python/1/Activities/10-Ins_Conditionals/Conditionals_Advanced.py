x = 1
y = 10

# == evaluates to True if the two values are equal
if (x == 1):
    print("x is equal to 1")

# != evaluates to True if the two values are NOT equal to each other
if (y != 1):
    print("y is not equal to 1")

# Checks if one value is less than another
if (x < y):
    print("x is less than y")

# Checks that one value is greater than another
if (y > x):
    print("y is greater than x")

# Checks that a value is less than or equal to another
if (x >= 1):
    print("x is greater than or equal to 1")

# Checks that both conditions are met using "and"
if (x == 1 and y == 10):
    print("Both values returned true")

# Checks if either of two conditions is met
if (x < 45 or y < 5):
    print("One or more of the statements were true")

# if - else statement
if (x > 5):
    print("x is large")
else:
    print("x is small")

# if - elif - else statement
if (y < 5):
    print("y is less than 5")
elif (y == 5):
    print("y is equal to 5")
else:
    print("y is greater than 5")

# Nested if statements
if (x < 10):
    if (y < 5):
        print("x is less than 10 and y is less than 5")
    elif (y == 5):
        print("x is less than 10 and y is equal to 5")
    else:
        print("x is less than 10 and y is greater than 5")

