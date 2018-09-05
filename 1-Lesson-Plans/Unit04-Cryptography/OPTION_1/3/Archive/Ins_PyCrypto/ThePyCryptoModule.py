# The PyCrypto module is helpful in creating all sorts of encryptions
# This is the string that we will be encrypting in all sorts of ways!
msg_to_encrypt = "UFO TOFU"

####################
## SHA-256 Hashes ##
####################

# Import SHA256 from Crypto.Hash
from Crypto.Hash import SHA256

# Call the SHA256 function and create a new encryption containing a string
hashed_message = SHA256.new(msg_to_encrypt.encode())

# Use hexdigest() to read the encrypted string
print("SHA256: " + str(hashed_message.hexdigest()))
print("-------------")

################
## DES Cipher ##
################

# Import DES from Crypto.Cipher
from Crypto.Cipher import DES

# When using a block cipher like DES the message's length has to be a multiple of the keys bytes. In this case the key is 8 bytes and, as such, the message has to be a multiple of 8 characters in length
block_key = "01234567"

# Create a new DES generator with the block key and specifying the mode of encryption to use
des = DES.new(block_key, DES.MODE_ECB)

# Use the des generator to encrypt the message
des_crypted_msg = des.encrypt(msg_to_encrypt.encode())
print("Encrypted: " + str(des_crypted_msg))

# Use the des generator to decrypt the message
print("Decrypted: " + str(des.decrypt(des_crypted_msg)))
print("-------------")

#########################
## Public/Private Keys ##
#########################

# Import RSA from Crypto.PublicKey
from Crypto.PublicKey import RSA

# Generate a new private key
# The integer passed as a parameter indicates the size of the key in bits
private_key = RSA.generate(1024)

# Use exportKey() in order to create a string version of the key
# Usually the public key is the one you would want to export so coded messages can be sent
private_key_export = private_key.exportKey()
print(str(private_key_export) + '\n')

# The RSA.importKey() function can then be used to pull an external key in
private_key_import = RSA.importKey(private_key_export)

# Generate a public key based upon the private key
public_key = private_key_import.publickey()

# Use the public key to encode a message
# Make sure that the string to encrypt is converted to bytes
pub_crypted_msg = public_key.encrypt(msg_to_encrypt.encode(), 32)
print("Encrypted: " + str(pub_crypted_msg))

# Using the private key to decode the message
print("Decrypted: " + str(private_key_import.decrypt(pub_crypted_msg)))

