# Create new folders to contain the image files
mkdir Pictures/JPG Pictures/PNG Pictures/TIFF

# Find and copy each type of file
find . -type f -iname '*.jpg' -exec cp {} Pictures/JPG \;
find . -type f -iname '*.png' -exec cp {} Pictures/PNG \;
find . -type f -iname '*.tiff' -exec cp {} Pictures/TIFF \;

# Create a file called PictureCounts.md
touch PictureCounts.md

# Count how many times each file type occurs
echo "JPEG" > PictureCounts.md
find . -type f -iname '*.jpg' | wc -l >> PictureCounts.md

echo "PNG" >> PictureCounts.md
find . -type f -iname '*.png' | wc -l >> PictureCounts.md

echo "TIFF" >> PictureCounts.md
find . -type f -iname '*.tiff' | wc -l >> PictureCounts.md