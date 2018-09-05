# By using the input() function, Python can take in user input from the command line
# The text stored within input() is the prompt the user will be given in the terminal
name = input("What is your name? ")
print("Hello " + name)

# Every input is taken in as a string
# This means integers/floats will have to be converted to be used properly
number = input("Please enter a number: ")
print(int(number) * 2)
