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
1. User selects a file to encrypt.
2. The application encrypts the file using AES-256.
3. The encrypted file is saved.
4. User can decrypt the file using the correct key/password.
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

## Building the Project Step by Step
- **src/secure_file_storage/__init__.py**: This file marks the directory as a Python package. It can be empty or contain package-level documentation.
- **src/secure_file_storage/main.py**: This is the entry point of the application. It will create the GUI and handle user interactions.
- **src/secure_file_storage/encryption.py**: This file will contain functions for encrypting and decrypting files using AES-256.
- **src/secure_file_storage/storage.py**: This file will handle file operations, such as saving and loading encrypted files.
- **src/secure_file_storage/utils.py**: This file will contain utility functions, such as logging activities and validating user input.
- **tests/**: This directory will contain unit tests for the encryption and storage functionalities.
- **.env.example**: This file will serve as a template for environment variables.
- **.gitignore**: This file specifies files and directories that should be ignored by Git.
- **README.md**: This file will contain documentation about the project, including how to set it up and use it.
- **requirements.txt**: This file lists the required Python packages for the project.
- **pyproject.toml**: This file is used for project metadata and dependencies.

## Setting Up the Project in VS Code on Mac
1. **Creating the project folder**: Open Terminal and run `mkdir secure-file-storage-system && cd secure-file-storage-system`.
2. **Creating a virtual environment**: Run `python3 -m venv venv` to create a virtual environment named `venv`.
3. **Activating the virtual environment**: Run `source venv/bin/activate` to activate the environment.
4. **Installing required packages**: Create a `requirements.txt` file with the following content:
   ```
   cryptography
   tkinter
   ```
   Then run `pip install -r requirements.txt` to install the packages.
5. **Running the program**: After completing the code, run `python3 src/secure_file_storage/main.py` to start the application.

## Project Documentation After Completion
- **Project Abstract**: A secure file storage system that encrypts and decrypts files using AES-256 encryption, ensuring data protection.
- **Problem Statement**: Users need a secure way to store sensitive files that can only be accessed by authorized individuals.
- **Objectives**: To develop a user-friendly application that encrypts files and maintains a log of encryption/decryption activities.
- **Software Requirements**: Python 3.x, Cryptography library, Tkinter.
- **Hardware Requirements**: Any computer capable of running Python.
- **System Architecture Explanation**: The application consists of a GUI for user interaction, a backend for encryption/decryption, and a logging system for tracking activities.
- **Algorithm**: The application will use AES-256 encryption for securing files, with a key/password for decryption.
- **Flowchart Description**: A flowchart will illustrate the steps from file selection to encryption and decryption.
- **Test Cases**: Test cases will cover scenarios such as successful encryption/decryption, handling incorrect keys, and logging activities.
- **Future Improvements**: Potential enhancements could include cloud storage integration and multi-user support.
- **Conclusion**: The project successfully demonstrates secure file storage using encryption, providing a foundation for further development.

## Viva Questions and Answers
- **Q: What is AES-256 encryption?**
  A: AES-256 is a symmetric encryption algorithm that uses a 256-bit key to encrypt and decrypt data, providing a high level of security.
- **Q: How does the application ensure file security?**
  A: The application encrypts files before saving them, requiring a key/password for decryption, thus preventing unauthorized access.
- **Q: What technologies were used in this project?**
  A: The project uses Python, the Cryptography library for encryption, Tkinter for the GUI, and SQLite for logging activities.