# The dictionary that will be used to encode our messages
shifty_dicty = {
  "a":"f",
  "b":"g",
  "c":"h",
  "d":"i",
  "e":"j",
  "f":"k",
  "g":"l",
  "h":"m",
  "i":"n",
  "j":"o",
  "k":"p",
  "l":"q",
  "m":"r",
  "n":"s",
  "o":"t",
  "p":"u",
  "q":"v",
  "r":"w",
  "s":"x",
  "t":"y",
  "u":"z",
  "v":"a",
  "w":"b",
  "x":"c",
  "y":"d",
  "z":"e"
}

# The original message and the variable the encoded message will be placed in
original_message = input("Please enter a message to encode...\n")
encoded_message = ""

# Loop through the original message character by character
for character in original_message:

  # Check to see if the current character is one of the keys in the dictionary
  if(character in shifty_dicty.keys()):

    # Use the current character as the index to place the new value into encoded_message
    encoded_message += shifty_dicty[character]
  
  # If the character is not a key in the dictionary, simply place the current character into encoded_message
  else:
    encoded_message += character

print(encoded_message)

