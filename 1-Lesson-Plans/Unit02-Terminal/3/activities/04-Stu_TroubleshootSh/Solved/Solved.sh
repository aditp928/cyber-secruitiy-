# Create a Sorted_Folder
mkdir Sorted_Folder

# Create subfolders for each folder type
mkdir Sorted_Folder/docx Sorted_Folder/xlsx Sorted_Folder/txt

# Find all files of each file type and move to its respective folder
find . -type f -iname "*.docx" -exec cp {} Sorted_Folder/docx \;
find . -type f -iname "*.xlsx" -exec cp {}  Sorted_Folder/xlsx \;
find . -type f -iname "*.txt" -exec cp {} Sorted_Folder/txt \;

# Count the number of incidences of each file type
find Sorted_Folder/docx -type f  | wc -l
find Sorted_Folder/xlsx -type f  | wc -l
find Sorted_Folder/txt -type f  | wc -l