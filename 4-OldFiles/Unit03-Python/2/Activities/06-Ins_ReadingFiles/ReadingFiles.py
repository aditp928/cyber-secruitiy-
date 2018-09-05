# External files can be opened and saved to a variable within python using the open() function

#######
# TXT #
#######

# The open() function holds two key parameters...
# The first parameter is the relative or absolute path to file to open
# The second parameter is a "r" string which tells Python to read the file
diary_txt = open("Diary.txt", "r")

# Using the .read() function then stringifies the file's contents
diaryText = diary_txt.read()
print(diaryText)
print("------------")

# Since the file is now a string, it can be modified and worked with using some string functions

# The split() function breaks a string apart into a list based upon common words/characters that appear in the original string
diarySplit = diaryText.split(" ")

# Since the string was split on spaces, individual words will now be printed when referenced
print(diarySplit[0])
print(diarySplit[1])
print(diarySplit[2])
print(diarySplit[3])
print("-----------")

# The find() function will navigate through some text, determine whether or not the string passed into it is contained within, and return the index of that string
print(diaryText.find("malarkey"))

# This can be exceptionally useful when checking to see if a file contains some specific keywords
if diaryText.find("malarkey") > -1:
    print("Malarkey found!")
if diaryText.find("juice") > -1:
    print("Juice found")
print("-----------")


#######
# CSV #
#######

wrestling_csv = open("WWE-Data-2016.csv", "r")
wrestling_text = wrestling_csv.read()

# Since a CSV is broken into rows and columns, it will need to be split twice
# The first split is to break the original text into rows by splitting on each new line
wrestling_rows = wrestling_text.split("\n")
print(wrestling_rows[0])
print(wrestling_rows[1])
print(wrestling_rows[2])
print(wrestling_rows[3])
print("-----------")


# The next split will then split the row into its respective columns on commas
wrestling_cells = wrestling_rows[0].split(",")
print(wrestling_cells[0])
print(wrestling_cells[1])
print(wrestling_cells[2])
print(wrestling_cells[3])
