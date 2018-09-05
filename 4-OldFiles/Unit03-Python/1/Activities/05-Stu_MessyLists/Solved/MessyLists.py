# Create a list of 25 IP addresses
IP_addresses = [
  "53.239.114.76",
  "210.139.118.14",
  "219.244.176.34",
  "92.66.150.44",
  "129.214.130.92",
  "201.162.172.112",
  "253.81.123.95",
  "191.17.33.30",
  "103.45.116.156",
  "137.19.78.70",
  "207.209.106.220",
  "154.94.120.111",
  "193.191.199.241",
  "173.63.87.241",
  "171.206.243.138",
  "214.0.115.26",
  "77.37.112.191",
  "82.82.0.22",
  "117.107.226.33",
  "65.136.121.223",
  "139.181.19.183",
  "4.230.145.100",
  "176.43.211.193",
  "67.35.193.108",
  "12.177.40.89"
]

# Find the length of the list
print(
  "The list is " + str(len(IP_addresses))) + " items long"
)

# Find the index for the IP "82.82.0.22"
print(
  "The index for 82.82.0.22 is " + str(IP_addresses.index("82.82.0.22"))
)

# Find the index for the IP "207.209.106.220"
print(
  "The index for 207.209.106.220 is " + str(IP_addresses.index("207.209.106.220"))
)

# Add a couple new IPs to the list
IP_addresses.append("220.66.146.40")
IP_addresses.append("245.201.208.161")
IP_addresses.append("208.222.148.199")
IP_addresses.append("104.216.140.187")
IP_addresses.append("73.57.167.115")

# Remove a couple old IPs from the list
IP_addresses.remove("53.239.114.76")
IP_addresses.remove("65.136.121.223")
