# UserAdmin
In this activity, you're given a CSV file with usernames, passwords, and a list of IP addresses that they are regularly connecting to. Your job is to identify the users who are connecting to your company's private server.

## Instructions

No starter file this time! Use the previous files from class for guidance and inspiration.

Your job is to write a Python script that prints information about users who have connected.

Given the CSV file, your Python script should read in information from the file, parse it, and print out the relevant information for users who are connecting to your company's private server in the following format:

```sh
COMPANY PRIVATE SERVER FOUND
USER: Ryan
PASSWORD: QLeyzpdW
HOURS ONLINE: 292
COMMON IPs:
248.150.250.24
223.229.166.82
229.62.232.190
198.1.152.204
215.252.4.108
117.59.161.190
169.59.2.142
144.91.68.253
27.127.60.188
182.151.186.176
----------
COMPANY PRIVATE SERVER FOUND
USER: Clark
PASSWORD: uUd2p3VH
HOURS ONLINE: 282
COMMON IPs:
248.150.250.24
223.229.166.82
229.62.232.190
198.1.152.204
215.252.4.108
117.59.161.190
169.59.2.142
144.91.68.253
27.127.60.188
182.151.186.176
----------
```

### Bonus

- Allow for searching by user or ip based on user input. For example, if I search for the name 'Taco', I should get Taco's information (but not Lisa's).
