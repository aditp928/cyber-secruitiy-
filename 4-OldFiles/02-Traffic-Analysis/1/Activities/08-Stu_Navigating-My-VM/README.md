# Instructions

- Download and launch the VM provided here: <https://drive.google.com/drive/folders/1Utc-lk1y7FKZNdxR1-NoCUlqzOXu6iUG?usp=sharing>
- Open a Terminal.
- **Exploring `/bin`**
    - Move into the `/bin` directory.
    - List all the files. Do you see anything familiar?
    - Choose a file with a unfamiliar name. Type it in, and hit enter. What happens?
    - What kind of files does this folder contain?
    - Move into `/sbin`. Repeat the above exercise, but run: `ifconfig`. What kind of files does this directory contain?
- **Tarballs**
  - Move to the root directory.
  - Find all files ending in `*.tar`. How many are there?
  - Next, find all files ending in `*.tar.gz`. How many do you find?
  - What can you conclude about which format Linux users prefer?
- **The Most Popular User**
  - Move to `/var/`.
  - Count how many times the word `"root"` appears in this folder.
  - Repeat the above, but in the folders `/etc/` and `~`.
  - What can you conclude about these different folders, based on your search results?

# Solutions

- First, move into and explore the `/bin` directory
  - `/bin/` contains program files, including all of the command-line tools we've been using
    - `cd /bin`
    - `ls`
    - Students should recognize some of the files in this folder (`less`, `grep`, `find`, etc.)
    - Have them pick an unfamiliar one, and type in its name, e.g.: `lsblk`
    - This new, unfamiliar name will run a command
    - You'll find the same thing is true with `/sbin`: It also contains programs. The difference is that `/sbin` stands for "**shared** **bin**aries", so it's where files that normal users on the machine will use (not just programs for administrators, which is what `/bin` is for)
    - **Teaching point**: Command-line tools *are just special files*! (In Unix, "everything is a file": <https://en.wikipedia.org/wiki/Everything_is_a_file>)
- Next, find all `*.tar` files on the entire system
  - The `/` directory is the top-level ("root") directory, so search from there
  - Run: `find / -type f -iname '*tar'`
  - This should return zero results
  - Next, look for all gzipped tarballs: `find / -type f -iname '*tar.gz'`
  - This should return some results. To count how many, run: `find / -type f -iname '*tar.gz'`
  - **Teaching point**: Always gzip your tarballs!
- Finally, find out how many times the `root` user is mentioned in each of the directories below
  - Run: `grep -r 'root' /var/ | wc -l` (finds 6296 occurrences)
  - Run: `grep -r 'root' /etc/ | wc -l` (finds 389 ocurrences)
  - Run: `grep -r 'root' ~ | wc -l` (finds 22 ocurrences)
  - Looks like the `/var` directory is the one that has the most to do with `root`
  - **Teaching Point**: What is `var` for? According to Google, `/var/` is a folder that the operating system saves "temporary" files to ("var" means "**var**iable"). Since running programs can save "sensitive" information (like, the names and contents of all the pictures you're editing in Photoshop!...), it makes sense that the trusted "root" user would be the one writing to this directory most often.

## Key Concepts

- Make sure to talk about `"root"` user vs "user accounts" (cover this in detail in next demo about SSH)

## Notes

- There's no `Solved` or `Unsolved` folder, since the link to the VM (`Unsolved`) all the answers (`Solved`) are in this file
- The number of files returned by the `find` commands above can change from VM to VM, so if your results are a bit different, that's okay, as long as the command works without error.
