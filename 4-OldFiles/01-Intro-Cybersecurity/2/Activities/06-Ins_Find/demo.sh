# Find all files in the current directory and all of its subdirectories
# `.` signifies current folder
# `-type f` signifies that we are looking for files
find . -type f

# Find all directories in the current directory and all of its subdirectories
# `-type d` signifies that we are looking for directories
find . -type d

# Find all files with a given name (-name)
find . -type f -name flag1.txt

# Find all files with a given name and ignore case (-iname)
find . -type f -iname FLAG1.txt

# Find all files in the Docs folder  with a given name and ignore case
find Docs -type f -iname flag2.txt

# Find all files in the Docs directory whose name ends with txt and ignore case
# `*` is a wildcard
find Docs -type f -iname '*.txt'

# Find all files in the Pictures directory whose name starts with 'flag' and ignore case
find ~/Pictures -type f -iname 'flag*'

