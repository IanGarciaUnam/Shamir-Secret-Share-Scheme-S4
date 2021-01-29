from Controller.Encrypter import Encrypter
from Controller.Decrypter import Decrypter
from Controller.Cifrador import Cifrador,Descifrador
from Controller.Actuador import Actuador
from Controller.Polynomio import Lagrange_Polynomial as Polynomio
from numpy.polynomial.polynomial import Polynomial as Poly
from random import randint
import pytest
from unittest import TestCase
from os import remove
import os
import io
class test_Polynomio(TestCase):
	"""
	Test for Polynomio
	"""

	def test_verify_degree(self):
		"""
		Check the degree of the polynomio
		"""
		minimum=randint(2,70)
		e = self.generate_Encrypter("test_files/")
		p = self.get_poly(e,"test_files/",minimum)
		polynomial = Poly(p.generate_random_poly())
		
		assert polynomial.degree()==minimum-1
	
	def test_verify_evaluation(self):
		"""
		Check the evaluation of the polynomio in Cero evaluation

				f(0)=key
				--------
		"""
		minimum=randint(2,235)
		e = self.generate_Encrypter("test_files/")
		p = self.get_poly(e,"test_files/", minimum)
		assert e.get_key() == p.generate_random_poly()[0]



	def generate_Encrypter(self,way):
		"""
		Generate an encrypter object
		
		Args:
			way(str): path of a file
		Returns:
			Object(Encrypter)
		"""
		return Encrypter(way+"test.cat", "contraseña")

	def get_poly(self, Encrypter,way,minimum):
		"""
		Generate an Polynomio Object

		Args:
			Object(Encrypter): Encrypter
			way(str): path of a file
			minimum(int): a minimum number
		"""
		PRIMO=208351617316091241234326746312124448251235562226470491514186331217050270460481
		e = Encrypter
		number_key= e.get_key()
		maximum=randint(71,500)
		return Polynomio(PRIMO, minimum, maximum, number_key)

