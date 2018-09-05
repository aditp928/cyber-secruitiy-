## Unit 2 Homework Assignment: Keys to My Command Line

In this homework assignment, you will be using the concepts you've learned in class to complete **3 out of 4** Command-Line Challenges. You may choose any two of the first three challenges, but you must complete Challenge 4. 

Each of these challenges encompass a real-world situation where your new scripting skills will come in handy. 

Good luck! 

### Before You Begin

1. From within your Google Drive, create a folder called **02-Terminal_Challenge**. 

2. Right-click the **02-Terminal_Challenge** folder and select **Get Shareable Link**. You will use this folder to submit your homework when complete and the folder needs to be shareable so we can access it.

3. Inside your **02-Terminal_Challenge** folder, include two subfolders, one for each of the assignments.

## Challenge 1: Picture Tracker

![Images/03-Images.jpg](Images/03-Images.jpg)

In this challenge, you've been given a zipped file (Pictures.zip) filled with folders of images. Your job is to create a shell script to complete the following:

* Create three folders called: **JPG**, **PNG**, **TIFF**.

* Locate all **.jpg**, **.png**, and **.tiff** files inside the folder and copy each into their respective folder. 

* Create a new file called **PictureCounts.md**.

* Count how many times each file type occurs and log the results to the **PictureCounts.md** file. 

Your final submission should come in the form of: 

* A shell script (**.sh** file) with each of the commands with a comment above. Add a comment above each command describing the action.  

* An annotated PDF document with screenshots of each of the commands being run in the command line and the results shown in the file explorer when relevant. 

## Challenge 2: VIP Customers

![Images/01-VIP.jpg](Images/01-VIP.jpg)

In this challenge, you are given a zip file (OrderRecords.zip) filled with Order and Inventory Records from 2012–2017. Your task is to create and run a shell script to complete the following:

1. Create a folder called **AllRecords**. 

2. Copy all of the order records from 2012–2017 into the **AllRecords** folder. 

3. Inside of the **AllRecords** folder, create a folder called **VIPCustomerOrders**.

4. Find all orders from the VIP Customers Michael Davis or Michael Campbell. Include line and file names in the output.

5. Move these specific files into the **VIPCustomerOrders** folder in the form of two files: **michael_campbell_orders.output** and **michael_davis_orders.output**.

6. Create a file called **VIPCustomerDetails.md** that details how many orders each of the two users made. 

Your final submission should come in the form of: 

* A shell script (**.sh** file) with each of the commands. Add a comment above each command describing the action.  

* An annotated PDF document with screenshots of each of the commands being run in the command line and the results shown in the file explorer when relevant. 

## Challenge 3: To-Do Counter

![Images/02-Todo.jpg](Images/02-Todo.jpg)

In this challenge, you've been given zip file (Todos.zip) that includes a set of folders related to three coworkers' to-do lists. Each coworker's to dos are included in their respective folder. Your job is to create a shell script to complete the following:

1. Within each of the folders, create an **all.txt** file that combines the to dos included in the individual's to-do lists.

2. Within each of the folders, create a file called **done.txt** that includes only to dos marked as done.

3. Within each of the folders, create a file called **unfinished.txt** that includes only to dos not marked as done.

4. Create a file called **ProductivityReport.md** at the base of the **Todos** folder that specifies the number of to dos each person completed and the number they have left. **Note:** Because of the complexity of this activity, you do not need to use the script to print your results to the ProductivityReport, but you must use a script to do the counting.

5. Your final **ProductivityReport.md** might look something like the following:

    ```
    Done:
    Carrie: 12
    Jennifer: 3
    John: 8
    
    To Still Do:
    Carrie: 1
    Jennifer: 9
    John: 2
    
    ```

Your final submission should come in the form of: 

* A shell script (**.sh** file) with each of the commands with a comment above. Add a comment above each command describing the action.  

* An annotated PDF document with screenshots of each of the commands being run in the command line and the results shown in the file explorer when relevant. 

## Challenge 4: The Secret Library (Required)

![Images/04-Books.jpg](Images/04-Books.jpg)

In this (extremely challenging) challenge, you've been given a Virtual Machine running Kali Linux. You'll be learning more about Kali at a later point in this course, but for now, just know that it is an operating system. In this case, in particular, you will be working with a non-GUI based instance of Kali. Your job is to complete the following tasks in sequence: 

* *Part I (Basic Setup - Easy)*:

    1. Download and run the provided virtual machine in VirtualBox: https://drive.google.com/open?id=1Utc-lk1y7FKZNdxR1-NoCUlqzOXu6iUG

    2. Log in to the VM using the user name **library-admin** and password **knowledgeIsPower!**. Then use the `ip addr` command to recover the IP address of the VM.

    3. Use a local instance of the command line to `ssh` into the VM using the retrieved IP address, user name **library-admin**, and password **knowledgeIsPower!**. 

    4. Take a few moments to explore the file system. You should see a folder titled **Files**. Inside, you will find a variety of folders associated with various books and text files.

    5. Return to the root directory and create a folder called **Solutions** on the same level as the **Files** folder. 

* *Part II (Finding Files - Easy)*:

    1. Execute a terminal command that finds files with the word **catalog** or **brace** in the file name. 

    2. Move these files into the **Solutions** folder. Your **Solutions** folder should now include two files. One with the word **catalog** in the title and the other with the word **brace**).

    3. Explore the contents of each using the `less` command.

* *Part III (Collecting Chapters - Hard)*:

    1. Create a folder called **Books** inside your **Solutions** folder. 

    2. Inside your **Books** folder, create folders called: **Frankenstein**, **MobyDick**, **PrideAndPrejudice**, **TomSawyer**, **HocusPocus**, **ATaleofTwoCities**, **AliceInWonderland**, **FairyTails**, **TheImportanceOfBeingEarnest**, **Dracula**.

    3. Navigate into each of the folders and run a search for all chapters relevant to these books.

    4. Once you've created a search string that works, use it to copy these contents into the relevant folder (that is, chapters on *Moby Dick* should go into the **MobyDick** folder). 

    5. While still inside the book's folder, count up the number of chapters associated with each book.  

    6. Use the `cat` command and *brace expansion* to combine each of the chapters into a single text file for each book (that is, combine chapters 1–47 of *Frankenstein* into a single text file called **Frankenstein.txt**). It's perfectly okay if you're search doesn't yield every single chapter. This is meant to be a rough capture. **Note:** This is a particularly challenging ask. It can be done in 1 line for each book, but it will require you to do some investigating. 

* *Part IV (Tar'ing It Up - Medium)*:

    1. Once you've created each of the full texts, use the `tar` command to compress the **Solutions** folder into `tar.gz` format.

* *Part V (Books Ahoy! - Easy)*:

    1. Exit `ssh` on your local machine.

    2. Use `scp` to transfer the created **Solutions.tar.gz** folder to your local machine.

    3. Confirm that the file has been loaded onto your local machine in the file explorer. 

Your final submission should come in the form of: 

* A shell script (**.sh** file) with each of the commands with a comment above. Add a comment above each command describing the action.  
* An annotated PDF document with screenshots of each of the commands being run in the command line and the results shown. 

## Hints and Considerations

* Be sure to look back at of the activities we have covered so far. Remember it all starts with the base commands: `find`, `grep`, `cat`, `cp`, etc.

* Each of these activities is challenging in its own way, but push yourself to find a way. While the first three exercises can be completed using only the commands taught in class, Challenge 4 will require you to do some independent investigation. Use Google to search for relevant shell commands that may help you achieve your goal. Stack Overflow is also your resourceful friend!

* You will absolutely run into errors you haven't seen before, but know that these activities are totally doable. Trudge through until you figure out a way. 

* For a reference of what your annotated PDF should look like, see this [example](resources/Sample_Report.pdf).

-----

## Copyright

Trilogy Education Services © 2018. All Rights Reserved.
