

 ## 13. Instructor Do: Intro to VoIP

* Explain to students that we will now identify VoIP messages found in Wireshark. 

* VoIP stands for Voice Over IP, meaning we're making phone calls using digital phones rather than analog phones. 

* Take a look a the image below.

![Images](Images/en1.jpg)

* Our voice is an alalog signal, but to be sent through the ineternet it needs to be turned into a digital signal.

* Once our alalog signal has been converted into a digital signal, it's incapsulated in an IP packet, where it is sent across the network as a digital signal, and converted back into an analog signal for the recipient to hear.

* Our voice literally turns into data!

* In Wireshark, VoIP works through a protocol called RTP or "Real-Time Protocol".

* While looking for Wireshark, try to identify the RTP protocol to find the VoIP message. 

**Scenario**

* Use the "Voip Instructor" for the live demo. 

* There was a capture the flag (CTF) contest held by Seccon in 2016. The mission was to find, and listen the VoIP call first to hear the code. The code then unlocked another piece of the puzzle and so on and so forth. Today we'll be learning on how to find the secret VoIP message in the pcap file. 

* RTP stands for Real-Time Protocol. This is the protocol that is used for delivering VoIP calls, which means that we found the VoIP transmission!
![img](Images/v1.png)

* However, RTP can be difficult for Wireshark to discriminate from other UDP payloads. This is because of the different signals that can come from different VoIP phones.

* In order to recognize RTP traffic from UDP packet, you 

* Explain to students that usually Wireshark will decode the information as RTP, but when it doesn't it will just show UDP data that is unrecognizable. 

![img](Images/communication.png)

* We can see that From the time the packets were sent and recieved that the UDP data is flowing being passed back and forth many times in less than a second. 

* Right click as a packet and click "Decode As" 

![img](Images/v2.png)

* Choose to be decoded as RTP 

![img](Images/v3.png)

* Go to Telephony, and "RTP" and then "Stream Analysis"

* Stream analysis will turn our RTP traffic into a format that we humans can understand. 

![img](Images/v4.png)

* Click on "Graph" and "Play Streams"

![img](Images/v5.png)

* Click on the triangle pointing to the right to hear the message.

![img](Images/v6.png)


### 14. Student Do: Password Leakage (VoIP)

* Send to students the pcap file entitled "Voip Students."

* Present the following scenario:

* You are the Systems Administrator at "Sugar and Spice and a lot of Dead Mice Exterminators." Romulas, the new Account Manager, complains to you that he didn't get his new IPAD. He claims someone from HR called him and promised it would be on his desk this morning.
* Use the packet capture in this folder to learn more about the phone call and answer the following question:  What is Romulus' password?
  
* *Hint* The RTP traffic has been disguesed as UDP traffic. You will first need to convert the UDP traffic to RTP traffic. 

### 15. Instructor Do: Password Leakage (VoIP) Review

* Point out that when trying to identify the VoIP traffic, Wireshark didn't decode anything. The hint in the scenario told us we need to convert the UDP packets into RTP packets. Let's go ahead and do that now. 

![img](Images/sv1.png)

* Right click as a packet and click "Decode As"

![img](Images/sv2.png)

* Decode as RTP

![img](Images/sv3.png)

* Go to Telephony, and "RTP," then "Stream Analysis"

![img](Images/sv4.png)

* Click on the triangle pointing to the right to hear the message.

![img](Images/sv5.png)

