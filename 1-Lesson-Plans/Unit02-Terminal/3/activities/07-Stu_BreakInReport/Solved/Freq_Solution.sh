# Create folder to hold report
mkdir Reports

# Create file for report 
touch Reports/Frequency_Report.txt

# Add Initial Text for Break-Ins by Month
echo "BREAK-IN ATTEMPTS (BY MONTH)" > Reports/Frequency_Report.txt
echo "---------------------------------" >> Reports/Frequency_Report.txt

# Add Monthly Breakdown
echo "November" >> Reports/Frequency_Report.txt
grep -i "BREAK-IN" * | grep -i "NOV" | wc -l >> Reports/Frequency_Report.txt

echo "December" >> Reports/Frequency_Report.txt
grep -i "BREAK-IN" * | grep -i "DEC" | wc -l >> Reports/Frequency_Report.txt

# Add Initial Text for Break-Ins by Hour
echo "" >> Reports/Frequency_Report.txt
echo "BREAK-IN ATTEMPTS (BY HOUR)" >> Reports/Frequency_Report.txt
echo "---------------------------------" >> Reports/Frequency_Report.txt

# Add Hourly Breakdown
echo "00" >> Reports/Frequency_Report.txt
grep -i "BREAK-IN" * | grep -i " 00:" | wc -l >> Reports/Frequency_Report.txt

echo "01" >> Reports/Frequency_Report.txt
grep -i "BREAK-IN" * | grep -i " 01:" | wc -l >> Reports/Frequency_Report.txt

echo "02" >> Reports/Frequency_Report.txt
grep -i "BREAK-IN" * | grep -i " 02:" | wc -l >> Reports/Frequency_Report.txt

echo "03" >> Reports/Frequency_Report.txt
grep -i "BREAK-IN" * | grep -i " 03:" | wc -l >> Reports/Frequency_Report.txt

echo "04" >> Reports/Frequency_Report.txt
grep -i "BREAK-IN" * | grep -i " 04:" | wc -l >> Reports/Frequency_Report.txt

echo "05" >> Reports/Frequency_Report.txt
grep -i "BREAK-IN" * | grep -i " 05:" | wc -l >> Reports/Frequency_Report.txt

echo "06" >> Reports/Frequency_Report.txt
grep -i "BREAK-IN" * | grep -i " 06:" | wc -l >> Reports/Frequency_Report.txt

echo "07" >> Reports/Frequency_Report.txt
grep -i "BREAK-IN" * | grep -i " 07:" | wc -l >> Reports/Frequency_Report.txt

echo "08" >> Reports/Frequency_Report.txt
grep -i "BREAK-IN" * | grep -i " 08:" | wc -l >> Reports/Frequency_Report.txt

echo "09" >> Reports/Frequency_Report.txt
grep -i "BREAK-IN" * | grep -i " 09:" | wc -l >> Reports/Frequency_Report.txt

echo "10" >> Reports/Frequency_Report.txt
grep -i "BREAK-IN" * | grep -i " 10:" | wc -l >> Reports/Frequency_Report.txt

echo "11" >> Reports/Frequency_Report.txt
grep -i "BREAK-IN" * | grep -i " 11:" | wc -l >> Reports/Frequency_Report.txt

echo "12" >> Reports/Frequency_Report.txt
grep -i "BREAK-IN" * | grep -i " 12:" | wc -l >> Reports/Frequency_Report.txt
