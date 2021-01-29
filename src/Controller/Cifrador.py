from Crypto.Cipher import AES
from .Encrypter import Encrypter
from .Decrypter import Decrypter
import hashlib
from Controller.Actuador import Actuador

class Cifrador:
	"""
	This class is  a Manager of Encrypter Class, simplify the work of developer
	to encrypte a file
	"""

	def __init__(self, key, file_orig):
		"""
		Builder of Cifrador

		Param:
			key(str)--Key given by the user 
			file_orig(str)--Original file to be encrypted

		"""
		self.key = key
		""" key(str) = Given as a string from the user"""
		self.file = file_orig
		""" file(str) = Original File"""
		self.encrypter = None
		""" encrypter(Encrypter) =given as a None """

	def get_key_number(self):
		"""
		Return the 256-Big Integer Number, after apply the encrypter methods
		
		Returns:
			Big Integer-key
		"""
		if self.encrypter == None:
			raise ValueError("You need to apply cifra(), before get_key_number")

		return self.encrypter.get_key()

	def cifra(self):
		"""
		A method that encrypte the file a write the encrypted one in the 
		same route
		Params:
			self. : The Cifrador's Object
		"""
		e = Encrypter(self.file, self.key)
		e.save_encrypted_file()
		self.encrypter = e

class Descifrador:
	"""
	A class implemented to facilitate the Decrypted work
	"""

	def __init__(self, file_frg):
		"""
		Descifrador's Builder 
		
		Param:
			file_frg:str : file_frg name's
		"""
		self.file_frg = file_frg

		
	def descifra(self, cryp_file, original_ext):
		"""
		Decrypt the file using the frg-file and save it with his own original name
		
		Param:
			cryp_file: file with the extension .aes
			original_ext (str): Original extension 
		
		"""


		shares = Actuador.convert_file_in_list(self.file_frg)
		d = Decrypter(cryp_file, shares)
		d.save_decrypted_file()






