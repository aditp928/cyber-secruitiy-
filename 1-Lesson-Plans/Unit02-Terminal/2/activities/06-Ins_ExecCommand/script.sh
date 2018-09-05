# Find all text files that begin with the word flag
find . -type f -iname flag*

# Create a folder called My_Flags
mkdir My_Flags

# Find and immediately copy all of these flag files to the current directory
find . -type f -iname flag* -exec cp {} My_Flags \;

# -------------------------------------------------

# Create a folder called NoPNGsAllowed
mkdir NoPNGsAllowed

# Find and copy all files that are not pngs into the NoPNGsAllowed folder.
find . -type f ! -iname *.png -exec cp {} NoPNGsAllowed \;