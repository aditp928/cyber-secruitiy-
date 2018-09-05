# Lists of parts of an IP address
networks = [22, 42, 35, 99, 65, 108, 51, 86, 77, 42]
nodes = ["13.226.95", "132.236.53", "207.190.5", "92.241.202", "141.68.121",
         "63.140.86", "176.227.105", "180.254.218", "197.86.150", "209.119.137"]

# Create a loop that goes through the network list and node list at the same time, pairing them together
# This will output 10 total IP addresses

# Loop through the range of the networks list
for x in range(len(networks)):

    # Use the index to refer to the values in both the networks and nodes list
    # Since the network list is integers and the node list is strings, the network values must be stringified
    print(str(networks[x]) + "." + nodes[x])

print("-----------")

# Create a pair of loops that goes through both lists and pairs all of the values together
# This will output 100 total IP addresses

# Loop through each value in the network list
for network in networks:

    # Loop through each value in the node list
    for node in nodes:

        print(str(network) + "." + node)
