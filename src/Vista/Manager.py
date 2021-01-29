import sys as system
from Controller.Encrypter import Encrypter
from Controller.Cifrador import Cifrador, Descifrador
from Controller.Actuador import Actuador
from Controller.LaGrangeInterpolation import LagrangeInterpolation as LGI
from Controller.Polynomio import Lagrange_Polynomial as Polynomio
import os
import sys as System

USO="Usage\n Encriptar: python main.py [c] <file-original> [total-points required >1 ] <total> \"minimum points required\" >1>  \n Decriptar: python main.py [d] <file-frg> <file-aes>"
""" Usage"""
PRIMO=208351617316091241234326746312124448251235562226470491514186331217050270460481
""" BIG PRIMO OF 257 """
class Manager:
	"""
	Class used to verify mistakes that could be done by user's entry and complete the work of each option as
	Crypt and Decrypt
	"""

	def __init__(self, file_original:str, total_points:int, minimum_points:int):
		"""
		Manager Builder

		Args:
			file_original(str): Original File to be encrypted
			total_points(int): Maximum of shares to be generated
			minimum_points(int): Polynomial degree 
		"""
		if not os.path.exists(file_original) or not os.path.isfile(file_original):
			print("Check your original file- The path is wrong or the file doesn't exists\n")
			print(USO)
			System.exit(1)

		if not isinstance(total_points,int):
			print("Total Points is not an integer value, check your data\n")
			print(USO)
			System.exit(1)
		if not isinstance(minimum_points, int):
			print("Minimum points required is not an Integer value, check your data\n")
			print(USO)
			System.exit(1)
		if minimum_points > total_points:
			print("Total points ought to be bigger or at least equals than Minimum points\n")
			print(USO)
			System.exit(1)
		if not os.path.isdir("./exit_files"):
			os.mkdir("./exit_files")
		self.file_original=file_original
		""" Original file to be decrypted"""
		self.total_points=total_points
		""" Maximum of shares to be generated"""
		self.minimum_points=minimum_points
		""" Polynomial Degree """



	def work_to_cipher(self,secret):
		"""
		Cipher the file, generate the frg and aes file

		"""
		c= Cifrador(secret,self.file_original)
		c.cifra()
		key=c.get_key_number()
		p = Polynomio(PRIMO, self.minimum_points, self.total_points, key)
		out_list=p.generate_random_shares()
		frg_file=self.file_original+".frg"#Actuador.change_to_new_term(self.file_original,"frg")
		Actuador.convert_list_in_file(out_list, frg_file, "./exit_files")

class Verifier_Builder:
	"""
	Class done to verify the user's parameters to decode a crypted file
	and decrypt it, reconstruiting the Polynomio and evaluating it in "0"

	"""
	def __init__(self, file_frg, encrypted_file):
		"""
		Verifier_Builder  Builder

		Args:
			file_frg(str): frg file, that contains tuple of (x,y) pairs
			encrypted_file(str): FIle to be decrypted

		"""
		if not os.path.isdir("./exit_files"):
			os.mkdir("./exit_files")
		if not os.path.exists(file_frg) or not os.path.isfile(file_frg):
			print("Check your original file- The path is wrong or the file doesn't exists\n")
			print(USO)
			System.exit(1)
		if not os.path.exists(encrypted_file) or not os.path.isfile(encrypted_file):
			print("Check your original file- The path is wrong or the file doesn't exists\n")
			print(USO)
			System.exit(1)
		self.file_frg=file_frg
		""" File frg """
		self.encrypted_file=encrypted_file
		""" File encrypted .aes"""


	def work_to_descipher(self):
		"""
		Analyze fragments of tuples and decrypt the aes file and save it in a safe way
		
		"""	
		d=Descifrador(self.file_frg)
		d.descifra(self.encrypted_file, Actuador.get_original_ext(str(self.encrypted_file)))

		




















