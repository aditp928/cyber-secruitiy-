# Pull in the CSV file and store it to file
file = open("../Resources/UserList.csv")

# Read the file to convert it into text to store in contents
contents = file.read()

# Split the contents into a list of rows based on the newline
rows = contents.split("\n")

# Get user action
action = input("What would you like to search by? (ip|user) ")

search_text = input("Please enter the " + action + " for which you'd like to search: ")
search_index = 0 if action == 'user' else 3

# boolean flag for if information was found
found = False

# Loop through the rows in order to find which ones contain the search term
for row in rows:
    # Split the current row on commas
    user_info = row.split(",")

    # get the value of the column searched for and if it contains the search term
    column_value = user_info[search_index]
    contains_search = column_value.find(search_text) > -1

    # If the text in the relevant column contains the search term
    if contains_search:
        print("ENTRY FOUND")

        # Print out the user's name, password, and hours online
        print("USER: " + user_info[0])
        print("PASSWORD: " + user_info[1])
        print("HOURS ONLINE: " + user_info[2])

        # Split the IP column into a list on semicolons
        ip_list = user_info[3].split(";")

        # Loop through the ip_list and print them to the screen
        print("IPs:")
        for IP in ip_list:
            print(IP)

        print("----------")

        # flag that we found a result
        found = True

# found is still false, which means we never found a row which matches the search term
if not found:
    print("Search item not found")
