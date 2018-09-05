## 7.2 Lesson Plan - Reading and Writing Files

### Overview

### Instructor Notes

----

### 1. Students Do: Python Warm-Up (0:10)

### 2. Everyone Do: Python Warm-Up Review (0:05)

### 3. Instructor Do: Introduction to Dictionaries (0:10)

* The basics of creating and working with dictionaries...
  * `"key" : "value"` pairings
  * Python dictionaries are automatically sorted alphabetically by their key names
  * Collecting specific values using `dictName["keyName"]`
  * Modifying specific values or adding new values using `dictName["keyName"] = newValue`
  * Removing key/value pairs using the `del(dictName["keyName"])` function
  * `dictName.keys()` to collect a list of keys in a dictionary
  * `dictName.values()` to collect a list of the values in a dictionary
* Looping through a list of dictionaries with the same key/value pairs

### 4. Students Do: The DNS Dictionary (0:15)

* Students are given a list of public DNS server IPs and their provider
  * They must loop through the lists and create a dictionary for each website before pushing these dictionaries into another list.
* Bonus: Some providers have secondary DNS servers. This means that there will be some dictionaries with three values whilst others have only two.
  * Students will have to read in a list of dictionaries containing the provider name and the secondary DNS server, compare it to the list of dictionaries they just created, and then push the secondary DNS servers into a new key on their side.

### 5. Everyone Do: The DNS Dictionary Review (0:05)

### 6. Instructor Do: Introduction to Functions and While Loops (0:10)

* The basics of creating and using functions...
  * `def functionName():` to create a function
  * Adding in parameters
  * `return` to escape a function and pass data back from it
* `while` loops that run until a condition is met
  * Used to run code where user input controls whether the code ends

### 7. Students Do: Admin Login (0:15)

* Students are given a list of admin accounts
  * They must create a function which checks user input and then logs them in if the account info matches
  * This code should run so long as the user's information does not match. This means the user can attempt to log in as many times in a row as possible

### 8. Everyone Do: Admin Login Review (0:05)

### BREAK (0:15)

### 9. Instructor Do: Reading Files (0:15)

* The basics of `open(fileName, "r")` to read in files
  * Reading text files
  * Reading CSV files
* Using `split()` to break strings apart
* Using `find()` if some text appears in a string 

### 10. Students Do: The User List (0:20)

* Students are given a CSV file with usernames, passwords, and a list of IP addresses that they are regularly connecting to.
  * They must read in the CSV, break it apart into parts, and then create a Python dictionary version of the CSV which can then be searched through for specific user information.

### 11. Everyone Do: The User List Review (0:05)

### 12. Instructor Do: Writing Files (0:10)

* Using `variableName = open(fileName, "w")` to write to files
  * If the file does not exist, it will be created by Python
  * The "w" parameter will always overwrite the current file
  * `variableName.write()` to push text into the file
* Using `variableName = open(fileName, "a")` to append text to a file
  * No longer does `variableName.write()` overwrite the previous file, it now appends text onto the end of the file instead

### 13. Students Do: User Summary (0:15)

* Building off of the previous activity, students will now create a new file which will contain a summary report on each of the users contained within the user list

### 14. Everyone Do: User Summary Review (0:05)