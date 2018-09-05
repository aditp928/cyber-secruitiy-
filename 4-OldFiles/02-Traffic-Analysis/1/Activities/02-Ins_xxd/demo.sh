# Generate hex dump of a GIF. Displays three columns:
#   Column 1: Line Number
#   Column 2: Hex Representation
#   Column 3: ASCII Table (Somewhat human-readable representation)
xxd lol.gif

# Generate hex dump of a GIF
# Don't include line numbers or ASCII table
xxd -p lol.gif

# Only look at beginning/end of hexdump
xxd lol.gif | head
xxd lol.gif | tail

# Use `less` to page through hexdump
xxd xkcd.png | less

# Note that the ASCII table for GIF and PNG images contain a clue as to which sort of image it is!
# Signature for .TIF is "II*"
xxd lol.gif
xxd xkcd.png
xxd sample.tif

# This is true even if the file doesn't have an extension
xxd gdpr_2x
xxd airfield
