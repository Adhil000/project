# File: /secure-file-storage-system/secure-file-storage-system/src/secure_file_storage/main.py

import tkinter as tk
from tkinter import filedialog, messagebox
from encryption import encrypt_file, decrypt_file
from storage import save_encrypted_file, load_encrypted_file
from utils import log_activity

class SecureFileStorageApp:
    def __init__(self, master):
        self.master = master
        master.title("Secure File Storage System")

        self.label = tk.Label(master, text="Secure File Storage System")
        self.label.pack()

        self.encrypt_button = tk.Button(master, text="Encrypt File", command=self.encrypt_file)
        self.encrypt_button.pack()

        self.decrypt_button = tk.Button(master, text="Decrypt File", command=self.decrypt_file)
        self.decrypt_button.pack()

    def encrypt_file(self):
        file_path = filedialog.askopenfilename()
        if not file_path:
            return
        
        key = self.get_key()
        if not key:
            return
        
        try:
            encrypted_data = encrypt_file(file_path, key)
            save_encrypted_file(encrypted_data, file_path + ".enc")
            log_activity(f"Encrypted file: {file_path}")
            messagebox.showinfo("Success", "File encrypted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def decrypt_file(self):
        file_path = filedialog.askopenfilename()
        if not file_path:
            return
        
        key = self.get_key()
        if not key:
            return
        
        try:
            decrypted_data = load_encrypted_file(file_path)
            original_file = decrypt_file(decrypted_data, key)
            with open(file_path.replace(".enc", ""), 'wb') as f:
                f.write(original_file)
            log_activity(f"Decrypted file: {file_path}")
            messagebox.showinfo("Success", "File decrypted successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def get_key(self):
        key = tk.simpledialog.askstring("Input", "Enter the encryption key:")
        if not key:
            messagebox.showwarning("Warning", "Key cannot be empty!")
        return key

if __name__ == "__main__":
    root = tk.Tk()
    app = SecureFileStorageApp(root)
    root.mainloop()