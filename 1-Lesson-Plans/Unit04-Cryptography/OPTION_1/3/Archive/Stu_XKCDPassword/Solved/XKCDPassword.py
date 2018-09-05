# Import the secrets module
import secrets

# Import the os module
import os

# Read in the word file
words_path = os.path.join("Words.txt")
words_file = open(words_path, "r")
words_text = words_file.read()

# Split the words_text variable on newlines
words_list = words_text.split("\n")

# Variable to store the passphrase
passphrase = ""

# Loop for however long you want the passphrase to be
for i in range(4):

  # Select a random word using the secrets module and add it to the passphrase
  passphrase += secrets.choice(words_list).capitalize()

# Print out the passphrase
print(passphrase)