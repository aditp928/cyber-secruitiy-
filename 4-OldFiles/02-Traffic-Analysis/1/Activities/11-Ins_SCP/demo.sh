# SSH lets us browse another computer, but not transfer files from it
# To get files from another device, we use SCP instead

# First, log into the target machine with SSH
ssh ahmed@192.168.1.7

# Then, do some exploring--find the `ip_information` file from before
# Write down the path to this file
find . -type f -name 'ip_information'

# Exit from SSH
exit

# Now, on the host machine, use SCP instead of SSH to copy that file to this directory
# You'll be prompted for a password, then the file transfer will happen
scp ahmed@192.168.1.7:/home/peleke/IPInformation/ip_information .

# Use `ls` to verify that the transfer worked!
ls

# To download a folder, use the `-r` switch
scp -r ahmed@192.168.1.7:/home/peleke/IPInformation .

# Finally, note that you can also copy a file FROM your local computer TO the server by changing the syntax a bit
# This copies `file_on_host_machine` to the folder `/home/peleke` in the VM
echo -e "This is a file from my host machine!" > file_from_host_machine
scp file_on_host_machine ahmed@192.168.1.7:/home/ahmed/

# Now, if you go to your VM, you'll be able to see this file on it!
