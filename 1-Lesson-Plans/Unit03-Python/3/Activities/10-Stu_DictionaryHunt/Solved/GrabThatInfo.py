# Import the os library
import os

# Create a list of keywords to search for
keywords = ["birthday", "password", "mother", "today"]

# Perform an os.walk on the Files folder
for root, dirs, files in os.walk("Files", topdown=False):

    # Loop through each file
    for file_name in files:

        # Construct the path to the current file
        file_path = os.path.join(root, file_name)

        # Open up the file
        file_ref = open(file_path, encoding="utf8")

        # Read the file in order to search through the text
        file_text = file_ref.read()

        # Since all of the keywords are lowercase, convert the text to lowercase
        file_text = file_text.lower()

        # Print out the name of the current file
        print(f'\nSearching {file_path} ...\n')

        # Loop through every keyword in the list of keywords
        for keyword in keywords:

            # Use a .find() in order to check if the keyword is inside of the file
            if (file_text.find(keyword) > -1):
                found_keyword = "TRUE"
            else:
                found_keyword = "false"

            # Print out the keyword and whether it was found in the current file
            print(f'{keyword}: {found_keyword}')

        print("\n--------------------")
