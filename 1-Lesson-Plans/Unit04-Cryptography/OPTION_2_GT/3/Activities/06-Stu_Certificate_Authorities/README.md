# Certificate Authorities and Trust

## Questions

Relying on mutual trust in Certificate Authorities makes intuitive sense, but it has its disadvantages.

- What if someone you're trying to communicate with doesn't trust the CA that's verified your identity?

- Imagine Eve tricks a CA into issuing her a certificate that says she's actually **Apple, Inc**.
  - How can Eve take advantage of this?
  - How would clients find out about such a mix-up?
  - How would the CA Eve duped go about fixing this mistake?

- Relying on certificate authorities isn't the _only_ way to establish trust in someone's identity. Read the **Simplified Explanation** of the Web of Trust: <https://en.wikipedia.org/wiki/Web_of_trust#Operation_of_a_web_of_trust>

  - How does the Web of Trust "prove" that a message came from a given individual? In other words: How does the Web of Trust use public/private keys to establish identity?

  - How is this different from the way Certificate Authorities establish identity?

  - In your own words, summarize one advantage and disadvantage of the CA model, and one advantage and disadvantage of the Web of Trust model.

## Bonus

- PGP is an encryption program that relies on the web of trust, and is used to encrypt a variety of data, including emails, files, and hard drives. 

- If you'd like to be extra safe and send _only_ encrypted email with your classmates, sign up for ProtonMail, a free email service that automatically encrypts emails you send to other ProtonMail users: <https://protonmail.com/>