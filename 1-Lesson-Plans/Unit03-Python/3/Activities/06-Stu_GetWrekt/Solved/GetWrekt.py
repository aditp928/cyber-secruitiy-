# Import the os module into Python
import os

# Walk through all of the files contained within the Diaries directory
for root, dirs, files in os.walk("Diaries", topdown=False):

    # Loop through all of the files in the current root
    for file_name in files:

        # Create and store the path to the current file
        file_path = os.path.join(root, file_name)

        # Open up the file in write mode
        current_diary = open(file_path, "w")

        # Write "GET WREKT SKRUB!!" to the file
        current_diary.write("GET WREKT SKRUB!!")
