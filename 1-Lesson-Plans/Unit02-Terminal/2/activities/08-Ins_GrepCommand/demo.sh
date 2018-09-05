# Return every line for which the word "John" appears (case-sensitive)
grep 'John' *

# Return every line for which the word "John" appears (case-insensitive)
grep -i 'john' *

# Return every line for which the word "John" does not appear (case-insensitive)
grep -iv 'john' *

# Return a list of files for which the word "hidden text" appears in the directory
grep -rl 'hidden text' * 