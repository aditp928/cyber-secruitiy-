# Dictionary that will be used to count how often a letter appears
alphabet_counts = {
  "a":0,
  "b":0,
  "c":0,
  "d":0,
  "e":0,
  "f":0,
  "g":0,
  "h":0,
  "i":0,
  "j":0,
  "k":0,
  "l":0,
  "m":0,
  "n":0,
  "o":0,
  "p":0,
  "q":0,
  "r":0,
  "s":0,
  "t":0,
  "u":0,
  "v":0,
  "w":0,
  "x":0,
  "y":0,
  "z":0
}

# The message that will be looped through
secret_message = 'p ctl uxgtuxvwitg lph qtxcv igpxcts qn pc das uxgt rwxtu. "wdl ldjas ndj gtpri xu p hjsstc uxgt uapgts je dc iwt ugdci du iwt qjxasxcv?" phzts iwt uxgt rwxtu. "qgtpz dji p uxgt wdht pcs hipgi hegpnxcv xi, rwxtu." pchltgts iwt ctl uxgtuxvwitg. "wdl ldjas ndj gtpri xu pcdiwtg uxgt uapgts je xc iwt qprz du iwt qjxasxcv?" phzts iwt uxgt rwxtu. "qgtpz dji pcdiwtg uxgt wdht pcs hipgi hegpnxcv xi, rwxtu." pchltgts iwt ctl uxgtuxvwitg. "pcs xu pcdiwtg wjvt uxgt uapgts je xc iwt qphtbtci, wdl ldjas ndj gtpri?" phzts iwt uxgt rwxtu. "qgtpz dji pcdiwtg uxgt wdht." pchltgts iwt ctl uxgtuxvwitg. "cdl lpxi p bxcjit, hdc," hpxs iwt uxgt rwxtu. "lwtgt pgt paa iwtht uxgt wdhth rdbxcv ugdb?" iwt ctl uxgtuxvwitg pchltgts, "iwt hpbt eaprt lwtgt paa du iwt uxgth pgt rdbxcv ugdb, rwxtu."'
# Loop through every character in the message
for character in secret_message:

  # Check if the character is a key in the alphabet_counts dictionary
  if(character in alphabet_counts.keys()):

    # Add one to the count to the key of the character found
    alphabet_counts[character] += 1
  
# Print out the completed dictionary
print(alphabet_counts)