### INTEGERS ###

# Creates a variable called "number_one" and stores an integer inside of it
number_one = 10
print(number_one)
print(type(number_one))

# Creates a variable called "number_two" and stores another integer inside of it
number_two = 5
print(number_two)

# Adding two integers together
sum_of_numbers = number_one + number_two
print(sum_of_numbers)

# Finding the difference between two integers
difference_of_numbers = number_one - number_two
print(difference_of_numbers)

# Dividing one number by another
division_number = number_one / number_two
print(division_number)

# Multiplying one number by another
multiplication_number = number_one * number_two
print(multiplication_number)

### FLOATS ###

# Creates a variable called "float_one" and stores a float inside of it
float_one = 1.25
print(float_one)
print(type(float_one))

# Adding a float to an integer works!
# The datatype of the new variable is a float as well!
float_sum = float_one + 1
print(float_sum)
print(type(float_sum))

### STRINGS ###

# Creates a variable called "text_one" and stores a string inside of it
text_one = "This is some nifty text!"
print(text_one)
print(type(text_one))

# Creates a variable called "text_two" and stores a string inside of it
text_two = "This is also some sweet text!"
print(text_two)

# Adding two strings together is called concatenation
# We add a space between the two texts so that there is a space between the sentences
joined_texts = text_one + " " + text_two
print(joined_texts)

# You cannot add an integer or a float to a string...
will_not_work = "My favorite number is " + 14
print(will_not_work)

# You can, however, convert the integer to a string using the str() function
this_will_work = "My favorite number is " + str(14)
print(this_will_work)

# A stringified number can be converted into an integer or float using either the int() or float() functions as well
text_int = "200"
text_float = "3.1459"
adding_together = int(text_int) + float(text_float)
print(adding_together)
