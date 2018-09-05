# Part 1: Integers
# =====================================

# Prints: 10
# Prints: # <class 'int'>
number_one = 10
print(number_one)
print(type(number_one))

# Prints: 5
number_two = 5
print(number_two)

# Prints: 15
sum_of_numbers = number_one + number_two
print(sum_of_numbers)

# Prints: 5
difference_of_numbers = number_one - number_two
print(difference_of_numbers)

# Prints: 2.0
# Prints: # <class 'float'>
division_number = number_one / number_two
print(division_number)
print(type(division_number))

# Prints: 50
multiplication_number = number_one * number_two
print(multiplication_number)


# Part 2: Floats
# =====================================

# Prints: 1.25
# Prints: # <class 'float'>
float_one = 1.25
print(float_one)
print(type(float_one))

# Prints: 2.25
# Prints: # <class 'float'>
float_sum = float_one + 1
print(float_sum)
print(type(float_sum))


# Part 3: Strings
# =====================================

# Prints: This is some nifty text!
# Prints: # <class 'str'>
text_one = "This is some nifty text!"
print(text_one)
print(type(text_one))

# Prints: This is also some sweet text!
text_two = "This is also some sweet text!"
print(text_two)

# Prints: This is some nifty text! This is also some sweet text!
joined_texts = text_one + " " + text_two
print(joined_texts)

# Prints: My favorite number is 14
this_will_work = "My favorite number is " + str(14)
print(this_will_work)

# Prints: 203.1459
text_int = "200"
text_float = "3.1459"
adding_together = int(text_int) + float(text_float)
print(adding_together)

# Part 4: Strings and Integers
# =====================================

# Bonus: Why will the below statement not work (if uncommented)
# will_not_work = "My favorite number is " + 14
# print(will_not_work)

# Answer: Strings and Integers cannot be combined without type casting (converting variable types)