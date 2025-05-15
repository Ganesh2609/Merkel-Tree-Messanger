# Secure File Transfer System with Merkle Tree Verification

A robust client-server communication system implemented in Python that enables secure file transfers with data integrity verification using Merkle trees. The system supports multiple concurrent clients, encrypted communications, and automatic file organization.

## 🚀 Features

### Core Capabilities
- **Secure File Transfer**: Transfer files between clients within the same subnet with end-to-end encryption
- **Merkle Tree Verification**: Ensure data integrity using cryptographic hash trees
- **Multi-Client Support**: Handle multiple simultaneous client connections with threading
- **Automatic File Organization**: Files are automatically sorted into `Sent/` and `Received/` directories by username

### Technical Features
- **Encryption**: All communications encrypted using Fernet symmetric encryption
- **Serialization**: Data serialized using Python's pickle library for efficient transmission
- **Threading**: Concurrent message processing for improved performance
- **Socket Programming**: Low-level network communication using TCP sockets

## 📋 System Architecture

### Basic Theory
The system implements a client-server architecture where:
1. **Server** acts as a central relay point, managing client connections and routing messages
2. **Clients** connect to the server and can send files to other connected clients
3. **Merkle Trees** are used to verify file integrity by creating a hierarchical hash structure

### How Merkle Trees Work
1. File is divided into blocks of specified size
2. Each block is hashed using SHA-256
3. Hashes are paired and hashed again, creating a tree structure
4. The root hash represents the entire file
5. Receiver rebuilds the tree and compares root hashes to verify integrity

### Security Model
- All communication is encrypted using symmetric key encryption (Fernet)
- Files are verified using cryptographic hashes
- Each client has separate directories for sent and received files

## 🛠️ Installation & Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. Install required dependencies:
   ```bash
   pip install cryptography
   ```

3. Generate encryption key (first time only):
   ```bash
   python Generate_Key.py
   ```

4. Update IP addresses in both `Server.py` and `Client.py`:
   ```python
   host = "YOUR_IP_ADDRESS"  # Replace with your actual IP
   ```

## 🚦 Usage

### Starting the Server
```bash
python Server.py
```
The server will start listening for client connections on the specified port.

### Running Clients
```bash
python Client.py
```
- Enter your username when prompted
- To send a file:
  1. Enter recipient's username
  2. Enter filename (must be in your `Sent/` directory)
  3. Enter block size for Merkle tree (e.g., 1024)

### File Organization
- Sent files: `Sent/<your_username>/`
- Received files: `Received/<your_username>/`

## 📁 Project Structure

```
.
├── Server.py           # Server implementation
├── Client.py           # Client implementation
├── Encrypt.py          # Encryption/decryption functions
├── Generate_Key.py     # Key generation utility
├── Clear_data.py       # Utility to clean directories
├── key.txt            # Shared encryption key
├── Sent/              # Directory for sent files
└── Received/          # Directory for received files
```

## 🔧 Technical Details

### Server.py
- Manages client connections using threading
- Routes messages between clients
- Maintains list of active connections
- Handles client disconnections gracefully

### Client.py
- Implements dual-threaded architecture (send/receive)
- Builds Merkle trees for file verification
- Manages local file storage
- Handles encryption/decryption of messages

### Encrypt.py
- Provides encryption/decryption wrapper functions
- Uses Fernet symmetric encryption
- Reads key from `key.txt` file

### Generate_Key.py
- Creates a new encryption key
- Saves key to `key.txt` for shared use

## ⚙️ Configuration

Before running, ensure:
1. All machines are on the same subnet
2. IP addresses are correctly configured in source files
3. Port 41720 is available (or change in both files)
4. Required directories exist or will be created automatically

## 🔐 Security Considerations

- The encryption key is shared among all clients (symmetric encryption)
- Key should be distributed securely outside of this system
- Files are stored unencrypted on local machines
- Network traffic is encrypted but endpoints must be trusted

## 🧪 Testing

1. Start the server
2. Launch multiple client instances
3. Send test files between clients
4. Verify files are received correctly
5. Check Merkle tree verification messages

## 💡 Troubleshooting

- **Connection refused**: Check IP address and ensure server is running
- **File not found**: Ensure file exists in `Sent/<username>/` directory
- **Authentication failed**: File may be corrupted during transfer
- **Client disconnection**: Check network connectivity

## 🚀 Future Enhancements

- GUI interface for easier interaction
- Support for file resumption
- Public key cryptography for enhanced security
- File compression before transfer
- Progress indicators for large files

## 📝 Dependencies

- Python 3.x
- cryptography library
- Standard libraries: socket, threading, pickle, hashlib, os, time
