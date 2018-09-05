# Create folder to hold report
mkdir Reports

# Create file for report 
touch Reports/IP_Report.txt

# Add Initial Text for Break-Ins by Month
echo "UNIQUE IP COUNT (BREAK-IN ATTEMPTS)" > Reports/IP_Report.txt
echo "------------------------------------" >> Reports/IP_Report.txt
grep -i "BREAK-IN" * | grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' | sort | uniq | wc -l >> Reports/IP_Report.txt

# List of IP Addresses with attempted Break-Ins
echo "" >> Reports/IP_Report.txt
echo "IP WATCH LIST" >> Reports/IP_Report.txt
echo "------------------------------------" >> Reports/IP_Report.txt
grep -i "BREAK-IN" * | grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' | sort | uniq >> Reports/IP_Report.txt
