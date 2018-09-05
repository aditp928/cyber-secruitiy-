# Import the two modules that will be used in this code
import os
import datetime

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
