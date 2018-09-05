# Speed Reading

Wireshark is a powerful tool, but poring through packet records can be tedious. Creating configuration profiles for common tasks speeds things up dramatically.

## Instructions

### HTTP Form Submissions

- Open [http_post.pcapng](Captures/http_post.pcapng).

- Recall that HTTP POST requests *send* data from our device to a server. This is where user-submitted form data lives.

- Create a new profile for finding form data.

- Filter for POST requests. Does this isolate the packets you're interested in?

- Click on the packet with form data.

  - Apply it as a filter. Did this do what you wanted it to? What does the display filter say now?

- Add a column indicating whether each packet contains form data.

### SMTP Email Attachments

- Open [mail_attachments.pcapng](Captures/mail_attachments.pcapng).

- Create a new profile for this type of data.

- SMTP powers most user-facing email applications. Refer to the [Wireshark Protocol Wiki](https://wiki.wireshark.org/SMTP). How does SMTP handle attachments?

- Apply a filter to show only packets with attachments.

- Explore the packet details for one of the emails carrying an attachment.

- Add the **From**, **To**, **Subject**, the value of `imf.value.type.type` property, and the value of `imf.extension.value` as columns.

### Finding FTP Passwords

- Open [ftp_transfer.pcapng](Captures/ftp_transfer.pcapng).

- Create a new profile for finding ftp passwords.

- Refer to the [Wireshark Protocol Wiki entry for FTP](https://wiki.wireshark.org/FTP).

  - What is the display filter for FTP traffic?

  - What are the standard TCP ports for FTP?

  - Anything interesting about FTP passwords?

- Filter for FTP traffic, and click on one of the packets containing a password.

- Find the **Request command** in the packet detail, and apply it as a filter. What filter does Wireshark apply?

- Add **Request Command** and **Request Arg** as columns.
