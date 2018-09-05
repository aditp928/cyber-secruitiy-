## 5.1 Lesson Plan: Knowing Networking

### Overview

Today is all about getting students thinking about networking - its complexities and the motivation behind them. We set up the discussion around OSI which we will further explore and visualize through Wireshark throughout the week as we analyze a variety of communication examples and protocols.

### Class Objectives

By the end of class, students will be able to:

- Define Network
- Explain how files are transmitted over the network
- Define Protocol
- Define OSI Model
- Explain each layer of the OSI Model
- Explain the steps of network communication in the context of the OSI Model
- Explain the purpose of Wireshark and start a capture

### Instructor Notes

* This week is all about introducing networking concepts to students and getting them comfortable. The week uses Wireshark as a tool to introduce and visualize complex protocols and network communication.

* Today's class is largely theoretical - the point is to convey concepts, which we'll dive into more deeply throughout the week.

* We strongly recommend running through this week's lecture portions of the class ahead of time, because much of the instruction is done working with Wireshark. Each extra screen, misstep, or keystroke you show is an opportunity for your students to get lost, so be intentional with each step. Take the time necessary to articulate what you are entering/doing at each step.

* We recommend increasing your cursor size so students can more easily follow your mouse and/or zooming into sections of the UI so it's easier for them to follow.

* Try to stay on track of time as best possible, but always feel free to add a few extra minutes to the clock if students are struggling with an activity. As always, have your TAs refer to the [Time Tracker](../5-TimeTracker.xlsx) to help you stay on track.

-------

### 1. Instructor: Intro Class and Networking (0:05)

- Welcome class back!

- Explain that this week we'll be switching gears and focusing on one of the most important topics in cybersecurity - networking.

- Explain that networking is extremely complex. At its core, it's all about communication between devices. Specifically, sharing information out to the world, and getting information back.

- Use the slides to introduce the concept of networking. Be sure to spend a moment talking about roles for which these topics are relevant, and how these concepts are used on the job.

### 2. Instructor: Journey of a File (0:10)

- Use the slides to introduce the following key concepts:

  - Network definition

  - Network communication

  - Client/Server

  - Request/Response

- Explain that stuff will seem like magic at some points, and that that is okay!

- Explain that we're covering things with broad strokes right now - so some terms and processes will still seem like magic. We'll slowly demystify these processes as we learn more.

  - Instructor: to this end, be sure to call and point out where things still feel like magic (and should). We want students grasping specific topics, but not stressing over small things (OSI Model layers, not things like TCP headers yet)

- Answer any questions before moving on.

### 3. Students: Explaining Communication (0:10)

- Explain to students that it's time for them to think about a few common tasks and how they might fit into this framework.

- Use the slide for the activity to distribute the activity instructions.

  - Students attempt to explain to each other at a high-level how network communication works for a few different use cases: file transfer, web, email.

### 4. Instructor: Review Explaining Communication (0:05)

- Use the slides to review the journey for each file type, elaborating on client/server architecture, and follow the flow of back and forth communication for things like a web page.

- Answer any questions before moving on.

### 5. Instructor: Networking Complexities - 0s and 1s (0:10)

- Explain that we've skipped a lot of the complexity of networking so far as "magic". Let's start to dig into that.

- Use the slides to start to discuss how data is transferred between computers - and how transferring data as 0s and 1s adds a lot of complexity.

- Touch on at least the key takeaways:

  - Computers use binary in communication (0s and 1s)

  - All data gets converted to binary somehow - images, music, etc.

  - The request must be converted to binary before sent to the server. The response must be converted to binary before sent back to the client.

  - A good parallel to limited communication of binary is morse code

### 6. Students: Morse Code pt. 1 (0:10)

- Explain that students are going to get some hands-on experience with limited communication.

- Use the slide for the activity to distribute the activity instructions.

- Walk around and help students as necessary.

### 7. Instructor: Review Morse Code (0:05)

- Use the slides to review the process of communicating via morse code. Key takeways:

  - It is similar to network request/response.

  - The message for morse code is shorter than that for binary, as binary is even more limiting

  - There are other limitations inherent to network communication.

### 8. Partners: Morse Code pt. 2 (0:10)

- Explain that to really understand the limitations of communication in this manner, we have to impose a few more restrictions.

- Use the slide for the activity to distribute the activity instructions.

- Walk around and mediate the activity. Don't worry if it gets too loud - that's just another realistic limitation!

### 9. Instructor: Review Morse Code pt. 2 (0:05)

- Ask the class what kinds of problems they ran into.

- Use the slide as a guide to talk about other problems.

- Explain that these problems are inherent to most types of communication, and that rules help us govern communication in a way such that it can be consistently interpreted.


### 10. Instructor: Introduce Protocols (0:10)

- Use the slides to introduce protocols as the answer to some of those problems. Key takeaways:

  - Protocols are sets of rules which specify how interactions between communicating entities should work.

  - Networks are how computers connect - protocols are how they physically and logically communicate.

  - There are a ton of protocols which solve various problems in communication throughout computer networking.

  - Protocols help you data content more effectively.

- Answer any questions before moving on.

### 11. Student: Morse Code pt. 3 (0:15)

- Explain that now it's time for them to build their own Morse code protocol. Their goal is to communicate as efficiently as possible.

- Use the slide for the activity to distribute the activity instructions.

- Walk around and mediate the activity. Again, don't worry if it gets too loud - that's just another realistic limitation! They should build fault tolerance into their protocol.

### 12. Instructor: Review Morse Code pt. 3 (0:10)

- Ask a student to volunteer their protocol solution.

- Use the slides to walk through existing solutions for International Morse Code protocols.

- Continue through the slides to talk about protocols in the context of network communication.

- Time permitting, go through the bonus slide of how to create a Morse Image Protocol

- Don't go in-depth into the TCP packet shown on the "Protocols in Networking" - this is just to get them thinking going into the second part of class.

- Answer any questions, and then break.

---

### 13. Break (0:15)

---

### 14. Instructor: The OSI Model (0:20)

- Explain that what we've covered so far is only the tip of the iceberg. Hundreds of protocols + magic probably = intimidation.

- Encourage them that it just takes time and effort to start to build a mental model.

- Explain that fortunately, a model has been used for some time already to think about these processes.

- Use the slides to go through the OSI Model. Key takeaways:

  - Name, purpose, and protocols of each layer.

  - Understanding that protocols are used at almost every layer to define the specifics of how data is being formed/communicated.

  - Encapsulation and Decapsulation involve the process of converting data to/from something that can be effectively communicated across the network.

### 15. Students: Fill in the Blanks (0:10)

- Explain that the important thing here is that they start to internalize the model.

- Encourage them to try to complete the activity from memory first, so that they can see what their gaps are, before turning to the internet.

- Use the slide for the activity to distribute the activity instructions.

- Walk around and encourage/help students.

### 16. Instructor: Review Fill in the Blanks, Request/Response OSI Model (0:05)

- Don't go on to the review slide yet. From the activity slide, call on various students to explain each layer and fill in the blank.

- Answer any questions before moving on.

### 17. Students: OSI Model HTML (0:15)

- Explain that now it's time to think about how real communication works through the OSI model.

- Explain that, using their newfound model, they should attempt to diagram/draw/explain how a request/response cycle for a web page might work.

- Use the slide for the activity to distribute the activity instructions.

### 18. Instructor: Review OSI Model HTML HTML (0:10)

- Time permitting, have a partner group come up to the front and explain/draw the process.

- To re-iterate, walk through each step, starting with the request.

- Use the slides as a visual in this explanation, or feel free to draw out the process yourself. Key Takeaways:

  - Client makes request to the server, server sends the response. Both times, a full cycle of encapsulation/decapsulation happens with the payload.

  - Content in both directions must be converted to binary to send across the network.

### 19. Instructor: Recap and Next Steps (0:05)

- Use the slide to recap the goals for today and answer any questions.

### 20. END


---

## Time permitting:

### 21. Instructor: Intro to Wireshark (0:05)

- Explain that wireshark is a tool which allows us to start looking at real communication across the network.

- Explain that Wireshark is widely used for forensics purposes to see what happened in network communication.

- Navigate to the Wireshark web page to show students where to install it: https://www.wireshark.org/

### 22. Instructor: Wireshark Demo (0:05)

- Walk through the process of choosing an interface, doing a basic capture, and stopping that capture.

- Don't go too in-depth - we'll have all day tomorrow. This is just to show them what's possible.

### 23. Students: Wireshark Install Check (0:05)

- Use the slide for the activity to distribute the activity instructions.

- Walk around and help debug any installation issues
