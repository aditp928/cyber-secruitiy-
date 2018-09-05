# Instructions

- Find all files ending in `dump`
- Use `xxd -r -p` to reverse the hex dumps
- Use `xxd | head -n 3` to find out each file's file type
- Add the appropriate extension to each "undumped" file

# Solution

From `Solved`:

- `mkdir Solutions`
- `cd Solutions`
- `mkdir UndumpedFiles AllDumps`
- Find all files ending in `dump`: `find ../Docs -type f -iname '*dump' -exec mv {} AllDumps \;`
- For each file in `AllDumps`, run: `xxd -r -p <filename>.dump > ../UndumpedFiles/<filename>.undumped`
- `cd ../UndumpedFiles`
- For each undumped file, run: `xxd <filename>.undumped | head -n 3`
  - This reveals the type of each file in the metadata
- Rename each file with the correct extension
  - Just use `mv` to rename manually
