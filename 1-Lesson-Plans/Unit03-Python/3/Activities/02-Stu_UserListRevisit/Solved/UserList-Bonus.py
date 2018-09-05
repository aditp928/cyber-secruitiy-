import os
import csv

# Build the path to the csv file and open it
file_path = os.path.join("..", "Resources", "UserList.csv")
file = open(file_path)

# use the csv module to read the file
reader = csv.reader(file)

# use the reader to loop through the file contents
for row in reader:

    # Split the IPs column on semicolons
    ip_list = row[3].split(";")

    # If the IP "229.62.232.190" is found in the ip_list then print "COMPANY SERVER FOUND" and user info
    if "229.62.232.190" in ip_list:
        print("COMPANY PRIVATE SERVER FOUND")

        # Print out the user's name, password, and hours online
        print("USER: " + row[0])
        print("PASSWORD: " + row[1])
        print("HOURS ONLINE: " + row[2])

        # Loop through the ip_list and print them to the screen
        print("IPs:")
        for IP in ip_list:
            print(IP)

        print("----------")
