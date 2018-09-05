# Find the name "John" in the file "chat_history.txt"
grep 'John' chat_history.txt

# Find the name "John" in the file "chat_history.txt", and ignore case (finds JOHN, John, john, etc.)
grep -i 'john' chat_history.txt

# Find the name "John" in the file "chat_history.txt", ignore case, and include line numbers 
grep -in 'john' chat_history.txt

# Find every line in `chat_history.txt` that does NOT contain the name `john`, ignore case
grep -iv 'john' chat_history.txt

# Find out how many lines in `chat_history.txt` DO contain the name `john`
# `| wc -l` signifies "word count" and so `wc -l` translates to word count in lines
grep -i 'john' chat_history.txt | wc -l

# Find out how many lines in `chat_history.txt` do NOT contain the name `john`
grep -iv 'john' chat_history.txt | wc -l

# Look for the words "hidden text" in every file in the current directory, and ignore case
# `-rl` indicates recursive search for files 
grep -rl 'hidden text' FilesWithHiddenText

# List all files in the current directory and all subdirectories, then see how many have the word `mysterious` in the title
# List all files, with each one on a single line; find filenames that contain mysterious; count the results
ls -R1 | grep -i 'mysterious' | wc -l
