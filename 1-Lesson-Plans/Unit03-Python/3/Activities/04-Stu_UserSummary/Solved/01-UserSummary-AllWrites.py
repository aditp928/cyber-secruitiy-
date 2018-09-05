import os
import csv

# Build the path to the csv file and open it
file_path = os.path.join("..", "Resources", "UserList.csv")
file = open(file_path)

# use the csv module to read the file
reader = csv.reader(file)

# Reference the file to place the summaries into
user_summary = open("PeopleToKeepEyesOn.txt", "w")

# use the reader to loop through the file contents
for row in reader:

    # Split the IPs column on semicolons
    ip_list = row[3].split(";")

    # If the IP "229.62.232.190" is found in the ip_list then write "COMPANY SERVER FOUND" and user info
    if "229.62.232.190" in ip_list:
        user_summary.write("COMPANY PRIVATE SERVER FOUND\n")

        # write out the user's name, password, and hours online
        user_summary.write(f'USER: {row[0]}\n')
        user_summary.write(f'PASSWORD: {row[1]}\n')
        user_summary.write(f'HOURS ONLINE: {row[2]}\n')

        # Loop through the ip_list and write them to the screen
        user_summary.write("IPs:")
        for IP in ip_list:
            user_summary.write(IP + "\n")

        user_summary.write("----------\n")
