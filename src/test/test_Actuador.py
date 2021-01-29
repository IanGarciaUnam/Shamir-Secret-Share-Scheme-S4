from Controller.Actuador import Actuador
from random import randint
from unittest import TestCase
from os import remove

class test_Actuador(TestCase):
	"""
	Test for Actuador Class
	"""
	def test_change_to_new_term(self):
		"""
		Verify the change_to_new_term() method
		"""
		f="archivo.txt.aes"
		out=Actuador.change_to_new_term(f, "txt")
		assert "archivo.txt"==out

	def test_convert_list_in_out_file(self):
		"""
		Verify the write and read method for frg's files
		"""
		maximum= randint(0, 346367)#Just a bigger and random number
		list_out:list=[]
		for i in range(maximum):
			list_out.append((randint(1,24646732534563432532), randint(1,325235325252262)))
		Actuador.convert_list_in_file(list_out, "test.frg","./test_files")
		list_in=Actuador.convert_file_in_list("./test_files/test.frg")
		assert list_in==list_out
		remove("test_files/test.frg")

	def test_get_original_ext(self):
		"""
		Verify the method that gets the original extension of a file modified
		"""
		maximum= str(randint(0, 3406367))+".pdf.aes"
		out= Actuador.get_original_ext(maximum)
		assert Actuador.get_original_ext(maximum) == "pdf"