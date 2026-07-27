def log_activity(message):
    with open("activity_log.txt", "a") as log_file:
        log_file.write(f"{message}\n")

def validate_key(key):
    if len(key) < 16:
        raise ValueError("Key must be at least 16 characters long.")
    return True

def get_file_extension(filename):
    return filename.split('.')[-1] if '.' in filename else ''