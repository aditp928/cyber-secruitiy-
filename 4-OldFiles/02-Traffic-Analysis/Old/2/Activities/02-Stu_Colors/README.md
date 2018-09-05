# Color Me Wired

This one might take some googling/research!

## Instructions

- Open [http_with_delays.pcapng](Captures/http_with_delays.pcapng).

- Create a new coloring rule that highlights packets with either a frame or tcp time delta greater than 1. (we want to see where gaps in communication happened!).

- Open [ftp_image.pcapng](Captures/ftp_image.pcapng).

- Create a coloring rule to highlight FTP requests. (these passwords don't get a pass).

## Hint

- Add a column for Delta time by going to Edit -> Preferences -> Appearance -> Columns, clicking the `+`, and in the `Type` dropdown choose `Delta time` (or `Delta time displayed`).
