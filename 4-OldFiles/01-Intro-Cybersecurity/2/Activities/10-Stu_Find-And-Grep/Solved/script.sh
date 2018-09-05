# Part I - Security Analysis
# ----------------------------

# Preview the security file
less awesome_security_resources.md

# Search for each keyword
grep -i 'Infosec' awesome_security_resources.md

# Count incidences
grep -i 'Infosec' awesome_security_resources | wc -l

# Repeat for each keyword
# ...

# Store the table of contents
grep '##' awesome_security_resources > TOC.txt

# Store the data in a table of contents with line numbers
grep -in '##' awesome_security_resources > TOC_with_line_numbers.txt 

# Part II - Security Analysis
# ----------------------------

# Count incidences of happy or sad
grep -rli 'happy' . | wc -l
grep -rli 'sad' . | wc -l

# Retrieve male vs female counts
find . -type f -iname *.male.* | wc -l
find . -type f -iname *.female.* | wc -l

# Count incidences of months
grep -rli "january" . | wc -l
grep -rli "february" . | wc -l

# Count incidences of horoscopes
find . -type f -iname *.Capricorn.* | wc -l
find . -type f -iname *.Taurus.* | wc -l

# Count number of GIFs
cd GIFs
ls | wc -l

# Count number of JPEGs
cd ..
cd JPEGs
ls | wc -l