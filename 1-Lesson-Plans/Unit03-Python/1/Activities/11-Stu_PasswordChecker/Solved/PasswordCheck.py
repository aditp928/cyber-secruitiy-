# Master Username and Password
master_user = "admin"
master_pass = "password"

# Capture user's username
username = input("What is your username? ")

# Capture user's password
password = input("What is your password? ")

# Check if Username and Password match Master. Inform user of outcome.
if (username == master_user and password == master_pass):
  print("You have been granted access!")

else:
  print("You have been denied access!")

  