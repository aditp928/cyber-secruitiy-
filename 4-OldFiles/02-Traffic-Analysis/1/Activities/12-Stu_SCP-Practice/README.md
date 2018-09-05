# Instructions

# Solutions

- On your VM, login with your new user account.
- Navigate to your home directory.
- Run the following commands. What do they do?
  - `whoami`
  - `uname -a`
- Save the output of these commands to a file.
  - First, run: `whoami`, and save its output to a file, called `system_information`.
  - Then, run: `uname -a`, and *append* its output to `system_information`.
- Use `pwd` to print the path to this file.
- Log out of your user account.

- Return to your host machine.
- Use `scp` to copy the file you just created to your host computer.
- Use `cat` to verify the information inside the file looks like you expect.
