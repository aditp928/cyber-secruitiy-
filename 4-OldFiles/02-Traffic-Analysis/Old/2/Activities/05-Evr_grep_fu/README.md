# grep-fu

Grep is a very powerful, very versatile tool. It comes with many options, and can perform most basic tasks around searching for text.

The best way to become familiar with its major switches is to simply use it. The next activity is an opportunity to expand on what you saw in the demonstration.

Next time you have a carved HTML file to inspect, you'll know exactly how to tell what's inside...Without even opening it.

## Instructions

- Use `grep` to find all occurrences of the string "jpg" in `7-horrifying-cures-from-medical-history.html`. Don't forget to include line numbers and a tab stop.

- Unfortunately, grep doesn't save this information to a file by default. Next, try: `grep -nT "jpg" 7-horrifying-cures-from-medical-history.html > jpg_occurrences`.

  - Afterwards, run `ls`. Open the new file. What did the `>` operator do?

  - Try this with other commands, such as `ls`. Does it do what you expect?

- We want to know how many JPG links this file contains. For that, we can use the **w**ord **c**ount tool. Run: `wc -l jpg_occurrences`.

  - This counts the number of lines in the file `jpg_occurrences`. How many does it report?

- Next, open the HTML file. Scroll all the way to the bottom. Add a new line with the text: `NONEXISTENT_IMAGE.JPG`.

- Re-run the grep command with `>` from above. How many lines long should the file be now?

- Count the lines in the file with `wc`. What do you notice?

- Return to the command line. Run: `grep -inT "jpg" 7-horrifying-cures-from-medical-history.html > jpg_occurrences`.

- Count the lines in `jpg_occurrences` again. What did adding `i` do?
