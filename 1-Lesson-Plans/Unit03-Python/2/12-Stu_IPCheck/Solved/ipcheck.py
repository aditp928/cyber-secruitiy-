# Capture user input on IP Address in question.
user_ip = input("What IP address would you like to check? ")

# Denied IP Addresses stored in a list variable.
denied = ["84.16.39.181", "177.5.219.112", "180.252.163.11", "31.47.26.40",
          "209.58.157.135", "112.236.38.133", "202.169.236.131",
          "185.181.55.65", "163.172.65.198", "217.20.114.218", "209.58.157.135",
          "112.236.38.133", "202.169.236.131", "209.58.157.135"]

# Conditional statement used to check if the IP in question falls in the denied list.
# If the IP Address falls in the list, the user is informed.
if user_ip in denied:
    index = denied.index(user_ip)

    print("IP Address " + user_ip + " found in the list at index " + str(index))

# If the IP Address does not fall in the list, the user is informed. 
else:
    print("IP Address " + user_ip + " not found")



