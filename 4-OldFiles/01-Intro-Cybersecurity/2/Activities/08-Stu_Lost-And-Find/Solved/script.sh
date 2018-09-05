# Part I
# -------------------------------------------------------------------
# Create folder
mkdir all_flags

# Search for flag across all files and copy the files into all_flags
find . -type f -iname flag* -exec cp {} all_flags \;

# Change into the all_flags folder
cd all_flags

# Combine all the flags into a single file
cat flag* > flags.txt

# View the contents 
less flags.txt

# Part II
# -------------------------------------------------------------------
# Create the PDF folder
cd ..
mkdir PDFS

# Find and copy all PDFs
find . -type f -iname *.pdf -exec cp {} PDFS \;

# Find and copy all "books"
find . -type f -iname *book* -exec cp {} PDFS \;

# Rename all books using the `mv` command for moving files
cd PDFS
find . -type f -iname '*book' -exec mv {} "{}.pdf" \;
