from cryptography.fernet import Fernet

def generate_key():
    """Generate a new AES-256 key."""
    return Fernet.generate_key()

def encrypt_file(file_path, key):
    """Encrypt the specified file using the provided key."""
    fernet = Fernet(key)
    
    with open(file_path, 'rb') as file:
        original_data = file.read()
    
    encrypted_data = fernet.encrypt(original_data)
    
    with open(file_path + '.encrypted', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

def decrypt_file(encrypted_file_path, key):
    """Decrypt the specified encrypted file using the provided key."""
    fernet = Fernet(key)
    
    with open(encrypted_file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    
    decrypted_data = fernet.decrypt(encrypted_data)
    
    with open(encrypted_file_path.replace('.encrypted', ''), 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)