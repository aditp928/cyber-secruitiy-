# Import the zipfile and os modules
import os
import zipfile

# List of files within the Passwords folder
file_names = ["0to1000.txt","1000to2000.txt","2000to3000.txt","3000to4000.txt","4000to5000.txt"]

# Create a function that will allow users to set which password file they would like to use
def collectPasswords(file_to_use):

    # Create the file path that points to the password dictionary
    passwords_path = os.path.join("Passwords", file_to_use)

    # Open the file and read it so that it is a string
    passwords_file = open(passwords_path, "r")
    passwords_string = passwords_file.read()

    # Split the file on newlines so that it is now a list
    passwords_list = passwords_string.split("\n")

    # Return the passwords list
    return passwords_list

# Create a function that will be used to crack the zip folders
def crackZips(passwords):

    # Loop through all of the zips using the os.walk() function
    for root, dirs, files in os.walk("ZippedFiles"):

        # Loop through each file that is collected
        for file_name in files:

            # Check that the file is a zip file by splitting on the period and checking for zip
            if(file_name.split(".")[1] == "zip"):

                # Create the path to the current file
                file_path = os.path.join(root, file_name)

                # Create a reference to the zipped file
                z_file = zipfile.ZipFile(file_path)

                # Loop through each password in the passwords list
                for password in passwords:

                    # Try to extract all of the files in the zipped file using the current password
                    try:

                        z_file.extractall(pwd=password.encode('cp850','replace'))

                        # Print out what the password for the zipped file was
                        print("The password for " + file_name + " was " + password)

                        break
                    
                    # If the file fails to open with the current password, move onto the next one
                    except:
                        pass

# Loop through the file names for the password files
for current_file in file_names:

    passwords = collectPasswords(current_file)
    crackZips(passwords)