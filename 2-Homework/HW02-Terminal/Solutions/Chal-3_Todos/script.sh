# Navigate into each of the individual's folders
cd Carrie

# Concatenate all of the to-dos into single files
cat * > all.txt

# Create a file for tasks already done
grep -i 'done' all.txt > done.txt

# Create a file for tasks already done
grep -iv 'done' all.txt > unfinshed.txt

# Count the number done and still unfinished
grep -i 'done' * | wc -l
grep -iv 'done' * | wc -l

# ----------------------------------------------

# Navigate into each of the individual's folders
cd ..
cd Jennifer

# Concatenate all of the to-dos into single files
cat * > all.txt

# Create a file for tasks already done
grep -i 'done' all.txt > done.txt

# Create a file for tasks already done
grep -iv 'done' all.txt > unfinshed.txt

# Count the number done and still unfinished
grep -i 'done' * | wc -l
grep -iv 'done' * | wc -l

# ----------------------------------------------

# Navigate into each of the individual's folders
cd ..
cd John

# Concatenate all of the to-dos into single files
cat * > all.txt

# Create a file for tasks already done
grep -i 'done' all.txt > done.txt

# Create a file for tasks already done
grep -iv 'done' all.txt > unfinshed.txt

# Count the number done and still unfinished
grep -i 'done' * | wc -l
grep -iv 'done' * | wc -l

# ----------------------------------------------
# Create a Productivity Report and save the contents from the counts previous
cd ..
touch ProductivityReport.md
