# Client-Server Architecture with Secure File Transfer (Merkel Tree)

## Overview
This project demonstrates a robust client-server communication setup using Python's socket programming. Key features include threaded message processing for simultaneous handling across clients, data serialization with pickle, and encryption using Fernet from the cryptography library. A Merkel tree is constructed on the client side to ensure data integrity during transmission. Files can be securely exchanged within the same subnet, with storage managed under designated usernames in Sent and Received folders on each client's machine.

## Features
- **Threading:** Utilizes Python's threading library for concurrent message processing in the client and across multiple clients on the server.
- **Serialization:** Data is serialized to byte streams using Python's pickle library for efficient transmission.
- **Encryption:** Messages are encrypted using Fernet to ensure secure communication channels.
- **Message Timing:** The time library records and prints the timing of sent messages for performance monitoring.
- **Subnet Communication:** Supports message exchange within the same subnet, facilitating communication between connected clients.
- **File Transfer:** Allows secure file transfer between clients, storing files under specified usernames in local Sent and Received folders.
- **Merkel Tree:** Implements a Merkel tree on the client side to verify the integrity of transferred content.

## Usage
1. Clone the repository:
   ```
   git clone <repository_url>
   ```
   
2. Navigate to the project directory:
   ```
   cd client-server-secure-transfer
   ```
   
3. Run the server:
   ```
   python server.py
   ```
   
4. Run the client:
   ```
   python client.py
   ```
   
5. Follow the on-screen prompts to send messages or files between clients within the same subnet.

## Dependencies
Ensure Python 3.x is installed along with the required libraries:
- cryptography
- pickle (standard library)
- threading (standard library)
- time (standard library)

## Contribution
Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

---

Feel free to customize the README further based on additional details or specific instructions for running and using your project.Here's a concise description and a longer README file for your GitHub repo:

---

**Client-Server Architecture with Secure File Transfer**

**Description:**
This repository implements a client-server architecture in Python using socket programming. It features threading for concurrent message handling, pickle for data serialization, Fernet for data encryption, and Merkel tree construction on the client side for content verification. Messages and files can be securely exchanged within the same subnet, stored under specified usernames in Sent and Received folders.

**README.md:**

# Client-Server Architecture with Secure File Transfer

## Overview
This project demonstrates a robust client-server communication setup using Python's socket programming. Key features include threaded message processing for simultaneous handling across clients, data serialization with pickle, and encryption using Fernet from the cryptography library. A Merkel tree is constructed on the client side to ensure data integrity during transmission. Files can be securely exchanged within the same subnet, with storage managed under designated usernames in Sent and Received folders on each client's machine.

## Features
- **Threading:** Utilizes Python's threading library for concurrent message processing in the client and across multiple clients on the server.
- **Serialization:** Data is serialized to byte streams using Python's pickle library for efficient transmission.
- **Encryption:** Messages are encrypted using Fernet to ensure secure communication channels.
- **Message Timing:** The time library records and prints the timing of sent messages for performance monitoring.
- **Subnet Communication:** Supports message exchange within the same subnet, facilitating communication between connected clients.
- **File Transfer:** Allows secure file transfer between clients, storing files under specified usernames in local Sent and Received folders.
- **Merkel Tree:** Implements a Merkel tree on the client side to verify the integrity of transferred content.

## Usage
1. Clone the repository:
   ```
   git clone <repository_url>
   ```
   
3. Run the server:
   ```
   python server.py
   ```
   
4. Run the client:
   ```
   python client.py
   ```
   
5. Follow the on-screen prompts to send messages or files between clients within the same subnet.

## Dependencies
Ensure Python 3.x is installed along with the required libraries:
- cryptography
- pickle (standard library)
- threading (standard library)
- time (standard library)
