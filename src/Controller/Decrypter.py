from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from .Encrypter import Encrypter
from base64 import b64decode
from .LaGrangeInterpolation import LagrangeInterpolation
import hashlib, sys, os


class Decrypter:
    """
    A class that has decrypting methods

    """
    def __init__(self , cryp_file, shares):
        """
        Constrcut a decrypter method

        Args:
            cryp_file (str): Encrypted file
            shares (list): List of shares to use
        """
        self.file = cryp_file
        """ file (str) = File's name"""
        self.shares = shares
        """ (list) List of Shares"""
        self.mode = AES.MODE_CFB
        """ mode = Mode of AES encrypter"""

        
    def decrypt_text(self, text, key):
        """
        Decrypts a given text

        Args:
            text (str): text to decrypt
            key (str): key to decrypt the text

        Returns:
            str: decrypted text
        """
        iv = 16 * b'0'
        password = self.alphanumric_pass(key)
        cipher = AES.new(password, self.mode, iv)
        decrypted_text = cipher.decrypt(text)
        
        return decrypted_text
        
    def decipher_file(self):
        """
        Decrypts the encrypted file

        Returns:
            file: Decrypted file
        """
        try:
            with open(self.file, 'rb') as f:
                encrypted_file = f.read()
        except:
            print("There was an error while reading " + str(self.file))
        
        
        secret = self.get_secret() 
        num = str(secret)
        decrypted_text = self.decrypt_text(encrypted_file, num)        
        return decrypted_text
    
    def get_secret(self):
        """
        Gets the password to decrypt the crypted file

        Returns:
            int: the password to decrypt
        """
        return LagrangeInterpolation.reconstruct_secret(self.shares, 0)
        
    
    def save_decrypted_file(self):
        """
        Saves the decrypted file

        Args:
            new_name (str): new name for the the decrypted file
        """
        file_name=self.file.split("/")

        new_file = os.path.join("./exit_files/", file_name[len(file_name)-1])
        with open(new_file[:-4], 'wb') as f:
            f.write(self.decipher_file())
            f.close()
            
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