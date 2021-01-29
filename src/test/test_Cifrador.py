from Controller.Encrypter import Encrypter
from Controller.Decrypter import Decrypter
from Controller.Cifrador import Cifrador,Descifrador
from Controller.Actuador import Actuador
from Controller.Polynomio import Lagrange_Polynomial as Polynomio
from random import randint
from unittest import TestCase
from os import remove
import os
import io
from shutil import rmtree

class test_Encrypter_Cifrador_Descifrador(TestCase):
	"""
	Class for test Cifrador Class
	"""

	def test_verify_encryption(self):
		"""
		Verify that the encryption become unreadable to the common user
		"""
		if not os.path.exists("./exit_files"):
			os.mkdir("./exit_files")


		file="./test_files/test.cat"
		readable=""
		with open(file,"r") as f:
			readable=f.read()
			f.close()

		e=Encrypter(file, "contraseña")
		e.save_encrypted_file()

		file_2= "./exit_files/test.cat.aes"
		unreadable=""
		with open(file_2, "rb") as t:
			unreadable=t.read()
			t.close()

		assert readable != unreadable
		rmtree("./exit_files")





	def test_encrypt_decrypt(self):
		"""
		Verify the encryption using Cifrador
		"""	
		os.mkdir("./exit_files/")
		file="./test_files/test.cat"
		readable=""
		with open(file,"r") as f:
			readable=f.read()
			f.close()
		e=Encrypter(file, "contraseña")

		e.save_encrypted_file()
		PRIMO=208351617316091241234326746312124448251235562226470491514186331217050270460481
		p=Polynomio(PRIMO, randint(2, 34), randint(35, 90), e.get_key())
		shares=p.generate_random_shares()

		d= Decrypter("./exit_files/test.cat.aes", shares)
		d.save_decrypted_file()

		returned=""
		with open(file,"r") as f:
			returned=f.read()
			f.close()

		rmtree("./exit_files")

		assert readable == returned





