# Unit 3 | "No, it isn't magic"

Fantastic news—Hogwarts has finally retired its outdated Simple Owl Transfer Protocol, and recently installed WiFi in every building on campus!

Of course, there's work to be done before the network is fully functional, and the sorting hat has chosen *you* to build it out.

To get things up and running, you'll need to complete the tasks below. Don't forget to verify connectivity after you're done!

## Instructions

For this exercise, you must accomplish the tasks below to configure the new Hogwarts network.

### Art

You will need to place the art building on their own switch. It should use a default gateway of `192.168.10.1`.

- You will need to set static IP addresses for the following students in that class:
  - Potter (computer)
  - Weasley (computer)
  - Granger (computer)
  - Longbottom (computer)
  - Griffen (which will be a printer)
- Use IP addresses in the range: `192.168.20.2-6`.

#### Science

 You will need to place the science building on their own switch using `192.168.40.1` as the gateway.

- The science building will need three different VLANS as they teach many courses.
- You will need to place them on their own VLAN and set static IP addresses for the following people that are in the Computer Science class using IP addresses in the range `192.168.30.2-5`.
  - Lovegood (computer)
  - Ollivander (computer)
  - Bagnold (computer)
  - Lockhart (computer)
- There will be a teachers lounge in the science building they need to be on their own VLAN using ip addresses `192.168.50.2-5`.
- There is an ethical hacking course taught in the science building. They will be on their own VLAN, and need static IP addresses for the following computers:
  - Riddle
  - Crabbe
  - Draco
  - Goyle
- Use IP addresses in the range `192.168.60.2-5`.

#### Ministry of Magic

Lastly, the Ministry of Magic provides servers for data retrieval and deposit. These sensitive computers are maintained beneath the Whomping Willow (...now you can see why it hits anyone who ventures too close).

It has the following four servers, and uses the ip addresses of `192.168.90.2-6`, and is on its own switch. It should use the gateway `192.168.90.1`.

- Magical Game and Sports
- Transportation
- Law Enforcement
- Magical Accidents

#### Connectivity

Finally, every computer will need to speak to everything that is connected to the router as a way to verify your network works. Use whatever methods you see fit to test for connectivity.

**Good luck!**

---

![](Images/1.png)

***"Use the force, Harry" - Gandalf***
