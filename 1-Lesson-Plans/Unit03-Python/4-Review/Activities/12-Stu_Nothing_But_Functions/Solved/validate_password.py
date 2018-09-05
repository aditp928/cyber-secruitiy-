# Define a function, called `validate_password`, which accepts a `password`
def validate_password(password):
    # Inside the function, check if the password is longer than 6 characters long
    if len(password) > 6:
        # If it is, return `True`
        return True
    else:
        # Otherwise, return `False`
        return False

# Should print `True`
result = validate_password('superSaf3Passw0rd')
print(result)

# Should print `False`
result = validate_password('lol')
print(result)
