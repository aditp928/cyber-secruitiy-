import os
import csv

# Build the path to the csv file and open it
file_path = os.path.join("..", "Resources", "UserList.csv")
file = open(file_path)

# use the csv module to read the file
reader = csv.reader(file)

# use the reader to loop through the file contents
for row in reader:

    # If the IP "229.62.232.190" is found in the IP list column (3) then print "COMPANY SERVER FOUND"
    if(row[3].find("229.62.232.190") > -1):
        print("COMPANY PRIVATE SERVER FOUND")

        # Print out the user's name, password, and hours online
        print("USER: " + row[0])
        print("PASSWORD: " + row[1])
        print("HOURS ONLINE: " + row[2])

        # Split the IP column into a list on semicolons
        ip_list = row[3].split(";")

        # Loop through the ip_list and print them to the screen
        print("COMMON IPs:")
        for IP in ip_list:
            print(IP)

        print("----------")
