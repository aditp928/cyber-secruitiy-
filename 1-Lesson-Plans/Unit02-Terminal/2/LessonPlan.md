## 2.2 Lesson Plan: Commanding the Command Line

### Overview

In today's class, students will expand their skills working on the command line to include new techniques for file searching and bulk operations. Throughout class, students will complete a series of activities involving the `find`, `exec`, `grep`, and `wc` commands.

### Class Objectives

By the end of class, students will be able to:

* Articulate and parse the elements of a basic Unix command.
* Utilize the `find` command to locate files based on various search parameters. 
* Use the `exec` command to perform bulk operations on files. 
* Use the `grep` command to search within the contents of files.  
* Utilize the `wc` command to count words and lines. 
* Devise strategies for combining multiple commands in sequence to accomplish intermediate IT tasks.  

### Instructor Notes

* Today's class builds on the previous one by introducing students to a new fleet of Unix commands. Be forewarned, this class will be considerably more challenging for students. Seemingly simple situations involving the `find`, `exec`, and `grep` commands in concert can hide their relative complexity. For those students still rusty on the commands that were taught in the last class, today's class will feel even more challenging to them. Be encouraging and continue to remind students that familiarity with using the command line comes with practice.

* Use your judgment on when to offer *live* vs *dry* walkthroughs when reviewing the activities with the students. Live walkthroughs, or reviews in which you run each command for students, are best used for straightforward activities that can be easily followed. Dry walkthroughs, or reviews in which you open the solution file and narrate the key points to students, are best used for more complex activities involving multiple steps. Consider the clock and play to your strengths. If you are running short on time or get lost easily during live demonstrations, stick to dry walkthroughs. If you have time to spare and notice students are struggling with some of the activities, sprinkle in a few live walkthroughs.

* As always, have your TAs refer to the [Time Tracker](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/blob/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/timetracker.xlsx) to help you stay on track.

-------

### 1. Instructor Do: Intro Class (0:07)

* Begin class by welcoming students back and informing them that today they will be expanding their command-line tool belt.

* Open the [PowerPoint](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/blob/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/Commanding_The_Command_Line.pptx) and use the slides to guide the introductory lecture.

  * Begin by showing a preview of the commands taught in the last class.

  * Then, transition into today's goals, before proceeding to the warm-up activity.

* As you proceed through class today, use the slides as an accompaniment.

### 2. Students Do: Warm-Up Activity (0:10)

* Let's start with a quick warm-up.

* Send students the following file and instructions: 

  * **File:**
    * [activities/01-Stu_Warmup/Unsolved/LogFiles.zip](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/blob/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/activities/01-Stu_Warmup/Unsolved/LogFiles.zip)

  * **Instructions:**
    * You've just been given a series of server logs. Your task is to use the command line to:

      1. Create a folder called **Archive**.
      2. Combine all of the logs contained in the **TodaysLog** folder into a single text file titled with today's date.
      3. Move the file you created to the **Archive** folder.
      4. Preview the file contents.

  * **Bonus:**
    * If you finish early, try to recomplete the task in just four commands.

### 3. Instructor Do: Review Warm-Up Activity (0:07)

* Once time is up, take a few minutes to review the activity.

* Fire up a terminal window and use the following commands to guide students through the solution. Be sure to call out the following as you do:

  * After creating the **Archive** folder, we navigated into the **TodaysLog** folder.

  * From within the **TodaysLog** folder we used the `cat`  command to combine each of the files and used `>` to redirect the output to a text file.

  * Next, we used the `mv {file} {Path}` command to move the resulting file to the new location. In this case, we used `../Archive` to specify that we wanted to move the file up one level from its current location.

  * Finally, we used `less` to preview the contents.

    ![assets/01-Warmup_01.png](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/raw/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/01-Warmup_01.png)

* For the bonus, we reduced the number of commands by combining multiple tasks into single commands.

  * For instance, we avoided having to `cd` into the **TodaysLog** folder, instead we explicitly passed the argument `TodaysLog/*` to specify that we wanted to combine all of the files within the folder.

  * We further avoided navigational commands, by directly specifying `Archive/09_15_18.txt` as the output location.

    * [![assets/01-Warmup_02.png](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/raw/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/01-Warmup_02.png)](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/blob/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/01-Warmup_02.png)

* Answer any questions that remain before sending students the solution and proceeding to the next section.

### 4. Instructor Do: Command-Line Structure (0:07)

* Return to the PowerPoint and use the slides to formally introduce students to the components of a Unix command.

* When prompted use the drills that follow to engage students for comprehension.

  * [![assets/00-Slides_01.png](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/raw/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/00-Slides_01.png)](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/blob/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/00-Slides_01.png)

### 5. Instructor Do: find Command (0:07)

* Next, you will introduce students to the basic use of the `find` command.

* Locate the **02-Ins_FindCommand/Docs** folder that was provided for you. This folder is a series of deeply nested folders and files. Using the **02-Ins_FindCommand/Docs** folder as a starting place, show the students how the `find` command can be used to quickly search for relevant files.

* As you run the commands, break down the elements of each command as follows:

  * `find` is the command itself.

  * `.` references the path to search. In this case, `.` conveys that we would like to search all files in the current directory.

  * `-type f` or `-type d` signifies that we are searching for files or directories respectively.

  * `-name {parameter}` signifies that we are searching for files with the name included.

* Don't let the conversation meander too much from these examples described above. You will be introducing students to more sophisticated search queries in another demo later.

* Answer any questions that remain before sending the solution and proceeding to the next activity.

  * [![assets/02-Find_01.png](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/raw/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/02-Find_01.png)](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/blob/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/02-Find_01.png)

  * [![assets/02-Find_02.png](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/raw/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/02-Find_02.png)](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/blob/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/02-Find_02.png)

  * [![assets/02-Find_03.png](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/raw/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/02-Find_03.png)](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/blob/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/02-Find_03.png)

### 6. Students Do: PathFinder Activity (0:12)

* Time for a student activity!

* Send students the following file and instructions:

  * **File:**
    * [activities/03-Stu_PathFinder/Unsolved/Mazes.zip](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/blob/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/activities/03-Stu_PathFinder/Unsolved/Mazes.zip)

  * **Instructions:**
    * Time to revisit an old challenge! In this challenge, you will revisit the Terminal Mazes activity from last class. This time you will be able to use your knowledge of the `find` command to speed things up.

    * Use the `find` command to identify the location of the **start.txt** and **Bonus.txt** files and the **End** directory folder that is contained within the **Mazes** directory.

    * Use the provided path results to help you copy each of the **start.txt** and **Bonus.txt** files into their respective **End** folder.

  * **Hint:**
    * You should be able to complete this task in 9–10 commands (including the **Bonus.txt** files).

### 7. Instructor Do: Review PathFinder Activity (0:07)

* Once time is complete, spend a few moments reviewing the solution. Use the following points as your guide:

  * Run `find . -type f -name start.txt` and `find . -type d -name End` to find the location of each **start.txt** file and **End** folder.

  * Explain to students that the yield from these `find` commands are the full paths of each file and folder.

  * Copy these paths into a `copy` command in the format `cp {starting path} {ending path}` in full. You may want to remind students that when referencing files you can always use the full path name to do so as in this case.

  * Repeat the above for the **Bonus.txt** files.

* Answer any questions that remain before sharing your solution and proceeding to the next example.

  * [![assets/03-PathFinder_01.png](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/raw/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/03-PathFinder_01.png)](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/blob/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/03-PathFinder_01.png)

  * [![assets/03-PathFinder_02.png](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/raw/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/03-PathFinder_02.png)](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/blob/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/03-PathFinder_02.png)

### 8. Instructor Do: find Command Options (0:10)

* Next you will drill further into `find` command options to introduce students to more advanced search queries.

* Use the **Docs** folder from your previous example to proceed through each of the following commands. As you do, be sure to point out that we can:

  * Specify the use of `find` in specific folders by using the `find {path}` construct.

  * Create case-insensitive file or folder searches using the `-iname` option.

  * Combine search parameters using the `-o` (or) and `-a` (and) options.

  * Search for all files of a certain type using the `*` (wildcard).

  * Specify creation date before, after, or between times using the `-ctime` option. In these cases, `+t` signifies after t-minutes, `-t` signifies before t-minutes.

  * Specify file sizes using the `-size` option.

* Answer any questions that remain before providing your solution file to students.

  * [![assets/04-FindOptions_01.png](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/raw/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/04-FindOptions_01.png)](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/blob/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/04-FindOptions_01.png)

### 9. Students Do: Gibberish Finder Activity (0:15)

* Time for some practice. In this activity, students are given a set of deeply nested folders (filled with gibberish). Their task is to use their new knowledge of `find` options to retrieve files based on specific search parameters.

* Send students the following file and instructions:

  * **File:**

    * [activities/05-Stu_GibberishFinder/Unsolved/Gibberish_Folder.zip](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/blob/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/activities/05-Stu_GibberishFinder/Unsolved/Gibberish_Folder.zip)

  * **Instructions:**

    * Use your knowledge of the `find` command to create search queries for each of the following tasks:

      **Part I: Simple Search**

      * Find a listing of all files
      * Find a listing of all folders

      **Part II: Title Search**

      * Find all files containing the letter z
      * Find all files that contain the word "rice"

      **Part III: File Type Search**

      * Find all Excel files
      * Find all Word files

      **Part IV: Combo Search**

      * Find all text files containing the number 2
      * Find all Word files at least 200 KB in size

      **Part V: Challenge Search (You may need to do some googling for these!)**

      * Find all Excel files, at most 15 KB in size, and a max of 3 levels of depth from the surface
      * Find all files that are not writable in **Gibberish_Folder/folder3**

      **Part VI: Partner Search**

      * If you finish early, create a file and modify the contents of a different file deep in the Gibberish folder. Then see if your partner can find them using the `find` command.

### 10. Instructor Do: Review Gibberish Finder Activity (0:07)

* Spend a few moments reviewing the solution to this activity.

* Consider using a dry walkthrough to narrate the key points in the solution. You can also use a live walkthrough where you call on students to share their solution. As you explain your solution, you should specifically call out the following:

  * We used the `-a` option when passing two `-iname` parameters in a single command. This is in contrast to the situation where we need to combine the `-iname` and `-size` options.

  * We used the `-maxdepth 3` and `! -writable` commands in the Challenge Search (Part V). These are the commands, the students would have needed to search for. You may want to use these challenges to introduce students to googling for unfamiliar commands. **Note:** We will be spending more time learning to troubleshoot unfamiliar situations in the next class.

  * We used the `-mmin` (modify date) command versus the `-cmin` (change date) command.

  * Answer any questions that remain before sharing your solution and proceeding to the next activity.
    * [![assets/05-Gibberish_01.png](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/raw/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/05-Gibberish_01.png)](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/blob/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/05-Gibberish_01.png)

------

### 11. Break (0:15)

------

### 12. Instructor Do: exec Command (0:10)

* In the next demonstration, you will be walking students through the basic use of the `exec` command. This is an important concept and students will need to understand it to be able to complete their homework assignment, so take your time to ensure student comprehension.

* Use the following guide and the **Docs** folder you've been using to this point to conduct your demo.

* Point out the following as you do:

  * For the first demo, we begin by running a search for all files containing the word **flag**.

  * From here, we create a **My_Flags** folder, which will ultimately serve as the dumping ground for these files.

  * Next, we use our `exec` command to locate each of these files and immediately copy them to the **My_Flags** folder.

  * As you run this command, be sure to break down the following elements:

    * `find {condition}` precedes the `exec` command. In this case, the results of the `find` command are fed into the `exec` command.

    * `-exec` is our actual command. It signifies that we'd like to run a subcommand.

    * `cp {} {destination}` signifies that we'd like to pass the previous file list into our `cp` command. The files are then copied to our destination folder.

    * `\;` signifies that our subcommand is complete. This is an easy element to forget to include, but without it  `-exec`  will not execute. This would be akin to forgetting key punctuation.

      * [![assets/06-Exec_01.png](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/raw/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/06-Exec_01.png)](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/blob/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/06-Exec_01.png)

  * For the second demo, create a folder called **NoPNGsAllowed**.

  * Run the `find` and `-exec` commands to find and copy all files that are *not* PNGs into the **NoPNGsAllowed** folder.

  * Be sure to break down the elements as follows:

    * `find . -type f ! -iname *.png` signifies that we are searching for all files that are not PNGs. The `!` in this case signifies *not*.

    * `-exec cp {} NoPNGsAllowed \;` signifies that we are copying each of the retrieved files to the **NoPNGsAllowed** folder.

      * [![assets/06-Exec_02.png](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/raw/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/06-Exec_02.png)](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/blob/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/06-Exec_02.png)

  * Answer any questions that remain before sharing your solution and proceeding to the next activity.

### 13. Students Do: Executive Cleaning Activity (0:10)

* In this activity, students will use `find` and `exec` to sort the **Gibberish_Folder** folder they worked with previously.

* Send students the following file and instructions:

  * **File:**
    * [activities/07-Stu_ExecutiveCleaning/Unsolved/Gibberish_Folder.zip](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/blob/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/activities/07-Stu_ExecutiveCleaning/Unsolved/Gibberish_Folder.zip)

  * **Instructions:**
    * You've been tasked with sorting the **Gibberish_Folder** folder. Specifically, you've been asked to do the following:

      * Create a folder called **Sorted_Gibberish**.

      * Create subfolders within this folder called **Docs**, **Data**, and **Text**.

      * Copy all Word documents into the **Docs** folder, Excel files into the **Data** folder, and text files into the **Text** folder.

  * **Bonus:**
    * Create a subfolder called **LargeFiles** in the **Sorted_Gibberish** folder.

    * Move all files that are larger than 200 KB into the **LargeFiles** folder.

### 14. Instructor Do: Review Executive Cleaning Activity (0:07)

* Once time is up, spend a few moments reviewing the solution. As you do, stress the following elements of the `find` and `-exec` command:

  * `find -type f -iname *{file type}*` signals that we are searching for one file type.

  * `-exec cp {} {destination}` signifies that we'd like to move these files to our new destination.

  * `\;` signifies that we are concluding our statement.

* Answer any questions that remain before sharing your solution and proceeding to the next activity.

  * [![assets/07-Cleaners_01.png](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/raw/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/07-Cleaners_01.png)](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/blob/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/07-Cleaners_01.png)

### 15. Instructor Do: grep Command (0:07)

* Next up, the `grep` command. In this demo, you will show students how the `grep` command can be used to search within the contents of text files. Use the **08-Ins_GrepCommand** folder that has been provided for you. This folder includes folders filled with text files.

* Use the following commands to guide your demo. As you do, explain the following:

  * The `grep` command is used to search within the body of file text.

  * The basic construction is: `grep` (command) `{text}` `{location}`.

  * Use the `-i` option to signify a case-insensitive search.

  * Use the `-iv` option to signify a search for all files *not* including the specified term.

  * Use `grep -rl {text} {location}` to search for a list of files that include the specified text.

  * Be sure to point out that `grep {text}` outputs the *lines of text* for which the text appears, whereas `grep -rl {text} {location}` outputs the *file list* for which the text appears.

    * [![assets/08-GrepCommand_01.png](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/raw/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/08-GrepCommand_01.png)](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/blob/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/08-GrepCommand_01.png)

    * [![assets/08-GrepCommand_02.png](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/raw/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/08-GrepCommand_02.png)](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/blob/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/08-GrepCommand_02.png)

  * Answer any questions that remain before sharing your solution and proceeding to the next example.

### 16. Students Do: grep Detective Activity (0:10)

* In this activity, students are given a series of chat logs. They will use the `grep` command to identify the power users as well as when these users logged on and off.

* Send students the following file and instructions:

  * **File:**

    * [activities/09-Stu_GrepDetective/Unsolved/IRC_Logs.zip](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/blob/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/activities/09-Stu_GrepDetective/Unsolved/IRC_Logs.zip)

  * **Instructions:**
    * You've just been given a series of chat logs from April 2014. Your task is to use the `grep` command to identify the following:

      * The days for which the users power2all, glanzmann, gansbrest, and E1ven were active in the channel.

      * The times for which these users logged on and off.

  * **Hint:**

    * When determining logon time, look for a string pattern that captures what you are specifically looking for.

  * **Bonus:**
    * If you finish early, try this challenge.

      * Create a folder for each of the users of interest.

      * Then, see if you can create a combination of `find`, `exec`, and `grep` that allows you to retrieve all logs for which these users were active and immediately copy these files into the respective folder. That is, any file in which the user glanzmann is active should be placed in the **glanzmann** folder.

      * This challenge will require you to do some independent research and will inevitably involve trial and error.

### 17. Instructor Do: Review grep Detective Activity (0:07)

* Once time is up, spend a few moments reviewing the solution. As you do, use the following commands and talking points:

  * To identify the activity dates of each user, we use the `grep -rli` command. This helps us to achieve our aim, because each of the file names list the date of the activity.

  * To identify the logon and logoff times, we use the `grep -i "user has"` command. In this case, limiting our search results to instances where the user's name appears in conjunction with the word "has" limits the view to only records with log on and log off activity. 

  * For the bonus, most likely students would have had to use a Google search to find the command sequence.

    * If successful, their search should have led them to the `find . -type f -exec grep -rli "power2all" {} \; -exec cp {} power2all \;` command. In this case, we used two `exec` commands.

    * The first `exec` command captures input from `find` and passes them to `grep` for a more narrow search.

    * The second `exec` command then uses the file list retrieved from `grep` to trigger the copy and paste.

      * [![assets/09-GrepDetective_01.png](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/raw/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/09-GrepDetective_01.png)](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/blob/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/09-GrepDetective_01.png)

      * [![assets/09-GrepDetective_02.png](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/raw/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/09-GrepDetective_02.png)](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/blob/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/09-GrepDetective_02.png)

  * Answer any questions that remain before sharing your solution and proceeding to the next example.

### 18. Instructor Do: wc Command (0:05)

* You've made it to the final demo of the day! In this activity, you'll be showing students how to use the `| wc -l` command to count the number of records retrieved via `find` and `grep`. This is another important concept for students to learn to be able to complete their homework assignment.

* Use the **IRC_Logs** folder from the previous example and the following image and commands to dictate your demo. As you do, be sure to explain the following:

  * `|` conveys that we are "piping" (transmitting) the results from our `find` and `grep` commands to the next command.

  * `wc -l` conveys that we are looking to count the number of lines retrieved.

  * Thus, when we use `| wc -l` in conjunction with `find` and `grep` we are retrieving the record count.

* Answer any questions that remain before sharing your solution and proceeding to the next example.

  * [![assets/10-WCL_01.png](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/raw/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/10-WCL_01.png)](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/blob/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/10-WCL_01.png)

### 19. Students Do: Log Counter Activity (0:10)

* Here's the final activity of the day! In this activity, students will expand on their investigative work from the previous IRC example to count the relative activity levels of various users.

* Send students the following file and instructions:

  * **File:**

    * [activities/11-Stu_LogCounter/Unsolved/IRC_Logs.zip](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/blob/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/activities/09-Stu_GrepDetective/Unsolved/IRC_Logs.zip)

  * **Instructions:**

    * Use your knowledge of the `wc -l` command to answer the following questions:

      **Part I: Basic Counts**

      * How many log files are included in the **IRC_Logs** folder?
      * How many log files exceed 100 KB in size?

      **Part II: Login Counter**

      * How many times did the user **glanzmann** log on?
      * How many times did the user **E1ven** log on?

      **Part III: Chat Counter**

      * How many times did the user **glanzmann** speak?
      * How many times did the user **E1ven** speak?

### 20. Instructor Do: Review Log Counter Activity (0:05)

* Have students share their answers and the commands they used. Feel free to use a dry walkthrough to review the solution with students.

  * [![assets/11-LogCounter.png](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/raw/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/11-LogCounter.png)](https://github.com/coding-boot-camp/Cybersecurity-Lesson-Plans/blob/Prod-Branch/1-Lesson-Plans/Unit02-Terminal/2/assets/11-LogCounter.png)

### 21. Instructor Do: Review and Close Class (0:05)

* Finally, return to the PowerPoint and complete the review activities before dismissing class.

* Great work today!

-------

### Copyright

Trilogy Education Services © 2018. All Rights Reserved.
