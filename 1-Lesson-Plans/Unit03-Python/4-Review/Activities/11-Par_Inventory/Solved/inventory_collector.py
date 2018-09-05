# TODO: Create an empty dictionary, called inventory
inventory = {}

# TODO: Ask the user how many items they have in their inventory
item_count = int(input("How many items do you have in your inventory? "))

# TODO: Use `range` and `for` to loop over each number up to the inventory number
# TODO: Inside the loop, prompt the user for the name of an item in their inventory ("What's the item? ")
# TODO: Then, prompt the user for the price of that item ("How much does it cost? ")
# TODO: Finally, put the item into the dictionary as the key, and associate it with its price
for _ in range(item_count):
    item_name = input("What's the item? ")
    item_price = input("What's its price? ")
    inventory[item_name] = item_price

# TODO: Outside of the loop, use `items` to print: "The price of <ITEM> is $<PRICE>."
for item, price in inventory.items():
    print("The price of " + item + " is $" + price + ".")
