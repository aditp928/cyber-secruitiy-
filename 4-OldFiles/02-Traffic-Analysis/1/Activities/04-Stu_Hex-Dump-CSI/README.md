# Instructions

- Move into `MysteryFiles`. This directory contains files without extensions. 
- Use `xxd` to figure out the right extension for each file, and rename each file accordingly.

# Solutions

From `Solved`:

- `cd MysteryFiles`
- `xxd <each file> | less`
  - The first line of each file's hexdump will contain metadata revealing its file type.
  - `sample` is an exception. It contains "EXIF" in the first line, but the file extension is JPG (you can find this on line 717 of the hexdump). Students can just write down "EXIF" as the file type for this one, that's fine. Tell them that this indicates a JPG file.
- Solutions are:
  - `sample.jpg`
  - `success.gif`
  - `poc_gtfo.pdf`
