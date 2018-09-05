# Create folders
mkdir GIFs JPEGs

# Check the signatures of a few "test" files
xxd angry.gif angry | head
xxd RmHs.gif | head

# Search all files for the presence of signatures
grep -rli 'jfif'
grep -rli 'gif'

# Bonus: Search all files and move into respective folders
grep -rli 'jfif' | xargs mv -t GIFs
grep -rli 'GIF' | xargs mv -t JPEGs

# Count the number of files in each folder
cd GIFs
ls | wc -l

cd ..
cd JPEGs
ls | wc -l