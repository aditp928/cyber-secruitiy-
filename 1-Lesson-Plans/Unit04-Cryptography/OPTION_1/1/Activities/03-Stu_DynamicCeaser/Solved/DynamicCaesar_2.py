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

# Print the Cipher Alphabet
print(cipherAlphabet)