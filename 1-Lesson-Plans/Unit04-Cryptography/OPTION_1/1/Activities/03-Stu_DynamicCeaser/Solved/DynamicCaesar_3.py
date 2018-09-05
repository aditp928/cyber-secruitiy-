# PART I: Obtaining User Inputs
# --------------------------------------------------------
# Sentence to encode
sentence = input("Enter a sentence to be shifted: ")


# Number of letters we will be shifting to create our cipher
shiftNumber = int(input("Enter a shift number: "))






# PART II: Creating the Cipher Alphabet 
# --------------------------------------------------------
# List of letters in the alphabet
regularAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 
                   'g', 'h', 'i', 'j', 'k', 'l', 
                   'm', 'n', 'o', 'p', 'q', 'r', 
                   's', 't', 'u', 'v', 'w', 'x', 
                   'y', 'z']

# Empty list for the shifted letters of the cipher
cipherAlphabet = []

# Loop through each letter of the alphabet and subtract for the shift overage.
# In the loop, append shifted keys into the cipherAlphabet
for i in range(0, len(regularAlphabet)-shiftNumber):
  cipherAlphabet.append(regularAlphabet[i+shiftNumber])


# Loop through the beginning part of the alphabet up to the shift key. 
# In the loop, append shifted keys into the cipherAlphabet
for i in range(0, shiftNumber):
  cipherAlphabet.append(regularAlphabet[i])

# Print the cipher alphabet
print(cipherAlphabet)



# PART III: Encrypt the Sentence Using the Cipher Alphabet
# --------------------------------------------------------
# Create a variable called newSentence
# Loop through each character in the sentence string
# In the loop: 
#  Check if the character exists in the cipherAlphabet (no punctuation or spaces)
#  Determine the index location of each letter in the regular alphabet
#  Use the index location to identify the corresponding cipherAlphabet letter.
#  Add each cipherAlphabet letter to the newSentence string.
#  If the the character is not a letter, add it without shifting.

# Outside the loop:
#  Print the newSentence

# Variable to hold the encrypted sentence
newSentence = ""

# Loops through each character in the sentence string
for i in sentence:

  # Handle the space by skipping it
  if i in cipherAlphabet:

    # Determine the index location of the letter in the alphabet 
    letterPosition = regularAlphabet.index(i)

    # Add the encoded letter to the new sentence
    newSentence = newSentence + cipherAlphabet[letterPosition]
  
  # If the character is a space, immediately incorporate it. 
  else:
    newSentence = newSentence + i

# Print the sentence to the screen
print("Your encoded sentence is: " + newSentence)

