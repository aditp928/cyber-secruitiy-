# Create a new folder
mkdir All_Articles

# Navigate into each subfolder
cd 2

# View the contents
ls

# Move the relevant file
mv 2_dangerous_js.txt ../All_Articles.txt

# Repeat the above steps for each folder
# ...

# Combine all files into a single file
cd ../All_Articles
cat *.txt > full.txt

# View the contents
head -3 full.txt
tail -3 full.txt