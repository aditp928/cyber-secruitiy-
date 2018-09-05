# Create a new folder called AllRecords
mkdir AllRecords

# Find all order records and copy into the AllRecords directory
find . -type f -iname 'order_records.csv*' -exec cp {} Allrecords \;

# Move into the AllRecords Folder
cd AllRecords

# Create a folder called VIPCustomerOrders
mkdir VIPCustomerOrders

# Use grep to find all orders from the VIP Customers
grep -i 'michael,campbell' * > VIPCustomerOrders/michael_campbell_orders.output
grep -i 'michael,davis' * > VIPCustomerOrders/michael_davis_orders.output

# Move into the VIPCustomerOrders folder
cd VIPCustomerOrders

# Create a file to store the results
touch VIPCustomerDetails.md

# Count the number of orders each made
echo "Michael Campbell Orders" > VIPCustomerDetails.md
grep -i "Michael,Campbell" michael_campbell_orders.output | wc -l >> VIPCustomerDetails.md

echo "Michael Davis Orders" >> VIPCustomerDetails.md
grep -i "Michael,Davis" michael_davis_orders.output | wc -l >> VIPCustomerDetails.md
