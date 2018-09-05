## 7.1 Lesson Plan - The Great White Wireshark 

**Overview**

- In today's class, students will learn about monitoring data, recognizing malware coming through, and read messages across the traffic. It is important to note, that Wireshark will not work in a home enviroment unless it is connected to a switch, with port mirroring turned on. Because of these restrictions we will be using pcap files (files from wireshark transfers) in order to replicate an enviromental network. Throughout the day, students will complete difficult exercises focused on using Wireshark.

**Class Objectives**

- Students should gain a better understanding networking protocols. 
- Students should gain a better understanding of packets "moving across the wire"
- Students should become familiar with recognizing malicious traffic. 

**Instructor Notes**

- Welcome to Day 1 ! Today's class is more hands-on, and difficult for students that are not paying attention. In this class, students will pick up from where they left off with Wireshark, as well as learn new skills that Cyber Analyst, and  System Administrators use to diagonose issues in the network.
- This class will be as difficult for the students that struggled with the first week of Wireshark. It is important to help those students that are struggeling to grasp the beginner concepts, and show them different examples on how to preform the same task. 
- Because this is still a "new" technolog to most students, it is highly reccommended to be familiar with the in class labs before teaching, to help the students navigate through any issues they may have. 
- Pay close attention to time today. There are many "mini-exercises" in today's class and it can get easy to lose time in the shuffle. 
- As always, have your TAs refer to the Time Tracker to stay on track.

### 1. Instructor Do: Introduce Our Categories of Network Security Problems  (0:05)

### 2. Students Do: Wireshark Review Activity  (0:07)

- **Instructions:**
  - XXX
  - XXX
  - XXX
  - XXX

### 3. Instructor Do: Review Wireshark Review Activity (0:05)

- Next, take a few moments to review the solution. As you do, use the below talking points to guide your discussion:
  - XXX
  - XXX
  - XXX
- Answer any questions that remain before proceeding to the next section.

### 4. Instructor Do: Intro to DDoS and Heartbleed (0:15)

### 5. Students Do: Identifying DDoS Attacks (0:10)

- **Instructions:**
  - XXX
  - XXX
  - XXX
  - XXX

### 6. Instructor Do: Review Identifying DDoS Attacks  (0:05)

- Next, take a few moments to review the solution. As you do, use the below talking points to guide your discussion:
  - XXX
  - XXX
  - XXX
- Answer any questions that remain before proceeding to the next section.

### 7. Students Do: Identifying Heartbleed Attacks (0:10)

- **Instructions:**
  - XXX
  - XXX
  - XXX
  - XXX

### 8. Instructor Do: Review Identifying DDoS Attacks  (0:05)

- Next, take a few moments to review the solution. As you do, use the below talking points to guide your discussion:
  - XXX
  - XXX
  - XXX
- Answer any questions that remain before proceeding to the next section.

------

### 9. Break (0:15)

------

### 10.  Instructor Do: Intro to Malware  (0:10)

### 11.  Instructor Do: Malware Relevant Filters  (0:07)

- Next, take a few moments to introduce students to the next set of Wireshark techniques:
  - `http.request` This filter shows requests to http pages.
  - `data.data` This filter finds TCP packets with information. 
  - `Statistics Endpoints`This shows communciations between devices and websites. It gives information on packet sizes as well. Show that you can see how many converations have been completed as well. 
  - Right clicking a packet and clicking on `Follow TCP/SSL/UDP Stream`This shows the protocol you have chosen in the same way an application layer sees it. For example, if you are looking for passwords of a Telnet stream or trying to make sense of a data stream. 

- Answer any questions that remain before proceeding to the next section.

### 12.  Students do: Malware PCAP Analysis  (0:10)

- **Instructions:**
  - XXX
  - XXX
  - XXX
  - XXX

### 13.  Instructor Do: Review Malware PCAP Analysis (0:08)

- Next, take a few moments to review the solution. As you do, use the below talking points to guide your discussion:
  - XXX
  - XXX
  - XXX
- Answer any questions that remain before proceeding to the next section.

### 14.  Students Do: Avengers Malware Activity  (0:20)

- **Instructions:**
  - XXX
  - XXX
  - XXX
  - XXX

### 15.  Instructor Do: Review Avengers Malware  (0:10)

- Next, take a few moments to review the solution. As you do, use the below talking points to guide your discussion:
  - XXX
  - XXX
  - XXX
- Answer any questions that remain before proceeding to the next section.

### 16.  Students Do: King Arthur Activity (0:20)

**Instructor:** This will be a live walkthrough of a lab. Slack the instructors, questions, and the pcap pollerman.pcap file to the students. 

- **Instructions:**
- You get a distress call on your brand new flip phone that you recieved from Steve Rogers. The avengers need your help and have called you down to their headquarters. When you get there, they explain to you that on Tuesday March 21st 2017, their IDS notified them that a Windows host at 192.168.22.94 was infected with maleware.  Your job is to review the pcap and answer the following questions...  
  - Find the start time of the activity.
  - MAC address of the affected Windows computer.
  - IP address of the affected Windows computer.
  - Host name of the affected Windows computer.
  - Find the website Pollman got the virus from and how the attack happened.
  - There was another attack that happened, from another website. What happened? 

### 17.  Instructor Do: Review King Arthur Activity  (0:10)

- Next, take a few moments to review the solution. As you do, use the below talking points to guide your discussion:
  - XXX
  - XXX
  - XXX
- Answer any questions that remain before proceeding to the next section.

### 18.  Instructor Do: Prelude Next Class (0:05)

------

### Copyright

Trilogy Education Services © 2018. All Rights Reserved.