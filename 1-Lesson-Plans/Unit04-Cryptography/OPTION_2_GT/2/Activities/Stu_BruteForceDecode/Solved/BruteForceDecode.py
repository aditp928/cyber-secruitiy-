# List of letters in the alphabet
regularAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 
                   'g', 'h', 'i', 'j', 'k', 'l', 
                   'm', 'n', 'o', 'p', 'q', 'r', 
                   's', 't', 'u', 'v', 'w', 'x', 
                   'y', 'z']

# Create a function that will create the shifted alphabets to test
def shiftAlphabet(shiftNumber):
    cipherAlphabet = []

    # Loop through the alphabet (26 minus the shiftNumber times to account for overage)
    for i in range(0, len(regularAlphabet)-shiftNumber):

        # Position each letter shifted from its original position in the alphabet
        cipherAlphabet.append(regularAlphabet[i+shiftNumber])

    # Loop through the beginning part of the alphabet and separately add it to the cipher list
    for i in range(0, shiftNumber):

        # Position each letter shifted from its original position in the alphabet
        cipherAlphabet.append(regularAlphabet[i])

    # Return the current cipher alphabet
    return cipherAlphabet

# Function used to decode encoded messages
def decodeMessage(encoded_message, cipherAlphabet):

    # Variable to hold our encoded sentence
    newSentence = ""

    # Loops through each character in the sentence string
    for i in encoded_message:

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
    print("Key " + str(shiftNumber) + ": " + newSentence)



# The encoded message
encoded_message = input("Enter the encoded message: ")

# Loop through all possible keys from 1 to 25
for shiftNumber in range(1,26):

    # Run the shiftAlphabet function with the current key
    cipher_alphabet = shiftAlphabet(shiftNumber)

    # Run the decodeMessage function with the encoded message and the cipherAlphabet
    decodeMessage(encoded_message, cipher_alphabet)