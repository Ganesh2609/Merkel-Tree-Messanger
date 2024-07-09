# Client-Server Architecture with Secure File Transfer (Merkel Tree)

## Overview
This project demonstrates a robust client-server communication setup using Python's socket programming. Key features include threaded message processing for simultaneous handling across clients, data serialization with pickle, and encryption using Fernet from the cryptography library. A Merkel tree is constructed on the client side to ensure data integrity during transmission. Files can be securely exchanged within the same subnet, with storage managed under designated usernames in Sent and Received folders on each client's machine.

## Features

### Threading
- **Concurrent Message Processing:** Utilizes Python's threading library to handle simultaneous message processing in the client and across multiple clients on the server, enhancing responsiveness and scalability.

### Serialization and Encryption
- **Data Serialization:** Implements data serialization using Python's pickle library to convert complex data structures into byte streams for efficient transmission over the network.
- **Data Encryption:** Ensures secure communication channels using Fernet from the cryptography library, encrypting messages to protect sensitive information from unauthorized access during transmission.

### Message Timing and Subnet Communication
- **Message Timing:** Utilizes Python's time library to record and display the timing of sent messages, aiding in performance monitoring and debugging.
- **Subnet Communication:** Enables seamless message exchange within the same subnet, facilitating communication between connected clients without external network configurations.

### Secure File Transfer and Merkel Tree
- **Secure File Transfer:** Supports secure file exchange between clients, maintaining confidentiality and integrity of transferred files. Files are stored under designated usernames in local Sent and Received folders on each client's machine.
- **Merkel Tree for Content Verification:** Implements a Merkel tree on the client side to verify the integrity of transmitted content, ensuring data consistency and reliability.

### User Management and Interaction
- **User-specific Storage:** Organizes sent and received files under specified usernames, ensuring personalized data management and retrieval for each client.
- **Interactive Communication:** Provides a user-friendly interface for sending messages and files, enhancing user interaction and experience during client-server interactions.

### Scalability and Performance
- **Scalable Architecture:** Designed for scalability, allowing seamless addition of new clients and efficient message handling across a growing network.
- **Performance Optimization:** Optimizes message processing and file transfer mechanisms to minimize latency and enhance overall system performance.

## Usage
1. Clone the repository:
   ```
   git clone https://github.com/Ganesh2609/Merkel-Tree-Messanger.git
   ```
   
3. Run the server:
   ```
   python server.py
   ```
   
4. Run the client:
   ```
   python client.py
   ```

   NOTE : Multiple clients can be run at the same time in the same device for file transfer over the subnet
   
5. Follow the on-screen prompts to send messages or files between clients within the same subnet.

## Dependencies
Ensure Python 3.x is installed along with the required libraries:
- cryptography
- pickle
- threading 
- time 
- socket
- hashlib
