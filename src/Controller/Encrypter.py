from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto import Random
from base64 import b64encode
import hashlib
import random
import sys, os

class Encrypter:
    """
    Class implemeted to encrypt a file and a key,using SHA-256 and AES algorithimics
    """
    def __init__(self, in_file, key):
        """
        Creates an object that encryptes a file

        Args:
            in_file (str): file to encrypt
            key (str): password
            prime_number (int) = prime_number to construct the polynomial
            n (int) = number of shares
            k (int) = mininum number of shares
        """
        self.file = in_file
        """ file (str) = File's name"""
        self.key = self.generate_number(key)
        """ key(int) = key given in a 256-number"""
        self.mode = AES.MODE_CFB
        """ mode = Mode of AES encrypter"""

    def get_key(self):
        """
        Return the key generated to encrypt a file
        
        Args:
            self
        Return:
             a number-key
        """
        return self.key
    
    def encrypt_text(self, text):
        """
        A function that encrypts text

        Args:
            text (str): text to encrypt

        Returns:
            str: encrypted text
        """
        iv = 16 * b'0'
        password = self.alphanumric_pass(self.key)
        cipher = AES.new(password, self.mode, iv)
        return cipher.encrypt(text)
        
    def encrypt_file(self):
        """
        Encrypts the file given

        Returns:
            file: The file encrypted with AES
        """
        try:
            
            with open(self.file, 'rb') as f:
                orig_file = f.read()
                
            enc_text = self.encrypt_text(orig_file)
        
        except:
            print("The file: " + str(self.file) + " does not exist")
            sys.exit(1)
        
            
        
        return enc_text
    
    
    def save_encrypted_file(self):
        """
        Encrypt and Saves the encrypted file

        Args:
            out_name (str): the new name for the encrypted file
        """

        file_name=self.file.split("/")

        new_file = os.path.join("./exit_files/", file_name[len(file_name)-1])
        with open(new_file+ ".aes", 'wb') as f:
            f.write(self.encrypt_file())
            f.close()

            

    
    def generate_number(self, key):
        """
        Given a password computes their sha256 and then transforms it to a number

        Args:
            key ([str]): password

        Returns:
            int: new password
        """
        secret = hashlib.sha256(key.encode('utf8')).digest()
        secret_int = int(secret.hex(),base=16)
        
        return secret_int
    
    def alphanumric_pass(self, key):
        """
        Applies sha256 to a string

        Args:
            key (str): password 

        Returns:
            str: pass with sha256 applied
        """
        num = str(key)
        return hashlib.sha256(num.encode('utf8')).digest()
    