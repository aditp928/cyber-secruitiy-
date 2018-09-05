from cryptography.fernet import Fernet
import pathlib
import os

keydir = "keys"
keyfile = "keyfile"
keyfile_path = pathlib.Path(f"{keydir}/{keyfile}")
target_files = "target_files"
encrypted_dirname = "encrypted_files"

# Get target files
targets = os.listdir(target_files)

# Create output directory to save encrypted files in
encrypted_files = pathlib.Path(encrypted_dirname, exist_ok=True)

# Encrypt each target
with open(keyfile_path, "w+") as keys:
    for target_filename in targets:
        with open(f"{target_files}/{target_filename}", "r", encoding="utf8") as target_file:
            target_file = target_file.read()

            # Fernet encrypt all files
            key = Fernet.generate_key()
            fernet = Fernet(key)

            # Save key to keyfile, and encrypted file to encrypted dir
            decoded_key = key.decode("utf8")
            keys.write(f"{decoded_key}\n")
            encrypted = fernet.encrypt(target_file.encode("utf8"))

            pathlib.Path(f"{encrypted_dirname}").mkdir(exist_ok=True)
            with open(f"{encrypted_dirname}/{target_filename}.encrypted", "w+") as encrypted_file:
                encrypted_file.write(encrypted.decode("utf8"))
