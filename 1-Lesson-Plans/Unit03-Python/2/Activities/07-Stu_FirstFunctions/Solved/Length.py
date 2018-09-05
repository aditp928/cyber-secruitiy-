# function to get the length of an item
def length(item):
    count = 0

    for i in item:
        count = count + 1

    return count

print(length("hello"))
print(length("goodbye"))
print(length(["hello", "goodbye"]))
