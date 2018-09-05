# IP Check

## Instructions

- Write code that checks to see if an IP address entered by the user is in the provided list.

  - If it’s in the list, print “IP Address X.X.X.X found in the list at index Y” (Y = index of IP).

  - Otherwise, print “IP Address X.X.X.X not found”.

## Hint

- Don’t use a loop! Look into using the `in` operator.

- We haven’t talked about getting a count of occurrences in a list yet. To the Internet!

## Bonuses
1. If the IP Address is in the list, have the program print an extra line: “IP Address X.X.X.X was found Z times” (Z = # times IP Address occurs in list)

2. Add another initial prompt for action. It should allow for “add” or “search” actions. search behaves as above, whereas add instead adds the IP to the existing list and prints out the new list of IP addresses.

3. If something other than “add” or “search” is entered (for step 2), the program should error before asking for the IP address.
