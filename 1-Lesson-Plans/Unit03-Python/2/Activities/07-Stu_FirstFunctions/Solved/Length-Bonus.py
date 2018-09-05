# returns true if item is lengthable, false otherwise
def lengthable(item):
    length_viable = type(item) is str or type(item) is list

    return length_viable

# returns the length of item
def length(item):
    if not lengthable(item):
        return None

    count = 0

    for i in item:
        count = count + 1

    return count

# returns the last element of item
def last(item):
    return item[length(item) - 1]


# function calls
hello = "hello"
array = [hello, "goodbye"]
print(length(hello))
print(length(array))
print(last(hello))
print(last(array))

print(length(4))
print(length({"name": "Daigo"}))
