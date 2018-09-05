# Instructions

# Solutions

- Create a user with a home directory on the VM
  - `useradd -m -s /bin/bash peleke`
  - `passwd peleke` (used: `dummyPassword`)
- Log in as the new user, and save your IP address information to a file:
  - `su peleke`
  - `cd /home/peleke`
  - `mkdir IPInformation`
  - `cd IPInformation`
  - `sbin/ifconfig | grep 'inet' | head -n 1 > ip_information`
  - `exit`
- Return to the host computer; log in via SSH; locate this file with `find`; and print its contents with `cat`
  - From host: `ssh peleke@192.168.1.7`
  - First, find out where you are: `pwd`
  - From SSH line: `find . -type f -name 'ip_information' -exec cat {} \;`
  - This should print the information you expect!
  - Exit from SSH: `exit`
