# Read and answer the comments
def sum(x, y):
    """<EXPLAIN WHAT THIS FUNCTION DOES>"""
    print(x + y)

# Prints: 5
sum(2, 3)

# Prints: 8
sum(5, 3)

# Prints: Nothing--this throws an error!
sum(2, 'a')

# Prints: `None`, because `sum` doesn't return anything!
result = sum(2, 2)
print(result)

# Update the sum function so that the print statement prints "4"
def sum_updated(x, y):
    # What do you need to change the print statement to?
    return x + y

result = sum_updated(2, 2)
print(result)
