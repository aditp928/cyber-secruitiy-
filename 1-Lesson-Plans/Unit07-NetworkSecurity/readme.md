# Unit Objectives

Unit 7 formally introduces students to the fundamentals of network security.

They will learn about threats, vulnerabilities, and risks; ways in which exposure leaks

By the end of Unit 7, students should:

1. Be able to analyze their own servers for vulnerabilities
1. Be able to profile remote hosts (e.g., determine their operating systems, etc.)
1. Be able to perform basic recon on remote hosts (e.g., port scans, service enumeration, etc.)
1. Be able to explain how the results of this recon can support later exploitation
1. Name common exploits
1. Identify and implement fundamental defenses against these exploits
1. Minimize exposure and attack surface (e.g., putting down unused services; implementing firewalls; etc.)

## Conceptual / Tenets

1. Understand the relationship between threats, vulnerabilities, and risks
1. Articulate details that attackers can learn about systems exposed to the public Internet (e.g., which services they run; what OS they run; kernel version;etc.)
1. Explain how attackers can use results of reconnaissance to identify vulnerabilities (e.g., "Linux servers running this particular kernel version are susceptible to this particular buffer overflow attack..."; "Devices with open SMTP ports, and which allow anonymous login, can leak information through VRFY requests"; etc.)
1. Explain the basics of how to identify this kind of reconnaissance using packet capture and other network monitoring tools (e.g., HIDS, NIDS, etc.)
1. Explain how an attacker's vulnerability assessment supports exploitation, and give examples of common exploits involving protocols and exposed services
1. Explain ways to minimize attack surface (e.g., put down unused services; use only secure protocols, when possible; etc.)
1. Identify and implement defenses against common vulnerabilities (e.g., disallow anonymous access to certain services; etc.)
1. Explain and implement firewalls to hinder vulnerability assessments

## Practice / Tools

- Linux service administration via scripts in `/etc/init.d` and/or `service` tool
- `nmap` (port scans and other sorts of recon)
- `iptables` (configuring firewall rules)
- Basic security monitoring (using, e.g., Snort to identify suspicious activity, e.g., spotting SYN scans, etc.)

## Certification / Tickets

The topics from this week cover many of the Network Security domain objectives on Network+, and many objectives in Security+.

Many of the topics in this unit are also pertinent to the OSCP, for students who are interested in pursuing it independently.

## Sources

Here links to references used in learning or building this material. In addition, other relevant resources are included.

- [Princeton Information Security Course Resources](https://www.cs.princeton.edu/courses/archive/fall16/cos432/)
- [RIT edX Course on Network Security](https://courses.edx.org/courses/course-v1:RITx+CYBER504x+1T2018/course/)

---

### Copyright

Trilogy Education Services © 2018. All Rights Reserved.
