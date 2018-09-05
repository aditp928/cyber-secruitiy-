# Show the first 10 lines of a file
head frank_1.txt

# Show the last 10 lines of a file 
tail frank_1.txt

# Print the contents of one or more files to the terminal: `cat <file1> <file2> ...`
cat frank_1.txt

# Combine two files into one (without saving)
cat frank_1.txt frank_2.txt

# Combine two files into one and save the result into a new file
# '>' translates to "save to file"
cat frank_1.txt frank_2.txt > frank_full.txt

# Combine two files into one, saves the result in a new file, and immediately preview its
# '| tee' translates to both "save to file" and "view the file" 
cat frank_1.txt frank_2.txt | tee frank_full.txt

# Appends to the bottom of a file. 
# '>>' translates to "append to the bottom". (No content will be written over).
echo -e "THIS WAS A GREAT BOOK" >> frank_full.txt

# Look at the last 10 lines of a file
# Note the presence of the appended line `THIS WAS A GREAT BOOK`!
tail frank_full.txt

# Look at last 3 lines of of a file
tail -3 frank_full.txt

# Look at FIRST 3 lines of a file
head -3 frank_full.txt

# Read the contents of a file on the command line: `less <filename>`
# Press `d` to page down; `u` to page up; `q` to quit
less frank_full.txt
