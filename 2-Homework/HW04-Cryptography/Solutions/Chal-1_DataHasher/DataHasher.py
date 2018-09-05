# Libraries
import hashlib
import csv

# List to Store Hashed Data
hashed_data = []

# Read CSV
with open("UserInfo.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0

    # Loop through each row
    for row in csv_reader:

        if line_count == 0:
            hashed_data.append(row)

        # Add each row to the hashed_data list and hash the relevant columns
        else:
            hashed_data.append([row[0], row[1], 
                hashlib.sha256(row[2].encode("utf-8")).hexdigest(),
                row[3],
                row[4],
                row[5],
                row[6],
                row[7],
                hashlib.sha256(row[8].encode("utf-8")).hexdigest(),
                row[9],
                row[10]])

        # Add one to the line count on each iteration
        line_count = line_count + 1

# Write New CSV
with open("UserInfo_Hashed.csv", "w") as new_csv_file:
    writer = csv.writer(new_csv_file)

    # Dump All Data into New CSV
    writer.writerows(hashed_data)

# Final Print Statement
print("Process Complete")

