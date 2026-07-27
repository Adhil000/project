# File: /secure-file-storage-system/secure-file-storage-system/tests/test_storage.py

import unittest
from secure_file_storage.storage import save_file, load_file

class TestStorage(unittest.TestCase):

    def setUp(self):
        self.test_file_path = 'test_file.txt'
        self.test_data = b'This is a test file.'

    def tearDown(self):
        try:
            import os
            os.remove(self.test_file_path)
        except FileNotFoundError:
            pass

    def test_save_file(self):
        save_file(self.test_file_path, self.test_data)
        with open(self.test_file_path, 'rb') as f:
            data = f.read()
        self.assertEqual(data, self.test_data)

    def test_load_file(self):
        save_file(self.test_file_path, self.test_data)
        data = load_file(self.test_file_path)
        self.assertEqual(data, self.test_data)

    def test_load_non_existent_file(self):
        with self.assertRaises(FileNotFoundError):
            load_file('non_existent_file.txt')

if __name__ == '__main__':
    unittest.main()