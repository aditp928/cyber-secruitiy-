# DNS Dictionary

You've been given a list of public DNS server IPs and their provider.

Your goal is to build different data structures for easily accessing information associated with these DNS properties.

## Instructions

Open up the `Unsolved/DNSDictionary.py` file. For each step, accomplish the following:

1. Use a for loop to create a dictionary mapping the provider names to their IPs.

   - For example, two entries in the dictionary would look like:

        ```python
        {
            'Level3': '209.244.0.3',
            'Verisign': '64.6.64.6'
        }
        ```

   - Use the dictionary to print Hurricane Electric's IP

2. Use a for loop to create a list of dictionaries with the associated information.

   - For example, two entries in the list would look like:

        ```python
        [
            {
                'provider_name': 'Level3',
                'primary_server': '209.244.0.3'
            },
            {
                'provider_name': 'Verisign',
                'primary_server': '64.6.64.6'
            }
        ]
        ```
   - Use the list to print the total number of providers.

## Bonuses

3. Use a for loop to update your dictionary from part 1 with the new IPs

   - For example, two entries in the dictionary would look like:

        ```python
        {
            'Level3': ['209.244.0.3', '209.244.0.4'],
            'Verisign': ['64.6.64.6', '64.6.65.6']
        }
        ```

   - The IPs should be in the form of an array of IPs.

   - Use the dictionary to print Google's IPs

4. Use nested for loops to update the list from part 2 with a "secondary_server" key.

   - For example, two entries in the list would look like:

        ```python
        [
            {
                'provider_name': 'Level3',
                'primary_server': '209.244.0.3',
                'secondary_server': '209.244.0.4'
            },
            {
                'provider_name': 'Verisign',
                'primary_server': '64.6.64.6',
                'secondary_server': '64.6.65.6'
            }
        ]
        ```

5. Super bonus: use the `pprint` module to print more elegantly. This will take a lot of research, but we will cover this in a future class.
