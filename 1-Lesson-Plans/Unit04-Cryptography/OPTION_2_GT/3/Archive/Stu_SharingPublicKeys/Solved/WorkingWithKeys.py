# Import RSA from Crypto.PublicKey
from Crypto.PublicKey import RSA

# Import the os module
import os

# Function to generate a private key and send a public key
def generateKeys():

  # Make a reference to the file path that the public key generated will be stored in
  public_key_path = os.path.join("Keys/PublicKey.pem")

  # Open up the public key file and set it to write bytes mode
  public_key_file = open(public_key_path,"wb")

  # Make a reference to the file path that the private key generated will be stored in
  private_key_path = os.path.join("Keys/PrivateKey.pem")

  # Open up the private key file and set it to write bytes mode
  private_key_file = open(private_key_path,"wb")

  # Generate a new private key
  private_key = RSA.generate(1024)

  # Write the private key to the private key file in the PEM format
  private_key_file.write(private_key.exportKey(format="PEM"))

  # Generate a public key based upon the private key
  public_key = private_key.publickey()

  # Write the public key to the public key file in the PEM format
  public_key_file.write(public_key.exportKey(format="PEM"))

# Function to use an external key and create an encrypted message
def useKey():

  # Create a variable which will hold the user's input for what to encrypt
  secret_message = input("What would you like to encrypt? ")

  # Make a reference to the file path that the public key generated is stored
  public_key_path = os.path.join("Keys/PublicKey.pem")

  # Open up the public key file and set it to read bytes mode
  public_key_text = open(public_key_path,"rb").read()

  # Use RSA.importKey() to generate the public key to use
  public_key = RSA.importKey(public_key_text)

  # Encrypt the message
  encrypted_message = public_key.encrypt(secret_message.encode(), 32)

  # Make a reference to the file where the encoded message will be stored
  encrypted_message_path = os.path.join("Messages/EncryptedMessage.pem")
  encrypted_message_file = open(encrypted_message_path,"wb")
  encrypted_message_file.write(encrypted_message[0])

# Function that decrypts the encrypted message file
def decrypt():

  # Make a reference to the file path that the private key generated is stored
  private_key_path = os.path.join("Keys/PrivateKey.pem")

  # Open up the private key file and set it to read bytes mode
  private_key_text = open(private_key_path,"rb").read()

  # Use RSA.importKey() to generate the private key to use
  private_key = RSA.importKey(private_key_text)

  # Take in the encrypted message and read it
  encrypted_message_path = os.path.join("Messages/EncryptedMessage.pem")
  encrypted_message_file = open(encrypted_message_path,"rb")
  encrypted_message = encrypted_message_file.read()

  # Decode the message and print it out to the screen
  print("The secret message is..." + str(private_key.decrypt(encrypted_message)))
  print("----------------------------------")

# Variable being used to store the user's input for the command line interface
user_input = ""

# Setting up the command line interface for this application
while(user_input != "quit"):

  # Printing out the options for the user
  print("Please choose one of the following...")
  print("(1) Generate new keys")
  print("(2) Encode a message with public key file")
  print("(3) Decrypt a message with private key file")
  print("(quit) Quit the application")
  print("----------------------------------")
  user_input = input("Select option... ")

  # If the user selects one, two files will be created...
  # The first file contains the public key to encrypt messages
  # The second file contains the private key to decrypt messages
  if(user_input == "1"):
    generateKeys()
  
  # If the user selects two, they will create a encrypted message...
  # This uses the public key file that is stored within the "Keys" folder
  # It then saves the encrypted message to a file in the "Messages" folder
  elif(user_input == "2"):
    useKey()
  
  # If the user selects three, they will decrypt the encrypted message...
  # This uses the private key stored within the "Keys" folder
  # It also reads the message from the file in the "Messages" folder
  elif(user_input == "3"):
    decrypt()

  # If the user enters quit, then the application will close


# With a partner, generate keys and messages, share the files, and see what happens when...
# You simply run the application in order (1, then 2, then 3)
# You generate keys and message, share the message with your partner, and then try to have them decode it
# You generate keys, share the public key file, have your partner generate a message, share the message file, and then decrypt using your private key