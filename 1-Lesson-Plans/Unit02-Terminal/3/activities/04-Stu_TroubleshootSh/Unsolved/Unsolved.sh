# Create a Sorted_Folder
mkdir Sorted_Folder

# Create subfolders for each document type
mkdir docx, xlsx txt, 

# Find all files of each file type and move to its respective folder
find -type d docx -exec cp {} docx /;
find -type f xlsx -exec cp {}  xlsx/;
find -type b txt -exec cp {} txt /;

# Count the number of incidences of each file type
grep docx
grep xlsx 
grep txt
