# The open() function with the "w" parameter will always overwrite existing text
# To simply add text onto the end of a file, the "a" parameter is used instead ("a"ppend)
diary_file = open("MyPersonalDiary.txt", "a")

diary_file.write("\nSincerely, \nJacob")
