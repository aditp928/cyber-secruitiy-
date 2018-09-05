# Not only can Python read files, it can also write to files as well
# The open() function is used once more but now "w" is used instead of "r"
diary_file = open("MyPersonalDiary.txt", "w")

parts_of_entry = ["Dear Diary,", "\n",
                  "Today I learned how to write text into files using Python!",
                  " ", "It was pretty great."]

# Text is written into files one string at a time. Because of this, it is usually a good idea to combine all of the text into a single string before writing it all at once.
full_text = ""
for part in parts_of_entry:

    # The += operator takes the original value of the variable and adds the following value to it
    full_text += part

print(full_text)

# The .write() function is then used to push the text into the external file
diary_file.write(full_text)
