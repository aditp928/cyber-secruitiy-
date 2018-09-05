providers = ["Level3", "Verisign", "Google", "Quad9", "DNS.WATCH", "Comodo Secure DNS", "OpenDNS Home", "Norton ConnectSafe", "GreenTeamDNS", "SafeDNS", "OpenNIC",
             "SmartViper", "Dyn", "FreeDNS", "Alternate DNS", "Yandex.DNS", "UncensoredDNS", "Hurricane Electric", "puntCAT", "Neustar", "Cloudflare", "Fourth Estate"]

primary_DNS_servers = ["209.244.0.3", "64.6.64.6", "8.8.8.8", "9.9.9.9", "84.200.69.80", "8.26.56.26", "208.67.222.222", "199.85.126.10", "81.218.119.11", "195.46.39.39", "69.195.152.204",
                       "208.76.50.50", "216.146.35.35", "37.235.1.174", "198.101.242.72", "77.88.8.8", "91.239.100.100", "74.82.42.42", "109.69.8.51", "156.154.70.1", "1.1.1.1", "45.77.165.194"]

# Create an empty list that the DNS dictionaries will be added to
DNS_dictionaries = []

# Loop through both of the lists
for x in range(len(providers)):

    # Create a new dictionary to store the current list values inside of
    DNS_dict = {
        "provider_name": providers[x],
        "primary_server": primary_DNS_servers[x]
    }

    # Push the dictionary into DNS_dictionaries
    DNS_dictionaries.append(DNS_dict)

# print out the list of dictionaries
print(DNS_dictionaries)

#############
### BONUS ###
#############

DNS_secondaries = [
    {
        "provider": "Level3",
        "secondary": "209.244.0.4"
    }, {
        "provider": "Verisign",
        "secondary": "64.6.65.6"
    }, {
        "provider": "Google",
        "secondary": "8.8.4.4"
    }, {
        "provider": "Quad9",
        "secondary": "149.112.112.112"
    }, {
        "provider": "DNS.WATCH",
        "secondary": "84.200.70.40"
    }, {
        "provider": "Comodo Secure DNS",
        "secondary": "8.20.247.20"
    }, {
        "provider": "OpenDNS Home",
        "secondary": "208.67.220.220"
    }, {
        "provider": "Norton ConnectSafe",
        "secondary": "199.85.127.10"
    }, {
        "provider": "GreenTeamDNS",
        "secondary": "209.88.198.133"
    }, {
        "provider": "SafeDNS",
        "secondary": "195.46.39.40"
    }, {
        "provider": "OpenNIC",
        "secondary": "23.94.60.240"
    }, {
        "provider": "SmartViper",
        "secondary": "208.76.51.51"
    }, {
        "provider": "Dyn",
        "secondary": "216.146.36.36"
    }, {
        "provider": "FreeDNS",
        "secondary": "37.235.1.177"
    }, {
        "provider": "Alternate DNS",
        "secondary": "23.253.163.53"
    }, {
        "provider": "Yandex.DNS",
        "secondary": "77.88.8.1"
    }, {
        "provider": "UncensoredDNS",
        "secondary": "89.233.43.71"
    }, {
        "provider": "Neustar",
        "secondary": "156.154.71.1"
    }, {
        "provider": "Cloudflare",
        "secondary": "1.0.0.1"
    }
]

# Loop through DNS_secondaries
for secondary in DNS_secondaries:

    # Loop through DNS_dictionaries
    for primary in DNS_dictionaries:

        # Check if the "provider" value of secondary is equal to the "provider_name" value of primary
        if(secondary["provider"] == primary["provider_name"]):

            # Add a new value called "secondary_server" into primary with the value stored in secondary["secondary"]
            primary["secondary_server"] = secondary["secondary"]

# print out the list of dictionaries
print(DNS_dictionaries)
