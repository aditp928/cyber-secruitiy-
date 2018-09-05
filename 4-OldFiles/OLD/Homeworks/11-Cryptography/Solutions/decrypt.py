import cryptography
from cryptography.fernet import Fernet
import os


def fernet_decrypt_files_with_keys(encrypted_dir, keyfile_path):
    # List of encrypted files
    encrypted_files = os.listdir(encrypted_dir)

    # Open file containing Fernet keys...
    with open(keyfile_path, "r") as keyfile:
        # Create list of Fernet keys
        keys = keyfile.read().splitlines()

        # Dict to save all possible decryptions for each file, given all keys
        decryption_possibilities = dict()

        # Try to decrypt each file with every key (brute force)
        for f in encrypted_files:
            # Loop over keys
            for index, key in enumerate(keys, start=1):
                with open(f"{encrypted_dir}/{f}", "r") as encrypted:
                    encrypted = encrypted.read()

                    # Convert string to bytes
                    encrypted = encrypted.encode("utf8")

                    # Create Fernet instance from key, and attempt to decrypt string
                    try:
                        fernet = Fernet(key)
                        decrypted = fernet.decrypt(encrypted)
                        decryption_possibilities[f] = decrypted
                    except cryptography.fernet.InvalidToken:
                        pass

        return decryption_possibilities


def decrypt(encrypted_dir, keyfile):
    # Decrypt with Fernet keys
    decryption_possibilities = fernet_decrypt_files_with_keys(encrypted_dir, keyfile)
    return decryption_possibilities


with open("output", "w+") as output:
    results = decrypt("encrypted_files", "keys/keyfile")
    for filename, decryptions in results.items():
        print(f"{filename}")
        print("=" * 12)
        print(decryptions[0:100])
