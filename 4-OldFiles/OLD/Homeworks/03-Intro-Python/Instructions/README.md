# Intro to Python HW - Cracking Into Evil

One of the super-hackers working for the League of Really Good Guys (LORGG) recently managed to break his way into the computer of Sir Evil, self-proclaimed nemesis of LORGG HQ.

In the grand scheme of things, however, Sir Evil is a relatively minor blip on the League's radar and so the process of cracking into his evil plans has been left to the newbie on the team... YOU!

In order to prove yourself to the senior superhackers, you decide you are going to manually create a Python script which will go through Sir Evil's password-protected zip files and crack them wide open. That should prove to them your time is better spent working on far more critical security threats!

## Instructions

* You have been provided with three different zip files, each one having a unique password. Using a couple text files containing 5000 of the most popular passwords and the `zipfile` module, create some code that will loop through the folders and extract the evil plans contained within.

    * You will definitely want to read through some of the documentation on the [zipfile](https://docs.python.org/3/library/zipfile.html) module in order to create this application. Start of by looking into `zipfile.ZipFile()` and `zipfile.extractall()`.

    * When trying passwords in your code, make sure you are encoding your strings properly. The specific encoding you will want is `passwordString.encode('cp850','replace')`

    * [Exception Handling](http://www.pythonforbeginners.com/error-handling/exception-handling-in-python) is a must for this activity. If a password fails and that code is not placed within a `try:` statement, then the entire application will break on the first attempt at cracking the zip.