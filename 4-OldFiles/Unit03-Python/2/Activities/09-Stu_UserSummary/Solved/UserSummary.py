# Pull in the CSV file and store it to users_csv
users_csv = open("../Resources/UserList.csv", "r")

# Reference the file to place the summaries into
user_summary = open("PeopleToKeepEyesOn.txt", "w")

# Read the users_csv to convert it into text to store in users_text
users_text = users_csv.read()

# Split the users_text into a list of rows based on the newline
user_rows = users_text.split("\n")

# Variable to write the user information into
text_to_write = ""

# Loop through the user_rows in order to find which ones contain "229.62.232.190"
for row in user_rows:

    # If the index of "229.62.232.190" is found then print "COMPANY SERVER FOUND"
    if(row.find("229.62.232.190") > -1):
        print("COMPANY PRIVATE SERVER FOUND")

        # Split the current row on commas
        user_info = row.split(",")

        text_to_write += "USER: " + user_info[0] + "\n"
        text_to_write += "PASSWORD: " + user_info[1] + "\n"
        text_to_write += "HOURS ONLINE: " + user_info[2] + "\n"

        # Split the common IPs on semicolons
        common_IPs = user_info[3].split(";")

        # Loop through the common_IPs and print them to the screen
        for IP in common_IPs:
            text_to_write += IP + "\n"

        text_to_write += "--------------\n"

user_summary.write(text_to_write)
