passwords = ["sawyer", "password123", "Tr0ub4dor&3",
             "AGreatPasscode", "PassPassPass",
             "correcthorsebatterystaple"]

# write a for loop to check each password
for password in passwords:
    output = "Password '" + password + "' is probably "

    # boolean: evaluated condition for insecure password
    is_weak = "pass" in password or "Pass" in password or len(password) < 8

    if is_weak:
        output += "insecure"
    else:
        output += "secure"

    print(output)
