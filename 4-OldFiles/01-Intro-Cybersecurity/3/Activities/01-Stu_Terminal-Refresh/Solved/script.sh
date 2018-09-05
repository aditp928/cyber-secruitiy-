# Navigate into Music folder
cd Music

# Create MP3 and FLAC folders
mkdir MP3 FLAC

# Find and copy all MP3 files
cd ..
find . -type f -iname '*.mp3' -exec cp {} Music/MP3 \;

# Count all MP3 files (367)
cd Music/Mp3
ls -R1 | wc -l

# Find and copy all FLAC files
cd ..
find . -type f -iname '*.flac' -exec cp {} Music/flac \;

# Count all FLAC files (142)
cd Music/FLAC
ls -R1 | wc -l

