# Import the two modules that will be used in this code
import os
import datetime

# User input to check if the user wants to remove offending files from the system
remove_response = input("Would you like to remove irregular files? (yes or no)\n")
should_remove = remove_response == "yes"

# Since there are so many files, os.walk would be wise
for root, dirs, files in os.walk('Text', topdown=False):

    print("CHECKING FILE SIZES")
    # Loop through all of the files in the current root
    for file_name in files:

        # Create the path to the current file
        file_path = os.path.join(root, file_name)

        # Collect the stats on the file and save it
        file_info = os.stat(file_path)

        # Collect the file size of the file
        file_size = file_info.st_size

        # Print out the file name and file size to the screen
        print(file_path + ": " + str(file_size))

        # if file size isn't 100 and the user wants us to delete things:
        if file_size != 100 and should_remove:

            # Print out a statement to say which file is being removed
            print("Removing " + file_path + "...")

            # Remove the file in question from the system
            os.remove(file_path)

            # Print out that the file has been removed
            print("Removed!")



