### 16.  Find and Grep 

  * **File**

    * `10-Stu_Find-And-Grep/Unsolved/Docs.zip`
  
  * **Instructions**

    * In pairs, complete as many of the challenges below as possible with the time remaining. 

    * Know in advance that these activities are meant to be challenging. So give it your all!

    * *Part 1: Security Analysis*

      * Unzip the folder provided and navigate into the `SecurityResources` folder. Inside you will find a file called `awesome_security_resources.md`. This is a markdown version of the contents listed here: https://github.com/sbilly/awesome-security. This site includes various tools, libraries, documents, and books relevant to security professionals. 

      * You will be using the command line tools you've learned thus far to quickly parse through this file for trends. 

      * Your first task is to use the command line to count the number of times each of the following words appears in the document. Create a `solution.txt` file and enter the counts you retrieve for each. (Note: You do not need to use the command line for appending the counts. Though... that would be pretty impressive if you did!)  

        ```
          Cybersecurity
          Infosec
          Web
          Operating System
          OS
          Security
          Awesome
          Kali
          Linux
          Windows
          Mac

        ```
      * Your next task is to use the command line to create a second file called `TOC.txt`. Then use the command line to retrieve and print each of the headers and sub-headers in the file into the `TOC.txt` file. In effect, you are building a table of contents for the page. (Hint: In markdown files, headers and sub-headers are indicated by the presence of `##` and `###`). Your TOC file will look like something below:

        ```
        ## Network
        ### Scanning / Pentesting
        ### Monitoring / Logging
        ### IDS / IPS / Host IDS / Host IPS
        ...
        ```

      * Finally, you will create a third file called `TOC_with_line_numbers.txt`. This will be similar to the previous example, but will also include the line number for which each of these headers and sub-headers can be found. Your `TOC_with_line_numbers.txt` file will look like something below:

      ```
        53:  ## Network
        55:  ### Scanning / Pentesting
        66:  ### Monitoring / Logging
        ...
      ```

      * Hint: Remember, this is a challenge. So take your time re-visiting old examples to complete this.

    * *Part 2: Blog Analysis*

      * Navigate to the folder called `Blogs`. Inside you will find a folder called `blog_data`. This folder contains an assortment of historic blog posts. 

      * Spend a few moments studying the title formats of each blog post. You will notice that they each use a familiar format that includes the age, gender, and horoscope of the author.
      
      * Then, use the `less` command to preview a random file contained within. Notice that they each contain the creation date.

      * You will be using your newfound command line skills to analyze these blog posts for patterns.

      * Your first task is to count the number of blog posts that include the word `happy`. Repeat this for the word `sad`. Store your findings in a file called `BlogReport.txt`.

      * Your second task is to count the number of blog posts by each gender. Store your findings in `BlogReport.txt`.  

      * Your third task is to count the number of blog posts by month. Store your findings in `BlogReport.txt`.  
      
      * Your final task is to  count the number of blog posts by horoscope. Store your findings in `BlogReport.txt`.  
      
      * Your final output might look something like the below:

      ```
        Happy vs. Sad
        Happy: 94
        Sad: 102

        Gender
        Male: 21
        Female: 19

        Month:
        ...

        Horoscope:
        ...
        
      ```

      * Hint: This activity is particularly challenging. In some cases, you are looking to search the file tree, while in others you are looking to search the contents. Remember, the commands are different for each.

      * Hint: You will need to manually re-run your script for each of the options (e.g. Male vs. Female; Capricorn vs. Acquarius vs. Taurus; etc.)

      * Bonus: If you finish early, look for other things you can do with the files provided. As an example, perhaps you can select all articles written in January, combine them into a file titled `January-Posts.xml`, and move them to the surface. 

      * Bonus: If you are interested in learning what else is possible, spend a few moments reading through the bash documentation: https://ss64.com/bash/