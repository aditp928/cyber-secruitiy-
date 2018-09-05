# Part I (Basic Setup)
# -----------------------------------
# SSH Into VM
# Assuming VM IP Address is 10.3.2202
ssh library-admin@10.3.2.202

# Explore File System
ls
cd Files
ls

# Make Solutions Folder
cd ..
mkdir Solutions

# Part II (Finding Files)
# -----------------------------------
# Search for phrase catalog in any file names. Copy files to Solutions.
find Files -type f -iname '*catalog*' -exec cp {} Solutions \;

# Search for phrase brace in any file names. Copy files to Solutions.
find Files -type f -iname '*brace*' -exec cp {} Solutions \;

# Part III (Collecting Chapters)
# -----------------------------------

# Create relevant folders
mkdir Books
cd Books
mkdir Frankenstein MobyDick PrideAndPrejudice TomSawyer 
mkdir HocusPocus ATaleOfTwoCities AliceInWonderland FairyTails 
mkdir TheImportanceOfBeing Earnest Dracula

# Find Relevant Chapters
cd Frankenstein
find ../../../Files/ -type f -iname '*frankenstein'

# Find and Copy Relevant Chapters
find ../../../Files/ -type f -iname '*frankenstein' cp {} . \;

# Explore Chapters
ls 

# Count Chapters
ls -1 | wc -ls

# Combine Chapters
cat {1..47}_frankenstein.txt > frankenstein.txt

# Repeat lines 34-48 other books
# ...

# Part IV (Tar'ing Files)
# -----------------------------------
cd ..
cd ..
tar -zcvf Solutions.tar.gz Solutions/

# Part V (Books Ahoy!)
# -----------------------------------
exit
scp librar-admin@10.3.2.202:Solutions.tar.gz
