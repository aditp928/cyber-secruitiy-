import os
# Module for reading CSVs
import csv

csv_path = os.path.join('Resources', 'WWE-Data-2016.csv')

###################################################
### Method 1: Improved Reading using CSV module ###
###################################################
file = open(csv_path)

contents = csv.reader(file)

# contents returned as a CSV object we can loop through
print(contents)

for row in contents:
    print(row)

    # rows are already created as lists of cells for us, so no need to split
    print(row[0])


#################################################
### Method 2 (Old): Plain Reading (no module) ###
#################################################
file = open(csv_path)
contents = file.read()

print(contents)

# contents is one big string, so we have to manually split it up
rows = contents.split("\n")

for row in rows:
    print(row)

    # row is still just one big string, so we have to manually split it up
    cells = row.split(",")

    print(cells[0])
