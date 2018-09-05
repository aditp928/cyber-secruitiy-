# Print a message
echo "hello, world"

# Print the path to the current folder
pwd

# Show all files in the current folder
ls

# Open the current folder in a GUI in Windows
explorer .

# Open the current folder in a GUI in Mac
open .

# Create a new directory/folder: `mkdir <directory_name>`
mkdir MyFolder

# Move into the directory `MyFolder`
cd MyFolder

# Clears the command line
clear 

# Create a new, empty file with a given name: `touch <filename>`
touch MyFile.txt

# Create a new folder called: `MySubFolder`
mkdir MySubFolder

# Navigate into `MySubFolder`
cd MySubFolder

# Move up one folder
cd ../

# Move up two folders
cd ../../

# Move into your home directory--the `~` is a "shortcut" for your home directory
cd ~

# Move back to the last folder you were in
cd -

# Copy a file from one place to another: `cp <file_name> <destination>`
# Copy a file called `example.txt` to the `Desktop` folder in your home directory
cp MyFile.txt ~/Desktop

# Move a file from one place to another: `cp <file_name> <destination>`
# Move a file called `example.txt` to the `Desktop` folder in your home directory
mv MyFile.txt ~/Desktop
