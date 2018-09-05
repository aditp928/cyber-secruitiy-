# Take in user input for the string to encrypt
original_string = input("Please enter the message to encrypt: ")

# Variable to store the encoded message as it is being made
encoded_string = ""

# Loop through every letter in the original message
for letter in original_string:

  # Check if the letter is "a" and replace it with "b"
  if(letter == "a"):
    encoded_string += "b"
  
  # Check if the letter is "e" and replace it with "f"
  elif(letter == "e"):
    encoded_string += "f"

  # Check if the letter is "i" and replace it with "j"
  elif(letter == "i"):
    encoded_string += "j"
  
  # Check if the letter is "o" and replace it with "p"
  elif(letter == "o"):
    encoded_string += "p"
  
  # Check if the letter is "u" and replace it with "v"
  elif(letter == "u"):
    encoded_string == "v"
  
  # Check if the letter is "y" and replace it with "z"
  elif(letter == "y"):
    encoded_string == "z"

  # If the letter is anything else, keep it as is
  else:
    encoded_string += letter

# Print the final encoded string
print(encoded_string)