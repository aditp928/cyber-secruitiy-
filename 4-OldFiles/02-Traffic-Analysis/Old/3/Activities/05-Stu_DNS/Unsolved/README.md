## Analyzing DNS in Wireshark

### Part 1

- Open the `dns-1.pcap` file.
- This file only contains DNS replies. How many DNS requests were there?
- When the user asked for `assets.espn.go.com`, what happened?
- What is/are the IP address(es) for `a1.espncdn.com`?

### Part 2

- Open the `dns-2.pcap` file.
- This capture contains an attempted query, but something went wrong.
  - What happened?
  - Which flag in the packet reveals what went wrong?
- The request went to 8.8.8.8. Did the response come directly from 8.8.8.8?
