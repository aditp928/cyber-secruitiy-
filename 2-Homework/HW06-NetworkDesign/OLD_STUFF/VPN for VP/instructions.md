## VPN's at Dunder Mifflin



Jan Levingston, is the VP of Sales at Dunder Mifflin. Because she's on the road a lot she needs the ability to log on in no matter what office she's at, and have a VPN set up to log into her server. Jan has come to you and asked if you could create her a VPN between the Dunder Mifflin Router, so she can access the FileServer, MailServer and WebServer.



**Objectives**



1.  Set Jan with the static IP address of 10.10.10.10
2.  Give the Dunder Mifflin router an IP address of 192.168.1.1
3.  Create and assign the following IP's to the following servers
  	   a. MailServer 192.168.1.8
  	   b. WebServer 192.168.1.16
  	   c. File Server 192.168.1.24
4.  The public IP address of the Dunder Mifflin router needs to be 10.10.10.11
5.  aaa authentication login will need to be set up on network abc1 local
6.  aaa authorization will need to be set up on network abc2 local
7.  Username needs to be admin with a password of paper. 
8.  Use crypto isakmp policy 10
9.  Use encryption 3des
10. Make sure the hash is md5
11. Authentication will need to be pre-share.
12. The VPN pool will need to be 172.168.1.1-172.168.1.50
13. The client configuration group will need to be managers, with a key of "password123"
14. Make sure the client can connect

**Hint** This is a difficult lab, be sure to consulte the glossary, and bring up any issues you are struggeling with in class. 
