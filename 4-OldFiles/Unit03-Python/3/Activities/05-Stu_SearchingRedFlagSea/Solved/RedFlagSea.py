# Import the two modules that will be used in this code
import os
import datetime

# Since there are so many files, os.walk would be wise
for root, dirs, files in os.walk('Text', topdown=False):

    print("CHECKING TIMESTAMPS")
    # Loop through all of the files in the current root
    for file_name in files:

        # Create the path to the current file
        file_path = os.path.join(root, file_name)

        # Using Try and Except to catch any possible errors...
        try:

            # Collect the stats on the file and save it
            fileInfo = os.stat(file_path)

            # Collect the last time at which the file was modified
            timeModified = fileInfo.st_mtime

            # Change the format of timeModified to datetime format
            timeModified = datetime.datetime.fromtimestamp(
                timeModified).strftime('%c')

            # Print out the file name and timestamp to the screen
            print(file_path + ": " + timeModified)

        except:
            pass

    print("---------------------")

    print("CHECKING FILE SIZES")
    # Loop through all of the files in the current root
    for file_name in files:

        # Create the path to the current file
        file_path = os.path.join(root, file_name)

        # Using Try and Except to catch any possible errors...
        try:

            # Collect the stats on the file and save it
            fileInfo = os.stat(file_path)

            # Collect the file size of the file
            fileSize = fileInfo.st_size

            # Print out the file name and file size to the screen
            print(file_path + ": " + str(fileSize))

        except:
            pass
