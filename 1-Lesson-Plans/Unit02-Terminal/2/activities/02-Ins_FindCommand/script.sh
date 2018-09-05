# Navigate into Docs folder
cd Docs

# Find all files in the current directory and all of its subdirectories
find . -type f

# Find all folders in the current directory and all of its subdirectories
find . -type d

# Find all files with a given name (-name)
find . -type f -name flag1

# Find all folders with a given name (-name)
find . -type d -name coffees

# Find all files with a given name and wildcard
find . -type f -name flag*
