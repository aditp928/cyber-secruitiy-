# The open() function is also used for writing, though it defaults to "r"ead
# so we have to use the "w" mode as the second argument ("w"rite, instead of "r"ead)
diary_file = open("MyPersonalDiary.txt", "w")


# The .write() function is then used to push the text into the external file
diary_file.write("I don't write in diaries.")
diary_file.write("Period.")
