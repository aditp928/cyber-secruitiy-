# Determine the IP Address on the **Virtual Machine**
ifconfig

# ------------------------------------------------------

# SSH into the Virtual Machine from the **Local Machine**
ssh poweruser@XXX.XXX.XXX.XXX

# Enter the password: grep

# Create a folder called Extract
mkdir Extract

# Find and copy the password file
find . -type f -iname "*password*" -exec cp {} Extract \;

# Find the finance file 
find . -type f -iname "*finance*" -exec cp {} Extract \;

# Find the email file
find . -type f -iname "*.ost" -exec cp {} Extract \;

# Find the topsecret file 
find . -type f -iname "*topsecret*" -exec cp {} Extract \;

# Tar the files 
tar -cvf Extract.tar Extract/