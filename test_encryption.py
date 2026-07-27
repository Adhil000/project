# File: /secure-file-storage-system/secure-file-storage-system/tests/test_encryption.py

import unittest
from src.secure_file_storage.encryption import encrypt_file, decrypt_file
from cryptography.exceptions import InvalidKey

class TestEncryption(unittest.TestCase):

    def setUp(self):
        self.test_file_path = 'test.txt'
        self.encrypted_file_path = 'test_encrypted.aes'
        self.key = b'my_secret_key_32_bytes_long!'  # 32 bytes for AES-256

        # Create a test file
        with open(self.test_file_path, 'w') as f:
            f.write('This is a test file.')

    def tearDown(self):
        import os
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)
        if os.path.exists(self.encrypted_file_path):
            os.remove(self.encrypted_file_path)

    def test_encrypt_file(self):
        encrypt_file(self.test_file_path, self.encrypted_file_path, self.key)
        self.assertTrue(os.path.exists(self.encrypted_file_path))

    def test_decrypt_file(self):
        encrypt_file(self.test_file_path, self.encrypted_file_path, self.key)
        decrypted_content = decrypt_file(self.encrypted_file_path, self.key)
        with open(self.test_file_path, 'r') as f:
            original_content = f.read()
        self.assertEqual(original_content, decrypted_content)

    def test_decrypt_with_invalid_key(self):
        encrypt_file(self.test_file_path, self.encrypted_file_path, self.key)
        with self.assertRaises(InvalidKey):
            decrypt_file(self.encrypted_file_path, b'invalid_key_32_bytes_long!')

if __name__ == '__main__':
    unittest.main()