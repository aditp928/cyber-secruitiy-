# Navigate into Docs folder
cd Docs


# Specific Folder Search
# ---------------------------------------------------
# Find all files within the doctor folder
find doctor -type f 

# Find all folders within the News folder
find News -type d



# Name Searches 
# ---------------------------------------------------
# Find all files with a given name 
find . -type f -name flag1

# Find all files with a given name (case-insensitive)
find . -type f -iname FlAG1



# Conditional Searches
# ---------------------------------------------------
# Find all files that meets either of the two conditions
find . -type f -name flag1 -o -name flag2

# Find all files that meets both of the two conditions
find . -type f -name *book* -a -name *dangerous*



# Type Searches
# ---------------------------------------------------
find . -type f -name *.txt
find . -type f -name *.pdf



# Time Searches
# ---------------------------------------------------
# Find all files and folders created at least 2 minutes ago
find . -cmin +2 

# Find all files and folders created between 2 and 6 minutes ago
find . -cmin +2 -cmin -6



# Size Searches
# ---------------------------------------------------
# Find all files and folders at least 5 kilobytes in size
find . -size +5k

# Find all files and folders less than 50 kilobytes in size
find . -size -50k





