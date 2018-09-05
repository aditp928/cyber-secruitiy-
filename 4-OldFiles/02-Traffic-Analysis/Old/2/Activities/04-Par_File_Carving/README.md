# Digital Sculpture: Or, File Carving

## Instructions

### Visit Rome

- Open [ftp_image.pcapng](Captures/ftp_image.pcapng).

- Reconstruct the image the user downloaded.

  - Where were they?

  - When did they last edit the file? What operating system did they use? What was the date?

### Intercept a Spreadsheet

- Open [ftp_transfer.pcapng](Captures/ftp_image.pcapng).

- What's the user's username? What's their password?

- Reconstruct the user's spreadsheet.

  - What does it look like they were collecting data on?

### Back to School

- Open [http_collegehumor.pcapng](Captures/http_collegehumor.pcapng).

- What's the name of the article the user was reading?

- Find the name of the HTML file/webpage the user was reading. Download it.

- Open the file in a text editor. Do a `Ctrl+F` search for `<img`.

  - This is the start of an "image" tag in HTML.

  - You should find 11 filenames ending in `jpg`. Write these down in a list.

- See how many of these images you can find and download in Wireshark.

  - You won't be able to find all of them. Look carefully at the links for each image. Why can you find some and not others?

- Use `curl` to download one of the files you can't find in Wireshark.
