# Libraries
import hashlib
import csv

# Receive Email and Password
print("")
print("")
print("Welcome to HackSafe Bank. The Safest Bank on the Planet")
print("-------------------------------------------------------")
print("")
print("To login please provide the requested information.")
email = input("What is your email address? ")
password = input("What is your password? ")

# Hash the Password Provided
hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()

# Open the CSV File
with open("UserInfo_Hashed.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0

    # Setup a bool to catch if no match is found
    no_match = True

    # Loop through each row
    for row in csv_reader:

        if row[1] == email and row[2] == hashed_password:
            print("")
            print("Welcome Back " + row[0] + "!")
            print("Your adress on file is: " + row[4] + " " + row[5] + " " + row[6] + " " + row[7])
            print("Your balance is: " + row[10])
            no_match = False

        # Add one to the line count on each iteration
        line_count = line_count + 1

    if no_match == True:
        print("Sorry. Invalid login. Try again?")
        print("")
