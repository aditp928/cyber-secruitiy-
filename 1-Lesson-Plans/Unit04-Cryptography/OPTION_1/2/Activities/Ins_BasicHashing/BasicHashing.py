# Import the hashlib module
import hashlib

# String that we will be hashing
string_to_hash = "Hello World!"

# By printing out hashlib.algorithms_guaranteed, a list of all the hashing methods included is shown
print(hashlib.algorithms_guaranteed)

# The hashing functions in Python3 require a sequence of bytes as a parameter
# This can be done by either using the encode() function or by placing a "b" before the quotations
md5_object = hashlib.md5(b"Hello World!")

# The hexdigest() function is then used on the hashed object to show the hex string representing the hash
print("Using md5: " + str(md5_object.hexdigest()))

# The digest function could also be used to show the hashed sequence of bytes
print("Using md5: " + str(md5_object.digest()))
print("-----------------")

# All of the other algorithms shown in hashlib.algorithms_guaranteed can also be used
sha1_object = hashlib.sha1(string_to_hash.encode())
print("Using sha1: " + str(sha1_object.hexdigest()))
print("Using sha1: " + str(sha1_object.digest()))
print("-----------------")
blake2b_object = hashlib.blake2b(string_to_hash.encode())
print("Using blake2b: " + str(blake2b_object.hexdigest()))
print("Using blake2b: " + str(blake2b_object.digest()))
print("-----------------")

# All of this can then, of course, be utilized to work with user input
mystring = input("Enter string to hash: ")
hash_object = hashlib.md5(mystring.encode())
print("Your hashed string is now... " + str(hash_object.hexdigest()))