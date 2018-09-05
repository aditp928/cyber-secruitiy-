passwords = ["sawyer", "Password123", "Tr0ub4dor&3",
             "AGreatPasscode", "PassPassPass",
             "correcthorsebatterystaple"]

# write a for loop to check each password
for password in passwords:

    if "Pass" in password:
        print("Password '" + password + "' is probably insecure")
    else:
        print("Password '" + password + "' is probably secure")
