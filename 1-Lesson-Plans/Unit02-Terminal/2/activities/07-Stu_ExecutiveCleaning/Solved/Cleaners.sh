# Create a New Folder Called Sorted_Gibberish
mkdir Sorted_Gibberish

# Create Subfolders in Sorted_Gibberish
mkdir Sorted_Gibberish/Docs Sorted_Gibberish/Data Sorted_Gibberish/Text

# Search for all Word Files and copy to Docs folder
find -type f -iname *docx* -exec cp {} Sorted_Gibberish/Docs \;

# Search for all Excel Files and copy to Data folder
find -type f -iname *xlsx* -exec cp {} Sorted_Gibberish/Data \;

# Search for all Text Files and copy to Text folder
find -type f -iname *txt* -exec cp {} Sorted_Gibberish/Text \;

# Bonus
# -------------------------------------------------------------

# Create LargeFiles folder
mkdir Sorted_Gibberish/LargeFiles

# Search for all large files (>200 KB) and move to a folder titled Sorted_Gibberish/LargeFiles 
find -type f -size +200 -exec mv {} Sorted_Gibberish/LargeFiles \;
