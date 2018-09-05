# Navigate into Gibberish Folder
cd IRC_Logs

# Count the number of resulting lines that appear from our search (effectively result count)
find . -type f | wc -l

# Count the number of logs that contain the "2" in the file name
find . -type f -iname *2* | wc -l

# Count the number of instances in which the word "heartbleed" appeared in the logs.
grep -i "heartbleed" * | wc -l

# Count the number of files in which the word "heartbleed" appeared in the logs.
grep -rli "heartbleed" * | wc -l
