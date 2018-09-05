## Hogwarts is moving to the cloud

After your third partner has been eaten by a Blast-Ended Skrewt, your boss at the auroras office wants you to try to tackle a more difficult problem. The ministry of magic wants to move all their data to the cloud, and it is your job to help connect  the three schools in the district to it. Additionally they would like to have frame relay set up in the cloud between the different networks. 

**Objectives**

For this exercise, you must accomplish the following...

1. Set up three networks to the cloud, with a router, a switch and a PC like so...

**Hogwarts**  	**Router** 192.168.1.1	 **PC** 192.168.1.2	 **WAN**	10.0.1.1

**Beauxbatons**	**Router** 192.168.4.1	 **PC** 192.168.4.2	 **WAN**	10.0.4.4

**Durmstrang** 	**Router** 192.168.2.1   **PC** 192.168.2.2  **WAN**	10.0.2.2


2. On the cloud you will need to set up the following...

**Serial1** hog - beau beau - hog
**Serial2** beau - durm beau - hog
**Serial4** dur - beau dur - hog

3. Lastly verify that the routers have static routes with thier ip addresses, as well as the current hops they will need to get from point a to point b.

   **Hint you will need to use the commmand encapsulation frame-relay**

   **Hint in order to connect the three networks you will need to add an additional piece to the cloud**















