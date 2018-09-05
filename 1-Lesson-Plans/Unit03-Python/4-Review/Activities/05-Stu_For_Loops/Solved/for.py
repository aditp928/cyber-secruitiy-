# TODO: Create a list, called `big_wins`.
big_wins = []
# TODO: Add five things you've learned in the past two weeks.
big_wins.extend([
    "Frequency analysis", 
    "Crib dragging", 
    "All about XOR ciphers", 
    "Coding is fun", 
    "Icelandic"
])

# TODO: Use a `for` loop to print: "Recently, I learned: <THING YOU LEARNED>."
for win in big_wins:
    print("Recently, I learned: " + win + ".")
