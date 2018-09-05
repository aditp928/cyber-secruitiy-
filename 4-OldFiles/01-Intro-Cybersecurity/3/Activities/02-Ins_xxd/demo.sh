# Generate hex dump of a GIF. Displays three columns:
#   Column 1: Line Number
#   Column 2: Hex Representation
#   Column 3: ASCII Table (Somewhat human-readable representation)
xxd lol.gif

# Generate hex dump of a GIF, but exclude line numbers and ASCII table.
xxd -p lol.gif

# Generate first and last set of lines of the hex dump
xxd lol.gif | head
xxd lol.gif | tail

# Use `less` to page through hex dump
xxd xkcd.png | less

# Use `>` to store the hex dump
xxd xkcd.png > xkcd.dump

# Pay attention to how the ASCII table for GIF and PNG images reveal the image format.
# Note: Signature for .TIF is "II*"
xxd lol.gif | head
xxd xkcd.png | head
xxd sample.tif | head

# This is true even if the file doesn't have an extension
xxd gdpr_2x | head
xxd airfield | head
