# Instructions

- On your host computer, navigate to this ASCII art generator in your browser: <http://www.chris.com/ascii/>
- Use it to generate a message, and save it in a file called `flag_file`.

- Next, create a new user account on your VM, called `guest`.
- Use `scp` to upload your flag file to the guest directory.

- Now, you'll have your partner find and download this file.
- First, tell your partner to log into the guest account from their machine.
- Then, have them find the flag file you created.
- Next, have them copy the flag to their own machine.
- Finally, have them read the contents of the file to find out which number you used in your flag.


# Solutions

- On your host computer, navigate to this ASCII art generator in your browser: <http://www.chris.com/ascii/>
- Use it to generate a message, and save it in a file called `flag_file`.

- Next, create a new user account on your VM, called `guest`.
  - `useradd -m -s /bin/bash guest`
  - `passwd guest`. Use password: `guestPassword`.
- Use `scp` to upload your flag file to the guest directory.
  `scp flag_file guest@192.168.1.7:/home/guest`

- Now, you'll have your partner find and download this file.
- First, tell your partner to log into the guest account from their machine.
  - `ssh guest@192.168.1.7`
- Then, have them find the flag file you created.
  - `find . -type f -iname '*flag*'`
- Next, have them copy the flag to their own machine.
  - `scp guest@192.168.1.7:/home/guest/flag_file .`
- Finally, have them read the contents of the file to find out which number you used in your flag.
  - `cat flag_file`
