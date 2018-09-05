# Encryption Isn't Everything

TLS/SSL offers some pretty impressive security guarantees...Obviously, or we wouldn't use it as the primary means for encrypting our web traffic!

But, encryption alone isn't everything. Discuss the questions below with your partner, and see if you can figure out what's still missing...

## Questions

We use TLS/SSL to ensure that noone snooping on our data can actually read it. What would they need to be able to "crack the code"?

- Recall that the server and client trade public keys before opening a connection. What does the server use the client's public key for?

- Recall that the server uses a symmetric key to encrypt data it sends to the server. How does the client decrypt the data it's getting from the server?

- Is it dangerous if the attacker gets ahold of either public key?

- Is it dangerous if the attacker gets ahold of either _private_ key?

- Is it dangerous if the attacker gets ahold of the symmetric key?

    - What would the attacker need to have to get ahold of the symmetric key?

- Let's think about a totally different scenario. Imagine you try to browse to YouTube to watch the latest Key and Peele skits, but some attacker tricks you into connecting to their website—`EvilYoutube.bad`—instead.

  - Before you open a connection what do you send to the attacker? What does the attacker send to you?

    - Hint: What are the first two steps of TLS/SSL?

  - What does the attacker do with the key you sent them?

    - Hint: What's the second step?

  - Say the attacker tries to Rick Roll you, insteaad of letting you watch the fine comedy you logged on for. Will they succeed, or does encryption protect you from this nefarious attack?

# Hints

- Regarding the questions about private and symmetric keys:

  - Which private key is needed to decrypt the symmetric key?
