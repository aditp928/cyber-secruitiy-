# TODO: Create a list, called `todos`, and populate it with a series of tasks you need to do
todos = [
    "Brush teeth",
    "Fry bacon",
    "Eat bacon",
    "Brush teeth again",
    "Take on the world",
    "Struggle",
    "Prevail",
    "Wind down",
    "Rinse",
    "Wash",
    "Repeat"
]

# TODO: Use a `for` loop and `enumerate` to print: "<NUMBER> <TASK> [ ]"
# NOTE: The brackets are just a place to write a checkmark!
for item_number, todo in enumerate(todos):
    print(str(item_number) + ". " + todo + " [_]")
