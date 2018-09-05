# Password Check Loop
In this activity, you'll work write a loop to parse a list of passwords to flag insecure passwords.

## Instructions

1. Open up the `Unsolved/PassCheck.py` file.

2. Add a for loop to loop through the list of passwords.

3. Check if each password is secure. If the password contains `Pass`, you should mark it insecure.

4. For each password, print out a string if it is secure/insecure:

   - e.g. `Password 'Password123' is probably insecure`

   - e.g. `Password 'correcthorsebatterystaple' is probably secure`

## Hint

- Use the `in` operator to check to see if a substring is in a string.

## Bonus

- Add a check: the password is insecure if it contains the lowercase `pass` as well.

- Add a check: the password is insecure if it is fewer than 8 characters.

- Assign the condition check to a separate variable for readability, and use that variable in the if statement.

- Write your code such that there is only one `print` statement. Try checking out the `+=` operator.
