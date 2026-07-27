# Secure File Storage System with AES-256 Encryption

## Project Overview
This project creates a secure file storage application that allows users to encrypt and decrypt files using AES-256 encryption. It protects files from unauthorized access by requiring a key/password for decryption.

### How Encryption Works
Encryption is the process of converting data into a coded format that can only be read by someone who has the key to decode it. AES (Advanced Encryption Standard) is a widely used encryption method that secures data by transforming it into an unreadable format.

### Technologies Used
- Python as the programming language
- Cryptography library for AES encryption
- Tkinter for the graphical user interface (GUI)
- SQLite for storing activity logs (if required)

### Project Workflow
1. selects a file to encrypt.
2. The application encrypts the file using AES-256.
3. The encrypted file is saved.
4. can decrypt the file using the correct key/password.
5. The application logs encryption/decryption activities.

## Folder Structure
```
secure-file-storage-system
├── src
│   └── secure_file_storage
│       ├── __init__.py
│       ├── main.py
│       ├── encryption.py
│       ├── storage.py
│       └── utils.py
├── tests
│   ├── __init__.py
│   ├── test_encryption.py
│   └── test_storage.py
├── .env.example
├── .gitignore
├── README.md
├── requirements.txt
└── pyproject.toml
```

