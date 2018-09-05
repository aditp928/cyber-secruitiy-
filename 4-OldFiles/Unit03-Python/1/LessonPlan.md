## 3.1 Lesson Plan - Intro To Python

### Overview

Today's class introduces students to the very basics of programming in Python while also explaining why this language is used within the Cyber Security industry.

### Instructor Notes

----

### 1. Instructor Do: What is Python? (0:10)

* What Python is and why it is used in CyberSecurity
  * "Python is one of the easiest programs to learn. Has a great balance between ease and usefulness."
  * "Allows for rapid development."
  * "Lots of pre-written modules that can be easily imported."
* Python 2.7 vs Python 3
  * Looking into the past vs Preparing for the future

### 2. Students Do: Check Python Installation (0:05)

* Python3 should already be installed 

### 3. Everyone Do: Installing VSCode and Running Python Scripts (0:12)

* Instructor leads the class through installing VSCode to their Kali VM
* Instructor goes over how to run Python Scripts from the terminal
  * `print()` to push text to the terminal

### 4. Instructor Do: Basic Variables (0:15)

* Introduction to core data types...
  * Integers
    * Addition, Subtraction, Multiplication, and Division
  * Floats
  * Strings
    * Concatenation
    * Type conversions
  * Boolean
* `type()` to check what data type a variable is

### 5. Students Do: Variable Addresses (0:10)

* Students are given basic information on a website (IP Address, port, endpoint, and URL) and must print all of this information out to the screen.

### 6. Everyone Do: Variable Addresses Review (0:05)

* Reviewing the solution for the previous activity

### 7. Instructor Do: Lists (0:10)

* Introduction to lists in Python...
  * Creating lists
  * Selecting values from a list using indexes
  * Finding an index based upon its value using `index()`
  * Adding values to a list using `append()`
  * Removing values from a list using `remove()`
  * Getting the length of a list using `len()`

### 8. Students Do: Messy Lists (0:15)

* Students are given a list of around 25 IP addresses. They are then asked to discover the length of the list and the index of some values before adding/removing some values.

### 9. Everyone Do: Messy Lists Review (0:05)

* Reviewing the solution for the previous activity

### 10. BREAK (0:15)

### 11. Instructor Do: For Loops (0:15)

* Introduction to the `for` loop...
  * Looping through the values in a list - `for x in list`
  * Looping through a range of numbers - `for x in range(10)`
* Using indexes to loop through a range in a list or through two lists of equal length
* Nested `for` loops to loop through lists of differing lengths

### 12. Students Do: Looping Through IPs and Ports (0:15)

* Students will first create a loop that will loop through all of the broadcast addresses for an IP.
* They will then loop through a list of ports to append them onto the end of an IP.

### 13. Everyone Do: Looping Through IPs and Ports Review (0:05)

* Reviewing the solution for the previous activity

### 14. Instructor Do: Conditionals (0:10)

* Introduction to `if` statements...
  * Checking to see if one value is equal to another
  * Checking to see if a value is greater or less than another
  * `and`/`or` to chain logic tests
* Introduction to `else` and `elif`

### 15. Students Do: Conditional Conundrum (0:10)

### 16. Everyone Do: Conditional Conundrum Review (0:05)

### 17. Instructor Do: User Input (0:05)

* Introduction to using `input()` to collect user input and store it inside a variable

### 18. Students Do: Python Login (0:20)

* Students are provided with a list of usernames and their associated passwords.
* They must create a `logged_username` and `logged_password` variable which they will then check against each of the usernames and passwords in the lists. If there is a matching username and password with the same index, then a "YOU LOGGED IN" message is printed. Otherwise a "INVALID ENTRY" message is printed.

### 19. Everyone Do: Python Login Review (0:10)

* Reviewing the solution for the previous activity
