# Find all text files that begin with the word flag
find . -type f -iname flag*

# Find and copy all flag files into the present directory
# `-exec` signals that we are executing a command
# `cp {}` signifies that we want to copy the contents we found
# `.` signifies that we want to copy these files to the current folder
# `\;` signifies that we want to end our command
find . -type f -iname flag* -exec cp {} . \;

# Find and copy all pngs and jpgs into the Pictures folder of the present directory.
find . -type f \( -iname '*png' -o -iname '*jpg' \) -exec cp {} ./Pictures \;

# Find and copy all files that are not pngs into the NoPNGsAllowed folder.
# `!` signifies that we are looking for all files except ones that match our term
find . -type f ! -iname *.png -exec cp {} NoPNGsAllowed \;