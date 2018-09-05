# Bonus 2: prompt for action first
action = input("What would you like to do? ")

# list of bad ip connections (https://myip.ms/browse/blacklist)
denied = ["84.16.39.181", "177.5.219.112", "180.252.163.11", "31.47.26.40",
          "209.58.157.135", "112.236.38.133", "202.169.236.131",
          "185.181.55.65", "163.172.65.198", "217.20.114.218", "209.58.157.135",
          "112.236.38.133", "202.169.236.131", "209.58.157.135"]

# do conditional check for action first - if search, do same logic as before
if (action == "search"):
    # wait to ask for IP until we know it's a valid action
    search_ip = input("What IP address would you like to check? ")

    if search_ip in denied:
        index = denied.index(search_ip)
        print("IP Address " + search_ip +
              " found in the list at index " + str(index))

        # Bonus #1 - use .count() to get # occurrences in list
        count = denied.count(search_ip)
        print("IP Address " + search_ip +
              " found in the list this many times: " + str(count))
    else:
        print("IP Address " + search_ip + " not found")

# if action is add, append
elif (action == "add"):
    # wait to ask for IP until we know it's a valid action
    add_ip = input("What IP address would you like to add? ")

    denied.append(add_ip)

    print("IP successfully added. List of denied IPs: ")
    print(denied)

# Bonus 3: wasn't caught by the add or search action, so the action was invalid
else:
    print("'" + action + "' is an invalid action. Please choose either 'add' or 'search'.")
