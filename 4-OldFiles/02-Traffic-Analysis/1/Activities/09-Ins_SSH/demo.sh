# STEP 1: Creating User Accounts
# Determine the current user
whoami

# Add a normal user with their very own directory in `/home`
useradd -m -s /bin/bash ahmed

# Sets the user's password through an interactive prompt. Use a dummy password, like: `password`
# The account isn't active until you do this step!
passwd ahmed

# Now, we can log in as the new user with the `su` command
# This will raise an interactive prompt to enter your password, which is: `password`
su ahmed

# Now, create a file...We'll  come back to this later
cd /home/ahmed
echo "hello, world!" > demo_file

# Now you're using the computer as ahmed, not root
# To demonstrate the difference...
cd /
touch /var/tmp/ahmeds_temp_file

# The above command won't work, because you're just a normal user
# Now, log in as root again. First, logout...
exit

# ...Then login as root, with password `toor`
su root

# Now, try the above again. This time, it'll work, because you're root!
cd /
touch /var/tmp/ahmeds_temp_file


# STEP 2: SSH
# We can use this account to log in to the computer from a different one!

# First, WHILE ON THE VM, find out the VM's IP address with `sbin/ifconfig`. 
# Find the block of information called `eth0` (look at the far left)
# Then, look at the line right below this row. The IP address is the number to the right of the word `inet`.
/sbin/ifconfig

# Alternatively, this command prints out only the row containing the `inet` number/IP address
# Write this number down. Let's say it's `192.168.1.4` for this demo`
/sbin/ifconfig | grep 'inet' | head -n 1

# Next, open a terminal on the HOST machine (your Windows or Mac--NOT the VM)
# This will prompt you for a password. Use the one you created your user account with on the VM
ssh ahmed@192.168.1.7

# Now you're connected to the VM's terminal, instead!
# From SSH terminal...
cd /home/ahmed
cat demo_file
