# Instructions

- Untar the archive you received (located in `Unsolved`)
- Find all mp3 or flac files
- Move them to `Music/`
- Grep song names to find out which decade the collection is (mostly) from

# Solutions

- Untar gzipped tarball: `tar -xzzvf archive.tar.gz`
- Make `Music/MP3` and `Music/FLAC` with one command: `mkdir -p Music/{MP3,FLAC}`
- Simpler alternative:
  - `mkdir Music`
  - `cd Music`
  - `mkdir MP3 FLAC`
- Find all MP3 or FLAC files and move to `Music`
  - `find . -type f \( -iname '*.mp3' -o -iname '*.flac' \) -exec mv {} Music \;`
