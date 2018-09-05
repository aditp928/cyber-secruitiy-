# Import the secrets module
import secrets

##################
# Random Numbers #
##################

# To generate a number that is below the number entered
# This will generate a number between 0 and 99
print(secrets.randbelow(100))

# To generate a random integer that is random bits long
# This will generate an integer that is 10 bits long
print(secrets.randbits(10))

# To collect a random value from a list
mylist = [1,2,3,4,5,6,7,8,9,0]
print(secrets.choice(mylist))

#################
# Random Tokens #
#################

# Return a random byte string containing the given number of bytes
# This will create a byte string that is 16 bytes long
print(secrets.token_bytes(16))

# Returns a random text string in hexadecimal that is the given number of bytes long
# This will create a text string that is 32 characters long (2 characters per byte)
print(secrets.token_hex(16))

##################
# Random Strings #
##################

# Bring in the string module
import string

# Create a string that is the alphabet and numbers combined
alphabet = string.ascii_letters + string.digits

# Create a variable to store our random string in
password = ""

# Loop for as long as you want the random string to be
for i in range(10):

  # Add a randomly selected character to the string
  password += secrets.choice(alphabet)

# Print out the password
print(password)