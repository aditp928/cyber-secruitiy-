# Instructions

- In your VM, create an account for your partner. Set the password they specify.
- On your own computer (in your host machine, *not* the VM), write a secret message into a text file, AND download an image from Giphy.
  - E.g.: `echo -e "Secretly, I'm terrified of GIFs." > file1"`
  - Also, download a GIF from e.g.: <https://giphy.com/gifs/americasgottalent-agt-americas-got-talent-d31w24psGYeekCZy/links>
- Still on your local computer, hexdump this message and picture. 
  - Save them as `file1.dump` and `file2.dump`, so your partner has no clue as to which file is which.
- Create a gzipped tarball containing these dumps, called `archive.tar.gz`.
- Use `scp` to upload this file to your partner's home directory in YOUR VM.
- Next, have your partner use `ssh` to log into their account on your VM.
- Then, have them find the file you saved for them, and use `scp` to copy it to their computer.
- Once they have it on their machine, have them extract the archive and use `xxd` to recover the original files.
- Find out the correct extension for each file, and rename them.
- Open up the file from Explorer or Finder to verify the extension was correct.
- **Celebrate!**


# Solutions

- In your VM, create an account for your partner. Set the password they specify.
  - `useradd -m -s /bin/bash myPartner`
  - `passwd myPartner` (Used password: `partnersPassword`)
- On your own computer (in your host machine, *not* the VM), write a secret message into a text file, OR download an image from Giphy.
  - E.g.: `echo -e "Secretly, I'm terrified of GIFs." > confession"`
  - Also, download a GIF from e.g.: <https://giphy.com/gifs/americasgottalent-agt-americas-got-talent-d31w24psGYeekCZy/links>
- Still on your local computer, turn this message or picture into a hexdump.
  - `xxd -p confession > confession.dump`
  - `xxd -p giphy.gif > giphy.dump`
  - `tar -cvzf archive.tar.gz file1.dump file2.dump`
- Use `scp` to upload this file to your partner's home directory in YOUR VM.
  - `scp archive.tar.gz myPartner@192.168.1.7:/home/myPartner`
- Next, have your partner use `ssh` to log into their account on your VM and locate this file.
  - `ssh myPartner@192.168.1.7`
  - `find . -type f -name '*tar.gz'`
- The, have them find the file you saved for them, and use `scp` to copy it to their computer.
  - `ssh myPartner@192.168.1.7:/home/myPartner/archive.tar.gz`
- Extract the archive.
  - `tar -xzvf archive.tar.gz`
- Once they have it on their machine, have them use `xxd -r -p > original` to recover the original file.
  - `xxd -r -p file1 > file1.undumped`
  - `xxd -r -p file2 > file2.undumped`
- Have them use `head` to identify which one is a text file, and which one is a GIF.
- Rename the file with the correct extension.
  - Either: `mv file1.undumped original.gif`
  - Or: `mv file2.undumped confession.txt`
- Open up the file from Explorer or Finder to verify extension.
- Celebrate!
