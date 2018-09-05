### Instructor Do: Protocols & Layered Models (0:15)

- **Objectives**: [Objectives.md](Objectives.md)

- **Slides**: [Protocols & Layered Models](TCP_IP_Model.pptx)

---

- Point out that there can be a wide variety of devices on any given network.
- There can be phones, different kinds of computers, printers, fax machines...
- Explain that devices use common protocols to get around these differences.
- Explain that a protocol acts as a “common language” that can be used by different devices.
- Explain that protocols define strict rules for how two devices are supposed to communicate.
- Explain that, as long as the two devices adhere to these rules, they’ll be able to understand each other, regardless as to what the devices are.
- Explain that protocols are typically defined in Requests For Comment (RFCs), such as the RFC for HTTP/1.1 (<https://tools.ietf.org/html/rfc7230>).

- Explain that protocols typically define rules for how devices should:

  - **Open connections**. Protocols specify how devices should request and negotiate connections with new devices. This process is often called handshaking.
  - **Configure the connection**. Protocols specify if the device should encrypt data; If so, how are keys traded; etc.
  - **Format Data**. Protocols define very specific data formats. Devices communicating under a certain protocol expect to receive messages adhering to the specification.
  - **Handle Errors**. Protocols specify how devices should handle situations such as corrupt data, dropped connections, etc.
  - **Terminate Connections**. Protocols specify how devices should end the connection between them.

- Explain that we’ll take a brief look at how the HTTP protocol specifies how to initiate requests and format data.

- Display the below quote to the class.

  > “A client sends an HTTP request to a server in the form of a request message, beginning with a request-line that includes a method, URI, and protocol version…, followed by header fields containing request modifiers, client information, and representation metadata…, an empty line to indicate the end of the header section, and finally a message body containing the payload body.”.

- Explain that this excerpt from RFC 7230 (<https://tools.ietf.org/html/rfc7230>), which defines Message Syntax for the HTTP protocol, gives a flavor of what defining a protocol entails.

  - Note that it defines how devices initiate connections (in the form of a request message), and the data format.

    GET /hello.txt HTTP/1.1
    User-Agent: curl/7.16.3 libcurl/7.16.3 OpenSSL/0.9.7l zlib/1.2.3
    Host: www.example.com
    Accept-Language: en, mi

- Explain that this example request implements the description from the RFC.

  - Point out that `GET` is the **Method**; `/hello.txt` is the **Path**; and `1.1` is the **Protocol Version**.

  - Also explain that **headers** are key-value pairs.

  - For example, explain that `Accept-Language` is the header key, and its value is `en, mi`.

- Explain that, when we communicate through the web (or via email, file transfer, etc.), our application sends data to another, receiving application.

- Explain that, for this to happen successfully, the user’s data must ultimately be converted into binary (“ones and zeros”) to be transmitted across the network; and then, from ones and zeros back to a format the target application can understand.

- Explain that there are different ways to conceptualize this series of conversions, called **layered models**.

- Explain that layered models divide the network into different logical “layers”.

  - Explain that each layer is responsible for a different set of tasks.
    Explain that one layer might be responsible for collecting user input; another would be responsible for putting that user input on the network; etc.

- Explain that the model used on the Internet is the TCP/IP Model, also called the Department of Defense Model.

- Explain that the TCP/IP model organizes this conversion into a series of four steps.

  ![](http://1.bp.blogspot.com/_FRSoY4n-eek/S21qmcKw5UI/AAAAAAAAAf4/mYCB2024Yrs/s640/TCPIP+Diagram.jpg)

- Explain that, at each step, data gets packaged and prepared for the devices and protocols at the next level.

- Explain that each level is associated with a different set of protocols and devices.

- Emphasize that not all applications use all seven layers.
- Explain that we’ll now take a look at each of these layer individually.
  Then, we will take a look at how they work together in a live example.

#### Application Layer

- Explain that the application layer is concerned with converting user data to a format that can be transmitted on the network.

- For web apps, the major protocol is HTTP (or HTTPS, which is the encrypted version).

- Emphasize that, at this level, data is formatted for user-facing applications to consume.

#### Transport Layer

- Explain that the transport layer is responsible for actually transmitting data across the network.

  - Explain that the transport layer also segments large pieces of data into chunks for transmission .

  - Explain that the transport layer also ensures devices don’t send more data than recipients can consume. This is called congestion control.

  - Explain that transport-layer protocols also implement robust error checking to check for dropped or corrupted packets, etc.

#### Internet Layer

- Explain that the Internet layer is responsible for routing data through physical networks.

  - In other words, the Internet layer ensures data gets to the correct destination.

- Explain that Internet-layer devices use IP address to identify target networks.

- Explain that Internet-layer devices use a protocol called ARP, or Address Resolution Protocol, to map IP addresses to hardware addresses.

  - Explain that this allows network hardware to map an IP address to an real, physical machine.

  - Explain that we’ll discuss this process in greater detail when we discuss switches.

- Explain that routers are examples of Internet-layer devices.

#### Network Access Layer

- Explain that the network access layer is responsible for converting packets into data that can be sent along physical wires or fibers to target devices. In other words, this is the layer that puts TCP/IP packets onto the network.

- Explain that this typically involves data being fed to a network adapter (e.g., a network card).

  - Explain that each physical network adapter is assigned an IP Address so that it can connect to the network

- Explain that this network adapter is responsible for packaging data from the computer’s physical hardware and passing it to a router for further transport along the network.

#### Data Encapsulation

- Remind students that, in the case of our web example, a user attempted to send data across the network.

- Point out that, obviously, the data the user wants to send will be part of the data that gets transmitted.

- Explain that, for this packet to get to its destination, it must include additional metainformation.

- Explain that this metainformation includes details such as the source/destination IP Addresses; the type of IP address in use (IPv4 vs IPv6); the transport-layer source/destination port; etc.

- Explain that, as data flows down, protocols responsible for sending data add this metainformation is added in the form of headers and footers, which are prepended/appended to the data.

- Explain that, as data flows back up on the other side, protocols responsible for reading data read this metainformation to determine what to do with it (i.e., which IP address to send it to; etc.), and then strip the headers/footers they needed before passing the data up to the next layer.

- Explain that the process of adding headers and footers in this manner is known as data encapsulation.

- Explain that the :package: of data that gets sent through the wire is called a Protocol Data Unit, or PDU.

![](http://www.satmagazine.com/cgi-bin/display_image.cgi?744052542)

- Explain that we’ll take an in-depth look at data encapsulation in later weeks, but that we’ll use Wireshark to take a sneak peek at how these layers look in real data.

#### Wireshark Demonstration

- Explain that we'll now use Wireshark to see the TCP/IP Model in action.

- Navigate to the [Aavtrain](http://www.aavtrain.com/index.asp) website.

  - Point out the login form on the home page.

  ![The insecure login form we'll be inspecting.](Images/insecure_login.png)

- Ask a student to explain which protocol this application will use to send data on the network.

  - Remind students that web applications communicate via HTTP.

- Explain that HTTP traffic is *not* encrypted. In other words, it is passed to the network as **cleartext**.

  - Explain that this means anyone can read data sent through HTTP requests and responses.

- Explain that we can see this by intercepting a login request with Wireshark.

- Open Wireshark, and filter for HTTP traffic.

- Return to the browser, and attempt to login with fake credentials. Any username/pass combination works just fine.

- Return to Wireshark, and point out the packets representing the request/response.

  ![Request/response packets from our login attemp.](Images/capture.png)

- Click on the packet corresponding to the POST request.

- In the Packet Details window of Wireshark, select the **HTML Form URL Encoded: application/x-url-encoded** tab, and show the submitted information—in cleartext!

  ![](Images/cleartext.png)

- Explain that passwords are *not* transmitted as cleartext on sites that use HTTPS, which is an encrypted version of HTTP.

  - Optionally, repeat the exercise on an HTTPS-enabled site to demonstrate the difference.

- Point out how the scrollbar in the Packet Bytes frame of Wireshark jumps to the very bottom of the window.

  - Explain that this is where we can see part of the Application Layer data we submitted in its raw form.

  - Explain that the highlighted cleartext on the right is the **POST Body**, which is the payload mentioned in the definition of HTTP requests.

  ![](Images/post_body.png)

- Click on the **Hypertext Transfer Protocol** tab in the Packet Details frame of Wireshark.

  - Point out that the highlighted text jumps again, this time to the beginning of the HTTP request.

  - Explain that this is what the Application Layer data looks like in its entirety.

    ![](Images/app_data.png)

- Explain that we can inspect data from the other layers, as well.

- Click on the **Transmission Control Protocol** tab.

  - Point out that we can see the Source Port and Destination Port, as well as other Transport Layer details.

  ![](Images/transport.png)

- Demonstrate the data under the **Internet Protocol** and **Ethernet** tabs, as well.

- Explain that we'll dig into the details of how data is formatted at each level in later classes.

- Return to the slides, and deliver the **Pulse Check**.

#### OSI Model

- Explain that another important model for data flow in the network is the OSI Model.

- Explain that both models are popular for categorizing protocols, but that TCP/IP is technically more in tune with modern day protocols.

  ![](Images/https://www.webopedia.com/imagesvr_ce/8023/7-layers-of-osi-icon.jpg)

- Explain that the OSI model organizes this conversion into a series of seven steps.

- Explain that, at each step, data gets packaged and prepared for the devices at the next level.

- Explain that each level is associated with a different set of protocols and devices.

- Emphasize that not all applications use all seven layers.

  - Explain that all seven are available for all applications, but not all applications need all seven layers.

- Explain that we’ll now take a look at each of these layer individually.

  - Talk through the slides on the OSI Model.

- Deliver the Pulse Check, and take a moment to address remaining questions before proceeding.
