# Create a folder called Undumped
mkdir Undumped

# Copy all dump files
find . -type f -iname '*dump*' -exec cp {} Undumped \;

# Look at all file names
ls

# Preview dump contents
head orchestra.dump

# Reverse dump each file (individually)
xxd -r -p orchestra.dump > orchestra.undump

# Use xxd to determine the true file signature (ID3 signifies MP3)
xxd orchestra.undump | head
