## 3.3 Lesson Plan - Reading and Writing Files

### Overview

### Instructor Notes

-----

### 01. Students Do: Python Warm-Up (0:10)

### 02. Everyone Do: Python Warm-Up Review (0:05)

### 03. Instructor Do: Introduction to Libraries and OS (0:15)
* Explain what libraries are within Python and how they are powerful tools in the belt of programmers
  * Python comes prepackaged with a ton of libraries already which can be pulled in and used without much hassle
* The OS library is used to navigate through the file system of a computer no matter what kind of operating system is being used.
  * This means that even the code written on a Windows machine will be able to navigate the file system of Macintosh and Unix systems as well
  * It is important to note that OS can still only look into files that exist. If a file or folder does not exist on the system in question, then Python will naturally not be able to push its way into it
* `os.path.join()` to create file paths
* `os.walk()` in order to navigate through multiple folders and files at the same time

### 04. Students Do: "GET WREKT SKRUB!!" (0:15)
* Students are given a folder of diary entries split up into multiple weeks. The goal of this activity is to to go through all of the folders/files and then replace the text within them with "GET WREKT SKRUB!"

### 05. Everyone Do: "GET WREKT SKRUB!!" Review (0:05)

### 06. Instructor Do: File Stats (0:15)
* `os.stat()` to collect information on a file
  * `st_size`: Size of the file
    * If a file's size seems out of place, that should be a red flag for something fishy going on
  * `st_atime`: Time of most recent access in unix epoch
  * `st_mtime`: Time of most recent modification in unix epoch
    * If a file's modification time is markedly different than all others in the same system, then that should be a red flag as well.
* `os.remove()` to delete files (DANGEROUS)
* `os.rmdir()` to delete folders (VERY DANGEROUS)

### 07. Students Do: Searching The Red Flag Sea (0:30)
* Students are given two folders containing a wide array of files within them. All of the files should be the same size and have been modified around the same time... but there are some that stand out. These rogue files should be cataloged and then removed.

### 08. Everyone Do: Searching The Red Flag Sea Review (0:10)

### BREAK (0:45)

### 09. Students Do: Cleaning The Red Flag Sea (0:30)

### 10. Everyone Do: Cleaning The Red Flag Sea Review (0:10)
* Students will now modify their previous application to keep track of the average file size and then, if a file exceeds the average file size, remove it from the system.

