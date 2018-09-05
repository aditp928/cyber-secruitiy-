# Instructions

Use `find`, `xxd`, and `grep` to figure out which file(s) are named with the wrong extensions.

- Find all files with a GIF extension.

- Use `xxd` and `grep` to check which of these files are actually JPGs.

- Next, find all files with either a JPG or JPEG extension.

- Use `xxd` and `grep` to check which of these files is actually a GIF.

# Solutions

From top-level activity directory:

- `cd Unsolved`
- `mkdir Solutions`
- `cd Solutions`
- Find misnamed GIFs: `find ../Pictures/ -type f \( -iname '*jpg' -o -iname '*jpeg' \) -exec grep -inT 'gif' {} \; >> misnamed_gifs`
- Find misnamed JPGs: `find ../Pictures/ -type f -iname '*gif' -exec grep -inT 'jfif' >> misnamed_jpgs`
  - **Note**: JFIF is the signature for JPG files, *not* the word JPG or JPEG
- Double-check that these were misnamed by looking at the headers in these files
  - Run: `xxd Pictures/did_it.jpg | less`
  - Run: `xxd Pictures/real_world.jpg | less`
  - Run: `xxd Pictures/favorite_file.gif | less`
- Change the file extensions
  - Run: `mv Pictures/did_it.jpg Pictures/did_it.gif`
  - Run: `mv Pictures/real_world.jpg Pictures/real_world.gif`
  - Run: `mv Pictures/favorite_file.gif Pictures/favorite_file.jpg`
