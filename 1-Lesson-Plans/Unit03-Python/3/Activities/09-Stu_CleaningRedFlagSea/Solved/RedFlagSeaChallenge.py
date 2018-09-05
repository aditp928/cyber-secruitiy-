# Import the two modules that will be used in this code
import os
import datetime

# Since there are so many files, os.walk would be wise
for root, dirs, files in os.walk('Text', topdown=False):

    # Collect the number of files so as to help find average
    num_files = len(files)

    # Create a variable to store the total size of the folder
    folder_size = 0

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

        # Add the current file's size to the folder's size
        folder_size += file_size

    # When the loop ends, find the average file size
    average_file_size = folder_size / num_files

    # Print out the number of files, the folder size, and average file size
    print("NUM FILES: " + str(num_files))
    print("FOLDER SIZE: " + str(folder_size))
    print("AVERAGE FILE SIZE: " + str(average_file_size))
    print("------------------")

    # User input to check if the user wants to remove offending files from the system
    remove_files = input(
        "Would you like to remove irregular files? (yes or no)\n")

    # If the user chooses "yes"
    if remove_files == "yes":

        # Loop through the files again
        for file_name in files:

            # Create the path to the current file
            file_path = os.path.join(root, file_name)

            # Collect the stats on the file and save it
            file_info = os.stat(file_path)

            # Collect the file size of the file
            file_size = file_info.st_size

            # Check if the file's size is greater than the average file size
            if(file_size > average_file_size):

                # Print out a statement to say which file is being removed
                print("Removing " + file_path + "...")

                # Remove the file in question from the system
                os.remove(file_path)

                # Print out that the file has been removed
                print("Removed!")
