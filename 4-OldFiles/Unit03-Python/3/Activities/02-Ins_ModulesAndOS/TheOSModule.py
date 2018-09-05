# In order to import the os library into Python use import OS
import os

# The os.path.join() function allows programmers to create file paths that work across multiple operating systems
real_file_path = os.path.join("Resources", "CoolText.txt")
not_a_file = os.path.join("Resources", "NotAFile.txts")

# This path can then be used for open()
cool_text = open(real_file_path, "r")
print(cool_text.read())
print("--------------")

# The os.path.isfile() function allows programmers to check if the file path provided points to an actual file
print(os.path.isfile(real_file_path))
print(os.path.isfile(not_a_file))
print("--------------")

# If there is a desire to navigate through a collection of folders/files, then os.walk() can be used
# This function returns three values for each step it takes: root, dirs, and files
for root, dirs, files in os.walk("Resources", topdown=False):

    # The root is the folder that is currently being searched through
    print("Currently inside of... " + root)

    # The dirs list stores all of the names of the folders inside the current root
    print("The folders in here are..." + str(dirs))

    # The files list stores all of the names of the files inside the current root
    print("The files in here are..." + str(files))
    print("~~~~~~~~~~")

print("--------------")

# In order to construct the file path to use dynamically...
for root, dirs, files in os.walk("Resources", topdown=False):

    # Loop through all of the files in the current root
    for file_name in files:

        # Create a path by taking the root, adding in a backslash, and then the file name
        current_file_path = os.path.join(root, file_name)
        print(current_file_path)

        # We can then check that the file exists through using os.path.isfile()
        print("EXISTS: " + str(os.path.isfile(current_file_path)))
