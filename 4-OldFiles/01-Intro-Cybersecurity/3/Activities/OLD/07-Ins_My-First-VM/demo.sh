# Load and start the provided VM in Virtual Box
# Note: If you idle for a long time, the VM will require you to log in
# The default password is: `toor` ("root" backwards)

# From the Desktop, click on the third icon from the top in the sidebar on the left of the screen, called "Files"
# This opens the Kali Linux equivalent of "Explorer" or "Finder"
# Point out that the directories look familiar, so students should feel right at home with the directory layout

# Next, click the icon right above Files, which opens a Terminal
# Tell students that the commands they've learned so far will all work on Linux, too!
cd ~
ls
cd Documents
mkdir MyFirstVirtualFolder
cd MyFirstVirtualFolder
echo -e "hello, world--from LINUX!" >> hello_world
cp hello_world throwaway_file

# We can use `find` and `grep`, as well
# Note: `/` is the root directory--the directory that contains all other directories and files
# Note: Only the "root" user can change files in this directory
cd /
find . -type f -iname 'throwaway*' -exec rm {} \;

# Pressing the Windows or Mac key brings up an "Application Search" bar
# Press this button, and type in "Terminal"
<Win/Mac> + "termineter" + ENTER

# Finally, show that we can create tabs in our Terminal...
<Ctrl + Shift + T>

# ...And that we can shift between tabs with Ctrl + PgDwn/Ctrl + PgUp
<Ctrl + PgUp>
<Ctrl + PgDown>
